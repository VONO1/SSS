from django.shortcuts import  render

def landing(request):
    name = 'pes'
    return render(request, 'landing/landing.html', locals())