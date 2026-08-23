"""myTableSQLOrdersDerivateWatchList.py."""

__title__: str = "myTableSQLOrdersDerivateWatchList"
__version__: str = "0.1.1"
__author__: str = "Oliver Rudow"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
import sqlite3
from typing import Optional
from mydatabase import mySQLDataBase, myTableSQL
from mysharesdefinition import myDerivateWatchListDefinitions
from myinvestments import myOrdersDefinition

STR_DATA_BASE_TABLE_NAME = 'orders_derivate_watch_list'


@dataclasses.dataclass(init=False)
class MyTableSQLOrdersDerivateWatchList(myTableSQL.MyTableSQL):
    """
        Class for providing variables and functions to manage the Web Shop List.
        The Class is based on SQLite3.
    """

    _str_derivate_watch_list_name: str = dataclasses.field(repr=False, default='')

    _dict_table_settings: dict[str, tuple] = dataclasses.field(repr=False, default=dict[str, tuple])

    # column indices
    _int_derivate_watch_list_order_id_column_index: int = dataclasses.field(repr=False, default=0)
    _int_derivate_watch_list_shares_short_column_index: int = dataclasses.field(repr=False, default=0)
    _int_derivate_watch_list_float_shares_column_index: int = dataclasses.field(repr=False, default=0)
    _int_derivate_watch_list_short_percent_of_float_column_index: int = dataclasses.field(repr=False, default=0)
    _int_derivate_watch_list_shares_outstanding_column_index: int = dataclasses.field(repr=False, default=0)
    _int_derivate_watch_list_short_ratio_column_index: int = dataclasses.field(repr=False, default=0)
    _int_derivate_watch_list_shares_short_prior_month_column_index: int = dataclasses.field(repr=False, default=0)
    _int_derivate_watch_list_short_percent_change_column_index: int = dataclasses.field(repr=False, default=0)
    _int_derivate_watch_list_shares_short_previous_month_date_column_index: int = dataclasses.field(repr=False, default=0)
    _int_derivate_watch_list_date_short_interest_column_index: int = dataclasses.field(repr=False, default=0)
    _int_derivate_watch_list_short_date_delta_last_month_column_index: int = dataclasses.field(repr=False, default=0)
    _int_derivate_watch_list_short_date_delta_this_month_column_index: int = dataclasses.field(repr=False, default=0)
    _int_derivate_watch_list_held_percent_insiders_column_index: int = dataclasses.field(repr=False, default=0)
    _int_derivate_watch_list_held_percent_institutions_column_index: int = dataclasses.field(repr=False, default=0)

    # column names
    _str_derivate_watch_list_order_id_column_name: str = dataclasses.field(repr=False, default='')
    _str_derivate_watch_list_shares_short_column_name: str = dataclasses.field(repr=False, default='')
    _str_derivate_watch_list_float_shares_column_name: str = dataclasses.field(repr=False, default='')
    _str_derivate_watch_list_short_percent_of_float_column_name: str = dataclasses.field(repr=False, default='')
    _str_derivate_watch_list_shares_outstanding_column_name: str = dataclasses.field(repr=False, default='')
    _str_derivate_watch_list_short_ratio_column_name: str = dataclasses.field(repr=False, default='')
    _str_derivate_watch_list_shares_short_prior_month_column_name: str = dataclasses.field(repr=False, default='')
    _str_derivate_watch_list_short_percent_change_column_name: str = dataclasses.field(repr=False, default='')
    _str_derivate_watch_list_shares_short_previous_month_date_column_name: str = dataclasses.field(repr=False, default='')
    _str_derivate_watch_list_date_short_interest_column_name: str = dataclasses.field(repr=False, default='')
    _str_derivate_watch_list_short_date_delta_last_month_column_name: str = dataclasses.field(repr=False, default='')
    _str_derivate_watch_list_short_date_delta_this_month_column_name: str = dataclasses.field(repr=False, default='')
    _str_derivate_watch_list_held_percent_insiders_column_name: str = dataclasses.field(repr=False, default='')
    _str_derivate_watch_list_held_percent_institutions_column_name: str = dataclasses.field(repr=False, default='')

    # value
    _str_derivate_watch_list_order_id_value: str = dataclasses.field(repr=False, default='')
    _int_derivate_watch_list_shares_short_value: int | str = dataclasses.field(repr=False, default='')
    _int_derivate_watch_list_float_shares_value: int | str = dataclasses.field(repr=False, default='')
    _float_derivate_watch_list_short_percent_of_float_value: float | str = dataclasses.field(repr=False, default='')
    _int_derivate_watch_list_shares_outstanding_value: int | str = dataclasses.field(repr=False, default='')
    _float_derivate_watch_list_short_ratio_value: float | str = dataclasses.field(repr=False, default='')
    _int_derivate_watch_list_shares_short_prior_month_value: int | str = dataclasses.field(repr=False, default='')
    _float_derivate_watch_list_short_percent_change_value: float | str = dataclasses.field(repr=False, default='')
    _int_derivate_watch_list_shares_short_previous_month_date_value: int | str = dataclasses.field(repr=False, default='')
    _int_derivate_watch_list_date_short_interest_value: int | str = dataclasses.field(repr=False, default='')
    _int_derivate_watch_list_short_date_delta_last_month_value: int | str = dataclasses.field(repr=False, default='')
    _int_derivate_watch_list_short_date_delta_this_month_value: int | str = dataclasses.field(repr=False, default='')
    _float_derivate_watch_list_held_percent_insiders_value: float | str = dataclasses.field(repr=False, default='')
    _float_derivate_watch_list_held_percent_institutions_value: float | str = dataclasses.field(repr=False, default='')

    # Variables for use with SQLite3
    _str_insert_string: str = dataclasses.field(repr=False, default='')

    _list_entire_row: list = dataclasses.field(repr=False, default_factory=list)

    def __init__(self, the_sql_connection: sqlite3.Connection,
                 the_sql_cursor: sqlite3.Cursor,
                 str_table_name: Optional[str] = None) -> None:
        super().__init__(the_sql_connection, the_sql_cursor)

        self._dict_table_settings = {}

        # SQL Data Base Scheme
        self.set_sql_data_base_schema(myDerivateWatchListDefinitions.STR_DATA_BASE_SCHEMA_NAME)

        # SQL Table Name
        if str_table_name is None:

            # default
            self.set_table_name(STR_DATA_BASE_TABLE_NAME)

        else:

            if isinstance(str_table_name, str):

                self.set_table_name(str_table_name)

            else:

                # default
                self.set_table_name(STR_DATA_BASE_TABLE_NAME)

        # column quote isin
        my_special_tuple = myOrdersDefinition.TUPLE_ORDERS_ORDER_ID

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column shares short
        my_special_tuple = myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column float shares
        my_special_tuple = myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_FLOAT_SHARES

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # short percent of float
        my_special_tuple = myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_PERCENT_OF_FLOAT

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column shares outstanding
        my_special_tuple = myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHARES_OUTSTANDING

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column short ratio
        my_special_tuple = myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_RATIO

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column shares short prior month
        my_special_tuple = myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT_PRIOR_MONTH

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # short percent change
        my_special_tuple = myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_PERCENT_CHANGE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column shares short previous month date
        my_special_tuple = myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT_PREVIOUS_MONTH_DATE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column short interest
        my_special_tuple = myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_DATE_SHORT_INTEREST

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        my_special_tuple = myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_DATE_DELTA_LAST_MONTH

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        my_special_tuple = myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_DATE_DELTA_THIS_MONTH

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column fifty-two-week high
        my_special_tuple = myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_HELD_PERCENT_INSIDERS

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column fifty-two-week high
        my_special_tuple = myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_HELD_PERCENT_INSTITUTIONS

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # SQL Data Base Column Settings
        self.set_dict_table_settings(self._dict_table_settings)

        # check static watch list exists
        self._str_some_table_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID)

        self._bool_sql_data_base_table = (self.check_sql_data_base_table_exists() and
                                      self.check_sql_data_base_table_column_name(self._str_some_table_column_name) and
                                      self.check_sql_data_base_table_is_not_empty())

        self._init_derivate_watch_list_columns()

        if not self._bool_sql_data_base_table:

            self.create_sql_data_base_table()

        # create SQL insert string for entire row
        self._helper_sql_data_base_insert_entire_row_string()

    def _init_derivate_watch_list_columns(self) -> None:

        self._str_derivate_watch_list_order_id_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID)

        self._int_derivate_watch_list_order_id_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID)

        self._str_derivate_watch_list_shares_short_column_name = self.get_column_name_from_dict(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT)

        self._int_derivate_watch_list_shares_short_column_index = self.get_column_index_from_list(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT)

        self._str_derivate_watch_list_float_shares_column_name = self.get_column_name_from_dict(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_FLOAT_SHARES)

        self._int_derivate_watch_list_float_shares_column_index = self.get_column_index_from_list(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_FLOAT_SHARES)

        self._str_derivate_watch_list_short_percent_of_float_column_name = self.get_column_name_from_dict(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_PERCENT_OF_FLOAT)

        self._int_derivate_watch_list_short_percent_of_float_column_index = self.get_column_index_from_list(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_PERCENT_OF_FLOAT)

        self._str_derivate_watch_list_shares_outstanding_column_name = self.get_column_name_from_dict(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHARES_OUTSTANDING)

        self._int_derivate_watch_list_shares_outstanding_column_index = self.get_column_index_from_list(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHARES_OUTSTANDING)

        self._str_derivate_watch_list_short_ratio_column_name = self.get_column_name_from_dict(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_RATIO)

        self._int_derivate_watch_list_short_ratio_column_index = self.get_column_index_from_list(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_RATIO)

        self._str_derivate_watch_list_shares_short_prior_month_column_name = self.get_column_name_from_dict(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT_PRIOR_MONTH)

        self._int_derivate_watch_list_shares_short_prior_month_column_index = self.get_column_index_from_list(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT_PRIOR_MONTH)

        self._str_derivate_watch_list_short_percent_change_column_name = self.get_column_name_from_dict(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_PERCENT_CHANGE)

        self._int_derivate_watch_list_short_percent_change_column_index = self.get_column_index_from_list(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_PERCENT_CHANGE)

        self._str_derivate_watch_list_shares_short_previous_month_date_column_name = self.get_column_name_from_dict(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT_PREVIOUS_MONTH_DATE)

        self._int_derivate_watch_list_shares_short_previous_month_date_column_index = self.get_column_index_from_list(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT_PREVIOUS_MONTH_DATE)

        self._str_derivate_watch_list_date_short_interest_column_name = self.get_column_name_from_dict(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_DATE_SHORT_INTEREST)

        self._int_derivate_watch_list_date_short_interest_column_index = self.get_column_index_from_list(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_DATE_SHORT_INTEREST)

        self._str_derivate_watch_list_short_date_delta_last_month_column_name = self.get_column_name_from_dict(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_DATE_DELTA_LAST_MONTH)

        self._int_derivate_watch_list_short_date_delta_last_month_column_index = self.get_column_index_from_list(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_DATE_DELTA_LAST_MONTH)

        self._str_derivate_watch_list_short_date_delta_this_month_column_name = self.get_column_name_from_dict(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_DATE_DELTA_THIS_MONTH)

        self._int_derivate_watch_list_short_date_delta_this_month_column_index = self.get_column_index_from_list(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_DATE_DELTA_THIS_MONTH)

        self._str_derivate_watch_list_held_percent_insiders_column_name = self.get_column_name_from_dict(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_HELD_PERCENT_INSIDERS)

        self._int_derivate_watch_list_held_percent_insiders_column_index = self.get_column_index_from_list(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_HELD_PERCENT_INSIDERS)

        self._str_derivate_watch_list_held_percent_institutions_column_name = self.get_column_name_from_dict(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_HELD_PERCENT_INSTITUTIONS)

        self._int_derivate_watch_list_held_percent_institutions_column_index = self.get_column_index_from_list(
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_HELD_PERCENT_INSTITUTIONS)

    def _helper_sql_data_base_insert_entire_row_string(self) -> None:

        string_column_names: str = ', '.join(list(self._dict_table_columns.values()))
        # built string question mark

        str_question_mark = '?'

        list_question_marks = []

        for num in range(self._int_table_columns_number):
            list_question_marks.append(str_question_mark)

        str_question_marks = ', '.join(list_question_marks)

        # built SQL command
        self._str_insert_string = (f'INSERT OR IGNORE INTO {self._str_sql_schema}.{self._str_table_name} '
                                  f'({string_column_names}) VALUES ({str_question_marks})')

    def _built_list_entire_row(self) -> None:

        self._list_entire_row = [self._str_derivate_watch_list_order_id_value,
                                 self._int_derivate_watch_list_shares_short_value,
                                 self._int_derivate_watch_list_float_shares_value,
                                 self._float_derivate_watch_list_short_percent_of_float_value,
                                 self._int_derivate_watch_list_shares_outstanding_value,
                                 self._float_derivate_watch_list_short_ratio_value,
                                 self._int_derivate_watch_list_shares_short_prior_month_value,
                                 self._float_derivate_watch_list_short_percent_change_value,
                                 self._int_derivate_watch_list_shares_short_previous_month_date_value,
                                 self._int_derivate_watch_list_date_short_interest_value,
                                 self._int_derivate_watch_list_short_date_delta_last_month_value,
                                 self._int_derivate_watch_list_short_date_delta_this_month_value,
                                 self._float_derivate_watch_list_held_percent_insiders_value,
                                 self._float_derivate_watch_list_held_percent_institutions_value]

    def _set_sql_table_derivate_watch_list_entire_row(self) -> None:
        if self._list_entire_row is not None:

            if self._list_entire_row.__len__() == self._int_table_columns_number:

                for ind, elem in enumerate(self._list_entire_row):

                    if elem is None:
                        self._list_entire_row[ind] = ''

                # check PRIMARY KEY
                if self._list_entire_row[myOrdersDefinition.INDEX_PRIMARY_KEY] != '':

                    self.set_table_entire_row(self._str_insert_string, tuple(self._list_entire_row))

                else:

                    print(f'---- Operational Error in {__title__}, {self.set_table_entire_row.__name__},'
                          f' the primary key is not set!')
            else:

                print(f'---- Operational Error in {__title__}, '
                      f'{self._set_sql_table_derivate_watch_list_entire_row.__name__},'
                      f' the list_entire_row {self._list_entire_row} does not fit the number of columns requirement!')

    # noinspection PyTypeChecker
    def set_sql_table_derivate_watch_list_entire_row(self,
            dict_derivate_watch_list_data: dict[str, str | int | float | None]) -> None:

        self._str_derivate_watch_list_order_id_value  = str(dict_derivate_watch_list_data[
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID[
                self._index_tuple.OPTION_NAME]])

        # shares short
        _shares_short_value = dict_derivate_watch_list_data[
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_shares_short_value, int):

            self._int_derivate_watch_list_shares_short_value = _shares_short_value

        else:

            self._int_derivate_watch_list_shares_short_value = ''

        # float shares
        _float_shares_value = dict_derivate_watch_list_data[
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_FLOAT_SHARES[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_float_shares_value, int):

            self._int_derivate_watch_list_float_shares_value = _float_shares_value

        else:

            self._int_derivate_watch_list_float_shares_value = ''

        # short_percent_of_float
        _short_percent_of_float_value = dict_derivate_watch_list_data[
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_PERCENT_OF_FLOAT[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_short_percent_of_float_value, float):

            self._float_derivate_watch_list_short_percent_of_float_value = _short_percent_of_float_value

        else:

            self._float_derivate_watch_list_short_percent_of_float_value = ''

        # shares outstanding
        _shares_outstanding_value = dict_derivate_watch_list_data[
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHARES_OUTSTANDING[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_shares_outstanding_value, int):

            self._int_derivate_watch_list_shares_outstanding_value = _shares_outstanding_value

        else:

            self._int_derivate_watch_list_shares_outstanding_value = ''

        # short ratio
        _short_ratio_value = dict_derivate_watch_list_data[
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_RATIO[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_short_ratio_value, float):

            self._float_derivate_watch_list_short_ratio_value = _short_ratio_value

        else:

            self._float_derivate_watch_list_short_ratio_value = ''

        # shares short prior month
        _shares_short_prior_month_value = dict_derivate_watch_list_data[
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT_PRIOR_MONTH[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_shares_short_prior_month_value, int):

            self._int_derivate_watch_list_shares_short_prior_month_value = _shares_short_prior_month_value

        else:

            self._int_derivate_watch_list_shares_short_prior_month_value = ''

        # shares short percent change
        _short_percent_change_value = dict_derivate_watch_list_data[
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_PERCENT_CHANGE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_short_percent_change_value, float):

            self._float_derivate_watch_list_short_percent_change_value = _short_percent_change_value

        else:

            self._float_derivate_watch_list_short_percent_change_value = ''

        # shares short previous math date
        _shares_short_previous_month_date_value = dict_derivate_watch_list_data[
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHARES_SHORT_PREVIOUS_MONTH_DATE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_shares_short_previous_month_date_value, int):

            self._int_derivate_watch_list_shares_short_previous_month_date_value = _shares_short_previous_month_date_value

        else:

            self._int_derivate_watch_list_shares_short_previous_month_date_value = ''

        # date short interest
        _date_short_interest_value = dict_derivate_watch_list_data[
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_DATE_SHORT_INTEREST[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_date_short_interest_value, int):

            self._int_derivate_watch_list_date_short_interest_value = _date_short_interest_value

        else:

            self._int_derivate_watch_list_date_short_interest_value = ''

        # short date delta last month
        _short_date_delta_last_month_value = dict_derivate_watch_list_data[
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_DATE_DELTA_LAST_MONTH[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_short_date_delta_last_month_value, int):

            self._int_derivate_watch_list_short_date_delta_last_month_value = _short_date_delta_last_month_value

        else:

            self._int_derivate_watch_list_short_date_delta_last_month_value = ''

        # short date delta this month
        _short_date_delta_this_month_value = dict_derivate_watch_list_data[
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_SHORT_DATE_DELTA_THIS_MONTH[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_short_date_delta_this_month_value, int):

            self._int_derivate_watch_list_short_date_delta_this_month_value = _short_date_delta_this_month_value

        else:

            self._int_derivate_watch_list_short_date_delta_this_month_value = ''

        # held percent insiders
        _held_percent_insiders_value = dict_derivate_watch_list_data[
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_HELD_PERCENT_INSIDERS[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_held_percent_insiders_value, float):

            self._float_derivate_watch_list_held_percent_insiders_value =_held_percent_insiders_value

        else:

            self._float_derivate_watch_list_held_percent_insiders_value = ''

        # held percent institutions
        _held_percent_institutions_value = dict_derivate_watch_list_data[
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_HELD_PERCENT_INSTITUTIONS[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_held_percent_institutions_value, float):

            self._float_derivate_watch_list_held_percent_institutions_value =_held_percent_institutions_value

        else:

            self._float_derivate_watch_list_held_percent_institutions_value = ''

        self._built_list_entire_row()

        self._set_sql_table_derivate_watch_list_entire_row()

    def check_sql_table_derivate_watch_list_is_quote_per_isin(self, str_isin: str) -> bool:

        str_text = (f'SELECT * FROM {self._str_sql_schema}.{self._str_table_name} '

                    f'WHERE {self._str_derivate_watch_list_quote_isin_column_name} = "{str_isin}"')

        bool_result = False

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.execute(str_text)

                tuple_result = self._my_sql_cursor.fetchone()

                if tuple_result is not None:
                    bool_result = True

                self._my_sql_connection.commit()


            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, '
                    f'{self.check_sql_table_derivate_watch_list_is_quote_per_isin.__name__} ----, \n'
                    f'---- the Text {str_text} has caused an Error {err} ! ----')

                exit(1)

        return bool_result

if __name__ == "__main__":
    mySQLDB = mySQLDataBase.MySQLDataBase()
