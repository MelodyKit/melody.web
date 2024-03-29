from pathlib import Path
from typing import Any, TypeVar, final

from attrs import define
from pendulum import Duration, duration
from toml import loads as load_string
from typing_aliases import IntoPath, StringDict
from typing_extensions import Self
from wraps.option import Option
from wraps.wraps import wrap_optional

from melody.kit.constants import DEFAULT_IGNORE_SENSITIVE
from melody.kit.enums import ErrorCorrection, LogLevel
from melody.shared.constants import DEFAULT_ENCODING, DEFAULT_ERRORS, EMPTY, HOME, ROOT

__all__ = ("CONFIG", "Config", "ConfigData", "get_config", "get_default_config")

T = TypeVar("T")


def ensure_directory(path: Path) -> Path:
    directory = path.expanduser()

    directory.mkdir(parents=True, exist_ok=True)

    return directory


CONFIG_NAME = ".config"
MELODY_NAME = "melody"

NAME = "kit.toml"

DEFAULT_PATH = ROOT / NAME
PATH = HOME / CONFIG_NAME / MELODY_NAME / NAME


def ensure_file(path: Path, default_path: Path) -> None:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)

        path.write_bytes(default_path.read_bytes())


ensure_file(PATH, DEFAULT_PATH)


class ConfigData(StringDict[T]):
    def __getattr__(self, name: str) -> Option[T]:
        return wrap_optional(self.get(name))


AnyConfigData = ConfigData[Any]


@define()
class EmailMessageConfig:
    subject: str
    content: str


@define()
class EmailConfig:
    host: str
    port: int
    support: str
    name: str
    password: str
    verification: EmailMessageConfig
    temporary: EmailMessageConfig


@define()
class HashConfig:
    time_cost: int
    memory_cost: int
    parallelism: int


@define()
class KitConfig:
    host: str
    port: int


@define()
class CodeConfig:
    cache: Path
    error_correction: ErrorCorrection
    box_size: int
    border: int


@define()
class ImageConfig:
    path: Path
    size_limit: int
    data_size_limit: int


@define()
class LogConfig:
    level: LogLevel


@define()
class RedisConfig:
    host: str
    port: int


@define()
class SecretConfig:
    size: int


@define()
class TOTPConfig:
    digits: int
    interval: int
    valid_window: int


@define()
class ExpiresConfig:
    years: float
    months: float
    weeks: float
    days: float
    hours: float
    minutes: float
    seconds: float

    @property
    def duration(self) -> Duration:
        return duration(
            years=self.years,
            months=self.months,
            weeks=self.weeks,
            days=self.days,
            hours=self.hours,
            minutes=self.minutes,
            seconds=self.seconds,
        )


@define()
class SpecificConfig:
    size: int
    expires: ExpiresConfig


@define()
class AccessConfig(SpecificConfig):
    pass


@define()
class RefreshConfig(SpecificConfig):
    pass


@define()
class TokenConfig:
    type: str

    access: AccessConfig
    refresh: RefreshConfig


@define()
class AuthorizationConfig(SpecificConfig):
    pass


@define()
class VerificationConfig(SpecificConfig):
    pass


@define()
class WebConfig:
    host: str
    port: int


@define()
class BotConfig:
    token: str


@define()
class ClientConfig:
    client_id: str
    client_secret: str


EXPECTED = "expected `{}`"
expected = EXPECTED.format


EXPECTED_MELODY = expected("melody")
EXPECTED_MELODY_NAME = expected("melody.name")
EXPECTED_MELODY_DOMAIN = expected("melody.domain")
EXPECTED_MELODY_OPEN = expected("melody.open")
EXPECTED_MELODY_SESSION_KEY = expected("melody.session_key")
EXPECTED_MELODY_EMAIL = expected("melody.email")
EXPECTED_MELODY_EMAIL_HOST = expected("melody.email.host")
EXPECTED_MELODY_EMAIL_PORT = expected("melody.email.port")
EXPECTED_MELODY_EMAIL_SUPPORT = expected("melody.email.support")
EXPECTED_MELODY_EMAIL_NAME = expected("melody.email.name")
EXPECTED_MELODY_EMAIL_PASSWORD = expected("melody.email.password")
EXPECTED_MELODY_EMAIL_VERIFICATION = expected("melody.email.verification")
EXPECTED_MELODY_EMAIL_VERIFICATION_SUBJECT = expected("melody.email.verification.subject")
EXPECTED_MELODY_EMAIL_VERIFICATION_CONTENT = expected("melody.email.verification.content")
EXPECTED_MELODY_EMAIL_TEMPORARY = expected("melody.email.temporary")
EXPECTED_MELODY_EMAIL_TEMPORARY_SUBJECT = expected("melody.email.temporary.subject")
EXPECTED_MELODY_EMAIL_TEMPORARY_CONTENT = expected("melody.email.temporary.content")
EXPECTED_MELODY_HASH = expected("melody.hash")
EXPECTED_MELODY_HASH_TIME_COST = expected("melody.hash.time_cost")
EXPECTED_MELODY_HASH_MEMORY_COST = expected("melody.hash.memory_cost")
EXPECTED_MELODY_HASH_PARALLELISM = expected("melody.hash.parallelism")
EXPECTED_MELODY_KIT = expected("melody.kit")
EXPECTED_MELODY_KIT_HOST = expected("melody.kit.host")
EXPECTED_MELODY_KIT_PORT = expected("melody.kit.port")
EXPECTED_MELODY_CODE = expected("melody.code")
EXPECTED_MELODY_CODE_CACHE = expected("melody.code.cache")
EXPECTED_MELODY_CODE_ERROR_CORRECTION = expected("melody.code.error_correction")
EXPECTED_MELODY_CODE_BOX_SIZE = expected("melody.code.box_size")
EXPECTED_MELODY_CODE_BORDER = expected("melody.code.border")
EXPECTED_MELODY_IMAGE = expected("melody.image")
EXPECTED_MELODY_IMAGE_PATH = expected("melody.image.path")
EXPECTED_MELODY_IMAGE_SIZE_LIMIT = expected("melody.image.size_limit")
EXPECTED_MELODY_IMAGE_DATA_SIZE_LIMIT = expected("melody.image.data_size_limit")
EXPECTED_MELODY_LOG = expected("melody.log")
EXPECTED_MELODY_LOG_LEVEL = expected("melody.log.level")
EXPECTED_MELODY_REDIS = expected("melody.redis")
EXPECTED_MELODY_REDIS_HOST = expected("melody.redis.host")
EXPECTED_MELODY_REDIS_PORT = expected("melody.redis.port")
EXPECTED_MELODY_SECRET = expected("melody.secret")
EXPECTED_MELODY_SECRET_SIZE = expected("melody.secret.size")
EXPECTED_MELODY_TOTP = expected("melody.totp")
EXPECTED_MELODY_TOTP_DIGITS = expected("melody.totp.digits")
EXPECTED_MELODY_TOTP_INTERVAL = expected("melody.totp.interval")
EXPECTED_MELODY_TOTP_VALID_WINDOW = expected("melody.totp.valid_window")
EXPECTED_MELODY_TOKEN = expected("melody.token")
EXPECTED_MELODY_TOKEN_TYPE = expected("melody.token.type")
EXPECTED_MELODY_TOKEN_ACCESS = expected("melody.token.access")
EXPECTED_MELODY_TOKEN_ACCESS_SIZE = expected("melody.token.access.size")
EXPECTED_MELODY_TOKEN_ACCESS_EXPIRES = expected("melody.token.access.expires")
EXPECTED_MELODY_TOKEN_ACCESS_EXPIRES_YEARS = expected("melody.token.access.expires.years")
EXPECTED_MELODY_TOKEN_ACCESS_EXPIRES_MONTHS = expected("melody.token.access.expires.months")
EXPECTED_MELODY_TOKEN_ACCESS_EXPIRES_WEEKS = expected("melody.token.access.expires.weeks")
EXPECTED_MELODY_TOKEN_ACCESS_EXPIRES_DAYS = expected("melody.token.access.expires.days")
EXPECTED_MELODY_TOKEN_ACCESS_EXPIRES_HOURS = expected("melody.token.access.expires.hours")
EXPECTED_MELODY_TOKEN_ACCESS_EXPIRES_MINUTES = expected("melody.token.access.expires.minutes")
EXPECTED_MELODY_TOKEN_ACCESS_EXPIRES_SECONDS = expected("melody.token.access.expires.seconds")
EXPECTED_MELODY_TOKEN_REFRESH = expected("melody.token.refresh")
EXPECTED_MELODY_TOKEN_REFRESH_SIZE = expected("melody.token.refresh.size")
EXPECTED_MELODY_TOKEN_REFRESH_EXPIRES = expected("melody.token.refresh.expires")
EXPECTED_MELODY_TOKEN_REFRESH_EXPIRES_YEARS = expected("melody.token.refresh.expires.years")
EXPECTED_MELODY_TOKEN_REFRESH_EXPIRES_MONTHS = expected("melody.token.refresh.expires.months")
EXPECTED_MELODY_TOKEN_REFRESH_EXPIRES_WEEKS = expected("melody.token.refresh.expires.weeks")
EXPECTED_MELODY_TOKEN_REFRESH_EXPIRES_DAYS = expected("melody.token.refresh.expires.days")
EXPECTED_MELODY_TOKEN_REFRESH_EXPIRES_HOURS = expected("melody.token.refresh.expires.hours")
EXPECTED_MELODY_TOKEN_REFRESH_EXPIRES_MINUTES = expected("melody.token.refresh.expires.minutes")
EXPECTED_MELODY_TOKEN_REFRESH_EXPIRES_SECONDS = expected("melody.token.refresh.expires.seconds")
EXPECTED_MELODY_AUTHORIZATION = expected("melody.authorization")
EXPECTED_MELODY_AUTHORIZATION_SIZE = expected("melody.authorization.size")
EXPECTED_MELODY_AUTHORIZATION_EXPIRES = expected("melody.authorization.expires")
EXPECTED_MELODY_AUTHORIZATION_EXPIRES_YEARS = expected("melody.authorization.expires.years")
EXPECTED_MELODY_AUTHORIZATION_EXPIRES_MONTHS = expected("melody.authorization.expires.months")
EXPECTED_MELODY_AUTHORIZATION_EXPIRES_WEEKS = expected("melody.authorization.expires.weeks")
EXPECTED_MELODY_AUTHORIZATION_EXPIRES_DAYS = expected("melody.authorization.expires.days")
EXPECTED_MELODY_AUTHORIZATION_EXPIRES_HOURS = expected("melody.authorization.expires.hours")
EXPECTED_MELODY_AUTHORIZATION_EXPIRES_MINUTES = expected("melody.authorization.expires.minutes")
EXPECTED_MELODY_AUTHORIZATION_EXPIRES_SECONDS = expected("melody.authorization.expires.seconds")
EXPECTED_MELODY_VERIFICATION = expected("melody.verification")
EXPECTED_MELODY_VERIFICATION_SIZE = expected("melody.verification.size")
EXPECTED_MELODY_VERIFICATION_EXPIRES = expected("melody.verification.expires")
EXPECTED_MELODY_VERIFICATION_EXPIRES_YEARS = expected("melody.verification.expires.years")
EXPECTED_MELODY_VERIFICATION_EXPIRES_MONTHS = expected("melody.verification.expires.months")
EXPECTED_MELODY_VERIFICATION_EXPIRES_WEEKS = expected("melody.verification.expires.weeks")
EXPECTED_MELODY_VERIFICATION_EXPIRES_DAYS = expected("melody.verification.expires.days")
EXPECTED_MELODY_VERIFICATION_EXPIRES_HOURS = expected("melody.verification.expires.hours")
EXPECTED_MELODY_VERIFICATION_EXPIRES_MINUTES = expected("melody.verification.expires.minutes")
EXPECTED_MELODY_VERIFICATION_EXPIRES_SECONDS = expected("melody.verification.expires.seconds")
EXPECTED_MELODY_WEB = expected("melody.web")
EXPECTED_MELODY_WEB_HOST = expected("melody.web.host")
EXPECTED_MELODY_WEB_PORT = expected("melody.web.port")
EXPECTED_MELODY_BOT = expected("melody.bot")
EXPECTED_MELODY_BOT_TOKEN = expected("melody.bot.token")
EXPECTED_MELODY_DISCORD = expected("melody.discord")
EXPECTED_MELODY_DISCORD_CLIENT_ID = expected("melody.discord.client_id")
EXPECTED_MELODY_DISCORD_CLIENT_SECRET = expected("melody.discord.client_secret")
EXPECTED_MELODY_SPOTIFY = expected("melody.spotify")
EXPECTED_MELODY_SPOTIFY_CLIENT_ID = expected("melody.spotify.client_id")
EXPECTED_MELODY_SPOTIFY_CLIENT_SECRET = expected("melody.spotify.client_secret")


@final
@define()
class Config:
    name: str
    domain: str
    open: str
    session_key: str
    email: EmailConfig
    hash: HashConfig
    kit: KitConfig
    code: CodeConfig
    image: ImageConfig
    log: LogConfig
    redis: RedisConfig
    secret: SecretConfig
    totp: TOTPConfig
    token: TokenConfig
    authorization: AuthorizationConfig
    verification: VerificationConfig
    web: WebConfig
    bot: BotConfig
    discord: ClientConfig
    spotify: ClientConfig

    def ensure_directories(self) -> Self:
        image = self.image

        image.path = ensure_directory(image.path)

        code = self.code

        code.cache = ensure_directory(code.cache)

        return self

    @classmethod
    def from_string(cls, string: str) -> Self:
        return cls.from_data(cls.parse(string))

    @classmethod
    def from_path(
        cls,
        path: IntoPath,
        encoding: str = DEFAULT_ENCODING,
        errors: str = DEFAULT_ERRORS,
    ) -> Self:
        return cls.from_string(Path(path).read_text(encoding, errors))

    @staticmethod
    def parse(string: str) -> AnyConfigData:
        return load_string(string, AnyConfigData)

    @classmethod
    def from_data(cls, data: AnyConfigData) -> Self:
        default_config = DEFAULT_CONFIG

        config_data = data.melody.unwrap_or_else(AnyConfigData)

        email_data = config_data.email.unwrap_or_else(AnyConfigData)
        email_config = default_config.email

        email_verification_data = email_data.verification.unwrap_or_else(AnyConfigData)
        email_verification_config = email_config.verification

        email_temporary_data = email_data.temporary.unwrap_or_else(AnyConfigData)
        email_temporary_config = email_config.temporary

        email = EmailConfig(
            host=email_data.host.unwrap_or(email_config.host),
            port=email_data.port.unwrap_or(email_config.port),
            support=email_data.support.unwrap_or(email_config.support),
            name=email_data.name.expect(EXPECTED_MELODY_EMAIL_NAME),
            password=email_data.password.expect(EXPECTED_MELODY_EMAIL_PASSWORD),
            verification=EmailMessageConfig(
                subject=email_verification_data.subject.unwrap_or(
                    email_verification_config.subject
                ),
                content=email_verification_data.content.unwrap_or(
                    email_verification_config.content
                ),
            ),
            temporary=EmailMessageConfig(
                subject=email_temporary_data.subject.unwrap_or(email_temporary_config.subject),
                content=email_temporary_data.content.unwrap_or(email_temporary_config.content),
            ),
        )

        hash_data = config_data.hash.unwrap_or_else(AnyConfigData)
        hash_config = default_config.hash

        hash = HashConfig(
            time_cost=hash_data.time_cost.unwrap_or(hash_config.time_cost),
            memory_cost=hash_data.memory_cost.unwrap_or(hash_config.memory_cost),
            parallelism=hash_data.parallelism.unwrap_or(hash_config.parallelism),
        )

        kit_data = config_data.kit.unwrap_or_else(AnyConfigData)
        kit_config = default_config.kit

        kit = KitConfig(
            host=kit_data.host.unwrap_or(kit_config.host),
            port=kit_data.port.unwrap_or(kit_config.port),
        )

        code_data = config_data.code.unwrap_or_else(AnyConfigData)
        code_config = default_config.code

        code = CodeConfig(
            cache=code_data.cache.map_or(code_config.cache, Path),
            error_correction=code_data.error_correction.map_or(
                code_config.error_correction, ErrorCorrection
            ),
            box_size=code_data.box_size.unwrap_or(code_config.box_size),
            border=code_data.border.unwrap_or(code_config.border),
        )

        image_data = config_data.image.unwrap_or_else(AnyConfigData)
        image_config = default_config.image

        image = ImageConfig(
            path=image_data.path.map_or(image_config.path, Path),
            size_limit=image_data.size_limit.unwrap_or(image_config.size_limit),
            data_size_limit=image_data.data_size_limit.unwrap_or(image_config.data_size_limit),
        )

        log_data = config_data.log.unwrap_or_else(AnyConfigData)
        log_config = default_config.log

        log = LogConfig(level=log_data.level.unwrap_or(log_config.level))

        redis_data = config_data.redis.unwrap_or_else(AnyConfigData)
        redis_config = default_config.redis

        redis = RedisConfig(
            host=redis_data.host.unwrap_or(redis_config.host),
            port=redis_data.port.unwrap_or(redis_config.port),
        )

        secret_data = config_data.secret.unwrap_or_else(AnyConfigData)
        secret_config = default_config.secret

        secret = SecretConfig(size=secret_data.size.unwrap_or(secret_config.size))

        totp_data = config_data.totp.unwrap_or_else(AnyConfigData)
        totp_config = default_config.totp

        totp = TOTPConfig(
            digits=totp_data.digits.unwrap_or(totp_config.digits),
            interval=totp_data.interval.unwrap_or(totp_config.interval),
            valid_window=totp_data.valid_window.unwrap_or(totp_config.valid_window),
        )

        token_data = config_data.token.unwrap_or_else(AnyConfigData)
        token_config = default_config.token

        access_data = token_data.access.unwrap_or_else(AnyConfigData)
        access_config = token_config.access

        access_expires_data = access_data.expires.unwrap_or_else(AnyConfigData)
        access_expires_config = access_config.expires

        refresh_data = token_data.refresh.unwrap_or_else(AnyConfigData)
        refresh_config = token_config.refresh

        refresh_expires_data = refresh_data.expires.unwrap_or_else(AnyConfigData)
        refresh_expires_config = refresh_config.expires

        token = TokenConfig(
            type=token_data.type.unwrap_or(token_config.type),
            access=AccessConfig(
                size=access_data.size.unwrap_or(access_config.size),
                expires=ExpiresConfig(
                    years=access_expires_data.years.unwrap_or(access_expires_config.years),
                    months=access_expires_data.months.unwrap_or(access_expires_config.months),
                    weeks=access_expires_data.weeks.unwrap_or(access_expires_config.weeks),
                    days=access_expires_data.days.unwrap_or(access_expires_config.days),
                    hours=access_expires_data.hours.unwrap_or(access_expires_config.hours),
                    minutes=access_expires_data.minutes.unwrap_or(access_expires_config.minutes),
                    seconds=access_expires_data.seconds.unwrap_or(access_expires_config.seconds),
                ),
            ),
            refresh=RefreshConfig(
                size=refresh_data.size.unwrap_or(refresh_config.size),
                expires=ExpiresConfig(
                    years=refresh_expires_data.years.unwrap_or(refresh_expires_config.years),
                    months=refresh_expires_data.months.unwrap_or(refresh_expires_config.months),
                    weeks=refresh_expires_data.weeks.unwrap_or(refresh_expires_config.weeks),
                    days=refresh_expires_data.days.unwrap_or(refresh_expires_config.days),
                    hours=refresh_expires_data.hours.unwrap_or(refresh_expires_config.hours),
                    minutes=refresh_expires_data.minutes.unwrap_or(refresh_expires_config.minutes),
                    seconds=refresh_expires_data.seconds.unwrap_or(refresh_expires_config.seconds),
                ),
            ),
        )

        authorization_data = config_data.authorization.unwrap_or_else(AnyConfigData)
        authorization_config = default_config.authorization

        authorization_expires_data = authorization_data.expires.unwrap_or_else(AnyConfigData)
        authorization_expires_config = authorization_config.expires

        authorization = AuthorizationConfig(
            size=authorization_data.size.unwrap_or(authorization_config.size),
            expires=ExpiresConfig(
                years=authorization_expires_data.years.unwrap_or(
                    authorization_expires_config.years
                ),
                months=authorization_expires_data.months.unwrap_or(
                    authorization_expires_config.months
                ),
                weeks=authorization_expires_data.weeks.unwrap_or(
                    authorization_expires_config.weeks
                ),
                days=authorization_expires_data.days.unwrap_or(authorization_expires_config.days),
                hours=authorization_expires_data.hours.unwrap_or(
                    authorization_expires_config.hours
                ),
                minutes=authorization_expires_data.minutes.unwrap_or(
                    authorization_expires_config.minutes
                ),
                seconds=authorization_expires_data.seconds.unwrap_or(
                    authorization_expires_config.seconds
                ),
            ),
        )

        verification_data = config_data.verification.unwrap_or_else(AnyConfigData)
        verification_config = default_config.verification

        verification_expires_data = verification_data.expires.unwrap_or_else(AnyConfigData)
        verification_expires_config = verification_config.expires

        verification = VerificationConfig(
            size=verification_data.size.unwrap_or(verification_config.size),
            expires=ExpiresConfig(
                years=verification_expires_data.years.unwrap_or(verification_expires_config.years),
                months=verification_expires_data.months.unwrap_or(
                    verification_expires_config.months
                ),
                weeks=verification_expires_data.weeks.unwrap_or(verification_expires_config.weeks),
                days=verification_expires_data.days.unwrap_or(verification_expires_config.days),
                hours=verification_expires_data.hours.unwrap_or(verification_expires_config.hours),
                minutes=verification_expires_data.minutes.unwrap_or(
                    verification_expires_config.minutes
                ),
                seconds=verification_expires_data.seconds.unwrap_or(
                    verification_expires_config.seconds
                ),
            ),
        )

        bot_data = config_data.bot.unwrap_or_else(AnyConfigData)

        bot = BotConfig(token=bot_data.token.expect(EXPECTED_MELODY_BOT_TOKEN))

        web_data = config_data.web.unwrap_or_else(AnyConfigData)
        web_config = default_config.web

        web = WebConfig(
            host=web_data.host.unwrap_or(web_config.host),
            port=web_data.port.unwrap_or(web_config.port),
        )

        discord_data = config_data.discord.unwrap_or_else(AnyConfigData)

        discord = ClientConfig(
            client_id=discord_data.client_id.expect(EXPECTED_MELODY_DISCORD_CLIENT_ID),
            client_secret=discord_data.client_secret.expect(EXPECTED_MELODY_DISCORD_CLIENT_SECRET),
        )

        spotify_data = config_data.spotify.unwrap_or_else(AnyConfigData)

        spotify = ClientConfig(
            client_id=spotify_data.client_id.expect(EXPECTED_MELODY_SPOTIFY_CLIENT_ID),
            client_secret=spotify_data.client_secret.expect(EXPECTED_MELODY_SPOTIFY_CLIENT_SECRET),
        )

        name = config_data.name.unwrap_or(default_config.name)
        domain = config_data.domain.unwrap_or(default_config.domain)
        open = config_data.open.unwrap_or(default_config.open)

        session_key = config_data.session_key.expect(EXPECTED_MELODY_SESSION_KEY)

        return cls(
            name=name,
            domain=domain,
            open=open,
            session_key=session_key,
            email=email,
            hash=hash,
            kit=kit,
            code=code,
            image=image,
            log=log,
            redis=redis,
            secret=secret,
            totp=totp,
            token=token,
            authorization=authorization,
            verification=verification,
            web=web,
            bot=bot,
            discord=discord,
            spotify=spotify,
        )

    @classmethod
    def unsafe_from_string(
        cls, string: str, ignore_sensitive: bool = DEFAULT_IGNORE_SENSITIVE
    ) -> Self:
        return cls.unsafe_from_data(cls.parse(string), ignore_sensitive=ignore_sensitive)

    @classmethod
    def unsafe_from_path(
        cls,
        path: IntoPath,
        encoding: str = DEFAULT_ENCODING,
        errors: str = DEFAULT_ERRORS,
        ignore_sensitive: bool = DEFAULT_IGNORE_SENSITIVE,
    ) -> Self:
        return cls.unsafe_from_string(
            Path(path).read_text(encoding, errors), ignore_sensitive=ignore_sensitive
        )

    @classmethod
    def unsafe_from_data(
        cls,
        data: AnyConfigData,
        ignore_sensitive: bool = DEFAULT_IGNORE_SENSITIVE,
    ) -> Self:
        config_data = data.melody.expect(EXPECTED_MELODY)

        email_data = config_data.email.expect(EXPECTED_MELODY_EMAIL)

        email_temporary_data = email_data.temporary.expect(EXPECTED_MELODY_EMAIL_TEMPORARY)

        email_verification_data = email_data.verification.expect(EXPECTED_MELODY_EMAIL_VERIFICATION)

        email = EmailConfig(
            host=email_data.host.expect(EXPECTED_MELODY_EMAIL_HOST),
            port=email_data.port.expect(EXPECTED_MELODY_EMAIL_PORT),
            support=email_data.support.expect(EXPECTED_MELODY_EMAIL_SUPPORT),
            name=(
                email_data.name.unwrap_or(EMPTY)
                if ignore_sensitive
                else email_data.name.expect(EXPECTED_MELODY_EMAIL_NAME)
            ),
            password=(
                email_data.password.unwrap_or(EMPTY)
                if ignore_sensitive
                else email_data.password.expect(EXPECTED_MELODY_EMAIL_PASSWORD)
            ),
            verification=EmailMessageConfig(
                subject=email_verification_data.subject.expect(
                    EXPECTED_MELODY_EMAIL_VERIFICATION_SUBJECT
                ),
                content=email_verification_data.content.expect(
                    EXPECTED_MELODY_EMAIL_VERIFICATION_CONTENT
                ),
            ),
            temporary=EmailMessageConfig(
                subject=email_temporary_data.subject.expect(
                    EXPECTED_MELODY_EMAIL_TEMPORARY_SUBJECT
                ),
                content=email_temporary_data.content.expect(
                    EXPECTED_MELODY_EMAIL_TEMPORARY_CONTENT
                ),
            ),
        )

        hash_data = config_data.hash.expect(EXPECTED_MELODY_HASH)

        hash = HashConfig(
            time_cost=hash_data.time_cost.expect(EXPECTED_MELODY_HASH_TIME_COST),
            memory_cost=hash_data.memory_cost.expect(EXPECTED_MELODY_HASH_MEMORY_COST),
            parallelism=hash_data.parallelism.expect(EXPECTED_MELODY_HASH_PARALLELISM),
        )

        kit_data = config_data.kit.expect(EXPECTED_MELODY_KIT)

        kit = KitConfig(
            host=kit_data.host.expect(EXPECTED_MELODY_KIT_HOST),
            port=kit_data.port.expect(EXPECTED_MELODY_KIT_PORT),
        )

        code_data = config_data.code.expect(EXPECTED_MELODY_CODE)

        code = CodeConfig(
            cache=code_data.cache.map(Path).expect(EXPECTED_MELODY_CODE_CACHE),
            error_correction=code_data.error_correction.map(ErrorCorrection).expect(
                EXPECTED_MELODY_CODE_ERROR_CORRECTION
            ),
            box_size=code_data.box_size.expect(EXPECTED_MELODY_CODE_BOX_SIZE),
            border=code_data.border.expect(EXPECTED_MELODY_CODE_BORDER),
        )

        image_data = config_data.image.expect(EXPECTED_MELODY_IMAGE)

        image = ImageConfig(
            path=image_data.path.map(Path).expect(EXPECTED_MELODY_IMAGE_PATH),
            size_limit=image_data.size_limit.expect(EXPECTED_MELODY_IMAGE_SIZE_LIMIT),
            data_size_limit=image_data.data_size_limit.expect(
                EXPECTED_MELODY_IMAGE_DATA_SIZE_LIMIT
            ),
        )

        log_data = config_data.log.expect(EXPECTED_MELODY_LOG)

        log = LogConfig(level=log_data.level.expect(EXPECTED_MELODY_LOG_LEVEL))

        redis_data = config_data.redis.expect(EXPECTED_MELODY_REDIS)

        redis = RedisConfig(
            host=redis_data.host.expect(EXPECTED_MELODY_REDIS_HOST),
            port=redis_data.port.expect(EXPECTED_MELODY_REDIS_PORT),
        )

        secret_data = config_data.secret.expect(EXPECTED_MELODY_SECRET)

        secret = SecretConfig(size=secret_data.size.expect(EXPECTED_MELODY_SECRET_SIZE))

        totp_data = config_data.totp.expect(EXPECTED_MELODY_TOTP)

        totp = TOTPConfig(
            digits=totp_data.digits.expect(EXPECTED_MELODY_TOTP_DIGITS),
            interval=totp_data.interval.expect(EXPECTED_MELODY_TOTP_INTERVAL),
            valid_window=totp_data.valid_window.expect(EXPECTED_MELODY_TOTP_VALID_WINDOW),
        )

        token_data = config_data.token.expect(EXPECTED_MELODY_TOKEN)

        access_data = token_data.access.expect(EXPECTED_MELODY_TOKEN_ACCESS)
        access_expires_data = access_data.expires.expect(EXPECTED_MELODY_TOKEN_ACCESS_EXPIRES)

        refresh_data = token_data.refresh.expect(EXPECTED_MELODY_TOKEN_REFRESH)
        refresh_expires_data = refresh_data.expires.expect(EXPECTED_MELODY_TOKEN_REFRESH_EXPIRES)

        token = TokenConfig(
            type=token_data.type.expect(EXPECTED_MELODY_TOKEN_TYPE),
            access=AccessConfig(
                size=access_data.size.expect(EXPECTED_MELODY_TOKEN_ACCESS_SIZE),
                expires=ExpiresConfig(
                    years=access_expires_data.years.expect(
                        EXPECTED_MELODY_TOKEN_ACCESS_EXPIRES_YEARS
                    ),
                    months=access_expires_data.months.expect(
                        EXPECTED_MELODY_TOKEN_ACCESS_EXPIRES_MONTHS
                    ),
                    weeks=access_expires_data.weeks.expect(
                        EXPECTED_MELODY_TOKEN_ACCESS_EXPIRES_WEEKS
                    ),
                    days=access_expires_data.days.expect(EXPECTED_MELODY_TOKEN_ACCESS_EXPIRES_DAYS),
                    hours=access_expires_data.hours.expect(
                        EXPECTED_MELODY_TOKEN_ACCESS_EXPIRES_HOURS
                    ),
                    minutes=access_expires_data.minutes.expect(
                        EXPECTED_MELODY_TOKEN_ACCESS_EXPIRES_MINUTES
                    ),
                    seconds=access_expires_data.seconds.expect(
                        EXPECTED_MELODY_TOKEN_ACCESS_EXPIRES_SECONDS
                    ),
                ),
            ),
            refresh=RefreshConfig(
                size=refresh_data.size.expect(EXPECTED_MELODY_TOKEN_REFRESH_SIZE),
                expires=ExpiresConfig(
                    years=refresh_expires_data.years.expect(
                        EXPECTED_MELODY_TOKEN_REFRESH_EXPIRES_YEARS
                    ),
                    months=refresh_expires_data.months.expect(
                        EXPECTED_MELODY_TOKEN_REFRESH_EXPIRES_MONTHS
                    ),
                    weeks=refresh_expires_data.weeks.expect(
                        EXPECTED_MELODY_TOKEN_REFRESH_EXPIRES_WEEKS
                    ),
                    days=refresh_expires_data.days.expect(
                        EXPECTED_MELODY_TOKEN_REFRESH_EXPIRES_DAYS
                    ),
                    hours=refresh_expires_data.hours.expect(
                        EXPECTED_MELODY_TOKEN_REFRESH_EXPIRES_HOURS
                    ),
                    minutes=refresh_expires_data.minutes.expect(
                        EXPECTED_MELODY_TOKEN_REFRESH_EXPIRES_MINUTES
                    ),
                    seconds=refresh_expires_data.seconds.expect(
                        EXPECTED_MELODY_TOKEN_REFRESH_EXPIRES_SECONDS
                    ),
                ),
            ),
        )

        authorization_data = config_data.authorization.expect(EXPECTED_MELODY_AUTHORIZATION)
        authorization_expires_data = authorization_data.expires.expect(
            EXPECTED_MELODY_AUTHORIZATION_EXPIRES
        )

        authorization = AuthorizationConfig(
            size=authorization_data.size.expect(EXPECTED_MELODY_AUTHORIZATION_SIZE),
            expires=ExpiresConfig(
                years=authorization_expires_data.years.expect(
                    EXPECTED_MELODY_AUTHORIZATION_EXPIRES_YEARS
                ),
                months=authorization_expires_data.months.expect(
                    EXPECTED_MELODY_AUTHORIZATION_EXPIRES_MONTHS
                ),
                weeks=authorization_expires_data.weeks.expect(
                    EXPECTED_MELODY_AUTHORIZATION_EXPIRES_WEEKS
                ),
                days=authorization_expires_data.days.expect(
                    EXPECTED_MELODY_AUTHORIZATION_EXPIRES_DAYS
                ),
                hours=authorization_expires_data.hours.expect(
                    EXPECTED_MELODY_AUTHORIZATION_EXPIRES_HOURS
                ),
                minutes=authorization_expires_data.minutes.expect(
                    EXPECTED_MELODY_AUTHORIZATION_EXPIRES_MINUTES
                ),
                seconds=authorization_expires_data.seconds.expect(
                    EXPECTED_MELODY_AUTHORIZATION_EXPIRES_SECONDS
                ),
            ),
        )

        verification_data = config_data.verification.expect(EXPECTED_MELODY_VERIFICATION)
        verification_expires_data = verification_data.expires.expect(
            EXPECTED_MELODY_VERIFICATION_EXPIRES
        )

        verification = VerificationConfig(
            size=verification_data.size.expect(EXPECTED_MELODY_VERIFICATION_SIZE),
            expires=ExpiresConfig(
                years=verification_expires_data.years.expect(
                    EXPECTED_MELODY_VERIFICATION_EXPIRES_YEARS
                ),
                months=verification_expires_data.months.expect(
                    EXPECTED_MELODY_VERIFICATION_EXPIRES_MONTHS
                ),
                weeks=verification_expires_data.weeks.expect(
                    EXPECTED_MELODY_VERIFICATION_EXPIRES_WEEKS
                ),
                days=verification_expires_data.days.expect(
                    EXPECTED_MELODY_VERIFICATION_EXPIRES_DAYS
                ),
                hours=verification_expires_data.hours.expect(
                    EXPECTED_MELODY_VERIFICATION_EXPIRES_HOURS
                ),
                minutes=verification_expires_data.minutes.expect(
                    EXPECTED_MELODY_VERIFICATION_EXPIRES_MINUTES
                ),
                seconds=verification_expires_data.seconds.expect(
                    EXPECTED_MELODY_VERIFICATION_EXPIRES_SECONDS
                ),
            ),
        )

        web_data = config_data.web.expect(EXPECTED_MELODY_WEB)

        web = WebConfig(
            host=web_data.host.expect(EXPECTED_MELODY_WEB_HOST),
            port=web_data.port.expect(EXPECTED_MELODY_WEB_PORT),
        )

        bot_data = config_data.bot.expect(EXPECTED_MELODY_BOT)

        bot = BotConfig(
            token=(
                bot_data.token.unwrap_or(EMPTY)
                if ignore_sensitive
                else bot_data.token.expect(EXPECTED_MELODY_BOT_TOKEN)
            ),
        )

        discord_data = config_data.discord.expect(EXPECTED_MELODY_DISCORD)

        discord = ClientConfig(
            client_id=(
                discord_data.client_id.unwrap_or(EMPTY)
                if ignore_sensitive
                else discord_data.client_id.expect(EXPECTED_MELODY_DISCORD_CLIENT_ID)
            ),
            client_secret=(
                discord_data.client_secret.unwrap_or(EMPTY)
                if ignore_sensitive
                else discord_data.client_secret.expect(EXPECTED_MELODY_DISCORD_CLIENT_SECRET)
            ),
        )

        spotify_data = config_data.spotify.expect(EXPECTED_MELODY_SPOTIFY)

        spotify = ClientConfig(
            client_id=(
                spotify_data.client_id.unwrap_or(EMPTY)
                if ignore_sensitive
                else spotify_data.client_id.expect(EXPECTED_MELODY_SPOTIFY_CLIENT_ID)
            ),
            client_secret=(
                spotify_data.client_secret.unwrap_or(EMPTY)
                if ignore_sensitive
                else spotify_data.client_secret.expect(EXPECTED_MELODY_SPOTIFY_CLIENT_SECRET)
            ),
        )

        name = config_data.name.expect(EXPECTED_MELODY_NAME)
        domain = config_data.domain.expect(EXPECTED_MELODY_DOMAIN)
        open = config_data.open.expect(EXPECTED_MELODY_OPEN)

        session_key = (
            config_data.session_key.unwrap_or(EMPTY)
            if ignore_sensitive
            else config_data.secret_key.expect(EXPECTED_MELODY_SESSION_KEY)
        )

        return cls(
            name=name,
            domain=domain,
            open=open,
            session_key=session_key,
            email=email,
            hash=hash,
            kit=kit,
            code=code,
            image=image,
            log=log,
            redis=redis,
            secret=secret,
            totp=totp,
            token=token,
            authorization=authorization,
            verification=verification,
            web=web,
            bot=bot,
            discord=discord,
            spotify=spotify,
        )


def get_default_config(encoding: str = DEFAULT_ENCODING, errors: str = DEFAULT_ERRORS) -> Config:
    return Config.unsafe_from_path(
        DEFAULT_PATH, encoding=encoding, errors=errors, ignore_sensitive=True
    ).ensure_directories()


DEFAULT_CONFIG = get_default_config()


def get_config(encoding: str = DEFAULT_ENCODING, errors: str = DEFAULT_ERRORS) -> Config:
    return Config.from_path(PATH, encoding=encoding, errors=errors).ensure_directories()


CONFIG = get_config()
