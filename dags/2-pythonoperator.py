from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello mi gente los quiero mucho")

with DAG(dag_id="pythonoperator",
        description="Pimer DAG utilizando Python Operator",
        schedule_interval="@once",
        start_date=datetime(2024, 7, 5)) as dag:

    t1 = PythonOperator(task_id="hello_python",
                        python_callable=print_hello)
    t1
