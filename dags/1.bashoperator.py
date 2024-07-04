from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="bashoperator",
        description="Utilizando bash operator",
        start_date=datetime(2024, 7, 1)) as dag:

    t1 = BashOperator(task_id="Hello_with_bash",
                    bash_command="echo 'Hola este es mi primer mensaje en airflow'")
    t1



