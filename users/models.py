from django.db import models

class CreateUsers(models.Model):
  
  name = models.CharField(max_length=511, null=False)
  credit_score = models.IntegerField(default=0)

  def __str__(self) -> str:
    return self.name