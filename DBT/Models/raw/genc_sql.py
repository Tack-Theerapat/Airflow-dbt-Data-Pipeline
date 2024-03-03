import pandas as pd
import os

def list_seeds(directory_path):

    files = [file for file in os.listdir(directory_path) if file.endswith(".csv")]

    return files
def create_sql(files):
    
    tables = []
    for table in files:
        
        df = pd.read_csv(os.path.join(directory_path, table))
        column_names = df.columns.tolist()
        obj = {'table': table.split('.')[0], 'column': column_names}
        tables.append(obj)


    source = "Ecom"
    for obj in tables :
        column_list = obj['column']
        column_list = ',\n'.join(column_list)
        sql = f"""
        {{{{
            config(
                materialized='table',
                schema= 'raw'
            )
        }}}}

        select
            {column_list}
        from {{{{ source('{source}','{obj['table']}') }}}}
        """

        file_name = f"raw_{obj['table']}.sql"
        with open(file_name, "w") as file:
            file.write(sql)

if __name__ == "__main__":

    # directory_path = 'Class_Project/Seeds'
    directory_path ='/home/ec2-user/dbt_lab/class_project/seeds'
    files = list_seeds(directory_path)
    create_sql(files)