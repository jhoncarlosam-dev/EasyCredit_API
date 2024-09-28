from django.db import models

# Create your models here.
class CreateCredit(models.Model):
  STATUSES = {
    "active": "Active",
    "canceled": "Inactive",
    "finalized": "Finalized",
  } 
  name = models.CharField(max_length=511, null=False)
  status = models.CharField(max_length=55, choices=STATUSES)

  def __str__(self) -> str:
    return self.name
  
  