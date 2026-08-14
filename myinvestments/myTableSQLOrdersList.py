"""myTableSQLOrdersList.py."""

__title__: str = "myTableSQLOrdersList"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
import sqlite3
from mydatabase import myTableSQL
from myinvestments import myOrdersDefinition


@dataclasses.dataclass(init=False)
class MyTableSQLOrdersList(myTableSQL.MyTableSQL):
    """
        Class for providing variables and functions to manage the Orders List.
        The Class is based on SQLite3.
    """

    _str_orders_list_name: str = dataclasses.field(repr=False, default='')

    _dict_table_settings: dict[str, tuple] = dataclasses.field(repr=False, default=dict[str, tuple])

    # column indices
    _int_orders_list_order_date_column_index: int = dataclasses.field(repr=False, default=0)
    _int_orders_list_order_number_column_index: int = dataclasses.field(repr=False, default=0)
    _int_orders_list_order_id_column_index: int = dataclasses.field(repr=False, default=0)
    _int_orders_list_isin_column_index: int = dataclasses.field(repr=False, default=0)
    _int_orders_list_order_price_column_index: int = dataclasses.field(repr=False, default=0)
    _int_orders_list_order_volume_column_index: int = dataclasses.field(repr=False, default=0)
    _int_orders_list_spending_column_index: int = dataclasses.field(repr=False, default=0)
    _int_orders_list_investment_status_column_index: int = dataclasses.field(repr=False, default=0)
    _int_orders_list_position_column_index: int = dataclasses.field(repr=False, default=0)
    _int_orders_list_performance_column_index: int = dataclasses.field(repr=False, default=0)

    # column names
    _str_orders_list_order_date_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_order_number_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_order_id_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_order_price_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_order_volume_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_spending_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_investment_status_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_position_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_performance_column_name: str = dataclasses.field(repr=False, default='')

    def __init__(self, the_sql_connection: sqlite3.Connection,
                 the_sql_cursor: sqlite3.Cursor) -> None:
        super().__init__(the_sql_connection, the_sql_cursor)

        self._dict_table_settings = {}

        # SQL Data Base Scheme
        self.set_sql_data_base_schema(myOrdersDefinition.STR_DATA_BASE_SCHEMA_NAME)

        # SQL Table Name
        self.set_table_name(myOrdersDefinition.STR_DATA_BASE_TABLE_NAME)

        # column order date
        my_special_tuple = myOrdersDefinition.TUPLE_ORDERS_ORDER_DATE

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column order number
        my_special_tuple = myOrdersDefinition.TUPLE_ORDERS_ORDER_NUMBER

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column order id
        my_special_tuple = myOrdersDefinition.TUPLE_ORDERS_ORDER_ID

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column isin
        my_special_tuple = myOrdersDefinition.TUPLE_ORDERS_ISIN

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column order price
        my_special_tuple = myOrdersDefinition.TUPLE_ORDERS_ORDER_PRICE

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column order volume
        my_special_tuple = myOrdersDefinition.TUPLE_ORDERS_ORDER_VOLUME

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column spending
        my_special_tuple = myOrdersDefinition.TUPLE_ORDERS_SPENDING

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column investment status
        my_special_tuple = myOrdersDefinition.TUPLE_ORDERS_INVESTMENT_STATUS

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column position
        my_special_tuple = myOrdersDefinition.TUPLE_ORDERS_POSITION

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column performance
        my_special_tuple = myOrdersDefinition.TUPLE_ORDERS_PERFORMANCE

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # SQL Data Base Column Settings
        self.set_dict_table_settings(self._dict_table_settings)

        # check Watch exists
        self._str_some_table_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID)

        self._bool_sql_data_base_table = (self.check_sql_data_base_table_exists() and
                                          self.check_sql_data_base_table_column_name(
                                              self._str_some_table_column_name) and
                                          self.check_sql_data_base_table_is_not_empty())

        self._init_orders_list_columns()

        if not self._bool_sql_data_base_table:
            self.create_sql_data_base_table()

    def _init_orders_list_columns(self) -> None:

        self._str_orders_list_order_date_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_DATE)

        self._int_orders_list_order_date_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_DATE)

        self._str_orders_list_order_number_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_NUMBER)

        self._int_orders_list_order_number_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_NUMBER)

        self._str_orders_list_order_id_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID)

        self._int_orders_list_order_id_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID)

        self._str_orders_list_isin_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_ISIN)

        self._int_orders_list_isin_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_ISIN)

        self._str_orders_list_order_price_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_PRICE)

        self._int_orders_list_order_price_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_PRICE)

        self._str_orders_list_order_volume_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_VOLUME)

        self._int_orders_list_order_volume_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_VOLUME)

        self._str_orders_list_spending_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_SPENDING)

        self._int_orders_list_spending_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_SPENDING)

        self._str_orders_list_investment_status_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_INVESTMENT_STATUS)

        self._int_orders_list_investment_status_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_INVESTMENT_STATUS)

        self._str_orders_list_position_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_POSITION)

        self._int_orders_list_position_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_POSITION)

        self._str_orders_list_performance_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_PERFORMANCE)

        self._int_orders_list_performance_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_PERFORMANCE)

    def place_order(self, str_isin: str, int_order_volume: int) -> None:

        _order_date = self._str_orders_list_order_date_column_name
        _order_number = self._str_orders_list_order_number_column_name
        _order_id = self._str_orders_list_order_id_column_name
        _isin = self._str_orders_list_isin_column_name
        _price = self._str_orders_list_order_price_column_name
        _volume = self._str_orders_list_order_volume_column_name
        _spending = self._str_orders_list_spending_column_name
        _status = self._str_orders_list_investment_status_column_name
        _position = self._str_orders_list_position_column_name
        _performance = self._str_orders_list_performance_column_name

        str_text = (f'INSERT INTO {self._str_sql_schema}.{self._str_table_name} '
                    f'({_order_date}, {_order_number}, {_order_id}, {_isin}, '
                    f'  {_price}, {_volume}, {_spending}, {_status}, {_position}, {_performance}) '
                    f'VALUES ( '
                    f'  date("now"), '
                    f'  COALESCE((SELECT MAX({_order_number}) FROM {self._str_sql_schema}.{self._str_table_name} '
                    f'      WHERE {_order_date} = date("now")), 0) + 1, '
                    f'  date("now") || "-" || (COALESCE((SELECT MAX({_order_number}) FROM {self._str_sql_schema}.{self._str_table_name} '
                    f'      WHERE {_order_date} = date("now")), 0) + 1), '
                    f'  "{str_isin}", '
                    f'  "",'
                    f'  {int_order_volume}, "", "", "", "")')

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.execute(str_text)
                self._my_sql_connection.commit()

            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, '
                    f'{self.place_order.__name__} ----, \n'
                    f'---- the Text {str_text} has caused an Error {err} ! ----')

                exit(1)












