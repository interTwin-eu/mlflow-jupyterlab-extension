# https://hub.docker.com/layers/kubeflownotebookswg/jupyter-scipy/v1.7.0/images/sha256-5499efaf779ff4dcedc7eeb7aea5c759347dda7b4b3ecbcb9b14d0bc4ae53eed?context=explore
FROM kubeflownotebookswg/jupyter-scipy:v1.7.0
COPY . /app/mlflow-ext
RUN pip install Cmake
RUN pip install /app/mlflow-ext