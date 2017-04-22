from django.db import models
#импортируем список пользователей
from landing.models import Subscriber
from applications.models import Unit


#Свойства очереди
class Queue(models.Model):
    #Последовательность согласования
    queue_test = [1,2,3]
    #Инициатор закупки
    #initiator = models.CharField(max_length=128, blank=False,default=None)
    #initiatorr = models.ForeignKey(Subscriber, blank=True, null=True, default=None)
    #Объект закупки
    initiator_obj = models.CharField(max_length=128)
    # Материально отвественный
    initiator_liable = models.CharField(max_length=128)
    #Инициатор закупки
    initiator_phone = models.CharField(max_length=128, blank=False,default=None)
    #состав заявки(пока текст) (в будущем заявка будет подгружаться отдельным файлом, а данное поле станет комментарием)
    comments = models.TextField(blank=True, null=True, default=None)
    #Изображение
    img = models.ImageField(upload_to='img/', blank=True, default=None)
    #Вносим автоматически информацию, когда объект создаётся или изменяется
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ на : %s  с id: %s" % (self.initiator_obj,  self.id)
        #return "Заказ на : %s от %s с id: %s" % (self.initiator_obj, self.initiator, self.id)

    class Meta:
        verbose_name = 'Queue'
        verbose_name_plural = 'Queues'

#Состав очереди
class Queue_links(models.Model):
    #is_active = True
    #Ссылка на таблицу с очередями
    q_links = models.ForeignKey(Queue, blank=True, default=None)

    #Ссылка на звено согласования (состав очереди)
    #q_applications = models.ForeignKey(Subscriber, blank=True, default=None)
    q_applications2 = models.ForeignKey(Unit, blank=True, default=None)

    #q_applications3 = models.ForeignKey(Unit, blank=True, default=None)
    #q_applications3 = models.ForeignKey(Subscriber, blank=True, default="cht-to")


    #Вносим автоматически информацию, когда объект создаётся или изменяется
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Очередь: %s с id: %s" % (self.q_links, self.q_applications2)

    class Meta:
        verbose_name = 'Conference'
        verbose_name_plural = 'Conference'