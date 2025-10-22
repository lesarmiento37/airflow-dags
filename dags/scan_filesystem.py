from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

def list_extra_volume():
    target_path = "/opt/airflow/extra-1/current/dags"
    print(f"🔍 Checking path: {target_path}")

    if not os.path.exists(target_path):
        print("❌ Path not found — maybe git-sync-extra isn't mounted in this pod.")
        return

    print("📂 Listing directory contents:")
    for root, dirs, files in os.walk(target_path):
        print(f"\n🗂 Directory: {root}")
        for d in dirs:
            print(f"   📁 {d}")
        for f in files:
            print(f"   📄 {f}")

with DAG(
    dag_id="check_extra_volume",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["debug", "git-sync-extra"]
) as dag:

    check_volume = PythonOperator(
        task_id="list_extra_dags_from_extra_volume",
        python_callable=list_extra_volume
    )

    check_volume
