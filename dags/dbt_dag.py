import os
from datetime import datetime

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping


profile_config = ProfileConfig(
    profile_name="linkedin_project",
    target_name="dev",
    profiles_yml_filepath="/usr/local/airflow/dags/dbt/linkedin_project/profiles.yml"
    # profile_mapping=SnowflakeUserPasswordProfileMapping(
    #     conn_id="snowflake", 
    #     profile_args={"database": "project", "schema": "raw"},
    # )
)

dbt_snowflake_dag = DbtDag(
    project_config=ProjectConfig("/usr/local/airflow/dags/dbt/linkedin_project",),
    operator_args={"install_deps": True},
    profile_config=profile_config,
    execution_config=ExecutionConfig(dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",),
    schedule_interval="@daily",
    start_date=datetime(2023, 9, 10),
    catchup=False,
    dag_id="dbt_dag",
)