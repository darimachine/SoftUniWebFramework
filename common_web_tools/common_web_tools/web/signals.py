from django.db.models import signals
from django.dispatch import receiver

from common_web_tools.web.models import Profile


@receiver(signals.pre_save,sender=Profile)
def profile_created(instance,sender,**kwargs):
    print(f"Pre create: {instance}")

@receiver(signals.post_save,sender=Profile)
def profile_created(instance,sender,**kwargs):
    print(f"Post create: {instance}")