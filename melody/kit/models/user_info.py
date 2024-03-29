from typing import Optional

from attrs import define
from edgedb import Object
from typing_extensions import Self

from melody.kit.models.base import Base, BaseData
from melody.shared.converter import CONVERTER

__all__ = ("UserInfo", "UserInfoData")


class UserInfoData(BaseData):
    verified: bool
    email: str
    password_hash: str
    secret: Optional[str]


@define(kw_only=True)
class UserInfo(Base):
    verified: bool
    email: str
    password_hash: str
    secret: Optional[str] = None

    @classmethod
    def from_object(cls, object: Object) -> Self:
        return cls(
            id=object.id,
            verified=object.verified,
            email=object.email,
            password_hash=object.password_hash,
            secret=object.secret,
        )

    @classmethod
    def from_data(cls, data: UserInfoData) -> Self:  # type: ignore[override]
        return CONVERTER.structure(data, cls)

    def into_data(self) -> UserInfoData:
        return CONVERTER.unstructure(self)  # type: ignore[no-any-return]

    def is_verified(self) -> bool:
        return self.verified

    def is_totp_enabled(self) -> bool:
        return self.secret is not None
