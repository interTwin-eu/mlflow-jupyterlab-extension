import setuptools

setuptools.setup(
    name="mlflow-jupyterlab-extension",
    version='0.0.1',
    author="Matteo Bunino @ interTwin",
    description="JupyterLab extension for MLFlow tracking server",
    packages=setuptools.find_packages(),
    install_requires=[
        'mlflow',
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'mlflow = mlflow_extension:mlflow_conf'
        ]
    },
    include_package_data=True,
    license='MIT'
)