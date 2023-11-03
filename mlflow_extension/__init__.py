import os


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

    return {
        'command': _mlflow_command,
        'absolute_url': False,
        'port': 50001,
        'timeout': 20,
        'launcher_entry': {
            'title': 'MLFlow server',
            'icon_path': os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                'icons',
                'MLflow-Logo.svg'
            )
        }
    }
