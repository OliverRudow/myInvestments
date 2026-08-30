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
from myinvestments import myOrdersDefinition, myExchangeDefinition
from mysharesdefinition import myPerformanceWatchListDefinitions


@dataclasses.dataclass(init=False)
class MyTableSQLOrdersList(myTableSQL.MyTableSQL):
    """
        Class for providing variables and functions to manage the Orders List.
        The Class is based on SQLite3.
    """

    _str_orders_list_name: str = dataclasses.field(repr=False, default='')

    _dict_table_settings: dict[str, tuple] = dataclasses.field(repr=False, default=dict[str, tuple])

    # column indices
    _int_orders_list_order_id_column_index: int = dataclasses.field(repr=False, default=0)
    _int_orders_list_order_date_column_index: int = dataclasses.field(repr=False, default=0)
    _int_orders_list_order_number_column_index: int = dataclasses.field(repr=False, default=0)
    _int_orders_list_isin_column_index: int = dataclasses.field(repr=False, default=0)
    _int_orders_list_name_column_index: int = dataclasses.field(repr=False, default=0)
    _int_orders_list_currency_column_index: int = dataclasses.field(repr=False, default=0)
    _int_orders_list_order_price_column_index: int = dataclasses.field(repr=False, default=0)
    _int_orders_list_order_volume_column_index: int = dataclasses.field(repr=False, default=0)
    _int_orders_list_spending_column_index: int = dataclasses.field(repr=False, default=0)
    _int_orders_list_position_column_index: int = dataclasses.field(repr=False, default=0)
    _int_orders_list_performance_column_index: int = dataclasses.field(repr=False, default=0)

    # column names
    _str_orders_list_order_id_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_order_date_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_order_number_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_name_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_currency_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_order_price_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_order_volume_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_spending_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_position_column_name: str = dataclasses.field(repr=False, default='')
    _str_orders_list_performance_column_name: str = dataclasses.field(repr=False, default='')

    _list_all_isin: list[str] = dataclasses.field(repr=False, default_factory=list)

    _str_performance_watch_list_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_current_price_column_name: str = dataclasses.field(repr=False, default='')

    _str_exchange_list_table_name: str = dataclasses.field(repr=False, default='')
    _str_exchange_list_currency_symbol_column_name: str = dataclasses.field(repr=False, default='')
    _str_exchange_list_exchange_rate_column_name: str = dataclasses.field(repr=False, default='')

    def __init__(self, the_sql_connection: sqlite3.Connection,
                 the_sql_cursor: sqlite3.Cursor) -> None:
        super().__init__(the_sql_connection, the_sql_cursor)

        self._dict_table_settings = {}

        # SQL Data Base Scheme
        self.set_sql_data_base_schema(myOrdersDefinition.STR_DATA_BASE_SCHEMA_NAME)

        # SQL Table Name
        self.set_table_name(myOrdersDefinition.STR_DATA_BASE_TABLE_NAME)

        # column order id
        my_special_tuple = myOrdersDefinition.TUPLE_ORDERS_ORDER_ID

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column order date
        my_special_tuple = myOrdersDefinition.TUPLE_ORDERS_ORDER_DATE

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column order number
        my_special_tuple = myOrdersDefinition.TUPLE_ORDERS_ORDER_NUMBER

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column isin
        my_special_tuple = myOrdersDefinition.TUPLE_ORDERS_ISIN

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column name
        my_special_tuple = myOrdersDefinition.TUPLE_ORDERS_NAME

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column currency
        my_special_tuple = myOrdersDefinition.TUPLE_ORDERS_CURRENCY

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

        self._init_performance_watch_list_column_names()

        self._init_exchange_list_column_names()

        if not self._bool_sql_data_base_table:
            self.create_sql_data_base_table()

        self._list_all_distinct_isin = []

    def _init_orders_list_columns(self) -> None:

        self._str_orders_list_order_id_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID)

        self._int_orders_list_order_id_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_ID)

        self._str_orders_list_order_date_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_DATE)

        self._int_orders_list_order_date_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_DATE)

        self._str_orders_list_order_number_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_NUMBER)

        self._int_orders_list_order_number_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_ORDER_NUMBER)

        self._str_orders_list_isin_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_ISIN)

        self._int_orders_list_isin_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_ISIN)

        self._str_orders_list_name_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_NAME)

        self._int_orders_list_name_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_NAME)

        self._str_orders_list_currency_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_CURRENCY)

        self._int_orders_list_currency_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_CURRENCY)

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

        self._str_orders_list_position_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_POSITION)

        self._int_orders_list_position_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_POSITION)

        self._str_orders_list_performance_column_name = self.get_column_name_from_dict(
            myOrdersDefinition.TUPLE_ORDERS_PERFORMANCE)

        self._int_orders_list_performance_column_index = self.get_column_index_from_list(
            myOrdersDefinition.TUPLE_ORDERS_PERFORMANCE)

    def _init_performance_watch_list_column_names(self) -> None:

        self._str_performance_watch_list_quote_isin_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_QUOTE_ISIN)[self._index_tuple.OPTION_NAME]

        self._str_performance_watch_list_current_price_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_CURRENT_PRICE)[self._index_tuple.OPTION_NAME]

    def _init_exchange_list_column_names(self) -> None:

        self._str_exchange_list_table_name = myExchangeDefinition.STR_DATA_BASE_TABLE_NAME

        self._str_exchange_list_currency_symbol_column_name = (
            myExchangeDefinition.TUPLE_EXCHANGE_CURRENCY_SYMBOL)[self._index_tuple.OPTION_NAME]

        self._str_exchange_list_exchange_rate_column_name =(
            myExchangeDefinition.TUPLE_EXCHANGE_EXCHANGE_RATE)[self._index_tuple.OPTION_NAME]

    def _get_all_distinct_isin(self):

        self._list_all_distinct_isin = []

        _isin = self._str_orders_list_isin_column_name

        # isin w/o duplicates
        str_text = f'SELECT DISTINCT {_isin} FROM {self._str_sql_schema}.{self._str_table_name} '

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.execute(str_text)

                _all_isin = self._my_sql_cursor.fetchall()

                self._my_sql_connection.commit()

                self._list_all_distinct_isin = [element[0] for element in _all_isin]

            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, '
                    f'{self._get_all_distinct_isin.__name__} ----, \n'
                    f'---- the Text {str_text} has caused an Error {err} ! ----')

                exit(1)

    def update_all_positions(self, str_performance_data_base_file_name: str, performance_table_name: str) -> None:

        self._get_all_distinct_isin()

        _isin = self._str_orders_list_isin_column_name
        _currency = self._str_orders_list_currency_column_name
        _volume = self._str_orders_list_order_volume_column_name
        _position = self._str_orders_list_position_column_name

        _quote_isin = self._str_performance_watch_list_quote_isin_column_name
        _price =  self._str_performance_watch_list_current_price_column_name

        _table_name_exchange = self._str_exchange_list_table_name
        _currency_symbol_column_name = self._str_exchange_list_currency_symbol_column_name
        _exchange_rate_column_name = self._str_exchange_list_exchange_rate_column_name

        # 1. (Falsy-Evaluation)
        if self._list_all_distinct_isin:

            if self._my_sql_connection and self._my_sql_cursor:

                try:
                    # ATTACH ausführen
                    self._my_sql_cursor.execute(
                        f'ATTACH DATABASE "{str_performance_data_base_file_name}" AS db_performance')

                    # 3. SQL-Query mit Platzhaltern (?) statt String-Formatierung
                    # Das UPDATE wurde so umgeschrieben, dass es ALLE ISINs auf einmal verarbeitet
                    # sql_update = f"""
                    #    UPDATE {self._str_sql_schema}.{self._str_table_name}
                    #    SET {_position} = (
                    #        SELECT {_volume}
                    #        FROM {self._str_sql_schema}.{self._str_table_name}
                    #        WHERE {self._str_sql_schema}.{self._str_table_name}.{_isin} = :isin
                    #    ) * (
                    #        SELECT {_price}
                    #        FROM db_performance.{performance_table_name}
                    #        WHERE db_performance.{performance_table_name}.{_quote_isin} = :isin
                    #    )
                    #    WHERE {_isin} = :isin
                    # """

                    sql_update = f"""
                        UPDATE {self._str_sql_schema}.{self._str_table_name} AS o
                        SET {_position} = ROUND(
                            (o.{_volume} * p.{_price} / e.{_exchange_rate_column_name}), 
                            2
                        )
                        FROM db_performance.{performance_table_name} AS p, {_table_name_exchange} AS e
                        WHERE o.{_isin} = p.{_quote_isin}
                          AND e.{_currency_symbol_column_name} = o.{_currency}
                          AND o.{_isin} = :isin
                    """

                    # 4. executemany() führt die Query für alle ISINs in einem Rutsch aus
                    # Wir übergeben eine Liste von Dicts für die Named Placeholders (:isin)
                    param_list = [{"isin": isin} for isin in self._list_all_distinct_isin]

                    self._my_sql_cursor.executemany(sql_update, param_list)

                    # 5. Nur EIN Commit nach allen Updates (enormer Geschwindigkeitsvorteil)
                    self._my_sql_connection.commit()

                except sqlite3.OperationalError as err:
                    print(
                        f'---- Operational Error in {__title__}, {self.update_all_positions.__name__} ----\n'
                        f'---- An error occurred during database operations: {err} ----'
                    )
                    exit(1)

                finally:
                    # 6. DETACH im finally-Block garantiert, dass die DB sauber getrennt wird,
                    # selbst wenn oben ein Fehler auftritt.
                    try:

                        self._my_sql_cursor.execute('DETACH DATABASE db_performance')
                        self._my_sql_connection.commit()

                    except sqlite3.OperationalError:

                        pass  # Verhindert Absturz, falls DETACH fehlschlägt, weil ATTACH schon fehlschlug

    def update_all_performances(self):

        _performance = self._str_orders_list_performance_column_name
        _spending = self._str_orders_list_spending_column_name
        _position = self._str_orders_list_position_column_name

        str_text = (f' UPDATE {self._str_sql_schema}.{self._str_table_name} '
                    f'  SET {_performance} = ROUND('
                    f'      CAST({_position} - {_spending} AS REAL) / {_spending} * 100, 2 ) '
                    f'  WHERE {_spending} IS NOT NULL AND {_spending} != 0 ')

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.execute(str_text)
                self._my_sql_connection.commit()

            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, '
                    f'{self.update_all_performances.__name__} ----, \n'
                    f'---- the Text {str_text} has caused an Error {err} ! ----')

                exit(1)

    def place_order(self, str_isin: str, str_name: str, str_curr_sym: str, int_order_volume: int, float_ask: float, float_price: float) -> None:

        _table_name_exchange = self._str_exchange_list_table_name
        _currency_symbol_column_name = self._str_exchange_list_currency_symbol_column_name
        _exchange_rate_column_name = self._str_exchange_list_exchange_rate_column_name

        _order_id = self._str_orders_list_order_id_column_name
        _order_date = self._str_orders_list_order_date_column_name
        _order_number = self._str_orders_list_order_number_column_name
        _isin = self._str_orders_list_isin_column_name
        _name = self._str_orders_list_name_column_name
        _currency = self._str_orders_list_currency_column_name
        _price = self._str_orders_list_order_price_column_name
        _volume = self._str_orders_list_order_volume_column_name
        _spending = self._str_orders_list_spending_column_name
        _position = self._str_orders_list_position_column_name
        _performance = self._str_orders_list_performance_column_name

        if self._my_sql_connection and self._my_sql_cursor:

            str_text = (f'SELECT {_exchange_rate_column_name}  '
                        f'FROM {self._str_sql_schema}.{_table_name_exchange} '
                        f'WHERE {_currency_symbol_column_name} = "{str_curr_sym}" ')

            try:

                self._my_sql_cursor.execute(str_text)

                _exchange_rate_value: float = self._my_sql_cursor.fetchone()[0]

                self._my_sql_connection.commit()

            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, '
                    f'{self.place_order.__name__} ----, \n'
                    f'---- the Text {str_text} has caused an Error {err} ! ----')

                exit(1)

            if _exchange_rate_value is None or _exchange_rate_value == 0:

                _exchange_rate_value  = 1

            if not (isinstance(float_price, float) or isinstance(float_price, int)):

                float_price = 0

            else:

                float_price = round(float(float_price / _exchange_rate_value), 2)

            _position_value: float = round(float_price  * int_order_volume, 2)

            if not (isinstance(float_ask, float) or isinstance(float_ask, int)):

                float_ask = float_price

            else:

                if not float_ask > 0:

                    float_ask = float_price

                else:

                    float_ask = round(float(float_ask / _exchange_rate_value), 2)

            _spending_value: float = round(float_ask * int_order_volume, 2)

            if _spending_value > 0:

                _performance_value: float = round((_position_value - _spending_value) / _spending_value * 100, 2)

            else:

                _performance_value: float = 0

            str_text = (f'INSERT INTO {self._str_sql_schema}.{self._str_table_name} '
                        f'( {_order_id}, {_order_date}, {_order_number}, {_isin}, {_name}, {_currency}, '
                        f'  {_price}, {_volume}, {_spending}, {_position}, {_performance}) '
                        f'VALUES ( '
                        f'  date("now") || "-" || (COALESCE((SELECT MAX({_order_number}) FROM {self._str_sql_schema}.{self._str_table_name} '
                        f'      WHERE {_order_date} = date("now")), 0) + 1), '
                        f'  date("now"), '
                        f'  COALESCE((SELECT MAX({_order_number}) FROM {self._str_sql_schema}.{self._str_table_name} '
                        f'      WHERE {_order_date} = date("now")), 0) + 1, '
                        f'  "{str_isin}", '
                        f'  "{str_name}", ' 
                        f'  "{str_curr_sym}", ' 
                        f'  {float_ask}, '
                        f'  {int_order_volume}, {_spending_value}, {_position_value}, {_performance_value})')

            try:

                self._my_sql_cursor.execute(str_text)
                self._my_sql_connection.commit()

            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, '
                    f'{self.place_order.__name__} ----, \n'
                    f'---- the Text {str_text} has caused an Error {err} ! ----')

                exit(1)

    @property
    def get_max_order_id(self) -> str:

        order_id = self._str_orders_list_order_id_column_name

        str_text = f'SELECT MAX({order_id}) FROM {self._str_sql_schema}.{self._str_table_name} '

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.execute(str_text)

                _result = self._my_sql_cursor.fetchone()

                self._my_sql_connection.commit()

                return _result[0]

            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, '
                    f'{self.get_max_order_id.__name__} ----, \n'
                    f'---- the Text {str_text} has caused an Error {err} ! ----')

                exit(1)

        else:

            return ''

    def get_overall_spending(self) -> float:

        _spending = self._str_orders_list_spending_column_name

        str_text = f'SELECT SUM({_spending}) FROM {self._str_sql_schema}.{self._str_table_name} '

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.execute(str_text)

                _result = self._my_sql_cursor.fetchone()

                self._my_sql_connection.commit()

                return float(_result[0])

            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, '
                    f'{self.get_overall_spending.__name__} ----, \n'
                    f'---- the Text {str_text} has caused an Error {err} ! ----')

                exit(1)

        else:

            return 0

    def get_total_position(self) -> float:

        _position = self._str_orders_list_position_column_name

        str_text = f'SELECT SUM({_position}) FROM {self._str_sql_schema}.{self._str_table_name} '

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.execute(str_text)

                _result = self._my_sql_cursor.fetchone()

                self._my_sql_connection.commit()

                return float(_result[0])

            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, '
                    f'{self.get_total_position().__name__} ----, \n'
                    f'---- the Text {str_text} has caused an Error {err} ! ----')

                exit(1)

        else:

            return 0
