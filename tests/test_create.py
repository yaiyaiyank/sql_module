from yai.entry.sql_module import sqlite

database = sqlite.SQLiteDataBase()
table_d = database.get_table_definition("test_table")
# column1 = table.get_column("uow", int, not_null=True, unique=True)
# column2 = table.get_column("oo", str)
# uni = sqlite.constraint.UniqueCompositeConstraint([column1, column2])
# create = table.create([column1, column2], [uni])

table_d.create_table()
