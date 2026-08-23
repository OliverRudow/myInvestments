"""myTableSQLOrdersFundamentalsWatchList.py."""

__title__: str = "myTableSQLOrdersFundamentalsWatchList"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
import sqlite3
from typing import Optional
from mydatabase import mySQLDataBase, myTableSQL
from mysharesdefinition import myFundamentalsWatchListDefinitions
from myinvestments import myOrdersDefinition

STR_DATA_BASE_TABLE_NAME = 'orders_fundamentals_watch_list'


@dataclasses.dataclass(init=False)
class MyTableSQLOrdersFundamentalsWatchList(myTableSQL.MyTableSQL):
    """
        Class for providing variables and functions to manage the Web Shop List.
        The Class is based on SQLite3.
    """

    _str_fundamentals_watch_list_name: str = dataclasses.field(repr=False, default='')

    _dict_table_settings: dict[str, tuple] = dataclasses.field(repr=False, default=dict[str, tuple])

    # column indices
    _int_fundamentals_watch_list_order_id_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_trailing_eps_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_forward_eps_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_trailing_pe_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_forward_pe_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_price_to_earning_to_growth_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_book_value_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_price_to_book_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_earnings_quarterly_growth_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_growth_trend_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_surprise_trend_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_surprise_credit_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_profit_margins_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_total_cash_per_share_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_quick_ratio_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_dividend_yield_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_payout_ratio_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_five_year_ave_dividend_yield_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_ratio_dividend_yield_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_ex_dividend_date_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_ex_dividend_delta_date_column_index: int = dataclasses.field(repr=False, default=0)
    _int_fundamentals_watch_list_enterprise_to_revenue_column_index: int = dataclasses.field(repr=False, default=0)

    # column names
    _str_fundamentals_watch_list_order_id_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_trailing_eps_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_forward_eps_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_trailing_pe_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_forward_pe_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_price_to_earning_to_growth_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_book_value_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_price_to_book_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_earnings_quarterly_growth_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_growth_trend_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_surprise_trend_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_surprise_credit_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_profit_margins_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_total_cash_per_share_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_quick_ratio_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_dividend_yield_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_payout_ratio_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_five_year_ave_dividend_yield_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_ratio_dividend_yield_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_ex_dividend_date_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_ex_dividend_delta_date_column_name: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_enterprise_to_revenue_column_name: str = dataclasses.field(repr=False, default='')

    # value
    _str_fundamentals_watch_list_order_id_value: str = dataclasses.field(repr=False, default='')
    _float_fundamentals_watch_list_trailing_eps_value: float | str = dataclasses.field(repr=False, default='')
    _float_fundamentals_watch_list_forward_eps_value: float | str = dataclasses.field(repr=False, default='')
    _float_fundamentals_watch_list_trailing_pe_value: float | str = dataclasses.field(repr=False, default='')
    _float_fundamentals_watch_list_forward_pe_value: float | str = dataclasses.field(repr=False, default='')
    _float_fundamentals_watch_list_price_to_earning_to_growth_value: float | str = dataclasses.field(repr=False, default='')
    _float_fundamentals_watch_list_book_value_value: float | str = dataclasses.field(repr=False, default='')
    _float_fundamentals_watch_list_price_to_book_value: float | str = dataclasses.field(repr=False, default='')
    _float_fundamentals_watch_list_earnings_quarterly_growth_value: float | str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_growth_trend_value: str = dataclasses.field(repr=False, default='')
    _str_fundamentals_watch_list_surprise_trend_value: str = dataclasses.field(repr=False, default='')
    _int_fundamentals_watch_list_surprise_credit_value: int | str = dataclasses.field(repr=False, default='')
    _float_fundamentals_watch_list_profit_margins_value: float | str = dataclasses.field(repr=False, default='')
    _float_fundamentals_watch_list_total_cash_per_share_value: float | str = dataclasses.field(repr=False, default='')
    _float_fundamentals_watch_list_quick_ratio_value: float | str = dataclasses.field(repr=False, default='')
    _float_fundamentals_watch_list_dividend_yield_value: float | str = dataclasses.field(repr=False, default='')
    _float_fundamentals_watch_list_payout_ratio_value: float | str = dataclasses.field(repr=False, default='')
    _float_fundamentals_watch_list_five_year_ave_dividend_yield_value: float | str = dataclasses.field(repr=False, default='')
    _float_fundamentals_watch_list_ratio_dividend_yield_value: float | str = dataclasses.field(repr=False,
                                                                                                       default='')
    _int_fundamentals_watch_list_ex_dividend_date_value: int | str = dataclasses.field(repr=False, default='')
    _int_fundamentals_watch_list_ex_dividend_delta_date_value: int | str = dataclasses.field(repr=False, default='')
    _float_fundamentals_watch_list_enterprise_to_revenue_value: float | str = dataclasses.field(repr=False, default='')

    # Variables for use with SQLite3
    _str_insert_string: str = dataclasses.field(repr=False, default='')

    _list_entire_row: list = dataclasses.field(repr=False, default_factory=list)

    def __init__(self, the_sql_connection: sqlite3.Connection,
                 the_sql_cursor: sqlite3.Cursor,
                 str_table_name: Optional[str] = None) -> None:
        super().__init__(the_sql_connection, the_sql_cursor)

        self._dict_table_settings = {}

        # SQL Data Base Scheme
        self.set_sql_data_base_schema(myFundamentalsWatchListDefinitions.STR_DATA_BASE_SCHEMA_NAME)

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

        # column trailing eps
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_TRAILING_EPS

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column forward eps
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_FORWARD_EPS

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column trailing pe
        my_special_tuple =myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_TRAILING_PE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column forward pe
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_FORWARD_PE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column price to earning to growth
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_PRICE_TO_EARNING_TO_GROWTH

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column book value
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_BOOK_VALUE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column price to book
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_PRICE_TO_BOOK

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column quarterly growth
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_EARNINGS_QUARTERLY_GROWTH

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column growth trend
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_GROWTH_TREND

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column surprise trend
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_SURPRISE_TREND

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column surprise credit
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_SURPRISE_CREDIT

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column recommendation key
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_PROFIT_MARGINS

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column weighted reversion
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_TOTAL_CASH_PER_SHARE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column weighted reversion
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_QUICK_RATIO

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column number of analyst
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_DIVIDEND_YIELD

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column payout_ratio
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_PAYOUT_RATIO

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column 5 years ave dividend yield
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_FIVE_YEAR_AVE_DIVIDEND_YIELD

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column ratio dividend yield
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_RATIO_DIVIDEND_YIELD

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column ex_divident_date
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_EX_DIVIDED_DATE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column ex_divident_delta_date
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_EX_DIVIDED_DELTA_DATE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column number of analyst
        my_special_tuple = myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_ENTERPRISE_TO_REVENUE

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

        self._init_fundamentals_watch_list_columns()

        if not self._bool_sql_data_base_table:

            self.create_sql_data_base_table()

        # create SQL insert string for entire row
        self._helper_sql_data_base_insert_entire_row_string()

    def _init_fundamentals_watch_list_columns(self) -> None:

        self._str_fundamentals_watch_list_order_id_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID)

        self._int_fundamentals_watch_list_order_id_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID)

        self._str_fundamentals_watch_list_trailing_eps_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_TRAILING_EPS)

        self._int_fundamentals_watch_list_trailing_eps_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_TRAILING_EPS)

        self._str_fundamentals_watch_list_forward_eps_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_FORWARD_EPS)

        self._int_fundamentals_watch_list_forward_eps_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_FORWARD_EPS)

        self.__str_fundamentals_watch_list_trailing_pe_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_TRAILING_PE)

        self._int_fundamentals_watch_list_trailing_pe_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_TRAILING_PE)

        self._str_fundamentals_watch_list_forward_pe_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_FORWARD_PE)

        self._int_fundamentals_watch_list_forward_pe_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_FORWARD_PE)

        self._str_fundamentals_watch_list_price_to_earning_to_growth_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_PRICE_TO_EARNING_TO_GROWTH)

        self._int_fundamentals_watch_list_price_to_earning_to_growth_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_PRICE_TO_EARNING_TO_GROWTH)

        self._str_fundamentals_watch_list_book_value_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_BOOK_VALUE)

        self._int_fundamentals_watch_list_book_value_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_BOOK_VALUE)

        self._str_fundamentals_watch_list_price_to_book_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_PRICE_TO_BOOK)

        self._int_fundamentals_watch_list_price_to_book_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_PRICE_TO_BOOK)

        self._str_fundamentals_watch_list_earnings_quarterly_growth_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_EARNINGS_QUARTERLY_GROWTH)

        self._int_fundamentals_watch_list_earnings_quarterly_growth_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_EARNINGS_QUARTERLY_GROWTH)

        self._str_fundamentals_watch_list_growth_trend_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_GROWTH_TREND)

        self._int_fundamentals_watch_list_growth_trend_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_GROWTH_TREND)

        self._str_fundamentals_watch_list_surprise_trend_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_SURPRISE_TREND)

        self._int_fundamentals_watch_list_surprise_trend_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_SURPRISE_TREND)

        self._str_fundamentals_watch_list_surprise_credit_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_SURPRISE_CREDIT)

        self._int_fundamentals_watch_list_surprise_credit_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_SURPRISE_CREDIT)

        self._str_fundamentals_watch_list_profit_margins_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_PROFIT_MARGINS)

        self._int_fundamentals_watch_list_profit_margins_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_PROFIT_MARGINS)

        self._str_fundamentals_watch_list_total_cash_per_share_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_TOTAL_CASH_PER_SHARE)

        self._int_fundamentals_watch_list_total_cash_per_share_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_TOTAL_CASH_PER_SHARE)

        self._str_fundamentals_watch_list_quick_ratio_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_QUICK_RATIO)

        self._int_fundamentals_watch_list_quick_ratio_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_QUICK_RATIO)

        self._str_fundamentals_watch_list_dividend_yield_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_DIVIDEND_YIELD)

        self._int_fundamentals_watch_list_dividend_yield_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_DIVIDEND_YIELD)

        self._str_fundamentals_watch_list_payout_ratio_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_PAYOUT_RATIO)

        self._int_fundamentals_watch_list_payout_ratio_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_PAYOUT_RATIO)

        self._str_fundamentals_watch_list_five_year_ave_dividend_yield_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_FIVE_YEAR_AVE_DIVIDEND_YIELD)

        self._int_fundamentals_watch_list_five_year_ave_dividend_yield_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_FIVE_YEAR_AVE_DIVIDEND_YIELD)

        self._str_fundamentals_watch_list_ratio_dividend_yield_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_RATIO_DIVIDEND_YIELD)

        self._int_fundamentals_watch_list_ratio_dividend_yield_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_RATIO_DIVIDEND_YIELD)

        self._str_fundamentals_watch_list_ex_dividend_date_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_EX_DIVIDED_DATE)

        self._int_fundamentals_watch_list_ex_dividend_date_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_EX_DIVIDED_DATE)

        self._str_fundamentals_watch_list_ex_dividend_delta_date_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_EX_DIVIDED_DELTA_DATE)

        self._int_fundamentals_watch_list_ex_dividend_delta_date_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_EX_DIVIDED_DELTA_DATE)

        self._str_fundamentals_watch_list_enterprise_to_revenue_column_name = self.get_column_name_from_dict(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_ENTERPRISE_TO_REVENUE)

        self._int_fundamentals_watch_list_enterprise_to_revenue_column_index = self.get_column_index_from_list(
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_ENTERPRISE_TO_REVENUE)

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

        self._list_entire_row = [self._str_fundamentals_watch_list_order_id_value,
                                 self._float_fundamentals_watch_list_trailing_eps_value,
                                 self._float_fundamentals_watch_list_forward_eps_value,
                                 self._float_fundamentals_watch_list_trailing_pe_value,
                                 self._float_fundamentals_watch_list_forward_pe_value,
                                 self._float_fundamentals_watch_list_price_to_earning_to_growth_value,
                                 self._float_fundamentals_watch_list_book_value_value,
                                 self._float_fundamentals_watch_list_price_to_book_value,
                                 self._float_fundamentals_watch_list_earnings_quarterly_growth_value,
                                 self._str_fundamentals_watch_list_growth_trend_value,
                                 self._str_fundamentals_watch_list_surprise_trend_value,
                                 self._int_fundamentals_watch_list_surprise_credit_value,
                                 self._float_fundamentals_watch_list_profit_margins_value,
                                 self._float_fundamentals_watch_list_total_cash_per_share_value,
                                 self._float_fundamentals_watch_list_quick_ratio_value,
                                 self._float_fundamentals_watch_list_dividend_yield_value,
                                 self._float_fundamentals_watch_list_payout_ratio_value,
                                 self._float_fundamentals_watch_list_five_year_ave_dividend_yield_value,
                                 self._float_fundamentals_watch_list_ratio_dividend_yield_value,
                                 self._int_fundamentals_watch_list_ex_dividend_date_value,
                                 self._int_fundamentals_watch_list_ex_dividend_delta_date_value,
                                 self._float_fundamentals_watch_list_enterprise_to_revenue_value]


    def _set_sql_table_fundamentals_watch_list_entire_row(self) -> None:
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
                      f'{self._set_sql_table_fundamentals_watch_list_entire_row.__name__},'
                      f' the list_entire_row {self._list_entire_row} does not fit the number of columns requirement!')


    def set_sql_table_fundamentals_watch_list_entire_row(self,
            dict_fundamentals_watch_list_data: dict[str, str | int | float | None]) -> None:

        self._str_fundamentals_watch_list_order_id_value  = str(dict_fundamentals_watch_list_data[
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID[
                self._index_tuple.OPTION_NAME]])

        # trailing eps
        _trailing_eps = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_TRAILING_EPS[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_trailing_eps, float):

            self._float_fundamentals_watch_list_trailing_eps_value = _trailing_eps

        else:

            self._float_fundamentals_watch_list_trailing_eps_value = ''

        # forward_eps
        _foreward_eps = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_FORWARD_EPS[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_foreward_eps, float):

            self._float_fundamentals_watch_list_forward_eps_value = _foreward_eps

        else:

            self._float_fundamentals_watch_list_forward_eps_value = ''

        # trailing pe
        _trailing_pe = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_TRAILING_PE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_trailing_pe, float):

            self._float_fundamentals_watch_list_trailing_pe_value = _trailing_pe

        else:

            self._float_fundamentals_watch_list_trailing_pe_value = ''

        # forward_pe
        _forward_pe = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_FORWARD_PE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_forward_pe, float):

            self._float_fundamentals_watch_list_forward_pe_value = _forward_pe

        else:

            self._float_fundamentals_watch_list_forward_pe_value = ''

        _price_to_earning_to_growth = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_PRICE_TO_EARNING_TO_GROWTH[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_price_to_earning_to_growth, float):

            self._float_fundamentals_watch_list_price_to_earning_to_growth_value = _price_to_earning_to_growth

        else:

            self._float_fundamentals_watch_list_price_to_earning_to_growth_value = ''

        # book_value
        _book_value = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_BOOK_VALUE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_book_value, float):

            self._float_fundamentals_watch_list_book_value_value = _book_value

        else:

            self._float_fundamentals_watch_list_book_value_value = ''

        # price_to_book
        _price_to_book = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_PRICE_TO_BOOK[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_price_to_book, float):

            self._float_fundamentals_watch_list_price_to_book_value = _price_to_book

        else:

            self._float_fundamentals_watch_list_price_to_book_value = ''

        # earnings quarterly growth
        _earnings_quarterly_growth = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_EARNINGS_QUARTERLY_GROWTH[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_earnings_quarterly_growth, float):

            self._float_fundamentals_watch_list_earnings_quarterly_growth_value = _earnings_quarterly_growth

        else:

            self._float_fundamentals_watch_list_earnings_quarterly_growth_value = ''

        # growth trend
        _growth_trend = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_GROWTH_TREND[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_growth_trend, str):

            self._str_fundamentals_watch_list_growth_trend_value = _growth_trend

        else:

            self._str_fundamentals_watch_list_growth_trend_value = ''

        # surprise trend
        _surprise_trend = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_SURPRISE_TREND[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_surprise_trend, str):

            self._str_fundamentals_watch_list_surprise_trend_value = _surprise_trend

        else:

            self._str_fundamentals_watch_list_surprise_trend_value = ''


        # surprise credit
        _surprise_credit = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_SURPRISE_CREDIT[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_surprise_credit, int):

            self._int_fundamentals_watch_list_surprise_credit_value = _surprise_credit

        else:

            self._int_fundamentals_watch_list_surprise_credit_value = ''

        # profit_margin
        _profit_margins = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_PROFIT_MARGINS[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_profit_margins, float):

            self._float_fundamentals_watch_list_profit_margins_value = _profit_margins

        else:

            self._float_fundamentals_watch_list_profit_margins_value = ''

        # recommendation key
        _total_cash_per_share = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_TOTAL_CASH_PER_SHARE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_total_cash_per_share, float):

            self._float_fundamentals_watch_list_total_cash_per_share_value = _total_cash_per_share

        else:

            self._float_fundamentals_watch_list_total_cash_per_share_value = ''

        # quick ratio
        _quick_ratio = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_QUICK_RATIO[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_quick_ratio, float):

            self._float_fundamentals_watch_list_quick_ratio_value = _quick_ratio

        else:

            self._float_fundamentals_watch_list_quick_ratio_value = ''

        # dividend_yield
        _dividend_yield = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_DIVIDEND_YIELD[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_dividend_yield, float):

            self._float_fundamentals_watch_list_dividend_yield_value = _dividend_yield

        else:

            self._float_fundamentals_watch_list_dividend_yield_value = ''

        #payout_ratio
        _payout_ratio = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_PAYOUT_RATIO[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_payout_ratio, float):

            self._float_fundamentals_watch_list_payout_ratio_value = _payout_ratio

        else:

            self._float_fundamentals_watch_list_payout_ratio_value = ''

        #five_year_ave_dividend_yield
        _five_year_ave_dividend_yield = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_FIVE_YEAR_AVE_DIVIDEND_YIELD[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_five_year_ave_dividend_yield, float):

            self._float_fundamentals_watch_list_five_year_ave_dividend_yield_value = _five_year_ave_dividend_yield

        else:

            self._float_fundamentals_watch_list_five_year_ave_dividend_yield_value = ''

        # ratio dividend yield
        _ratio_dividend_yield = dict_fundamentals_watch_list_data[myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_RATIO_DIVIDEND_YIELD[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_ratio_dividend_yield, float):

            self._float_fundamentals_watch_list_ratio_dividend_yield_value = _ratio_dividend_yield

        else:
            
            self._float_fundamentals_watch_list_ratio_dividend_yield_value = ''

        #ex_dividend_date
        _ex_dividend_date = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_EX_DIVIDED_DATE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_ex_dividend_date, int):

            self._int_fundamentals_watch_list_ex_dividend_date_value = _ex_dividend_date

        else:

            self._int_fundamentals_watch_list_ex_dividend_date_value = ''

        # ex_dividend_date
        _ex_dividend_delta_date = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_EX_DIVIDED_DELTA_DATE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_ex_dividend_delta_date, int):

            self._int_fundamentals_watch_list_ex_dividend_delta_date_value = _ex_dividend_delta_date

        else:

            self._int_fundamentals_watch_list_ex_dividend_delta_date_value = ''

        #enterprise_to_revenue
        _enterprise_to_revenue = dict_fundamentals_watch_list_data[
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_ENTERPRISE_TO_REVENUE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_enterprise_to_revenue, float):

            self._float_fundamentals_watch_list_enterprise_to_revenue_value = _enterprise_to_revenue

        else:

            self._float_fundamentals_watch_list_enterprise_to_revenue_value = ''

        self._built_list_entire_row()

        self._set_sql_table_fundamentals_watch_list_entire_row()


if __name__ == "__main__":
    mySQLDB = mySQLDataBase.MySQLDataBase()
