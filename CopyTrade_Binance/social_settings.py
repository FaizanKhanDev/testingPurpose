import os

GITHUB_ID     = os.getenv('GITHUB_ID', None)
GITHUB_SECRET = os.getenv('GITHUB_SECRET', None)
GITHUB_AUTH   = GITHUB_SECRET is not None and GITHUB_ID is not None