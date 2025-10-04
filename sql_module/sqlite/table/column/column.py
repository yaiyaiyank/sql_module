from yai.entry import Log, dataclass, field, Path, datetime
from .interface import ColumnLike
from ...driver import Driver
from .name import ColumnName
from .column_constraint import ColumnConstraint


@dataclass
class Column(ColumnLike):  # ColumnLikeは別ファイルのColumnConstraintと相互依存しているため
    """
               ↓ ここ
    Table -> Column -> Field
    """

    driver: Driver
    name: ColumnName
    constraint: ColumnConstraint
    log: Log = field(default_factory=Log)

    def make_index(self):
        """インデックス生成"""
