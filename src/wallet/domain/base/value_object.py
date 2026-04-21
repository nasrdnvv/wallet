from abc import ABC, abstractmethod
from dataclasses import astuple, dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class ValueObject(ABC):
    def __post_init__(self) -> None:
        self._validate()

    @abstractmethod
    def _validate(self) -> None: ...

    def __composit_values__(self) -> tuple[str]:
        return astuple(self)


@dataclass(frozen=True)
class CommonValueObject(ValueObject, Generic[T]):
    value: T