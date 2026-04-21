from datetime import datetime
from wallet.domain.transaction.money import Money
from wallet.domain.transaction.transaction import Transaction
from wallet.domain.transaction.transaction_type import TransactionType

class TransactionService:
    @staticmethod
    def transfer(debit_account, credit_account, amount: Money, category: str, note: str=None):
        debit_tx = Transaction(
            account_id=debit_account.id,
            amount=Money(-amount.amount, amount.currency),
            date=datetime.now(),
            type=TransactionType.TRANSFER,
            category=category,
            note=note
        )

        credit_tx = Transaction(
            account_id=credit_account.id,
            amount=amount,
            date=datetime.now(),
            type=TransactionType.TRANSFER,
            category=category,
            note=note
        )

        return debit_tx, credit_tx