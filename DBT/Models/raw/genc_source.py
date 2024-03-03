import os

def list_seeds(directory_path):

    files = [file for file in os.listdir(directory_path) if file.endswith(".csv")]

    return files
def create_source(files):
    
    tables = []
    source_name = "Ecom"
    schema_name = "dev"

    for table in files:
        tables.append(table.split('.')[0])

    #tables = ['table_a', 'table_b', 'table_c'

    table_soure = []
    for table in tables:
        table_soure.append(f"""
            - name: {table}
            """)
    table_soure = '\n'.join(table_soure)
    table_soure = '\n'.join(line for line in table_soure.splitlines() if line.strip())


    source = f"""
version: 1
sources:
    - name: {source_name}
      schema: {schema_name}
      tables:
            {table_soure}
    """


    file_name = "sources.yml"
    with open(file_name, "w") as file:
        file.write(source)

if __name__ == "__main__":

    # directory_path = 'D:/DE_Project/FutureSkill/EP4_Workshop/Class_Project/Seeds'
    directory_path ='/home/ec2-user/dbt_lab/class_project/seeds'
    files = list_seeds(directory_path)
    create_source(files)