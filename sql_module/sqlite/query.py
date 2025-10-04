from yai.entry import Log, dataclass, field, Path, datetime, Literal, base_utils_module
from .driver import Driver


@dataclass
class Querable:
    query: str
    driver: Driver

    def execute(self):
        self.driver.execute_cursor(self.query)
