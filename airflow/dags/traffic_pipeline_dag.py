from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

dag = DAG(
    'traffic_pipeline',
    default_args=default_args,
    description='Pipeline de traitement du trafic urbain - Smart City',
    schedule_interval=timedelta(minutes=5),
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['smart-city', 'traffic', 'bigdata'],
)

def log_start(**context):
    """Log le démarrage du pipeline"""
    print("=" * 80)
    print("🚀 DÉBUT DU PIPELINE DE TRAITEMENT DU TRAFIC")
    print(f"⏰ Timestamp: {datetime.now()}")
    print(f"📊 Execution Date: {context['execution_date']}")
    print("=" * 80)

def log_success(**context):
    """Log la fin réussie du pipeline"""
    print("=" * 80)
    print("✅ PIPELINE EXÉCUTÉ AVEC SUCCÈS")
    print(f"⏰ Timestamp: {datetime.now()}")
    print(f"⏱️ Durée: {context['ti'].duration} secondes")
    print("📊 Données traitées et disponibles dans PostgreSQL")
    print("=" * 80)

# Tâche 1: Log de démarrage
start_task = PythonOperator(
    task_id='log_pipeline_start',
    python_callable=log_start,
    provide_context=True,
    dag=dag,
)

# Tâche 2: Traitement Spark - VERSION FONCTIONNELLE
process_traffic = BashOperator(
    task_id='process_traffic_data',
    bash_command="""
    docker exec spark-master /opt/spark/bin/spark-submit \
    --master spark://spark-master:7077 \
    --jars /opt/spark/jars/postgresql-new.jar \
    /opt/spark-apps/traffic_processing.py
    """,
)



# Tâche 3: Log de succès
success_task = PythonOperator(
    task_id='log_pipeline_success',
    python_callable=log_success,
    provide_context=True,
    dag=dag,
)

# Définition du workflow
start_task >> process_traffic >> success_task