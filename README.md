# DBT-Airflow-pipeline
A data pipeline and load into the database(AWS Redshift) for Data engineer

## Architecture
![image for my workflow](https://github.com/Tack-Theerapat/DBT-Airflow-pipeline/blob/main/work_flow3.png)

1. User upload data in [AWS S3](https://aws.amazon.com/s3/)
2. Copy into [AWS Redshift](https://aws.amazon.com/redshift/)
3. Transform using [dbt](https://www.getdbt.com/)
4. Orchestrate with [Airflow](https://airflow.apache.org/) in [AWS EC2](https://aws.amazon.com/ec2/)
