from django.db import models

class Expenses(models.Model):
    expenses_id = models.BigAutoField(primary_key=True)
    expenses_total_cost = models.FloatField(default=0.0)
    expenses_date = models.DateField()

    def __str__(self) -> str:
        return f'{self.expenses_date}'

class ExpensesDetails(models.Model):
    expenses_details_id = models.BigAutoField(primary_key=True)
    expenses_for = models.TextField()
    expenses_cost = models.FloatField(default=0.0)
    expenses = models.ForeignKey(Expenses, on_delete=models.DO_NOTHING, related_name='expenses_details')

    def __str__(self) -> str:
        return f'{self.expenses_for}'