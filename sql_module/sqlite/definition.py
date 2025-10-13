from yai.entry import dataclass, abstractmethod
from yai.entry.sql_module import sqlite


@dataclass
class TableDefinition:
    """カラムにself.id_columnみたいにアクセスできる"""

    table: sqlite.Table

    def __post_init__(self):
        self.id_column = self.table.get_column("id", type=int)
        self.set_colmun_difinition()

    @abstractmethod
    def set_colmun_difinition(self):
        """カラムの定義"""

    def create_table(
        self,
        composite_constraint_list: list[sqlite.constraint.CompositeConstraint] | None = None,
        is_column_sort: bool = True,
    ):
        column_list = self._get_create_column(is_column_sort)
        self.table.create(column_list, composite_constraint_list)

    def _get_create_column(self, is_column_sort: bool):
        attrs = self.__dict__.values()
        column_attrs = [attr for attr in attrs if isinstance(attr, sqlite.Column)]
        column_list = self._sort_by_base_column(column_attrs, is_column_sort)
        return column_list

    def _sort_by_base_column(self, column_attrs: list[sqlite.Column], is_column_sort: bool) -> list[sqlite.Column]:
        # TODO ソート処理やる
        return column_attrs


@dataclass
class AtDateTableDefinition(TableDefinition):
    """カラムにself.id_columnみたいにアクセスできる"""


["id", "post_id", "site_id", "updated_at", "created_at", "name"]
