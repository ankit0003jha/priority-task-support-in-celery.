# priority-task-support-in-celery. (RabbitMQ)
You can set priority to your celery task using #Rabbitmq as a message broker.

You can define priority level in celery function. you can observe the difference when you run celery in solo --pool with concurrency level=1.

# celery cmd ---> celery -A celtest.helpers worker --loglevel=info --pool=solo --concurrency=1
