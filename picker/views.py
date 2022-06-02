from django.shortcuts import render
import random
# Create your views here.
def pick(request):
    name = 'yeo_eun'
    number = random.randrange(1,45)
    return render(request, 'result.html', {'name': name, 'number': number})
