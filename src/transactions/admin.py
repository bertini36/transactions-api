import io
from csv import reader

from django.contrib import admin, messages

from .actions import create_transactions
from .models import Transaction, UploadedCSVFile


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'account', 'amount')


@admin.register(UploadedCSVFile)
class UploadedCSVFileAdmin(admin.ModelAdmin):
    fields = ('file',)
    list_display = ('filename',)

    def save_model(self, request, obj, form, change):
        obj.filename = obj.file.name
        raw_transactions = io.StringIO(obj.file.read().decode('utf-8'))
        csv_reader = reader(raw_transactions)
        next(csv_reader)  # Ignore header
        raw_transactions = list(csv_reader)
        transactions = create_transactions(raw_transactions)
        messages.add_message(
            request,
            messages.SUCCESS,
            f'{len(transactions)} transactions have been registered'
        )
        obj.save()
