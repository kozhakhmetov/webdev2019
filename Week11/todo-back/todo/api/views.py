from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse

from api.models import TaskList, Task

def hello(request):
    return HttpResponse("qweqwe")


def task_lists(request):
    models = TaskList.objects.all()
    json_list = [i.to_json() for i in models]
    return JsonResponse(json_list, safe=False)


def task_list_by_id(request, id):
    try:
        models = TaskList.objects.filter(id=id)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    json_list = [i.to_json() for i in models]
    return JsonResponse(json_list, safe=False)


def get_tasks_by_id(request, id):

    try:
        models = Task.objects.filter(id=id)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    json_list = [i.to_json() for i in models]
    return JsonResponse(json_list, safe=False)


