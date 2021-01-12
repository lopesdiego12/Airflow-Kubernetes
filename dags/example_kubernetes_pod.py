from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow import configuration as conf

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


dag = DAG('example_kubernetes_pod',
          schedule_interval='@once',
          default_args=default_args)

# This is where we define our desired resources.
compute_resources = \
  {'request_cpu': '80m',
  'request_memory': '1Gi',
  'limit_cpu': '80m',
  'limit_memory': '1Gi'}

with dag:
    k = KubernetesPodOperator(
        namespace="default",
        image="hello-world",
        labels={"foo": "bar"},
        name="airflow-test-pod",
        task_id="task-one",
        in_cluster=in_cluster, # if set to true, will look in the cluster, if false, looks for file
        cluster_context='docker-for-desktop', # is ignored when in_cluster is set to True
        config_file=config_file,
        resources=compute_resources,
        is_delete_operator_pod=True,
        get_logs=True)