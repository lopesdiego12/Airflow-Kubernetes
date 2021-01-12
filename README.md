# Airflow + Kubernetes

Steps to follow


# Install dashboard
`kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0/aio/deploy/recommended.yaml`

# Find list of secrets
`kubectl get secrets`

# Get token
`kubectl describe secret default-token-p6xlb`

# Access the dashboard
`kubectl proxy`

# Install helm charts
`helm repo add stable https://charts.helm.sh/stable`

# git clone my project 
`git clone git@github.com:lopesdiego12/Airflow-Kubernetes.git`

# Deploy Apache Airflow with yaml file
`helm install airflow stable/airflow -f config/airflow-helm-config.yaml --version 7.2.0`

# List helm installation
`helm list`

# Get pods and make localhost:8080 available

`export POD_NAME=$(kubectl get pods --namespace default -l "component=web,app=airflow" -o jsonpath="{.items[0].metadata.name}")
echo http://127.0.0.1:8080
kubectl port-forward --namespace default $POD_NAME 8080:8080`
