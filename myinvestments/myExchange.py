"""myExchange.py."""

__title__: str = "myExchange"
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
from myinvestments import myTableSQLExchangeList, myExchangeDefinition
from mystaticwatchlist import myStaticWatchList
from myexchangerate import myExchangeRate


STR_WORKING_DIRECTORY: str = '/Users/oliverrudow/PycharmProjects/Data'

STR_CURRENT_DATA_BASE_FILE_NAME: str = 'shares_data_base.db'

STR_TARGET_DIRECTORY_FOR_SAFETY_COPY: str = '/Users/oliverrudow/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/Data'


@dataclasses.dataclass(init=False)
class MyExchange(mySQLDataBase.MySQLDataBase):
    """

    """

    # Tuple Definition
    _index_tuple: myTuple.MyTuple = dataclasses.field(repr=False, default_factory=type(myTuple.MyTuple))

    _str_working_directory: str = dataclasses.field(init=False, default_factory=str)

    _str_investments_data_base_file_name: str = dataclasses.field(init=False, default_factory=str)

    _str_target_directory_for_safety_copy: str = dataclasses.field(init=False, default_factory=str)

    # FileBase
    _my_file: myFileBase.MyFileBase = dataclasses.field(repr=False, default_factory=type(myFileBase.MyFileBase))

    # column indices
    _int_exchange_list_currency_symbol_column_index: int = dataclasses.field(repr=False, default=0)
    _int_exchange_list_exchange_rate_column_index: int = dataclasses.field(repr=False, default=0)

    # column names
    _str_exchange_list_currency_symbol_column_name: str = dataclasses.field(repr=False, default='')
    _str_exchange_list_exchange_rate_column_name: str = dataclasses.field(repr=False, default='')

    _list_column_names: list = dataclasses.field(repr=False, default_factory=list)

    _my_table_sql_exchange_list: myTableSQLExchangeList.MyTableSQLExchangeList = (
        dataclasses.field(repr=False, default_factory=type(myTableSQLExchangeList.MyTableSQLExchangeList)))

    # static watch list
    _my_static_watch_list: myStaticWatchList.MyStaticWatchList = dataclasses.field(repr=False,
                                                                default_factory=myStaticWatchList.MyStaticWatchList)

    _list_currency_data: list[tuple] = dataclasses.field(repr=False, default_factory=list[tuple])

    _my_exchange_rate: myExchangeRate.MyExchangeRate = dataclasses.field(repr=False,
                                                                         default_factory=myExchangeRate.MyExchangeRate)

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

            self._my_file.set_file_name(myExchangeDefinition.STR_DATA_BASE_FILE_NAME)

        self._list_column_names = []

        # SQL Data Base Name
        self.set_sql_data_base_name(self._my_file.get_entire_file_name)

        # SQL Data Base Connection Settings
        self.set_sql_connection_timeout(myExchangeDefinition.DATA_BASE_TIMEOUT)

        self.set_sql_connection_uri(myExchangeDefinition.DATA_BASE_CONNECTION_URI)

        # Open SQL DataBase
        self.open_sql_data_base()

        self._my_table_sql_exchange_list = myTableSQLExchangeList.MyTableSQLExchangeList(
                                                            self._my_sql_connection,
                                                            self._my_sql_cursor)

        self._list_column_names = self._my_table_sql_exchange_list.get_column_names()

        if self._list_column_names.__len__() == 0:

            self._list_column_names = myExchangeDefinition.LIST_EXCHANGE_COLUMN_NAMES

        self._init_exchange_list_column_indices()

        self._init_exchange_list_column_names()

        self._my_static_watch_list = myStaticWatchList.MyStaticWatchList(None,
                                                                         self._str_working_directory,
                                                                         STR_CURRENT_DATA_BASE_FILE_NAME)

        self._list_currency_data = []

        self._get_currency_symbol_list()

        self._my_exchange_rate = myExchangeRate.MyExchangeRate()

        self._update_currency_symbol_list()

        self._str_target_directory_for_safety_copy = STR_TARGET_DIRECTORY_FOR_SAFETY_COPY

        self._my_file.set_target_directory_for_copy(self._str_target_directory_for_safety_copy)

    def _init_exchange_list_column_indices(self) -> None:

        self._int_exchange_list_currency_symbol_column_index = self._list_column_names.index(
            myExchangeDefinition.TUPLE_EXCHANGE_CURRENCY_SYMBOL[self._index_tuple.OPTION_NAME])

        self._int_exchange_list_exchange_rate_column_index = self._list_column_names.index(
            myExchangeDefinition.TUPLE_EXCHANGE_EXCHANGE_RATE[self._index_tuple.OPTION_NAME])

    def _init_exchange_list_column_names(self) -> None:

        self._str_exchange_list_currency_symbol_column_name = (
            self._list_column_names)[self._int_exchange_list_currency_symbol_column_index]

        self._str_exchange_list_exchange_rate_column_name = (
            self._list_column_names)[self._int_exchange_list_exchange_rate_column_index]

    def _get_currency_symbol_list(self) -> None:

        self._list_currency_data = self._my_static_watch_list.get_list_currencies

    def _update_currency_symbol_list(self) -> None:

        if self._list_currency_data.__len__() > 0:

            result = 1

            for index, element in enumerate(self._list_currency_data):

                if element[0].__len__() > 0:

                    if element[0] in myExchangeDefinition.DICT_LOOKUP_TABLE_CURRENCY_SYMBOL:

                        _symbol = myExchangeDefinition.DICT_LOOKUP_TABLE_CURRENCY_SYMBOL[element[0]]

                    else:

                        _symbol = element[0]

                    result = self._my_exchange_rate.get_exchange_rate(_symbol)

                    if not result:

                        result = 1

                self._list_currency_data[index] = (element[0], result)

    def set_exchange_rate_table(self) -> None:

        self._my_table_sql_exchange_list.set_exchange_rate_table(self._list_currency_data)

    def close_exchange(self) -> None:

        self._my_static_watch_list.close_sql_data_base()

if __name__ == "__main__":

    my_exchange_list = MyExchange()
    my_exchange_list.set_exchange_rate_table()
