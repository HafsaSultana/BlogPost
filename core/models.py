from django.db import models

# Create your models here.

from account.models import User

class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="created_%(app_label)s_%(class)s")
    updated_by=models.ForeignKey(User, null=True, on_delete=models.SET_NULL,  related_name="updated_%(app_label)s_%(class)s")

    class Meta:
        abstract=True