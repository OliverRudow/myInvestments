"""myOrdersDefinitions.py."""

__title__: str = "myExchangeDefinitions"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

from mydatabase.mySQLDataBase import STR_SQL_DATA_DIR_NAME
from mytuple import myTuple

STR_DATA_BASE_FILE_NAME: str = 'investments.db'

STR_DATA_BASE_DIR_NAME: str = STR_SQL_DATA_DIR_NAME

STR_DATA_BASE_TABLE_NAME: str = 'exchange_rates'

STR_DATA_BASE_SCHEMA_NAME: str = 'main'

DATA_BASE_TIMEOUT: float = 5.0

DATA_BASE_CONNECTION_URI: bool = True

TUPLE_EXCHANGE_CURRENCY_SYMBOL: tuple[str, str, tuple[str, str, str], type[tuple]] = \
    ('EXCHANGE.CURRENCY_SYMBOL',
    'currency_symbol',
    ('currency_symbol', 'TEXT', 'PRIMARY KEY'),
    tuple)

TUPLE_EXCHANGE_EXCHANGE_RATE: tuple[str, str, tuple[str, str, str], type[tuple]] = \
    ('EXCHANGE.EXCHANGE_RATE',
    'exchange_rate',
    ('exchange_rate', 'REAL', 'NOT NULL'),
    tuple)

DICT_LOOKUP_TABLE_CURRENCY_SYMBOL: dict[str, str] = {'GBp': 'GBP', 'ZAc': 'ZAC'}


_index_tuple = myTuple.MyTuple

LIST_EXCHANGE_COLUMN_NAMES: list[str] = [TUPLE_EXCHANGE_CURRENCY_SYMBOL[_index_tuple.OPTION_NAME],
                                         TUPLE_EXCHANGE_EXCHANGE_RATE[_index_tuple.OPTION_NAME]]

INDEX_PRIMARY_KEY = 0



