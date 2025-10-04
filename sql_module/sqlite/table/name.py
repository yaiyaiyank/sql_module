from yai.entry import Log, dataclass, field


@dataclass
class TableName:  # Table・columnオブジェクトに持たせてシングルトン的な感じで使うイミュータブルオブジェクト
    now: str
    old: str | None = None
    log: Log = field(default_factory=Log)

    def set_new_name(self, name: str):
        if not self.old is None:
            self.log.error(f"set_new_nameメソッドはoldがNoneのときのみです。old: {self.old}")
            raise ValueError
        if not isinstance(name, str):
            raise ValueError
        self.old = self.now
        self.now = name

    def return_name(self):
        if self.old is None:
            self.log.error("return_nameメソッドはoldがstrのときのみです。")
            raise ValueError
        self.now = self.old
        self.old = None

    def get(self, is_as: bool = False):
        """
        is_as (bool): ASを含めるかどうか
        fromなどで使う
        """
        if self.old is None or not is_as:
            return self.now
        else:
            return f"{self.old} AS {self.now}"
