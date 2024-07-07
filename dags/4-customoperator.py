from airflow import DAG 
from datetime import datetime
from hioperator import HelloOperator

with DAG(dag_id="customoperator",
         description="Este es un operador hecho a la medida",
         start_date=datetime(2022,8,1)) as dag:
    
    t1 = HelloOperator(task_id="hello",
                       name="Dani")
    t1