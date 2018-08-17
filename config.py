import os
from dotenv import load_dotenv


def load_env_from_file():
    env_file = os.getenv('ENV_FILE', None)
    if env_file is not None:
        load_dotenv(dotenv_path=env_file)


load_env_from_file()

# Config
API_INTERFACE = 'MuApiV2'  # mudbjson, sspanelv2, sspanelv3, sspanelv3ssr, MuApiV2

mu_uri = os.getenv('MU_URI', '')
node_id = os.getenv('MU_NODE_ID', 1)
token = os.getenv('MU_TOKEN', '')
