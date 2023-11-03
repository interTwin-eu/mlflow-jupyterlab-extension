import os
# import pkg_resources

try:
    from importlib.resources import files
except ImportError:
    from importlib_resources import files


def mlflow_conf():
    """
    Returns a configuration to launch MLFlow extension.
    """

    def _mlflow_command(port):
        logs_dir = './mlflow_logs'
        cmd = (
            f"mlflow server --backend-store-uri {logs_dir} "
            f"--host 127.0.0.1 --port {port}"
        )
        return cmd.split()

    this_module_path = files('mlflow_extension')
    icon_path = os.path.join(this_module_path, 'icons/MLflow-Logo.svg')

    return {
        'command': _mlflow_command,
        'absolute_url': False,
        'port': 50001,
        'timeout': 20,
        'launcher_entry': {
            'title': 'MLFlow server',
            'icon_path': icon_path
        }
    }
