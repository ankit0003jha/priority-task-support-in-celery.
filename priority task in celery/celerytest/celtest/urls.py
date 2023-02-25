from django.urls import path

from celtest.views import CheckCeleryTask1, CheckCeleryTask2, CheckCeleryTask3, CheckCeleryTask4, CheckCeleryTask5

urlpatterns = [
    path("check/celery/1", CheckCeleryTask1.as_view(), name="check1"),
    path("check/celery/2", CheckCeleryTask2.as_view(), name="check2"),
    path("check/celery/3", CheckCeleryTask3.as_view(), name="check3"),
    path("check/celery/4", CheckCeleryTask4.as_view(), name="check4"),
    path("check/celery/5", CheckCeleryTask5.as_view(), name="check5"),
]
