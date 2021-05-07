import io

from django.contrib import admin, messages

from .actions import create_transactions
from .models import Transaction, UploadedCSVFile
from .utils import get_raw_transactions_from_read_obj


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'account', 'amount')


@admin.register(UploadedCSVFile)
class UploadedCSVFileAdmin(admin.ModelAdmin):
    fields = ('file',)
    list_display = ('filename',)

    def save_model(self, request, obj, form, change):
        obj.filename = obj.file.name
        read_obj = io.StringIO(obj.file.read().decode('utf-8'))
        raw_transactions = get_raw_transactions_from_read_obj(read_obj)
        transactions = create_transactions(raw_transactions)
        messages.add_message(
            request,
            messages.SUCCESS,
            f'{len(transactions)} transactions have been registered',
        )
        super().save_model(request, obj, form, change)
