import os
os.system('celery -A tasks worker --loglevel=info')