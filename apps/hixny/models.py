from django.db import models
from django.contrib.auth import get_user_model
from ..accounts.models import UserProfile
# Copyright Videntity Systems Inc.
__author__ = "Alan Viars"


class HIXNYProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,
                                db_index=True, null=False)
    mrn = models.CharField(max_length=64, default='', blank=True)
    stageuser_password = models.CharField(
        max_length=64, default='', blank=True)
    stageuser_token = models.CharField(max_length=64, default='', blank=True)
    data_requestor = models.CharField(
        max_length=64, default='ActualCBOUser', blank=True)
    terms_accepted = models.TextField(default='', blank=True)
    terms_string = models.TextField(default='', blank=True)
    user_accept = models.BooleanField(default=False, blank=True)
    cda_content = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        display = '%s %s (%s)' % (self.user.first_name,
                                  self.user.last_name,
                                  self.user.username)
        return display

    @property
    def consent_to_share_data(self):
        if self.user_accept is True:
            return '1'
        return '0'

    @property
    def subject(self):
        up, g_or_c = UserProfile.objects.get_or_create(user=self.user)
        return up.subject

    @property
    def terms_string_stripped(self):
        return self.terms_string.strip('\\n').strip('\\t')
