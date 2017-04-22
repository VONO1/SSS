from django.db import models
#Импортируем список сотрудников, подписанных на рассылки
from landing.models import Subscriber
#from queues.models import Queue_links




#Статус заказа
class Status(models.Model):
    #name = models.CharField(max_length=24, blank=True, null=True, default=None)
    #Состояние
    is_active = models.BooleanField(default=True)

    #Вносим автоматически информацию, когда объект создаётся или изменяется
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус : %s" % (self.is_active)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'


#Изображение заявки
class Order_img(models.Model):
    #image = models.ForeignKey(Queue, blank=True, null=True, default=None)
    #order  = models.ForeignKey(Queue_links, blank=True, null=True, default=None)
    img = models.ImageField(upload_to='img/')


    def __str__(self):
        return "Заявка на оборудование"

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'


#Звено цепи согласования
class Unit(models.Model):
    #ссылка на сотрудника
    user = models.ForeignKey(Subscriber, blank=True, null=True)
    #Состояние
    status = models.ForeignKey(Status)

    #Вносим автоматически информацию, когда объект создаётся или изменяется
    created = models.DateTimeField(auto_now_add=False, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        #return "юнит"
        return "Статус : %s с состоянием: %s" % (self.user, self.status.is_active)

    class Meta:
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'

