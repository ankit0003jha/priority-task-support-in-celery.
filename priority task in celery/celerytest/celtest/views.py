# import main
from rest_framework import status
from rest_framework.views import APIView

from celtest.helpers import api_response, check_queue1, check_queue2, check_queue3, check_queue4, check_queue5

"""
This api will help you to get all the loco state list.
"""
# REDIS_HIGH_PRIORITY = 0
# REDIS_LOW_PRIORITY = 9


class CheckCeleryTask1(APIView):
    def get(self, request):
        check_queue1.apply_async(queue="task1", priority=1)
        return api_response(status.HTTP_200_OK, "Successfully fetched all data", "ok", 1)


class CheckCeleryTask2(APIView):
    def get(self, request):
        check_queue2.apply_async(queue="task1", priority=2)
        return api_response(status.HTTP_200_OK, "Successfully fetched all data", "ok", 1)


class CheckCeleryTask3(APIView):
    def get(self, request):
        check_queue3.apply_async(queue="task1", priority=3)
        return api_response(status.HTTP_200_OK, "Successfully fetched all data", "ok", 1)


class CheckCeleryTask4(APIView):
    def get(self, request):
        check_queue4.apply_async(queue="task1", priority=4)
        return api_response(status.HTTP_200_OK, "Successfully fetched all data", "ok", 1)


class CheckCeleryTask5(APIView):
    def get(self, request):
        check_queue5.apply_async(queue="task1", priority=5)
        return api_response(status.HTTP_200_OK, "Successfully fetched all data", "ok", 1)


# celery -A celtest.helpers worker --loglevel=info --pool=solo --concurrency=1
