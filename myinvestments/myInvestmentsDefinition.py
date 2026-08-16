"""myInvestmentsDefinitions.py."""

__title__: str = "myInvestmentsDefinitions"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

from mytuple import myTuple

STR_DATA_BASE_FILE_NAME: str = 'investments.db'

STR_DATA_BASE_DIR_NAME: str = '/Users/oliverrudow/PycharmProjects/Data'

STR_DATA_BASE_TABLE_NAME: str = 'investments'

STR_DATA_BASE_SCHEMA_NAME: str = 'main'

DATA_BASE_TIMEOUT: float = 5.0

DATA_BASE_CONNECTION_URI: bool = True

TUPLE_INVESTMENTS_DATE: tuple[str, str, tuple[str, str, str, str], type[tuple]] = \
    ('INVESTMENTS.DATE',
    'date',
    ('date', 'TEXT', 'NOT NULL', 'PRIMARY KEY'),
    tuple)

TUPLE_INVESTMENTS_SPENDING: tuple[str, str, tuple[str, str, str], type[tuple]] = \
    ('INVESTMENTS.SPENDING',
     'spending',
    ('spending', 'REAL', 'NOT NULL'),
    tuple)

TUPLE_INVESTMENTS_POSITION: tuple[str, str, tuple[str, str, str], type[tuple]] = \
    ('INVESTMENTS.POSITION',
     'position',
    ('position', 'REAL', 'NOT NULL'),
    tuple)

TUPLE_INVESTMENTS_EARNINGS: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('INVESTMENTS.EARNINGS',
     'earnings',
    ('earnings', 'REAL'),
    tuple)

TUPLE_INVESTMENTS_PERFORMANCE: tuple[str, str, tuple[str, str, str], type[tuple]] = \
    ('INVESTMENTS.PERFORMANCE',
     'performance',
    ('performance', 'REAL', 'NOT NULL'),
    tuple)

_index_tuple = myTuple.MyTuple

LIST_INVESTMENTS_COLUMN_NAMES: list[str] = [TUPLE_INVESTMENTS_DATE[_index_tuple.OPTION_NAME],
                                       TUPLE_INVESTMENTS_SPENDING[_index_tuple.OPTION_NAME],
                                       TUPLE_INVESTMENTS_POSITION[_index_tuple.OPTION_NAME],
                                       TUPLE_INVESTMENTS_EARNINGS[_index_tuple.OPTION_NAME],
                                       TUPLE_INVESTMENTS_PERFORMANCE[_index_tuple.OPTION_NAME]]

INDEX_PRIMARY_KEY = LIST_INVESTMENTS_COLUMN_NAMES.index(TUPLE_INVESTMENTS_DATE[_index_tuple.OPTION_NAME])



