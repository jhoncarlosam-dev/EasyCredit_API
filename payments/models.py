from django.db import models

class Payment(models.Model):
    id = models.AutoField(primary_key=True)  # Django genera automáticamente un ID único
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Pago de ${self.amount} el {self.payment_date} por {self.payment_method}"