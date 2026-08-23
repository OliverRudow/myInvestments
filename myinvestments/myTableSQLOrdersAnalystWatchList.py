"""myTableSQLOrdersAnalystWatchList.py."""

__title__: str = "myTableSQLOrdersAnalystWatchList"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
import sqlite3
from typing import Optional
from mydatabase import mySQLDataBase, myTableSQL
from mysharesdefinition import myAnalystWatchListDefinitions
from myinvestments import myOrdersDefinition

STR_DATA_BASE_TABLE_NAME = 'orders_analyst_watch_list'


@dataclasses.dataclass(init=False)
class MyTableSQLOrdersAnalystWatchList(myTableSQL.MyTableSQL):
    """
        Class for providing variables and functions to manage the Web Shop List.
        The Class is based on SQLite3.
    """

    _str_analyst_watch_list_name: str = dataclasses.field(repr=False, default='')

    _dict_table_settings: dict[str, tuple] = dataclasses.field(repr=False, default=dict[str, tuple])

    # column indices
    _int_analyst_watch_list_order_id_column_index: int = dataclasses.field(repr=False, default=0)
    _int_analyst_watch_list_current_price_column_index: int = dataclasses.field(repr=False, default=0)
    _int_analyst_watch_list_target_high_price_column_index: int = dataclasses.field(repr=False, default=0)
    _int_analyst_watch_list_target_low_price_column_index: int = dataclasses.field(repr=False, default=0)
    _int_analyst_watch_list_target_mean_price_column_index: int = dataclasses.field(repr=False, default=0)
    _int_analyst_watch_list_target_median_price_column_index: int = dataclasses.field(repr=False, default=0)
    _int_analyst_watch_list_upside_potential_column_index: int = dataclasses.field(repr=False, default=0)
    _int_analyst_watch_list_risk_reward_ratio_column_index: int = dataclasses.field(repr=False, default=0)
    _int_analyst_watch_list_analyst_dispersion_column_index: int = dataclasses.field(repr=False, default=0)
    _int_analyst_watch_list_recommendation_mean_column_index: int = dataclasses.field(repr=False, default=0)
    _int_analyst_watch_list_recommendation_key_column_index: int = dataclasses.field(repr=False, default=0)
    _int_analyst_watch_list_weighted_revision_index_column_index: int = dataclasses.field(repr=False, default=0)
    _int_analyst_watch_list_weighted_revision_trend_column_index: int = dataclasses.field(repr=False, default=0)
    _int_analyst_watch_list_weighted_revision_trend_credit_column_index: int = dataclasses.field(repr=False, default=0)
    _int_analyst_watch_list_number_of_analyst_opinions_column_index: int = dataclasses.field(repr=False, default=0)

    # column names
    _str_analyst_watch_list_order_id_column_name: str = dataclasses.field(repr=False, default='')
    _str_analyst_watch_list_current_price_column_name: str = dataclasses.field(repr=False, default='')
    _str_analyst_watch_list_target_high_price_column_name: str = dataclasses.field(repr=False, default='')
    _str_analyst_watch_list_target_low_price_column_name: str = dataclasses.field(repr=False, default='')
    _str_analyst_watch_list_target_mean_price_column_name: str = dataclasses.field(repr=False, default='')
    _str_analyst_watch_list_target_median_price_column_name: str = dataclasses.field(repr=False, default='')
    _str_analyst_watch_list_upside_potential_column_name: str = dataclasses.field(repr=False, default='')
    _str_analyst_watch_list_risk_reward_ratio_column_name: str = dataclasses.field(repr=False, default='')
    _str_analyst_watch_list_analyst_dispersion_column_name: str = dataclasses.field(repr=False, default='')
    _str_analyst_watch_list_recommendation_mean_column_name: str = dataclasses.field(repr=False, default='')
    _str_analyst_watch_list_recommendation_key_column_name: str = dataclasses.field(repr=False, default='')
    _str_analyst_watch_list_weighted_revision_index_column_name: str = dataclasses.field(repr=False, default='')
    _str_analyst_watch_list_weighted_revision_trend_column_name: str = dataclasses.field(repr=False, default='')
    _str_analyst_watch_list_weighted_revision_trend_credit_column_name: str = dataclasses.field(repr=False, default='')
    _str_analyst_watch_list_number_of_analyst_opinions_column_name: str = dataclasses.field(repr=False, default='')

    # value
    _str_analyst_watch_list_order_id_value: str = dataclasses.field(repr=False, default='')
    _float_analyst_watch_list_current_price_value: float | str = dataclasses.field(repr=False, default='')
    _float_analyst_watch_list_target_high_price_value: float | str = dataclasses.field(repr=False, default='')
    _float_analyst_watch_list_target_low_price_value: float | str = dataclasses.field(repr=False, default='')
    _float_analyst_watch_list_target_mean_price_value: float | str = dataclasses.field(repr=False, default='')
    _float_analyst_watch_list_target_median_price_value: float | str = dataclasses.field(repr=False, default='')
    _float_analyst_watch_list_upside_potential_value: float | str = dataclasses.field(repr=False, default='')
    _float_analyst_watch_list_risk_reward_ratio_value: float | str = dataclasses.field(repr=False, default='')
    _float_analyst_watch_list_analyst_dispersion_value: float | str = dataclasses.field(repr=False, default='')
    _float_analyst_watch_list_recommendation_mean_value: float | str = dataclasses.field(repr=False, default='')
    _str_analyst_watch_list_recommendation_key_value: str = dataclasses.field(repr=False, default='')
    _float_analyst_watch_list_weighted_revision_index_value: float | str = dataclasses.field(repr=False, default='')
    _str_analyst_watch_list_weighted_revision_trend_value: str = dataclasses.field(repr=False, default='')
    _float_analyst_watch_list_weighted_revision_trend_credit_value: float | str = dataclasses.field(repr=False, default='')
    _int_analyst_watch_list_number_of_analyst_opinions_value: int | str = dataclasses.field(repr=False, default='')

    # Variables for use with SQLite3
    _str_insert_string: str = dataclasses.field(repr=False, default='')

    _list_entire_row: list = dataclasses.field(repr=False, default_factory=list)

    def __init__(self, the_sql_connection: sqlite3.Connection,
                 the_sql_cursor: sqlite3.Cursor,
                 str_table_name: Optional[str] = None) -> None:
        super().__init__(the_sql_connection, the_sql_cursor)

        self._dict_table_settings = {}

        # SQL Data Base Scheme
        self.set_sql_data_base_schema(myAnalystWatchListDefinitions.STR_DATA_BASE_SCHEMA_NAME)

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

        # column current price
        my_special_tuple = myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_CURRENT_PRICE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column target high price
        my_special_tuple = myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_TARGET_HIGH_PRICE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column target low price
        my_special_tuple = myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_TARGET_LOW_PRICE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column target mean price
        my_special_tuple = myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_TARGET_MEAN_PRICE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column target median price
        my_special_tuple = myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_TARGET_MEDIAN_PRICE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column upside potential
        my_special_tuple = myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_UPSIDE_POTENTIAL

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column risk_reward_ratio
        my_special_tuple = myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_RISK_REWARD_RATIO

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column analyst dispersion
        my_special_tuple = myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_ANALYST_DISPERSION

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column recommendation mean
        my_special_tuple = myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_RECOMMENDATION_MEAN

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column recommendation key
        my_special_tuple = myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_RECOMMENDATION_KEY

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column weighted reversion
        my_special_tuple = myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_INDEX

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column weighted reversion
        my_special_tuple = myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_TREND

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column weighted reversion
        my_special_tuple = myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_TREND_CREDIT

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column number of analyst
        my_special_tuple = myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_NUMBER_OF_ANALYST_OPINIONS

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

        self._init_analyst_watch_list_columns()

        if not self._bool_sql_data_base_table:

            self.create_sql_data_base_table()

        # create SQL insert string for entire row
        self._helper_sql_data_base_insert_entire_row_string()

    def _init_analyst_watch_list_columns(self) -> None:

        self._str_analyst_watch_list_order_id_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID)

        self._int_analyst_watch_list_order_id_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID)

        self._str_analyst_watch_list_current_price_column_name = self.get_column_name_from_dict(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_CURRENT_PRICE)

        self._int_analyst_watch_list_current_price_column_index = self.get_column_index_from_list(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_CURRENT_PRICE)

        self._str_analyst_watch_list_target_high_price_column_name = self.get_column_name_from_dict(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_TARGET_HIGH_PRICE)

        self._int_analyst_watch_list_target_high_price_column_index = self.get_column_index_from_list(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_TARGET_HIGH_PRICE)

        self._str_analyst_watch_list_target_low_price_column_name = self.get_column_name_from_dict(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_TARGET_LOW_PRICE)

        self._int_analyst_watch_list_target_low_price_column_index = self.get_column_index_from_list(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_TARGET_LOW_PRICE)

        self._str_analyst_watch_list_target_mean_price_column_name = self.get_column_name_from_dict(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_TARGET_MEAN_PRICE)

        self._int_analyst_watch_list_target_mean_price_column_index = self.get_column_index_from_list(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_TARGET_MEAN_PRICE)

        self._str_analyst_watch_list_target_median_price_column_name = self.get_column_name_from_dict(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_TARGET_MEDIAN_PRICE)

        self._int_analyst_watch_list_target_median_price_column_index = self.get_column_index_from_list(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_TARGET_MEDIAN_PRICE)

        self._str_analyst_watch_list_upside_potential_column_name = self.get_column_name_from_dict(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_UPSIDE_POTENTIAL)

        self._int_analyst_watch_list_upside_potential_column_index = self.get_column_index_from_list(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_UPSIDE_POTENTIAL)

        self._str_analyst_watch_list_risk_reward_ratio_column_name = self.get_column_name_from_dict(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_RISK_REWARD_RATIO)

        self._int_analyst_watch_list_risk_reward_ratio_column_index = self.get_column_index_from_list(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_RISK_REWARD_RATIO)

        self._str_analyst_watch_list_analyst_dispersion_column_name = self.get_column_name_from_dict(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_ANALYST_DISPERSION)

        self._int_analyst_watch_list_analyst_dispersion_column_index = self.get_column_index_from_list(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_ANALYST_DISPERSION)

        self._str_analyst_watch_list_recommendation_mean_column_name = self.get_column_name_from_dict(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_RECOMMENDATION_MEAN)

        self._int_analyst_watch_list_recommendation_mean_column_index = self.get_column_index_from_list(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_RECOMMENDATION_MEAN)

        self._str_analyst_watch_list_recommendation_key_column_name = self.get_column_name_from_dict(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_RECOMMENDATION_KEY)

        self._int_analyst_watch_list_recommendation_key_column_index = self.get_column_index_from_list(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_RECOMMENDATION_KEY)

        self._str_analyst_watch_list_weighted_reversion_index_column_name = self.get_column_name_from_dict(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_INDEX)

        self._int_analyst_watch_list_weighted_reversion_index_column_index = self.get_column_index_from_list(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_INDEX)

        self._str_analyst_watch_list_weighted_reversion_trend_column_name = self.get_column_name_from_dict(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_TREND)

        self._int_analyst_watch_list_weighted_reversion_trend_column_index = self.get_column_index_from_list(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_TREND)

        self._str_analyst_watch_list_weighted_reversion_trend_credit_column_name = self.get_column_name_from_dict(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_TREND_CREDIT)

        self._int_analyst_watch_list_weighted_reversion_trend_credit_column_index = self.get_column_index_from_list(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_TREND_CREDIT)

        self._str_analyst_watch_list_number_of_analyst_opinions_column_name = self.get_column_name_from_dict(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_NUMBER_OF_ANALYST_OPINIONS)

        self._int_analyst_watch_list_number_of_analyst_opinions_column_index = self.get_column_index_from_list(
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_NUMBER_OF_ANALYST_OPINIONS)

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

        self._list_entire_row = [self._str_analyst_watch_list_order_id_value,
                                 self._float_analyst_watch_list_current_price_value,
                                 self._float_analyst_watch_list_target_high_price_value,
                                 self._float_analyst_watch_list_target_low_price_value,
                                 self._float_analyst_watch_list_target_mean_price_value,
                                 self._float_analyst_watch_list_target_median_price_value,
                                 self._float_analyst_watch_list_upside_potential_value,
                                 self._float_analyst_watch_list_risk_reward_ratio_value,
                                 self._float_analyst_watch_list_analyst_dispersion_value,
                                 self._float_analyst_watch_list_recommendation_mean_value,
                                 self._str_analyst_watch_list_recommendation_key_value,
                                 self._float_analyst_watch_list_weighted_revision_index_value,
                                 self._str_analyst_watch_list_weighted_revision_trend_value,
                                 self._float_analyst_watch_list_weighted_revision_trend_credit_value,
                                 self._int_analyst_watch_list_number_of_analyst_opinions_value]


    def _set_sql_table_analyst_watch_list_entire_row(self) -> None:
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
                      f'{self._set_sql_table_analyst_watch_list_entire_row.__name__},'
                      f' the list_entire_row {self._list_entire_row} does not fit the number of columns requirement!')


    def set_sql_table_analyst_watch_list_entire_row(self,
            dict_analyst_watch_list_data: dict[str, str | int | float | None]) -> None:

        self._str_analyst_watch_list_order_id_value  = str(dict_analyst_watch_list_data[
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID[
                self._index_tuple.OPTION_NAME]])

        # curren price
        _current_price = dict_analyst_watch_list_data[
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_CURRENT_PRICE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_current_price, float):

            self._float_analyst_watch_list_current_price_value = _current_price

        else:

            self._float_analyst_watch_list_current_price_value = ''

        # target high price
        _target_high_price = dict_analyst_watch_list_data[
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_TARGET_HIGH_PRICE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_target_high_price, float):

            self._float_analyst_watch_list_target_high_price_value = _target_high_price

        else:

            self._float_analyst_watch_list_target_high_price_value = ''

        # target low price
        _target_low_price = dict_analyst_watch_list_data[
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_TARGET_LOW_PRICE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_target_low_price, float):

            self._float_analyst_watch_list_target_low_price_value = _target_low_price

        else:

            self._float_analyst_watch_list_target_low_price_value = ''

        # target mean price
        _target_mean_price = dict_analyst_watch_list_data[
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_TARGET_MEAN_PRICE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_target_mean_price, float):

            self._float_analyst_watch_list_target_mean_price_value = _target_mean_price

        else:

            self._float_analyst_watch_list_target_mean_price_value = ''

        # target median price
        _target_median_price = dict_analyst_watch_list_data[
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_TARGET_MEDIAN_PRICE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_target_median_price, float):

            self._float_analyst_watch_list_target_median_price_value = _target_median_price

        else:

            self._float_analyst_watch_list_target_median_price_value = ''

        # upside_potential
        _upside_potential = dict_analyst_watch_list_data[
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_UPSIDE_POTENTIAL[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_upside_potential, float):

            self._float_analyst_watch_list_upside_potential_value = _upside_potential

        else:

            self._float_analyst_watch_list_upside_potential_value = ''

        # risk_reward_ratio
        _risk_reward_ratio = dict_analyst_watch_list_data[
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_RISK_REWARD_RATIO[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_risk_reward_ratio, float):

            self._float_analyst_watch_list_risk_reward_ratio_value = _risk_reward_ratio

        else:

            self._float_analyst_watch_list_risk_reward_ratio_value = ''

        # analyst_dispersion
        _analyst_dispersion = dict_analyst_watch_list_data[
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_ANALYST_DISPERSION[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_analyst_dispersion, float):

            self._float_analyst_watch_list_analyst_dispersion_value = _analyst_dispersion

        else:

            self._float_analyst_watch_list_analyst_dispersion_value = ''

        # recommendation_mean
        _recommendation_mean = dict_analyst_watch_list_data[
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_RECOMMENDATION_MEAN[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_recommendation_mean, float):

            self._float_analyst_watch_list_recommendation_mean_value = _recommendation_mean

        else:

            self._float_analyst_watch_list_recommendation_mean_value = ''

        # recommendation key
        _recommendation_key = dict_analyst_watch_list_data[
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_RECOMMENDATION_KEY[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_recommendation_key, str):

            self._str_analyst_watch_list_recommendation_key_value = _recommendation_key

        else:

            self._str_analyst_watch_list_recommendation_key_value = ''

        # weighted_revisions_index
        _weighted_revision_index = dict_analyst_watch_list_data[
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_INDEX[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_weighted_revision_index, float):

            self._float_analyst_watch_list_weighted_revision_index_value = _weighted_revision_index

        else:

            self._float_analyst_watch_list_weighted_revision_index_value = ''

        # weighted_revisions_trend
        _weighted_revision_trend = dict_analyst_watch_list_data[
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_TREND[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_weighted_revision_trend, str):

            self._str_analyst_watch_list_weighted_revision_trend_value = _weighted_revision_trend

        else:

            self._str_analyst_watch_list_weighted_revision_trend_value = ''

        # weighted_revisions_trend
        _weighted_revision_trend_credit = dict_analyst_watch_list_data[
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_WEIGHTED_REVISION_TREND_CREDIT[
                self._index_tuple.OPTION_NAME]]

        if  isinstance(_weighted_revision_trend_credit, int | float):

            self._float_analyst_watch_list_weighted_revision_trend_credit_value = _weighted_revision_trend_credit

        else:

            self._float_analyst_watch_list_weighted_revision_trend_credit_value = ''

        # number of analyst opinions
        _number_of_analyst_opinions = dict_analyst_watch_list_data[
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_NUMBER_OF_ANALYST_OPINIONS[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_number_of_analyst_opinions, int):

            self._int_analyst_watch_list_number_of_analyst_opinions_value = _number_of_analyst_opinions

        else:

            self._int_analyst_watch_list_number_of_analyst_opinions_value = ''

        self._built_list_entire_row()

        self._set_sql_table_analyst_watch_list_entire_row()


if __name__ == "__main__":
    mySQLDB = mySQLDataBase.MySQLDataBase()
