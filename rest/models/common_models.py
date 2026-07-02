from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict

T = TypeVar("T")

class DataWrapper(BaseModel, Generic[T]):
    model_config = ConfigDict(frozen=True)

    data: T