from django.contrib import admin
from .models import  *



class Order_imgAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Order_img._meta.fields]



    # exclude = ["email"]

    class Meta:
        model = Order_img


admin.site.register(Order_img, Order_imgAdmin)


class UnitAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Unit._meta.fields]



    # exclude = ["email"]

    class Meta:
        model = Unit


admin.site.register(Unit, UnitAdmin)



class StatusAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]



    # exclude = ["email"]

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)