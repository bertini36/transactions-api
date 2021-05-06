from csv import reader

import structlog
from django.core.management import BaseCommand

from ...actions import create_transactions

logger = structlog.get_logger()


class Command(BaseCommand):
    help = (
        'Creates transactions in base a csv file. Each row of this CSV '
        'file must have the transaction day (yyyy-mm-dd), the associated '
        'account id and the amount'
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--csv-file',
            dest='csv_file',
            help='Path to CSV file',
            default='sample-data.csv',
        )

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        logger.info('load-transactions-csv', csv_file=csv_file)
        with open(options['csv_file'], 'r') as read_obj:
            csv_reader = reader(read_obj)
            next(csv_reader)  # Ignore header
            raw_transactions = list(csv_reader)

        transactions = create_transactions(raw_transactions)
        logger.info(
            'load-transactions-csv', created_transactions=len(transactions)
        )
