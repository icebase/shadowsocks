import os

# Config
API_INTERFACE = 'MuApiV2' #mudbjson, sspanelv2, sspanelv3, sspanelv3ssr, MuApiV2

mu_uri = os.getenv('MU_URI', '')
node_id = os.getenv('MU_NODE_ID', 1)
token = os.getenv('MU_TOKEN', '')
