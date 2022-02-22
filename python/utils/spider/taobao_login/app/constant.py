import os
from pathlib import Path

current_file_path = os.path.abspath(__file__)

PROJECT_PATH = Path(current_file_path).parent.parent

EXPRESS_DOMAIN_URL = 'https://fly.cainiao.com/login.htm?fromUrl=https://fly.cainiao.com/branch/branchOverall.htm'
POINT_DOMAIN_URL = 'https://fly.cainiao.com/login.htm?fromUrl=https://fly.cainiao.com/branch/branchOverallForBranch.htm'
# LINK_DOMAIN_URL = 'https://fly.cainiao.com/login.htm?fromUrl=https://fly.cainiao.com/logistics/chainTimeAnalysis.htm#/fulllink'

WIDTH, HEIGHT = 1366, 768

ACCOUNT = [
    {
        'username': '187****2160',
        'password': '****'
    },
    {
        'username': '184****3212',
        'password': '****'
    }
]

# HEADLESS = True
HEADLESS = False

# REDIS_HOST = '10.131.*.*'  # prd/docker linux
REDIS_HOST = '127.0.0.1'  # prd/docker linux
REDIS_PORT = 6366
REDIS_PASS = 'redis'
