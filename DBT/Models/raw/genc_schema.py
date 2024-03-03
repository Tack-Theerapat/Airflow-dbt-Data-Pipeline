import os
import pandas as pd

def list_seeds(directory_path):

    files = [file for file in os.listdir(directory_path) if file.endswith(".csv")]

    return files
def create_test_case(files):
    
    tables = []
    source = "Ecom"

    for table in files:
        
        df = pd.read_csv(os.path.join(directory_path, table))
        column_names = df.columns.tolist()
        obj = {'table': table.split('.')[0], 'column': column_names}
        tables.append(obj)

    
    for obj in tables :
        column_list = obj['column']
        column_test = []
        
        for column in column_list:
            
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
        test_table= f"""
        - name: raw_{obj['table']}
          description: this is raw {obj['table']} table
          columns:
            {column_test}
        """
        #print(test_table)
        table_test_with_header = header + test_table
        file_name = f"class_prj_{obj['table']}_schema.yml"
        with open(file_name, "w") as file:
            file.write(table_test_with_header)

if __name__ == "__main__":

    # directory_path = 'D:/DE_Project/FutureSkill/EP4_Workshop/Class_Project/Seeds'
    #directory_path = 'C:\\Users\\sakda\\OneDrive\\BackUp\\Old\\Documents\\DBT_LAB\\EP4_Workshop\\Seeds'
    directory_path ='/home/ec2-user/dbt_lab/class_project/seeds'
    files = list_seeds(directory_path)
    create_test_case(files)