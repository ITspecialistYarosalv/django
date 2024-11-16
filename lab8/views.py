from django.shortcuts import render
from .models import Client,Phone,Call,Tariff
import datetime
def project_info(request):
    clients = Client.objects.all()
    phones = Phone.objects.all()
    calls = Call.objects.all()
    tariffs = Tariff.objects.all()

    return render(request, 'project_info.html', {
        'project_name': 'Django-project 8 lab',
        'student_name': 'Олексієнко Ярослав',
        'group': 'КІБ21015б',
        'clients': clients,
        'phones': phones,
        'calls': calls,
        'tariffs': tariffs,
    })
