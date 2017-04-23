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
    #передаём все заявки
    Qu_allq = Qu


    #print(Qu.q_applications2.id)
    z = []
    for v in Qu:
        if v.q_applications2.id == 1:
            z.append(v)
            print(v.q_applications2.id)
        #print(z)


    #передаём только заявки пользователя
    Qu_meq = z

    return render(request, 'landing/home.html', locals())