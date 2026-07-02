import dataclasses

@dataclasses.dataclass(frozen=True)
class Account:
    id: str
    code: str
    name: str
    active: bool
