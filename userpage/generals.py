from .models import *

def webInfo(request):
    context = {
        'data': WebInfo.objects.last()
    }
    # render nagari page ko data matra pass garne
    return context