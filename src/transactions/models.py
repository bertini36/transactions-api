from django.db import models
from django.db.models import CharField, F, QuerySet, Sum, Value
from django.db.models.functions import Concat


class TransactionQuerySet(models.QuerySet):
    def annual_balance(self, account: int = None, year: int = None) -> QuerySet:
        kwargs = {}
        if account:
            kwargs['account'] = account
        if year:
            kwargs['date__year'] = year

        return (
            self.filter(**kwargs)
            .values('account')
            .order_by('account')
            .annotate(balance=Sum('amount'))
        )

    def monthly_balance(
        self, account: int = None, year: int = None, month: int = None
    ) -> QuerySet:
        kwargs = {}
        if account:
            kwargs['account'] = account
        if year and month:
            kwargs['date__year'] = year
            kwargs['date__month'] = month

        return (
            self.filter(**kwargs)
            .values('account', 'date__month')
            .order_by('account', 'date__month')
            .annotate(balance=Sum('amount'))
            .annotate(
                month=Concat(
                    F('date__year'),
                    Value('-'),
                    F('date__month'),
                    output_field=CharField(),
                )
            )
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
