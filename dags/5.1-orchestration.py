from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="orquestation",
        description="Utilizando bash operator",
        schedule_interval="@daily",
        start_date=datetime(2024, 7, 1),
        end_date=datetime(2024, 8, 1),
        default_args={"depends_on_past": True},
        max_active_runs=1
        ) as dag:

    t1 = BashOperator(task_id="task1",
                    bash_command="sleep 2 && echo 'Orquestando en tarea 1'")
    t2 = BashOperator(task_id="task2",
                    bash_command="sleep 3 && echo 'Orquestando en tarea 2'")
    t3 = BashOperator(task_id="task3",
                    bash_command="sleep 3 && echo 'Orquestando en tarea 3'")
    t4 = BashOperator(task_id="task14",
                    bash_command="sleep 2 && echo 'Orquestando en tarea 4'")
    
    t1.set_downstream(t2)
    t2.set_downstream([t3,t4])

