from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP

@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: str

    def __post_init__(self):
        object.__setattr__(self, "amount",
                           self.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
        if self.amount < 0:
            raise ValueError("Money cannot be negative")


def __add__(self, other: "Money") -> "Money":
    self._check_currency(other)
    return Money(self.amount + other.amount, self.currency)


def __sub__(self, other: "Money") -> "Money":
    self._check_currency(other)

    result = self.amount - other.amount
    if result < 0:
        raise ValueError("Money cannot go negative")

    return Money(result, self.currency)


def __lt__(self, other: "Money") -> bool:
    self._check_currency(other)
    return self.amount < other.amount


def __le__(self, other: "Money") -> bool:
    return self < other or self == other

def _check_currency(self, other: "Money"):
    if self.currency != other.currency:
        raise ValueError(
            f"Currency mismatch: {self.currency} != {other.currency}"
        )