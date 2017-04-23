from django.shortcuts import  render
from .forms import SubscriberForm
from queues.models import Queue_links

def landing(request):
    name = 'pes'
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        new_form = form.save()
    return render(request, 'landing/landing.html', locals())



def home(request):
    Qu = Queue_links.objects.all()
    Qu_allq = Qu.filter(q_applications2__id=1)
    Qu_meq = Qu.filter(q_applications2__id=1)
    return render(request, 'landing/home.html', locals())