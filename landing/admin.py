from django.contrib import admin
from .models import  *




class SubscriberAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ('rank',)
    search_fields =['name', 'email', 'id']
    fields = ['name']

    # exclude = ["email"]

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)