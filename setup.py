import setuptools
# from glob import glob

setuptools.setup(
    name="mlflow-jupyterlab-extension",
    version='0.0.1',
    author="Matteo Bunino @ interTwin",
    description="JupyterLab extension for MLFlow tracking server",
    packages=['mlflow_extension'],
    package_dir={'': 'src'},
    install_requires=[
        'mlflow',
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'mlflow = mlflow_extension:mlflow_conf'
        ]
    },
    package_data={
        'mlflow_extension': ['icons/MLflow-Logo.svg'],
    },
    # data_files=[
    #     ('icons-data', glob('icons/*.svg')),
    # ],
    include_package_data=True,
    license='MIT'
)
