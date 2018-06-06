from django.contrib import admin
from .models import Module,Training,Group,Student,Event,Trainer,Payment
# Register your models here.

admin.site.register(Module)
admin.site.register(Training)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Trainer)
admin.site.register(Event)
admin.site.register(Payment)