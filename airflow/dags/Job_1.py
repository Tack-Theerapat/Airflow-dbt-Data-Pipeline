import datetime

import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="My_DBT_Pipeline_ClassProject",
    schedule="@daily",
    start_date=pendulum.datetime(2021, 1, 1,7,0,0, tz="UTC"),
    catchup=False,
    tags=["class project"]
) as dag:
    # [START howto_operator_bash]
    step_1 = BashOperator(
        task_id="dbt_seed",
        bash_command="/home/ec2-user/dbt_lab/.env/bin/dbt seed --project-dir /home/ec2-user/dbt_lab/class_project/",
    )
    step_2 = BashOperator(
        task_id="dbt_run",
        bash_command="/home/ec2-user/dbt_lab/.env/bin/dbt run --project-dir /home/ec2-user/dbt_lab/class_project/",
    )
    step_3 = BashOperator(
        task_id="dbt_test",
        bash_command="/home/ec2-user/dbt_lab/.env/bin/dbt test --project-dir /home/ec2-user/dbt_lab/class_project/",

    )

    step_1 >> step_2 >> step_3