import time
from celery import Celery
# from decouple import config
# REDIS_URL = config('REDIS_URL')

# For localhost
app = Celery(
            'my_app', 
             broker='redis://localhost:6379', 
             backend='redis://localhost:6379', 
             broker_connection_retry_on_startup=True
)

# app = Celery(
#             'my_app', 
#              broker=f'{REDIS_URL}?ssl_cert_reqs=CERT_NONE', 
#              backend=f'{REDIS_URL}?ssl_cert_reqs=CERT_NONE', 
#              broker_connection_retry_on_startup=True
# )

@app.task
def add_numbers(arg1, arg2):
    return arg1 + arg2

@app.task
def mockup_task(arg1, arg2):
    time.sleep('simulating a long task')
    result = add_numbers.delay(arg1, arg2)
    return result
