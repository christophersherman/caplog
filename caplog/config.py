# config.py

import os
import subprocess

def set_database_url():

    os.environ['TESTING_URL'] = "mysql://user:@127.0.0.1:3306/caplog_test_case"

    # Determine the current Git branch
    branch = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], capture_output=True).stdout.decode().strip()
    
    # Set the DATABASE_URL environment variable based on the current Git branch
    if branch == 'develop':
        f = open('config/dev.env')
        os.environ['DATABASE_URL'] = f.read().strip()
        f.close()

    else:
        f = open('config/prod.env')
        os.environ['DATABASE_URL'] = f.read().strip()
        f.close()

