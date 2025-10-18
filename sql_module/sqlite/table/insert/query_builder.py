from yai.entry import Log, dataclass, field, Path, datetime, base_utils_module
from yai.entry.sql_module.exceptions import ConstraintConflictError
from yai.entry.sql_module.sqlite import Column, Field

from ...placeholder import PlaceHolderable


@dataclass
class InsertQueryBuilder(PlaceHolderable):
    @staticmethod
    def get_head_query() -> str:
        """最初のクエリ作成"""
        return "INSERT INTO"

    def get_value_query(self, record: list[Field]) -> str:
        keys_query = self._get_keys_query(record)
        place_holder_keys_query = self._get_place_holder_keys_query_query(record)
        return f"({keys_query}) VALUES ({place_holder_keys_query})"

    def _get_keys_query(self, record: list[Field]) -> str:
        # record -> ['name', 'age']
        keys = [field_.column.name.now for field_ in record]
        # ['name', 'age'] -> 'name, age'
        keys_query = base_utils_module.str_.join_comma(keys)
        return keys_query

    def _get_place_holder_keys_query_query(self, record: list[Field]) -> str:
        place_holder_keys = []
        for field_ in record:
            place_holder_key = self.add_placeholder(field_.sql_value)
            place_holder_keys.append(place_holder_key)

        place_holder_keys_query = base_utils_module.str_.join_comma(place_holder_keys)
        return place_holder_keys_query

    def get_on_conflict_query(self, record: list[Field]) -> str:
        pass
