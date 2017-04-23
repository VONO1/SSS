from django.shortcuts import  render
from queues.models import Queue_links


def queue(request, queue_id):
    queue = Queue_links.objects.get(id=queue_id)
    return render(request, 'queues/queue.html', locals())