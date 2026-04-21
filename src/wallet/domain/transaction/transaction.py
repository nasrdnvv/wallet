from dataclasses import dataclass, field
from uuid import uuid4
from datetime import datetime
from wallet.domain.base.entity import AggregateRoot
from wallet.domain.transaction.money import Money
from wallet.domain.transaction.transaction_type import TransactionType
from wallet.domain.transaction.status import TransactionStatus
from wallet.domain.transaction.recurrence import Recurrence


@dataclass
class Transaction(AggregateRoot):
    account_id: str
    amount: Money
    date: datetime
    type: TransactionType
    category: str
    note: str | None = None
    recurrence: Recurrence = field(default_factory=Recurrence)
    status: TransactionStatus = TransactionStatus.PENDING
    id: str = field(default_factory=lambda: str(uuid4()))

    def confirm(self):
        self.status = TransactionStatus.CONFIRMED

    def schedule_next(self):
        return self.recurrence.next_date(self.date)
