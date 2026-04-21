import datetime
from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(frozen=True, eq=False, kw_only=True)
class Event:
    id_: UUID = field(default_factory=uuid4)
    occured_at: datetime.datetime = field(default_factory=datetime.datetime.now)
    aggregate_id: UUID

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, type(self)):
            return False

        return self.id_ == value.id_

    def __hash__(self) -> int:
        return hash(self.id_)