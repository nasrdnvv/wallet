from dataclasses import dataclass, field
from uuid import UUID

from wallet.domain.base.event import Event

@dataclass(eq=False, kw_only=True)
class Entity:
    id_: UUID

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, type(self)):
            return False
        return self.id_ == value.id_

    def __hash__(self) -> int:
        return hash(self.id_)

@dataclass(kw_only=True)
class AggregateRoot(Entity):
    _events: list[Event] = field(default_factory=list, repr=False)

    def _record_event(self, event: Event) -> None:
        self._events.append(event)

    @property
    def events(self) -> list[Event]:
        return self._events