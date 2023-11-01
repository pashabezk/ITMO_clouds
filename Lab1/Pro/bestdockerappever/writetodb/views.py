from django.shortcuts import render

# Create your views here.
from writetodb.models import BootRecord


def getpaste(request):
    pastes = BootRecord.objects.all()
    return render(request, 'html/pastes.html', {'pastes': pastes})
