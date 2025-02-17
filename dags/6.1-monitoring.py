from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

def myfunction():
    raise Exception

with DAG(dag_id="monitoring",
        description="Monitoreando nuestras Dag",
        schedule_interval="@daily",
        start_date=datetime(2024, 1, 1),
        end_date=datetime(2024, 6, 1)
        ) as dag:

    t1 = BashOperator(task_id="tarea1",
                      bash_command="sleep 2 && echo 'Primera tarea !!'")
    t2 = BashOperator(task_id="tarea2",
                      bash_command="sleep 2 && echo 'Segunda tarea !!'")
    t3 = BashOperator(task_id="tarea3",
                      bash_command="sleep 2 && echo 'Tercera tarea !!'")
    t4= PythonOperator(task_id="tarea4",
                        python_callable=myfunction)
    t5= BashOperator(task_id="tarea5",
                      bash_command="sleep 2 && echo 'Cuarta tarea !!'")
    
    t1 >> t2 >> t3 >> t4 >> t5