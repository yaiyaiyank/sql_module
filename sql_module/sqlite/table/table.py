from yai.entry import Log, dataclass
from ..conn_and_cursor import Driver
from .column.column import Column

# TODO 複合カラムの設計変えるかも
# columnがTableの情報を使わずに行けるかも


@dataclass
class TableName:  # columnオブジェクトにも持たせてシングルトン的な感じで使うイミュータブルオブジェクト
    now: str
    old: str = None


@dataclass
class Table:
    """
        ↓ ここ
    Table -> Column -> Field
    """

    driver: Driver
    name: TableName
    old_name: str = None

    def __post_init__(self):
        self.log = Log()
        self.create_column_list: list[Column] = []  # テーブル作成時のカラムリスト
        # 複合カラムの設計変えるかも
        # self.composite_constraints: list[CompositeConstraint] = []  # composite: 複合, constraint: 制約

    def __repr__(self) -> str:
        text = f"テーブル名: {self.name}"
        return text

    def get_name(self, is_as: bool = False):
        """
        is_as (bool): ASを含めるかどうか
        fromなどで使う
        """
        # これ使うの
        if self.name.old is None or not is_as:
            return self.name.now
        else:
            return f"{self.name.old} AS {self.name.now}"
