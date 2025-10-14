from yai.entry import Log, dataclass, field, Path, datetime, base_utils_module
from yai.entry.sql_module.exceptions import ConstraintConflictError
from ..column.column import Column, ColumnConstraint

@dataclass
class InsertQueryBuilder:
    log: Log = field(default_factory=Log)

    @staticmethod
    def get_head_query(exists_ok: bool) -> str:
        """最初のクエリ作成"""
        if exists_ok:
            return "INSERT"
        return "INSERT"