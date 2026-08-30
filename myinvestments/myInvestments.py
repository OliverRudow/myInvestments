"""myInvestments.py."""

__title__: str = "myInvestments"
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
from myinvestments import myOrders, myOrdersDefinition, myTableSQLInvestmentsList, myInvestmentsDefinition, myExchange


STR_WORKING_DIRECTORY: str = '/Users/oliverrudow/PycharmProjects/Data'

STR_CURRENT_DATA_BASE_FILE_NAME: str = 'shares_data_base.db'

STR_TARGET_DIRECTORY_FOR_SAFETY_COPY: str = '/Users/oliverrudow/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/Data'


@dataclasses.dataclass(init=False)
class MyInvestments(mySQLDataBase.MySQLDataBase):
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
    _my_table_sql_investments_list: myTableSQLInvestmentsList.MyTableSQLInvestmentsList = (
        dataclasses.field(repr=False, default_factory=type(myTableSQLInvestmentsList.MyTableSQLInvestmentsList)))

    # column names
    _str_investments_date_column_name: str = dataclasses.field(repr=False, default='')
    _str_investments_spending_column_name: str = dataclasses.field(repr=False, default='')
    _str_investments_position_column_name: str = dataclasses.field(repr=False, default='')
    _str_investments_earnings_column_name: str = dataclasses.field(repr=False, default='')
    _str_investments_performance_column_name: str = dataclasses.field(repr=False, default='')

    _list_column_names: list = dataclasses.field(repr=False, default_factory=list)

    _my_orders: myOrders.MyOrders = dataclasses.field(repr=False, default_factory=type(myOrders.MyOrders))

    _my_exchange: myExchange.MyExchange = dataclasses.field(repr=False, default_factory=type(myExchange.MyExchange))

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

            self._my_file.set_file_name(myInvestmentsDefinition.STR_DATA_BASE_FILE_NAME)

        self._str_data_base_file_name = self._my_file.get_file_name

        self._list_column_names = []

        # SQL Data Base Name
        self.set_sql_data_base_name(self._my_file.get_entire_file_name)

        # SQL Data Base Connection Settings
        self.set_sql_connection_timeout(myOrdersDefinition.DATA_BASE_TIMEOUT)

        self.set_sql_connection_uri(myOrdersDefinition.DATA_BASE_CONNECTION_URI)

        # Open SQL DataBase
        self.open_sql_data_base()

        self._my_table_sql_investments_list = myTableSQLInvestmentsList.MyTableSQLInvestmentsList(
                                                            self._my_sql_connection,
                                                            self._my_sql_cursor)

        self._list_column_names = self._my_table_sql_investments_list.get_column_names()

        if self._list_column_names.__len__() == 0:

            self._list_column_names = myInvestmentsDefinition.LIST_INVESTMENTS_COLUMN_NAMES

        self._init_investments_list_column_names()

        self._my_orders = myOrders.MyOrders(self._str_working_directory, self._str_data_base_file_name)

        self._my_exchange = myExchange.MyExchange(self._str_working_directory, self._str_data_base_file_name)

        self._my_exchange.set_exchange_rate_table()

        self._str_target_directory_for_safety_copy = STR_TARGET_DIRECTORY_FOR_SAFETY_COPY

        self._my_file.set_target_directory_for_copy(self._str_target_directory_for_safety_copy)

    def _init_investments_list_column_names(self) -> None:

        self._str_investments_date_column_name = (
            myInvestmentsDefinition.TUPLE_INVESTMENTS_DATE)[self._index_tuple.OPTION_NAME]

        self._str_investments_spending_column_name = (
            myInvestmentsDefinition.TUPLE_INVESTMENTS_SPENDING)[self._index_tuple.OPTION_NAME]

        self._str_investments_position_column_name = (
            myInvestmentsDefinition.TUPLE_INVESTMENTS_POSITION)[self._index_tuple.OPTION_NAME]

        self._str_investments_earnings_column_name = (
            myInvestmentsDefinition.TUPLE_INVESTMENTS_EARNINGS)[self._index_tuple.OPTION_NAME]

        self._str_investments_performance_column_name = (
            myInvestmentsDefinition.TUPLE_INVESTMENTS_PERFORMANCE)[self._index_tuple.OPTION_NAME]

    def evaluate_investments(self) -> None:

        self._my_table_sql_investments_list.evaluate_investment(self._my_orders.get_overall_spending(),
                                                                self._my_orders.get_total_position(),
                                                                0)
    def perform_automatic_investments(self) -> None:

        self._my_orders.update_orders()
        self._my_orders.automatic_order()


if __name__ == "__main__":

    my_investments_list = MyInvestments()
    # my_investments_list.perform_automatic_investments()
    my_investments_list.evaluate_investments()
