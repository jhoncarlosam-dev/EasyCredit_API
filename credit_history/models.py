from django.db import models

class CreditHistory(models.Model):
  
  date = models.DateField() 
  old_status = models.CharField(max_length=50)  
  new_status = models.CharField(max_length=50)

  def __str__(self) -> str:
    return f"Credit History: Date - {self.date}, Old Status - {self.old_status}, New Status - {self.new_status}"