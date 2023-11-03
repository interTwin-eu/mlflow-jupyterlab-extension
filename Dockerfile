# https://hub.docker.com/layers/kubeflownotebookswg/jupyter-scipy/v1.7.0/images/sha256-5499efaf779ff4dcedc7eeb7aea5c759347dda7b4b3ecbcb9b14d0bc4ae53eed?context=explore
FROM kubeflownotebookswg/jupyter-scipy:v1.7.0

# COPY . /app/mlflow-ext
ADD dist/mlflow_jupyterlab_extension-0.0.1-py3-none-any.whl mlflow_jupyterlab_extension-0.0.1-py3-none-any.whl

# # RUN sudo apt-get install gcc libpq-dev -y
# # RUN sudo apt-get install python-dev  python-pip -y
# # RUN sudo apt-get install python3-dev python3-pip python3-venv python3-wheel -y
# RUN pip install --upgrade pip
# RUN pip install wheel setuptools --upgrade
# # RUN pip install Cmake --upgrade
# # RUN pip install cmake --upgrade

# RUN pip install /app/mlflow-ext
# RUN cd /app/mlflow-ext && pip install .
RUN pip install --no-cache-dir mlflow_jupyterlab_extension-0.0.1-py3-none-any.whl