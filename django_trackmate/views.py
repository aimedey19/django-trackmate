import json

from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ActivityLog


def trackmate_admin(request):
    logs = ActivityLog.objects.all().order_by('-action_time')

    context = {
        'logs_json': json.dumps([{
            'id': log.id,
            'timestamp': log.action_time.isoformat(),
            'action_type': log.action_type,
            'actor': log.actor,
            'remarks': log.remarks,
            'response': log.response,
            'data': log.data
        } for log in logs], default=str)
    }

    return render(request, 'django_trackmate/trackmate_admin.html', context)


def fetch_logs(request):
    logs = ActivityLog.objects.all().order_by('-action_time')

    context = {
        'logs_json': json.dumps([{
            'id': log.id,
            'timestamp': log.action_time.isoformat(),
            'action_type': log.action_type,
            'actor': log.actor,
            'remarks': log.remarks,
            'response': log.response,
            'data': log.data
        } for log in logs], default=str)
    }

    return JsonResponse(context)