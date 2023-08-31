from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES=(
        ("ad", "admin"),
        ("md", "moderator"),
        ("us", "user"),
    )

    role=models.CharField(max_length=5, choices=ROLE_CHOICES)
    created_at=models.DateField(auto_now_add=True)
    created_by=models.ForeignKey("self",on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.get_full_name} {self.role}'