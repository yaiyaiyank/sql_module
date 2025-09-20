class SQLException(Exception):
    """SQL系の基底例外"""


class FetchNotFoundError(SQLException):
    """Fetchするものがなかった"""
