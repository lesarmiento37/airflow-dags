from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import logging

# Usamos el logger nativo de Airflow
logger = logging.getLogger("airflow.task")

def list_extra_volume():
    target_path = "/opt/airflow/extra-1/current/dags"
    logger.info(f"🔍 Checking path: {target_path}")

    if not os.path.exists(target_path):
        logger.error("❌ Path not found — maybe git-sync-extra isn't mounted in this pod.")
        return

    logger.info("📂 Listing directory contents:")
    for root, dirs, files in os.walk(target_path):
        logger.info(f"\n🗂 Directory: {root}")
        for d in dirs:
            logger.info(f"   📁 {d}")
        for f in files:
            logger.info(f"   📄 {f}")

    # Ejemplo adicional: confirmar que el DAG tiene permisos de lectura
    try:
        total_files = sum(len(files) for _, _, files in os.walk(target_path))
        logger.info(f"✅ Found {total_files} files in {target_path}")
    except Exception as e:
        logger.exception(f"⚠️ Error counting files: {e}")

with DAG(
    dag_id="check_extra_volume_with_logs",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["debug", "git-sync-extra", "logging"]
) as dag:

    check_volume = PythonOperator(
        task_id="list_extra_dags_from_extra_volume",
        python_callable=list_extra_volume
    )

    check_volume
