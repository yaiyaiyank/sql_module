from yai.entry import Log, dataclass, field, Path, datetime, Literal, base_utils_module
from ..driver import Driver
from .name import TableName
from .column.name import ColumnName
from .column.column import Column, ColumnConstraint

# create系
from yai.entry.sql_module.sqlite.constraint import CompositeConstraint
from yai.entry.sql_module.sqlite.querables import Create

# exceptions
from ...exceptions import ColumnAlreadyRegistrationError

# テーブルのメイン操作系
from .create.query_builder import CreateQueryBuilder

# TODO 複合カラムの設計変えるかも
# columnがTableの情報を使わずに行けるかも


@dataclass
class Table:
    """
        ↓ ここ
    Table -> Column -> Field
    """

    driver: Driver
    name: TableName
    log: Log = field(default_factory=Log)

    def __repr__(self) -> str:
        text = f"テーブル名: {self.name}"
        return text

    def get_column(
        self,
        name: str,
        type: type,
        unique: bool = False,
        not_null: bool = False,
        primary: bool = False,  # AUTO_INCREMENTは廃止されました。そのうちuuid対応するかも
        references: Column | None = None,
        default_value: str | int | bytes | Path | datetime.date | None = None,  # bool, datetime.datetime内包
    ) -> Column:
        """カラムを取得"""
        # カラム名
        column_name = ColumnName(self.name, name)
        # 列制約
        column_constraint = ColumnConstraint(
            python_type=type,
            unique=unique,
            not_null=not_null,
            primary=primary,
            references=references,
            default_value=default_value,
        )
        # カラム
        column = Column(driver=self.driver, name=column_name, constraint=column_constraint)
        return column

    def make_index(self, column_list: list[Column]):
        """インデックス生成(複合)"""

    def create(
        self,
        column_list: list[Column],
        composite_constraint_list: list[CompositeConstraint] | None = None,
        exists_ok: bool = True,
        is_execute: bool = True,
    ):
        """
        テーブル作成

        つまり、SQLのコマンドの例:
        'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)'
        を作って実行する

        Aegs:
            column_list (list[Column]): テーブルの各カラムの型の設定
            composite_constraint_list (list[CompositeConstraint]): 複合キー制約
            exists_ok (bool): 既にテーブルがあってもok。既に作られたテーブルを上書くことはない
        """
        query_builder = CreateQueryBuilder()
        # 最初のクエリ
        head_query = query_builder.get_head_query(exists_ok)
        # 列定義・列制約のクエリ
        column_define_constraint_query = query_builder.get_column_define_constraint_query(column_list)
        # 表制約のクエリ
        composite_constraint_query = query_builder.get_composite_constraint_query(composite_constraint_list)
        # 制約クエリ(列+表)
        constraint_query = base_utils_module.str_.join_comma(
            [column_define_constraint_query, composite_constraint_query], no_empty=True
        )

        query = f"{head_query} {self.name.now} ({constraint_query})"
        create = Create(query=query, driver=self.driver)

        if is_execute:
            create.execute()

        return create
