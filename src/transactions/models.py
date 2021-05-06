from django.db import models


class Transaction(models.Model):
    date = models.DateField(blank=False)
    account = models.IntegerField(blank=False)
    amount = models.FloatField(blank=False)

    def __str__(self) -> str:
        return f'[{self.date}] {self.account} {self.amount}'

    class Meta:
        verbose_name = 'transaction'
        verbose_name_plural = 'transactions'
        db_table = 'transactions'
