import re
import os
def list_sql_file(directory_path):
    files = [file for file in os.listdir(directory_path) if file.endswith(".sql")]
   
    return files    

def read_file(directory_path, files):
    contents = []
    for file in files:
        table_name =file.split('.')[0]
        print(table_name)
        file_contents =""
        file = os.path.join(directory_path, file)
        print(file)
        try:
            # Open the file for reading (you can use 'w' for writing or 'a' for appending)
            with open(file, 'r') as file:
                # Read the entire file content into a string
                file_contents = file.read()
                # Alternatively, you can read the file line by line
                # for line in file:
                #     print(line)
            
            # Now, you can work with the contents of the file
        
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        #-------------------------------------------------------------------------------------
        pattern = r"SELECT(.*?)from"
        matches = re.search(pattern, file_contents, re.DOTALL)
        print(matches)

        if matches:
            result = matches.group(1).strip()
            cleaned = []
            result =  [item.strip() for item in result.split(',')] 
            for column in result:
                if ' as ' in column:
                    column = column.split(' as ')[1]
                if '.' in column:
                    column = column.split('.')[1]
                # if ' as ' and '.' in column:
                #     column = column.split('.')[1] 

                cleaned.append(column)   
            
            column_test = []
            table_test = []
            for column in cleaned:
                
                test = f"""
                - name: {column}
                  description: this is {column}
                  tests: 
                    - dbt_expectations.expect_column_values_to_not_be_null
                    - dbt_expectations.expect_column_values_to_be_of_type:
                            column_type: character varying
                    """
                column_test.append(test)
            column_test = '\n'.join(column_test)
           
            header ="""
version: 1
models:
"""
            tests = f"""
            - name: {table_name}
              description: this is {table_name} table
              columns:
                {column_test}
            """

            table_test_with_header = header + tests

            try:
                # Open the file for writing (creates or overwrites the file)
                with open(f"clss_prj_{table_name}_schema.yml", 'w') as file:
                    # Write the content to the file
                    file.write(table_test_with_header)
                
                print("File has been written successfully.")
            except Exception as e:
                print(f"An error occurred while writing the file: {str(e)}")

    


if __name__ == "__main__":
    # directory_path = 'C:\\Users\\sakda\\OneDrive\\BackUp\\Old\\Documents\\DBT_LAB\\EP4_Workshop\\models\\serving'
    directory_path = 'D:/DE_Project/FutureSkill/EP4_Workshop/Class_Project/serving'
    # directory_path ='/home/ec2-user/dbt_lab/class_project/models/serving_zone'
    files = list_sql_file(directory_path)
    content = read_file(directory_path, files)
