from enum import Enum
from dataclasses import dataclass
from datetime import datetime, timedelta

class RecurrenceFrequency(Enum):
    NONE = "NONE"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"

@dataclass(frozen=True)
class Recurrence:
    frequency: RecurrenceFrequency = RecurrenceFrequency.NONE

    def next_date(self, current_date: datetime) -> datetime | None:
        if self.frequency == RecurrenceFrequency.DAILY:
            return current_date + timedelta(days=1)
        elif self.frequency == RecurrenceFrequency.WEEKLY:
            return current_date + timedelta(weeks=1)
        elif self.frequency == RecurrenceFrequency.MONTHLY:
            return current_date + timedelta(days=30)
        elif self.frequency == RecurrenceFrequency.YEARLY:
            return current_date + timedelta(days=365)
        return None