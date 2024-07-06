from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

def print_hello():
    print("Hello mi gente los quiero mucho")

with DAG(dag_id="dependencias",
        description="Pimer DAG utilizando dependencias",
        schedule_interval="@once",
        start_date=datetime(2024, 7, 5)) as dag:

    t1 = PythonOperator(task_id="tarea1",
                        python_callable=print_hello)
    t2 = BashOperator(task_id="tarea2",
                      bash_command="echo 'Esta es la tarea 2'")
    t3 = BashOperator(task_id="tarea3",
                      bash_command="echo 'Esta es la tarea 3'")
    t4= BashOperator(task_id="tarea4",
                      bash_command="echo 'Esta es la tarea 4'")

    t1 >> t2 >> [t3, t4]