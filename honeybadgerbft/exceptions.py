class HoneybadgerbftError(Exception):
    """Base exception class."""


class BroadcastError(HoneybadgerbftError):
    """Base class for broadcast errors.""" 


class UnknownTagError(BroadcastError):
    """Raised when an unknown broadcast tag is detected."""


# TODO: Must figure if that is really how the protocol must behave.
class RedundantMessageError(BroadcastError):
    """Raised when a rdundant message is received."""
