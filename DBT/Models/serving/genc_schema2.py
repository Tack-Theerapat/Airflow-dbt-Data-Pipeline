import re
import os
import jinja2

def list_sql_file(directory_path):
    files = [file for file in os.listdir(directory_path) if file.endswith(".sql")]
    return files    

def read_file(directory_path, files):
    # Jinja2 environment setup
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(directory_path))
    
    for file in files:
        table_name = file.split('.')[0]
        file_contents = ""
        file_path = os.path.join(directory_path, file)
        
        try:
            # Define context with required variables like 'config', 'ref', etc.
            context = {
                'config': lambda *args, **kwargs: '',
                'ref': lambda *args, **kwargs: '',
                # You might need to define more variables here depending on your templates
            }
            
            # Render the file using Jinja2 with the defined context
            template = env.get_template(file)
            file_contents = template.render(context)
        except jinja2.exceptions.TemplateNotFound:
            print(f"Template file not found: {file_path}")
            continue
        except Exception as e:
            print(f"An error occurred while rendering template {file}: {str(e)}")
            continue

        # Now you can apply your regex pattern and generate YAML files as before
        # (the rest of the code remains the same)

if __name__ == "__main__":
    # directory_path = 'C:\\Users\\sakda\\OneDrive\\BackUp\\Old\\Documents\\DBT_LAB\\EP4_Workshop\\models\\serving'
    directory_path = 'D:/DE_Project/FutureSkill/EP4_Workshop/Class_Project/serving'
    # directory_path ='/home/ec2-user/dbt_lab/class_project/models/serving_zone'
    files = list_sql_file(directory_path)
    content = read_file(directory_path, files)
