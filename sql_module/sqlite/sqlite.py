from dataclasses import dataclass
from pathlib import Path
from .conn_and_cursor import Driver
from .table.table import Table


class SQLite:
    db_path: Path | str

    def __post_init__(self):
        self.driver = Driver(self.db_path)

    def get_table(self, name: str) -> Table:
        return Table(self.driver, name)

    def get_table_list(self) -> list[Table]:
        self.driver.execute_cursor("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.driver.fetchall()
        return [Table(self.driver, table[0]) for table in tables]
