from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor

from datetime import datetime


with DAG(dag_id="filesensor",
         description="FileSensor",
         schedule_interval="@daily",
         start_date=datetime(2022, 9, 20),
         end_date=datetime(2022, 12, 22),
         max_active_runs=1
        ) as dag:

    t1 = BashOperator(task_id="creating_file",
                      bash_command="sleep 10 && echo 'Hi, from my first FileSensor.' > /tmp/file.txt",
                      )
    
    t2 = FileSensor(task_id="waiting_file",
                    filepath="/tmp/file.txt")

    t3 = BashOperator(task_id="end_task",
                      bash_command="echo 'The file has been received, and contains this: ' && cat /tmp/file.txt")
    
    t1 >> t2 >> t3