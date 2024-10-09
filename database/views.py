from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from object_detection.models import DetectedObject

@login_required
def database_view(request):
    objects = DetectedObject.objects.all()
    return render(request, 'database_view.html', {'objects': objects})
