from yai.entry import dataclass, ABC
from ...driver import Driver
from .name import ColumnName


@dataclass
class ColumnLike(ABC):
    name: ColumnName
