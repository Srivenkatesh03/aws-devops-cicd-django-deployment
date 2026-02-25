from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Student
import os

@receiver(post_delete, sender=Student)
def delete_student_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

import os
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Student


@receiver(pre_save, sender=Student)
def delete_old_image_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_instance = Student.objects.get(pk=instance.pk)
    except Student.DoesNotExist:
        return

    old_image = old_instance.image
    new_image = instance.image

    if old_image and old_image != new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
