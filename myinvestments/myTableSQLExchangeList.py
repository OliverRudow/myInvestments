"""myTableSQLExchangeList.py."""

__title__: str = "myTableSQLExchangeList"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
import sqlite3
from mydatabase import myTableSQL
from myinvestments import myExchangeDefinition


@dataclasses.dataclass(init=False)
class MyTableSQLExchangeList(myTableSQL.MyTableSQL):
    """
        Class for providing variables and functions to manage the Orders List.
        The Class is based on SQLite3.
    """

    _str_orders_list_name: str = dataclasses.field(repr=False, default='')

    _dict_table_settings: dict[str, tuple] = dataclasses.field(repr=False, default=dict[str, tuple])

    # column indices
    _int_exchange_list_currency_symbol_column_index: int = dataclasses.field(repr=False, default=0)
    _int_exchange_list_exchange_rate_column_index: int = dataclasses.field(repr=False, default=0)

    # column names
    _str_exchange_list_currency_symbol_column_name: str = dataclasses.field(repr=False, default='')
    _str_exchange_list_exchange_rate_column_name: str = dataclasses.field(repr=False, default='')

    _list_all_isin: list[str] = dataclasses.field(repr=False, default_factory=list)


    def __init__(self, the_sql_connection: sqlite3.Connection,
                 the_sql_cursor: sqlite3.Cursor) -> None:
        super().__init__(the_sql_connection, the_sql_cursor)

        self._dict_table_settings = {}

        # SQL Data Base Scheme
        self.set_sql_data_base_schema(myExchangeDefinition.STR_DATA_BASE_SCHEMA_NAME)

        # SQL Table Name
        self.set_table_name(myExchangeDefinition.STR_DATA_BASE_TABLE_NAME)

        # column currency symbol
        my_special_tuple = myExchangeDefinition.TUPLE_EXCHANGE_CURRENCY_SYMBOL

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column exchange rate
        my_special_tuple = myExchangeDefinition.TUPLE_EXCHANGE_EXCHANGE_RATE

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # SQL Data Base Column Settings
        self.set_dict_table_settings(self._dict_table_settings)

        # check Watch exists
        self._str_some_table_column_name = self.get_column_name_from_dict(
            myExchangeDefinition.TUPLE_EXCHANGE_CURRENCY_SYMBOL)

        self.drop_sql_table()

        self._bool_sql_data_base_table = (self.check_sql_data_base_table_exists() and
                                          self.check_sql_data_base_table_column_name(
                                              self._str_some_table_column_name) and
                                          self.check_sql_data_base_table_is_not_empty())

        self._init_exchange_list_columns()

        if not self._bool_sql_data_base_table:
            self.create_sql_data_base_table()

        self._list_all_distinct_isin = []

    def _init_exchange_list_columns(self) -> None:

        self._str_exchange_list_currency_symbol_column_name = self.get_column_name_from_dict(
            myExchangeDefinition.TUPLE_EXCHANGE_CURRENCY_SYMBOL)

        self._int_exchange_list_currency_symbol_column_index = self.get_column_index_from_list(
            myExchangeDefinition.TUPLE_EXCHANGE_CURRENCY_SYMBOL)

        self._str_exchange_list_exchange_rate_column_name = self.get_column_name_from_dict(
            myExchangeDefinition.TUPLE_EXCHANGE_EXCHANGE_RATE)

        self._int_exchange_list_exchange_rate_column_index = self.get_column_index_from_list(
            myExchangeDefinition.TUPLE_EXCHANGE_EXCHANGE_RATE)

    def set_exchange_rate_table(self, list_tuples: list[tuple]) -> None:

        _str_text = (f'INSERT INTO {self._str_sql_schema}.{self._str_table_name} '
                     f'({self._str_exchange_list_currency_symbol_column_name}, {self._str_exchange_list_exchange_rate_column_name}) '
                     f'VALUES (?, ?)')

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.executemany(_str_text, list_tuples)

                self._my_sql_connection.commit()

            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, '
                    f'{self.set_exchange_rate_table.__name__} ----, \n'
                    f'---- the Text {_str_text} has caused an Error {err} ! ----')

                exit(1)