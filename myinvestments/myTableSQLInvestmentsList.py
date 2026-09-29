"""myTableSQLInvestmentsList.py."""

__title__: str = "myTableSQLInvestmentsList"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
import sqlite3
from mydatabase import myTableSQL
from myinvestments import myInvestmentsDefinition


@dataclasses.dataclass(init=False)
class MyTableSQLInvestmentsList(myTableSQL.MyTableSQL):
    """
        Class for providing variables and functions to manage the Orders List.
        The Class is based on SQLite3.
    """

    _str_investments_list_name: str = dataclasses.field(repr=False, default='')

    _dict_table_settings: dict[str, tuple] = dataclasses.field(repr=False, default=dict[str, tuple])

    # column indices
    _int_investments_date_column_index: int = dataclasses.field(repr=False, default=0)
    _int_investments_spending_column_index: int = dataclasses.field(repr=False, default=0)
    _int_investments_position_column_index: int = dataclasses.field(repr=False, default=0)
    _int_investments_earnings_column_index: int = dataclasses.field(repr=False, default=0)
    _int_investments_performance_column_index: int = dataclasses.field(repr=False, default=0)

    # column names
    _str_investments_date_column_name: str = dataclasses.field(repr=False, default='')
    _str_investments_spending_column_name: str = dataclasses.field(repr=False, default='')
    _str_investments_position_column_name: str = dataclasses.field(repr=False, default='')
    _str_investments_earnings_column_name: str = dataclasses.field(repr=False, default='')
    _str_investments_performance_column_name: str = dataclasses.field(repr=False, default='')

    def __init__(self, the_sql_connection: sqlite3.Connection,
                 the_sql_cursor: sqlite3.Cursor) -> None:
        super().__init__(the_sql_connection, the_sql_cursor)

        self._dict_table_settings = {}

        # SQL Data Base Scheme
        self.set_sql_data_base_schema(myInvestmentsDefinition.STR_DATA_BASE_SCHEMA_NAME)

        # SQL Table Name
        self.set_table_name(myInvestmentsDefinition.STR_DATA_BASE_TABLE_NAME)

        # column date
        my_special_tuple = myInvestmentsDefinition.TUPLE_INVESTMENTS_DATE

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column spending
        my_special_tuple = myInvestmentsDefinition.TUPLE_INVESTMENTS_SPENDING

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column position
        my_special_tuple = myInvestmentsDefinition.TUPLE_INVESTMENTS_POSITION

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column earnings
        my_special_tuple = myInvestmentsDefinition.TUPLE_INVESTMENTS_EARNINGS

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column performance
        my_special_tuple =myInvestmentsDefinition.TUPLE_INVESTMENTS_PERFORMANCE

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # SQL Data Base Column Settings
        self.set_dict_table_settings(self._dict_table_settings)

        # check Watch exists
        self._str_some_table_column_name = self.get_column_name_from_dict(
            myInvestmentsDefinition.TUPLE_INVESTMENTS_DATE)

        self._bool_sql_data_base_table = (self.check_sql_data_base_table_exists() and
                                          self.check_sql_data_base_table_column_name(
                                              self._str_some_table_column_name) and
                                          self.check_sql_data_base_table_is_not_empty())

        self._init_orders_list_columns()

        if not self._bool_sql_data_base_table:
            self.create_sql_data_base_table()

    def _init_orders_list_columns(self) -> None:

        self._str_investments_date_column_name = self.get_column_name_from_dict(
            myInvestmentsDefinition.TUPLE_INVESTMENTS_DATE)

        self._int_investments_date_column_index = self.get_column_index_from_list(
            myInvestmentsDefinition.TUPLE_INVESTMENTS_DATE)

        self._str_investments_spending_column_name = self.get_column_name_from_dict(
            myInvestmentsDefinition.TUPLE_INVESTMENTS_SPENDING)

        self._int_investments_spending_column_index = self.get_column_index_from_list(
            myInvestmentsDefinition.TUPLE_INVESTMENTS_SPENDING)

        self._str_investments_position_column_name = self.get_column_name_from_dict(
            myInvestmentsDefinition.TUPLE_INVESTMENTS_POSITION)

        self._int_investments_position_column_index = self.get_column_index_from_list(
            myInvestmentsDefinition.TUPLE_INVESTMENTS_POSITION)

        self._str_investments_earnings_column_name = self.get_column_name_from_dict(
            myInvestmentsDefinition.TUPLE_INVESTMENTS_EARNINGS)

        self._int_investments_earnings_column_index = self.get_column_index_from_list(
            myInvestmentsDefinition.TUPLE_INVESTMENTS_EARNINGS)

        self._str_investments_performance_column_name = self.get_column_name_from_dict(
            myInvestmentsDefinition.TUPLE_INVESTMENTS_PERFORMANCE)

        self._int_investments_performance_column_index = self.get_column_index_from_list(
            myInvestmentsDefinition.TUPLE_INVESTMENTS_PERFORMANCE)

    def evaluate_investment(self, float_spending: float, float_position: float, float_earnings: float) -> None:

        _date = self._str_investments_date_column_name
        _spending = self._str_investments_spending_column_name
        _position = self._str_investments_position_column_name
        _earnings = self._str_investments_earnings_column_name
        _performance = self._str_investments_performance_column_name

        _spending_value = float_spending
        _position_value = float_position
        _earnings_value = float_earnings

        if _spending_value != 0:

            _performance_value = round((_position_value + _earnings_value - _spending_value) / _spending_value * 100, 2)

        else:

            _performance_value = 0

        str_text = (f'INSERT INTO {self._str_sql_schema}.{self._str_table_name} '
                    f'({_date}, {_spending}, {_position}, {_earnings}, {_performance}) '
                    f'VALUES (date("now"),  {_spending_value}, {_position_value}, {_earnings_value}, {_performance_value}) '
                    f'ON CONFLICT({_date}) DO UPDATE SET '
                    f'  {_spending} = excluded.{_spending}, '
                    f'  {_position} = excluded.{_position}, '
                    f'  {_earnings} = excluded.{_earnings}, '
                    f'  {_performance} = excluded.{_performance} ')

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.executescript(str_text)
                self._my_sql_connection.commit()

            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, '
                    f'{self.evaluate_investment.__name__} ----, \n'
                    f'---- the Text {str_text} has caused an Error {err} ! ----')

                exit(1)

    def get_latest_invest_data(self) -> tuple:

        _date = self._str_investments_date_column_name

        str_text = f'SELECT * FROM {self._str_sql_schema}.{self._str_table_name} ORDER BY {_date} DESC LIMIT 1'

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.execute(str_text)

                result = tuple(round(x, 2) for x in self._my_sql_cursor.fetchone())

                self._my_sql_connection.commit()

                if result is not None and result.__len__() > 0:

                    return tuple(result)

                else:

                    return ()


            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, '
                    f'{self.get_latest_invest_data.__name__} ----, \n'
                    f'---- the Text {str_text} has caused an Error {err} ! ----')

                exit(1)

        else:

            return ()


    def get_all_invest_data(self) -> list[tuple]:

        str_text = f'SELECT * FROM {self._str_sql_schema}.{self._str_table_name}'

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.execute(str_text)

                result = self._my_sql_cursor.fetchall()

                self._my_sql_connection.commit()

                if result is not None and result.__len__() > 0:

                    return result

                else:

                    return []


            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, '
                    f'{self.get_all_invest_data.__name__} ----, \n'
                    f'---- the Text {str_text} has caused an Error {err} ! ----')

                exit(1)

        else:

            return []


    def get_performance_vs_date_data(self) -> list[tuple]:

        _date = self._str_investments_date_column_name
        _performance = self._str_investments_performance_column_name

        str_text = f'SELECT {_date}, {_performance} FROM {self._str_sql_schema}.{self._str_table_name} ORDER BY {_date}'

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.execute(str_text)

                result = self._my_sql_cursor.fetchall()

                self._my_sql_connection.commit()

                if result is not None and result.__len__() > 0:

                    return result

                else:

                    return []


            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, '
                    f'{self.get_performance_vs_date_data.__name__} ----, \n'
                    f'---- the Text {str_text} has caused an Error {err} ! ----')

                exit(1)

        else:

            return []


