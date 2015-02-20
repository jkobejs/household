from django.test import TestCase
from transaction.models import Transaction

class TransactionTestCase(TestCase):
    def setUp(self):
        Transaction.objects.create(id=1,
            description="Deposit initial sum of cash,",
            amount=400,
            transaction_type=True    )
        Transaction.objects.create(id=2,
            description="Bought cheese, brad, salam and milk.",
            amount=40,
            transaction_type=True)

    def test_transactions_has_amount(self):
        """Transactions have amount"""
        first_transaction = Transaction.objects.get(id=1)
        second_transaction = Transaction.objects.get(id=2)
        self.assertEqual(first_transaction.amount, 400)
        self.assertEqual(second_transaction.amount, 40)
