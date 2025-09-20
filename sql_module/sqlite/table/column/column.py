from yai.entry import Log, dataclass
# is_asあたりを整理する


@dataclass
class Column:
    """
               ↓ ここ
    Table -> Column -> Field
    """
