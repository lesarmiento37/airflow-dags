from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Definición básica del DAG
with DAG(
    dag_id="hello_leonardo",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",          
    catchup=False,
    tags=["example"]
) as dag:
    
    # Tarea con BashOperator
    say_hello = BashOperator(
        task_id="say_hello",
        bash_command='echo "Hola Leonardo"'
    )

    say_hello
