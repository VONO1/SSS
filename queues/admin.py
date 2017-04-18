from django.contrib import admin
from .models import  *




class QueueAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Queue._meta.fields]



    # exclude = ["email"]

    class Meta:
        model = Queue


admin.site.register(Queue, QueueAdmin)


class Queue_linksAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Queue_links._meta.fields]



    # exclude = ["email"]

    class Meta:
        model = Queue_links


admin.site.register(Queue_links, Queue_linksAdmin)