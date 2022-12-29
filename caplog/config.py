# config.py

import os
import subprocess

def set_database_url():
    # Determine the current Git branch
    branch = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], capture_output=True).stdout.decode().strip()

    # Set the DATABASE_URL environment variable based on the current Git branch
    if branch == 'develop':
        os.environ['DATABASE_URL'] = open('../config/dev.env').read().strip()
    else:
        os.environ['DATABASE_URL'] = open('../config/prod.env').read().strip()
