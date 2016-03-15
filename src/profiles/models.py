from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver

from allauth.socialaccount.signals import social_account_added

from .utils import get_youtube_subscriptions


@receiver(social_account_added)
def new_social_account(request, sociallogin, **kwargs):
    print(get_youtube_subscriptions(sociallogin.token.token))
