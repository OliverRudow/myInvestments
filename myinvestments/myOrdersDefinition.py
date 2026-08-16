"""myOrdersDefinitions.py."""

__title__: str = "myOrdersDefinitions"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

from mydatabase.mySQLDataBase import STR_SQL_DATA_DIR_NAME
from mytuple import myTuple

STR_DATA_BASE_FILE_NAME: str = 'investments.db'

STR_DATA_BASE_DIR_NAME: str = STR_SQL_DATA_DIR_NAME

STR_DATA_BASE_TABLE_NAME: str = 'orders'

STR_DATA_BASE_SCHEMA_NAME: str = 'main'

DATA_BASE_TIMEOUT: float = 5.0

DATA_BASE_CONNECTION_URI: bool = True

TUPLE_ORDERS_ORDER_DATE: tuple[str, str, tuple[str, str, str], type[tuple]] = \
    ('ORDERS.ORDER_DATE',
    'order_date',
    ('order_date', 'TEXT', 'NOT NULL'),
    tuple)

TUPLE_ORDERS_ORDER_NUMBER: tuple[str, str, tuple[str, str, str], type[tuple]] = \
    ('ORDERS.ORDER_NUMBER',
    'order_number',
    ('order_number', 'INTEGER', 'NOT NULL'),
    tuple)

TUPLE_ORDERS_ORDER_ID: tuple[str, str, tuple[str, str, str, str], type[tuple]] = \
    ('ORDERS.ORDER_ID',
    'order_id',
    ('order_id', 'TEXT', 'NOT NULL', 'PRIMARY KEY'),
    tuple)

TUPLE_ORDERS_ISIN: tuple[str, str, tuple[str, str, str], type[tuple]] = \
    ('ORDERS.ISIN',
     'isin',
    ('isin', 'TEXT', 'NOT NULL'),
    tuple)

TUPLE_ORDERS_ORDER_PRICE: tuple[str, str, tuple[str, str, str], type[tuple]] = \
    ('ORDERS.ORDER_PRICE',
     'order_price',
    ('order_price', 'REAL', 'NOT NULL'),
    tuple)

TUPLE_ORDERS_ORDER_VOLUME: tuple[str, str, tuple[str, str, str], type[tuple]] = \
    ('ORDERS.ORDER_VOLUME',
     'order_volume',
    ('order_volume', 'INTEGER', 'NOT NULL'),
    tuple)

TUPLE_ORDERS_SPENDING: tuple[str, str, tuple[str, str, str], type[tuple]] = \
    ('ORDERS.SPENDING',
     'spending',
    ('spending', 'REAL', 'NOT NULL'),
    tuple)

TUPLE_ORDERS_POSITION: tuple[str, str, tuple[str, str, str], type[tuple]] = \
    ('ORDERS.POSITION',
     'position',
    ('position', 'REAL', 'NOT NULL'),
    tuple)

TUPLE_ORDERS_PERFORMANCE: tuple[str, str, tuple[str, str, str], type[tuple]] = \
    ('ORDERS.PERFORMANCE',
     'performance',
    ('performance', 'REAL', 'NOT NULL'),
    tuple)

_index_tuple = myTuple.MyTuple

LIST_ORDERS_COLUMN_NAMES: list[str] = [TUPLE_ORDERS_ORDER_DATE[_index_tuple.OPTION_NAME],
                                       TUPLE_ORDERS_ORDER_NUMBER[_index_tuple.OPTION_NAME],
                                       TUPLE_ORDERS_ORDER_ID[_index_tuple.OPTION_NAME],
                                       TUPLE_ORDERS_ISIN[_index_tuple.OPTION_NAME],
                                       TUPLE_ORDERS_ORDER_PRICE[_index_tuple.OPTION_NAME],
                                       TUPLE_ORDERS_ORDER_VOLUME[_index_tuple.OPTION_NAME],
                                       TUPLE_ORDERS_SPENDING[_index_tuple.OPTION_NAME],
                                       TUPLE_ORDERS_POSITION[_index_tuple.OPTION_NAME],
                                       TUPLE_ORDERS_PERFORMANCE[_index_tuple.OPTION_NAME]]

INDEX_PRIMARY_KEY = LIST_ORDERS_COLUMN_NAMES.index(TUPLE_ORDERS_ORDER_ID[_index_tuple.OPTION_NAME])



