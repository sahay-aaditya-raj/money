from django.db import models

# Create your models here.

class Payement(models.Model):
    
    type = models.TextField(max_length=100)
    
    def __str__(self):
        return self.type
    
class ExpenseType(models.Model):
    expense_type = models.TextField(max_length=100)
    
    def __str__(self):
        return self.expense_type
    
class Entry(models.Model):
    
    type = models.ForeignKey(Payement, blank=False, null=False, on_delete=models.CASCADE)
    exp_type = models.ForeignKey(ExpenseType,on_delete=models.CASCADE)
    description = models.TextField(max_length=100, blank=True)
    amount = models.FloatField(null=False, blank=False)
    date = models.DateField()
    
    def __str__(self):
        return str(self.description[:40])
    
    
