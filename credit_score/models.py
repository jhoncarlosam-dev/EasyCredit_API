from django.db import models

class CreditScore(models.Model):
    id = models.AutoField(primary_key=True)  # Django genera automáticamente un ID único
    score = models.IntegerField()
    calculation_date = models.DateField()

    def __str__(self):
        return f"Puntuación de crédito: {self.score} (calculada el {self.calculation_date})"