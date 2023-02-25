# priority-task-support-in-celery. (RabbitMQ)
You can set priority to your celery task using #Rabbitmq as a message broker.

You can define priority level in celery function. you can observe the difference when you run celery in solo --pool with concurrency level=1.

You can find config. inside this file path ---> priority-task-support-in-celery./priority task in celery/celerytest/celtest/helpers.py

# celery cmd ---> celery -A celtest.helpers worker --loglevel=info --pool=solo --concurrency=1
