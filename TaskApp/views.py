import json

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import Task, CustomUser


def login_page(request):
    return render(request, 'login.html', status=201)


def main_page(request):
    return render(request, 'taskPage.html')


@csrf_exempt
def login_user(request):
    """email = result['email']
    password = result['password']
    user = authenticate(email=email, password=password)
    if user is None:
        return JsonResponse({"is_error": True}, status=200)"""

    return JsonResponse(data={"haha": "855"}, status=201)


@csrf_exempt
def get_tasks(request):
    data = serializers.serialize('json', Task.objects.all(),
                                 fields=('pk', 'description', 'is_completed', 'created_by'))
    return JsonResponse(data=data, status=200, safe=False)

@csrf_exempt
def add_task(request):
    serialized_data = json.loads(request.body)
    description = serialized_data['description']
    created_by = CustomUser.objects.get(pk=serialized_data['created_by'])
    task = Task.objects.create(description=description, created_by=created_by)
    task.save()
    return JsonResponse({"message": "added"}, status=201)

@csrf_exempt
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return JsonResponse({"message": "deleted"}, status=200)

@csrf_exempt
def complete_task(request, pk):
    serialized_data = json.loads(request.body)
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = serialized_data['is_completed']
    task.save()
    return JsonResponse({"message": "changed"}, status=200)


@csrf_exempt
def clear_all_tasks(request):
    Task.objects.all().delete()
    return JsonResponse({"message": "Deleted all Tasks"}, status=204)
