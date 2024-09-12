
from django.db import models
from django.contrib.auth.models import User
class IntermediaryCloudAccess(models.Model):
    broker_agent_name = models.CharField(max_length=255)
    tin_no = models.CharField(max_length=15)
    vrn_registered = models.BooleanField()
    vrn_no = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    company_email = models.EmailField()
    tin_document = models.FileField(upload_to='tin_document')
    tira_cert = models.FileField(upload_to='tira_cert')
    brela_document = models.FileField(upload_to='brela_document' )
    vrn_document = models.FileField(upload_to='vrn_document', blank=True, null=True)

def __str__(self):
        return self.broker_agent_name


class CCEmail(models.Model):
    intermediary_cloud_access = models.ForeignKey(IntermediaryCloudAccess, related_name='cc_emails', on_delete=models.CASCADE)
    cc_email = models.EmailField()

def __str__(self):
        return self.cc_email


class CloudAccessEmail(models.Model):
    intermediary_cloud_access = models.ForeignKey(IntermediaryCloudAccess, related_name='cloud_access_emails', on_delete=models.CASCADE)
    cloud_access_email = models.EmailField()
def __str__(self):
        return self.cloud_access_email

