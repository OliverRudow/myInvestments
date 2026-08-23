"""myTableSQLOrdersRankingWatchList.py."""

__title__: str = "myTableSQLOrdersRankingWatchList"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
import sqlite3
from typing import Optional
from mydatabase import mySQLDataBase, myTableSQL
from mysharesdefinition import myRankingWatchListDefinitions
from myinvestments import myOrdersDefinition

STR_DATA_BASE_TABLE_NAME = 'orders_ranking_watch_list'


@dataclasses.dataclass(init=False)
class MyTableSQLOrdersRankingWatchList(myTableSQL.MyTableSQL):
    """
        Class for providing variables and functions to manage the Web Shop List.
        The Class is based on SQLite3.
    """

    _str_ranking_watch_list_name: str = dataclasses.field(repr=False, default='')

    _dict_table_settings: dict[str, tuple] = dataclasses.field(repr=False, default=dict[str, tuple])

    # column indices
    _int_ranking_watch_list_order_id_column_index: int = dataclasses.field(repr=False, default=0)
    _int_ranking_watch_list_analyst_score_column_index: int = dataclasses.field(repr=False, default=0)
    _int_ranking_watch_list_derivate_score_column_index: int = dataclasses.field(repr=False, default=0)
    _int_ranking_watch_list_fundamentals_score_column_index: int = dataclasses.field(repr=False, default=0)
    _int_ranking_watch_list_performance_score_column_index: int = dataclasses.field(repr=False, default=0)
    _int_ranking_watch_list_overall_score_column_index: int = dataclasses.field(repr=False, default=0)
    _int_ranking_watch_list_shift_column_index: int = dataclasses.field(repr=False, default=0)

    # column names
    _str_ranking_watch_list_order_id_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_analyst_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_derivate_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_fundamentals_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_performance_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_overall_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_shift_column_name: str = dataclasses.field(repr=False, default='')

    # value
    _str_ranking_watch_list_order_id_value: str = dataclasses.field(repr=False, default='')
    _float_ranking_watch_list_analyst_score_value: str | float = dataclasses.field(repr=False, default='')
    _float_ranking_watch_list_derivate_score_value: str | float = dataclasses.field(repr=False, default='')
    _float_ranking_watch_list_fundamentals_score_value: str | float = dataclasses.field(repr=False, default='')
    _float_ranking_watch_list_performance_score_value: str | float = dataclasses.field(repr=False, default='')
    _float_ranking_watch_list_overall_score_value: str | float = dataclasses.field(repr=False, default='')
    _int_ranking_watch_list_shift_value: str | int = dataclasses.field(repr=False, default='')

    # Variables for use with SQLite3
    _str_insert_string: str = dataclasses.field(repr=False, default='')

    _list_entire_row: list = dataclasses.field(repr=False, default_factory=list)

    def __init__(self, the_sql_connection: sqlite3.Connection,
                 the_sql_cursor: sqlite3.Cursor,
                 str_table_name: Optional[str] = None) -> None:
        super().__init__(the_sql_connection, the_sql_cursor)

        self._dict_table_settings = {}

        # SQL Data Base Scheme
        self.set_sql_data_base_schema(myRankingWatchListDefinitions.STR_DATA_BASE_SCHEMA_NAME)

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

        # column analyst score
        my_special_tuple = myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_ANALYST_SCORE

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column derivate score
        my_special_tuple = myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_DERIVATE_SCORE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column fundamentals score
        my_special_tuple = myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_FUNDAMENTALS_SCORE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column performance score
        my_special_tuple = myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_PERFORMANCE_SCORE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column overall score
        my_special_tuple = myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_OVERALL_SCORE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column shift
        my_special_tuple = myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_SHIFT

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # SQL Data Base Column Settings
        self.set_dict_table_settings(self._dict_table_settings)

        # check Watch exists
        self._str_some_table_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID)

        self._bool_sql_data_base_table = (self.check_sql_data_base_table_exists() and
                                      self.check_sql_data_base_table_column_name(self._str_some_table_column_name) and
                                      self.check_sql_data_base_table_is_not_empty())

        self._init_ranking_watch_list_columns()

        if not self._bool_sql_data_base_table:

            self.create_sql_data_base_table()

        # create SQL insert string for entire row
        self._helper_sql_data_base_insert_entire_row_string()

    def _init_ranking_watch_list_columns(self) -> None:

        self._str_ranking_watch_list_order_id_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID)

        self._int_ranking_watch_list_order_id_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID)

        self._str_ranking_watch_list_analyst_score_column_name = self.get_column_name_from_dict(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_ANALYST_SCORE)

        self._int_ranking_watch_list_analyst_score_column_index = self.get_column_index_from_list(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_ANALYST_SCORE)

        self._str_ranking_watch_list_derivate_score_column_name = self.get_column_name_from_dict(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_DERIVATE_SCORE)

        self._int_ranking_watch_list_derivate_score_column_index = self.get_column_index_from_list(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_DERIVATE_SCORE)

        self._str_ranking_watch_list_fundamentals_score_column_name = self.get_column_name_from_dict(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_FUNDAMENTALS_SCORE)

        self._int_ranking_watch_list_fundamentals_score_column_index = self.get_column_index_from_list(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_FUNDAMENTALS_SCORE)

        self._str_ranking_watch_list_performance_score_column_name = self.get_column_name_from_dict(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_PERFORMANCE_SCORE)

        self._int_ranking_watch_list_performance_score_column_index = self.get_column_index_from_list(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_PERFORMANCE_SCORE)

        self._str_ranking_watch_list_overall_score_column_name = self.get_column_name_from_dict(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_OVERALL_SCORE)

        self._int_ranking_watch_list_overall_score_column_index = self.get_column_index_from_list(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_OVERALL_SCORE)

        self._str_ranking_watch_list_shift_column_name = self.get_column_name_from_dict(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_SHIFT)

        self._int_ranking_watch_list_shift_column_index = self.get_column_index_from_list(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_SHIFT)

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

        self._list_entire_row = [self._str_ranking_watch_list_order_id_value,
                                 self._float_ranking_watch_list_analyst_score_value,
                                 self._float_ranking_watch_list_derivate_score_value,
                                 self._float_ranking_watch_list_fundamentals_score_value,
                                 self._float_ranking_watch_list_performance_score_value,
                                 self._float_ranking_watch_list_overall_score_value,
                                 self._int_ranking_watch_list_shift_value]

    def _set_sql_table_ranking_watch_list_entire_row(self) -> None:
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
                      f'{self._set_sql_table_ranking_watch_list_entire_row.__name__},'
                      f' the list_entire_row {self._list_entire_row} does not fit the number of columns requirement!')

    def set_sql_table_ranking_watch_list_entire_row(self,
            dict_ranking_watch_list_data: dict[str, str | int | float | None]) -> None:

        self._str_ranking_watch_list_order_id_value  = str(dict_ranking_watch_list_data[
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID[
                self._index_tuple.OPTION_NAME]])

        # analyst score
        _analyst_score_value = dict_ranking_watch_list_data[
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_ANALYST_SCORE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_analyst_score_value, float):

            self._float_ranking_watch_list_analyst_score_value = _analyst_score_value

        else:

            self._float_ranking_watch_list_analyst_score_value = ''

        # derivate score value
        _derivate_score_value = dict_ranking_watch_list_data[
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_DERIVATE_SCORE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_derivate_score_value, float):

            self._float_ranking_watch_list_derivate_score_value= _derivate_score_value

        else:

            self._float_ranking_watch_list_derivate_score_value = ''

        # fundamental score value
        _fundamental_score_value = dict_ranking_watch_list_data[
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_FUNDAMENTALS_SCORE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_fundamental_score_value, float):

            self._float_ranking_watch_list_fundamentals_score_value = _fundamental_score_value

        else:

            self._float_ranking_watch_list_fundamentals_score_value = ''

        # performance score value
        _performance_score_value = dict_ranking_watch_list_data[
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_PERFORMANCE_SCORE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_performance_score_value, float):

            self._float_ranking_watch_list_performance_score_value = _performance_score_value

        else:

            self._float_ranking_watch_list_performance_score_value = ''

        # overall score value
        _overall_score_value = dict_ranking_watch_list_data[
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_OVERALL_SCORE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_overall_score_value, float):

            self._float_ranking_watch_list_overall_score_value = _overall_score_value

        else:

            self._float_ranking_watch_list_overall_score_value = ''

        # shift value
        _shift_value = dict_ranking_watch_list_data[
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_SHIFT[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_shift_value, int):

            self._int_ranking_watch_list_shift_value = _shift_value

        else:

            self._int_ranking_watch_list_shift_value = ''

        self._built_list_entire_row()

        self._set_sql_table_ranking_watch_list_entire_row()


if __name__ == "__main__":
    mySQLDB = mySQLDataBase.MySQLDataBase()
