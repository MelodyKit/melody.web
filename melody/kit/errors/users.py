from typing import Optional
from uuid import UUID

from fastapi import status

from melody.kit.errors.core import Error, ErrorCode
from melody.kit.errors.decorators import default_code, default_status_code

__all__ = (
    "UserError",
    "UserNotFound",
    "UserInaccessible",
    "UserImageNotFound",
    "UserFollowSelfForbidden",
    "UserFollowSelfPlaylistsForbidden",
)


@default_code(ErrorCode.USER_ERROR)
class UserError(Error):
    def __init__(
        self,
        user_id: UUID,
        message: str,
        code: Optional[ErrorCode] = None,
        status_code: Optional[int] = None,
    ) -> None:
        super().__init__(message, code, status_code)

        self._user_id = user_id

    @property
    def user_id(self) -> UUID:
        return self._user_id


USER_NOT_FOUND = "user `{}` not found"
user_not_found = USER_NOT_FOUND.format


@default_code(ErrorCode.USER_NOT_FOUND)
@default_status_code(status.HTTP_404_NOT_FOUND)
class UserNotFound(UserError):
    def __init__(self, user_id: UUID) -> None:
        super().__init__(user_id, user_not_found(user_id))


USER_INACCESSIBLE = "user `{}` is inaccessible"
user_inaccessible = USER_INACCESSIBLE.format


@default_code(ErrorCode.USER_INACCESSIBLE)
@default_status_code(status.HTTP_403_FORBIDDEN)
class UserInaccessible(UserError):
    def __init__(self, user_id: UUID) -> None:
        super().__init__(user_id, user_inaccessible(user_id))


USER_IMAGE_NOT_FOUND = "user `{}` image not found"
user_image_not_found = USER_IMAGE_NOT_FOUND.format


@default_code(ErrorCode.USER_IMAGE_NOT_FOUND)
@default_status_code(status.HTTP_404_NOT_FOUND)
class UserImageNotFound(UserError):
    def __init__(self, user_id: UUID) -> None:
        super().__init__(user_id, user_image_not_found(user_id))


USER_CAN_NOT_FOLLOW_SELF = "user `{}` can not follow themselves"
user_can_not_follow_self = USER_CAN_NOT_FOLLOW_SELF.format


@default_code(ErrorCode.USER_FOLLOW_SELF_FORBIDDEN)
@default_status_code(status.HTTP_403_FORBIDDEN)
class UserFollowSelfForbidden(UserError):
    def __init__(self, user_id: UUID) -> None:
        super().__init__(user_id, user_can_not_follow_self(user_id))


USER_CAN_NOT_FOLLOW_SELF_PLAYLISTS = "user `{}` can not follow their own playlists"
user_can_not_follow_self_playlists = USER_CAN_NOT_FOLLOW_SELF_PLAYLISTS.format


@default_code(ErrorCode.USER_FOLLOW_SELF_PLAYLISTS_FORBIDDEN)
@default_status_code(status.HTTP_403_FORBIDDEN)
class UserFollowSelfPlaylistsForbidden(UserError):
    def __init__(self, user_id: UUID) -> None:
        super().__init__(user_id, user_can_not_follow_self_playlists(user_id))
