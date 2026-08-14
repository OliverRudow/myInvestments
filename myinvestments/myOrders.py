"""myOrders.py."""

__title__: str = "myOrders"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
from typing import Optional
from mytuple import myTuple
from mydatabase import mySQLDataBase
from myfilebase import myFileBase
from myinvestments import myTableSQLOrdersList, myOrdersDefinition


@dataclasses.dataclass(init=False)
class MyOrders(mySQLDataBase.MySQLDataBase):
    """

    """

    # Tuple Definition
    _index_tuple: myTuple.MyTuple = dataclasses.field(repr=False, default_factory=type(myTuple.MyTuple))

    # FileBase
    _my_file: myFileBase.MyFileBase = dataclasses.field(repr=False, default_factory=type(myFileBase.MyFileBase))

    # SQL Table Static Watch List
    _my_table_sql_orders_list: myTableSQLOrdersList.MyTableSQLOrdersList = (
        dataclasses.field(repr=False, default_factory=type(myTableSQLOrdersList.MyTableSQLOrdersList)))

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

    _list_column_names: list = dataclasses.field(repr=False, default_factory=list)

    def __init__(self, str_working_directory: Optional[str] = None,
             str_data_base_filename: Optional[str] = None) -> None:
        super().__init__()

        # init myTuple
        self._index_tuple = myTuple.MyTuple

        # init FileBase w/o Config
        self._my_file = myFileBase.MyFileBase()

        # init working directory for Data Base
        if str_working_directory is not None:

            self._my_file.set_directory(str_working_directory)

        else:

            self._my_file.set_directory(myOrdersDefinition.STR_DATA_BASE_DIR_NAME)

        # init data base filename
        if str_data_base_filename is not None:

            self._my_file.set_file_name(str_data_base_filename)

        else:

            self._my_file.set_file_name(myOrdersDefinition.STR_DATA_BASE_FILE_NAME)

        self._list_column_names = []

        # SQL Data Base Name
        self.set_sql_data_base_name(self._my_file.get_entire_file_name)

        # SQL Data Base Connection Settings
        self.set_sql_connection_timeout(myOrdersDefinition.DATA_BASE_TIMEOUT)

        self.set_sql_connection_uri(myOrdersDefinition.DATA_BASE_CONNECTION_URI)

        # Open SQL DataBase
        self.open_sql_data_base()

        self._my_table_sql_orders_list = myTableSQLOrdersList.MyTableSQLOrdersList(
                                                            self._my_sql_connection,
                                                            self._my_sql_cursor)

        self._list_column_names = self._my_table_sql_orders_list.get_column_names()

        if self._list_column_names.__len__() == 0:

            self._list_column_names = myOrdersDefinition.LIST_ORDERS_COLUMN_NAMES

        self._init_orders_list_column_indices()

        self._init_orders_list_column_names()

    def _init_orders_list_column_indices(self) -> None:

        self._int_orders_list_order_date_column_index = self._list_column_names.index(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_DATE[self._index_tuple.OPTION_NAME])

        self._int_orders_list_order_number_column_index = self._list_column_names.index(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_NUMBER[self._index_tuple.OPTION_NAME])

        self._int_orders_list_order_id_column_index = self._list_column_names.index(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID[self._index_tuple.OPTION_NAME])

        self._int_orders_list_isin_column_index = self._list_column_names.index(
            myOrdersDefinition.TUPLE_ORDERS_ISIN[self._index_tuple.OPTION_NAME])

        self._int_orders_list_order_price_column_index = self._list_column_names.index(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_PRICE[self._index_tuple.OPTION_NAME])

        self._int_orders_list_order_volume_column_index = self._list_column_names.index(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_VOLUME[self._index_tuple.OPTION_NAME])

        self._int_orders_list_spending_column_index = self._list_column_names.index(
            myOrdersDefinition.TUPLE_ORDERS_SPENDING[self._index_tuple.OPTION_NAME])

        self._int_orders_list_investment_status_column_index = self._list_column_names.index(
            myOrdersDefinition.TUPLE_ORDERS_INVESTMENT_STATUS[self._index_tuple.OPTION_NAME])

        self._int_orders_list_position_column_index = self._list_column_names.index(
            myOrdersDefinition.TUPLE_ORDERS_POSITION[self._index_tuple.OPTION_NAME])

        self._int_orders_list_performance_column_index = self._list_column_names.index(
            myOrdersDefinition.TUPLE_ORDERS_PERFORMANCE[self._index_tuple.OPTION_NAME])

    def _init_orders_list_column_names(self) -> None:

        self._str_orders_list_order_date_column_name = (
            self._list_column_names)[self._int_orders_list_order_date_column_index]

        self._str_orders_list_order_number_column_name = (
            self._list_column_names)[self._int_orders_list_order_number_column_index]

        self._str_orders_list_order_id_column_name = (
            self._list_column_names)[self._int_orders_list_order_id_column_index]

        self._str_orders_list_isin_column_name = (
            self._list_column_names)[self._int_orders_list_isin_column_index]

        self._str_orders_list_order_price_column_name = (
            self._list_column_names)[self._int_orders_list_order_price_column_index]

        self._str_orders_list_order_volume_column_name = (
            self._list_column_names)[self._int_orders_list_order_volume_column_index]

        self._str_orders_list_spending_column_name = (
            self._list_column_names)[self._int_orders_list_spending_column_index]

        self._str_orders_list_investment_status_column_name = (
            self._list_column_names)[self._int_orders_list_investment_status_column_index]

        self._str_orders_list_position_column_name = (
            self._list_column_names)[self._int_orders_list_position_column_index]

        self._str_orders_list_performance_column_name = (
            self._list_column_names)[self._int_orders_list_performance_column_index]

    def place_order(self, str_isin: str, int_order: int) -> None:

        self._my_table_sql_orders_list.place_order(str_isin, int_order)

if __name__ == "__main__":

    my_orders_list = MyOrders()
    my_orders_list.place_order('NL0011683594', 1)
    my_orders_list.close_sql_data_base()




