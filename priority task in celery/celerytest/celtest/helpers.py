import time

from celery import shared_task
from rest_framework.response import Response


def api_response(code, message, data, status=None):
    data = {
        "status": status if status is not None else code,
        "message": message,
        "data": data,
    }
    return Response(data=data, status=code)


import os

from celery import Celery

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celerytest.settings")
# app = Celery("celerytest")
# app.config_from_object("django.conf:settings", namespace="CELERY")
from kombu import Exchange, Queue

celery_app = Celery()
celeryconfig = {}
celeryconfig["broker_url"] = "amqp://localhost"
celeryconfig["result_backend"] = "rpc://localhost"
celeryconfig["task_queues"] = (
    Queue("task1", Exchange("task1"), routing_key="task1", queue_arguments={"x-max-priority": 10}),
)
celeryconfig["task_acks_late"] = True
celeryconfig["worker_prefetch_multiplier"] = 1
celeryconfig["task_inherit_parent_priority"] = True
# celeryconfig["broker_transport_options"] = {"priority_steps": [8, 6, 4, 2, 0]}
celery_app.config_from_object(celeryconfig)


# @celery_app.task(bind=True)
# def debug_task(self):
#     print(f"Request: {self.request!r}")


@celery_app.task
def check_queue1():
    print("Let's start1")
    time.sleep(10)
    print("Lets done1")
    return "queue1"


@celery_app.task
def check_queue2():
    print("Let's start2")
    time.sleep(13)
    print("Lets done2")
    return "queue2"


@celery_app.task
def check_queue3():
    print("Let's start3")
    time.sleep(16)
    print("Lets done3")
    return "queue3"


@celery_app.task
def check_queue4():
    print("Let's start4")
    time.sleep(19)
    print("Lets done4")
    return "queue4"


@celery_app.task
def check_queue5():
    print("Let's start5")
    time.sleep(23)
    print("Lets done5")
    return "queue5"
