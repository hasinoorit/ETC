from django.db import models


# Create your models here.
class Cost(models.Model):
    purpose = models.CharField(max_length=220)
    cost_type = models.CharField(max_length=10)
    amount = models.PositiveIntegerField()
    balance = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.purpose
