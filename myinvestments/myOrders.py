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
from mysharesdefinition import myPerformanceWatchListDefinitions
from mystaticwatchlist import myStaticWatchList
from myperformancewatchlist import myPerformanceWatchList
from watchlist_me import myReportTopList

STR_WORKING_DIRECTORY: str = '/Users/oliverrudow/PycharmProjects/Data'

STR_CURRENT_DATA_BASE_FILE_NAME: str = 'shares_data_base.db'

STR_TARGET_DIRECTORY_FOR_SAFETY_COPY: str = '/Users/oliverrudow/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/Data'


@dataclasses.dataclass(init=False)
class MyOrders(mySQLDataBase.MySQLDataBase):
    """

    """

    # Tuple Definition
    _index_tuple: myTuple.MyTuple = dataclasses.field(repr=False, default_factory=type(myTuple.MyTuple))

    _str_working_directory: str = dataclasses.field(init=False, default_factory=str)

    _str_data_base_file_name: str = dataclasses.field(init=False, default_factory=str)

    _str_investments_data_base_file_name: str = dataclasses.field(init=False, default_factory=str)

    _str_target_directory_for_safety_copy: str = dataclasses.field(init=False, default_factory=str)

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
    _str_orders_list_position_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_performance_column_name: str = dataclasses.field(repr=False, default='')

    _list_column_names: list = dataclasses.field(repr=False, default_factory=list)

    # static watch list
    _my_static_watch_list: myStaticWatchList.MyStaticWatchList = dataclasses.field(repr=False,
                                                                default_factory=myStaticWatchList.MyStaticWatchList)

    # performance watch list
    _my_performance_watch_list: myPerformanceWatchList.MyPerformanceWatchList = dataclasses.field(repr=False,
                                                        default_factory=myPerformanceWatchList.MyPerformanceWatchList)

    _my_report_top_list: myReportTopList.MyReportTopList = dataclasses.field(init=False,
                                                                             default_factory=myReportTopList.MyReportTopList)

    _str_performance_watch_list_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_ask_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_current_price_column_name: str = dataclasses.field(repr=False, default='')

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

            self._my_file.set_directory(STR_WORKING_DIRECTORY)

        self._str_working_directory = self._my_file.get_directory_name

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

        self._my_static_watch_list = myStaticWatchList.MyStaticWatchList(None,
                                                                         self._str_working_directory,
                                                                         STR_CURRENT_DATA_BASE_FILE_NAME)

        self._my_performance_watch_list = myPerformanceWatchList.MyPerformanceWatchList(None,
                                                                                        self._str_working_directory,
                                                                                        STR_CURRENT_DATA_BASE_FILE_NAME)

        self._my_report_top_list = myReportTopList.MyReportTopList(self._str_working_directory,
                                                                   STR_CURRENT_DATA_BASE_FILE_NAME)

        self._init_performance_watch_list_column_names()

        self._str_target_directory_for_safety_copy = STR_TARGET_DIRECTORY_FOR_SAFETY_COPY

        self._my_file.set_target_directory_for_copy(self._str_target_directory_for_safety_copy)


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

        self._str_orders_list_position_column_name = (
            self._list_column_names)[self._int_orders_list_position_column_index]

        self._str_orders_list_performance_column_name = (
            self._list_column_names)[self._int_orders_list_performance_column_index]

    def _init_performance_watch_list_column_names(self) -> None:

        self._str_performance_watch_list_quote_isin_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_QUOTE_ISIN)[self._index_tuple.OPTION_NAME]

        self._str_performance_watch_list_ask_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_ASK)[self._index_tuple.OPTION_NAME]

        self._str_performance_watch_list_current_price_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_CURRENT_PRICE)[self._index_tuple.OPTION_NAME]

    def automatic_order(self):

        _list = self._my_report_top_list.get_combined_overall_score_twenty_day_change_table()[1:6]

        _list_isin_to_order = [element[0] for element in _list]

        for elem in _list_isin_to_order:

            self.place_order(elem, 1)

    def place_order(self, str_isin: str, int_order: int) -> None:

        if self._my_static_watch_list.check_quote_in_watch_list(str_isin):

            if int_order > 0:

                if isinstance(int_order, int):

                    if self._my_performance_watch_list.check_quote_in_watch_list(str_isin):

                        _data = self._my_performance_watch_list.get_performance_watch_list_data_per_quote_isin(str_isin)

                        self._my_table_sql_orders_list.place_order(str_isin,
                                                                   int_order,
                                                                   _data[self._str_performance_watch_list_ask_column_name],
                                                                   _data[self._str_performance_watch_list_current_price_column_name])

                else:

                    print(f'----- Info from {__title__}.{self.place_order.__name__}: '
                          f'the Order Volume: {int_order} is corrupt!')

            else:

                print(f'----- Info from {__title__}.{self.place_order.__name__}: '
                      f'the Order Volume: {int_order} is corrupt!')

        else:

            print(f'----- Info from {__title__}.{self.place_order.__name__}: '
                  f'the ISIN: {str_isin} is not within the static watch list!')

    def update_orders(self) -> None:

        _list_performance_watch_lists = self._my_performance_watch_list.get_available_performance_watch_list_tables

        if _list_performance_watch_lists.__len__() > 0:

            _actual_performance_watch_list = _list_performance_watch_lists[0]

            self._my_file.set_directory(STR_WORKING_DIRECTORY)

            self._my_file.set_file_name(STR_CURRENT_DATA_BASE_FILE_NAME)

            _str_entire_file_name_performance_data_base = self._my_file.get_entire_file_name

            self._my_table_sql_orders_list.update_all_positions(_str_entire_file_name_performance_data_base,
                                                                _actual_performance_watch_list)

            self._my_table_sql_orders_list.update_all_performances()

    def get_overall_spending(self) -> float:

        return self._my_table_sql_orders_list.get_overall_spending()

    def get_total_position(self) -> float:

        return self._my_table_sql_orders_list.get_total_position()

    def close_investments(self) -> None:

        self._my_file.make_copy_from_file()

        self._my_performance_watch_list.close_sql_data_base()

if __name__ == "__main__":

    my_orders_list = MyOrders()
    my_orders_list.update_orders()
    # my_orders_list.automatic_order()
    print(my_orders_list.get_overall_spending())
    my_orders_list.close_sql_data_base()
