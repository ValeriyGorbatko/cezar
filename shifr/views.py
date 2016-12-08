from django.shortcuts import render

def index(request):
    if request.POST: # проверяешь что пришел ПОСТ, тогда берез из него данные
        orig = request.POST['original']
        ste = request.POST['step']
    return render(request, 'shifr/index.html', {'key': orig})
