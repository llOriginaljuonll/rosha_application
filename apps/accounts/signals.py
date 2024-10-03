from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def set_judge_status(sender, instance, **kwargs):
    # ตรวจสอบว่า instance กำลังอัปเดตหรือไม่
    if not getattr(instance, '_is_updating_judge', False):
        instance._is_updating_judge = True  # ตั้ง flag เพื่อป้องกัน recursion error
        instance.is_judge = instance.is_staff or instance.is_superuser
        instance.save(update_fields=['is_judge'])
