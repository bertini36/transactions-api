from django.db import models
from django.db.models import QuerySet, Sum


class TransactionQuerySet(models.QuerySet):
    def account_balances(self) -> QuerySet:
        return (
            self.values('account')
            .order_by('account')
            .annotate(balance=Sum('amount'))
        )


class Transaction(models.Model):
    date = models.DateField(blank=False)
    account = models.IntegerField(blank=False)
    amount = models.FloatField(blank=False)

    objects = TransactionQuerySet.as_manager()

    def __str__(self) -> str:
        return f'[{self.date}] {self.account} {self.amount}'

    class Meta:
        verbose_name = 'transaction'
        verbose_name_plural = 'transactions'
        db_table = 'transactions'


class UploadedCSVFile(models.Model):
    filename = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/%Y/%m/%d')

    def __str__(self) -> str:
        return self.filename

    class Meta:
        verbose_name = 'uploaded CSV file'
        verbose_name_plural = 'uploaded CSV files'
