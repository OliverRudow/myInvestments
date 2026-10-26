"""myPerformanceAssessment.py."""

__title__: str = "myPerformanceAssessment"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
from typing import Optional
from datetime import date
from mytuple import myTuple
from mysharesdefinition import myRankingWatchListDefinitions, myOrderVectorDefinition
from mydatabase import mySQLDataBase
from myfilebase import myFileBase
from myauxiliary import myAuxiliary


STR_WORKING_DIRECTORY: str = '/Users/oliverrudow/PycharmProjects/Data'

def built_dict_from_two_lists(list_key: list, list_value: list) -> dict:

    if list_key.__len__() == list_value.__len__():

        return dict(zip(list_key, list_value))

    else:

        return {}

@dataclasses.dataclass(init=False)
class MyPerformanceAssessment(mySQLDataBase.MySQLDataBase):
    """

    """

    # Tuple Definition
    _index_tuple: myTuple.MyTuple = dataclasses.field(repr=False, default_factory=type(myTuple.MyTuple))

    _str_working_directory: str = dataclasses.field(init=False, default_factory=str)

    # FileBase
    _my_file: myFileBase.MyFileBase = dataclasses.field(repr=False, default_factory=type(myFileBase.MyFileBase))

    # ranking column numbers
    _int_ranking_watch_list_analyst_score_column_index: int = dataclasses.field(repr=False, default=0)
    _int_ranking_watch_list_derivate_score_column_index: int = dataclasses.field(repr=False, default=0)
    _int_ranking_watch_list_fundamentals_score_column_index: int = dataclasses.field(repr=False, default=0)
    _int_ranking_watch_list_performance_score_column_index: int = dataclasses.field(repr=False, default=0)
    _int_ranking_watch_list_overall_score_column_index: int = dataclasses.field(repr=False, default=0)
    _int_ranking_watch_list_shift_column_index: int = dataclasses.field(repr=False, default=0)

    _list_ranking_list_column_names: list = dataclasses.field(init=False, default_factory=list)

    # order vector section names
    _int_order_vector_header_segment_index: int = dataclasses.field(repr=False, default=0)
    _int_order_vector_ranking_segment_index: int = dataclasses.field(repr=False, default=0)
    _int_order_vector_analyst_segment_index: int = dataclasses.field(repr=False, default=0)
    _int_order_vector_derivate_segment_index: int = dataclasses.field(repr=False, default=0)
    _int_order_vector_fundamentals_segment_index: int = dataclasses.field(repr=False, default=0)
    _int_order_vector_performance_segment_index: int = dataclasses.field(repr=False, default=0)

    _list_order_vector_segment_names: list = dataclasses.field(init=False, default_factory=list)

    _list_performance_vector: list = dataclasses.field(init=False, default_factory=list)

    _list_order_vectors: list = dataclasses.field(init=False, default_factory=list)

    _list_working_days_from_order_list: list = dataclasses.field(init=False, default_factory=list)

    _list_performance_change_from_order_list: list = dataclasses.field(init=False, default_factory=list)

    _list_overall_score_change_from_order_list: list = dataclasses.field(init=False, default_factory=list)

    _list_analyst_score_change_from_order_list: list = dataclasses.field(init=False, default_factory=list)

    _list_derivate_score_change_from_order_list: list = dataclasses.field(init=False, default_factory=list)

    _list_fundamentals_score_change_from_order_list: list = dataclasses.field(init=False, default_factory=list)

    _list_performance_score_change_from_order_list: list = dataclasses.field(init=False, default_factory=list)

    def __init__(self, str_working_directory: Optional[str] = None) -> None:
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

        self._list_ranking_list_column_names = myRankingWatchListDefinitions.LIST_RANKING_WATCH_LIST_COLUMN_NAMES

        self._init_ranking_column_numbers()

        self._list_order_vector_segment_names = myOrderVectorDefinition.LIST_ORDER_VECTOR_COLUMN_NAMES

        self._init_order_vector_segment_indices()

        self._list_order_ids = []

        self._list_performance_vector = []

        self._list_order_vectors = []

        self._list_working_days_from_order_list = []

        self._list_performance_change_from_order_list = []

        self._list_overall_score_change_from_order_list = []

        self._list_analyst_score_change_from_order_list = []

        self._list_derivate_score_change_from_order_list = []

        self._list_fundamentals_score_change_from_order_list = []

        self._list_performance_score_change_from_order_list = []

    def _init_ranking_column_numbers(self) -> None:

        self._int_ranking_watch_list_analyst_score_column_index = self._list_ranking_list_column_names.index(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_ANALYST_SCORE[self._index_tuple.DATA_CONTENT][0])

        self._int_ranking_watch_list_derivate_score_column_index = self._list_ranking_list_column_names.index(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_DERIVATE_SCORE[self._index_tuple.DATA_CONTENT][0])

        self._int_ranking_watch_list_fundamentals_score_column_index = self._list_ranking_list_column_names.index(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_FUNDAMENTALS_SCORE[self._index_tuple.DATA_CONTENT][0])

        self._int_ranking_watch_list_performance_score_column_index = self._list_ranking_list_column_names.index(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_PERFORMANCE_SCORE[self._index_tuple.DATA_CONTENT][0])

        self._int_ranking_watch_list_overall_score_column_index = self._list_ranking_list_column_names.index(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_OVERALL_SCORE[self._index_tuple.DATA_CONTENT][0])

        self._int_ranking_watch_list_shift_column_index = self._list_ranking_list_column_names.index(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_SHIFT[self._index_tuple.DATA_CONTENT][0])

    def _init_order_vector_segment_indices(self) -> None:

        self._int_order_vector_header_segment_index = self._list_order_vector_segment_names.index(
            myOrderVectorDefinition.TUPLE_ORDER_VECTOR_HEADER[self._index_tuple.DATA_CONTENT][0])

        self._int_order_vector_ranking_segment_index = self._list_order_vector_segment_names.index(
            myOrderVectorDefinition.TUPLE_ORDER_VECTOR_RANKING[self._index_tuple.DATA_CONTENT][0])

        self._int_order_vector_analyst_segment_index = self._list_order_vector_segment_names.index(
            myOrderVectorDefinition.TUPLE_ORDER_VECTOR_ANALYST[self._index_tuple.DATA_CONTENT][0])

        self._int_order_vector_derivate_segment_index = self._list_order_vector_segment_names.index(
            myOrderVectorDefinition.TUPLE_ORDER_VECTOR_DERIVATE[self._index_tuple.DATA_CONTENT][0])

        self._int_order_vector_fundamentals_segment_index = self._list_order_vector_segment_names.index(
            myOrderVectorDefinition.TUPLE_ORDER_VECTOR_FUNDAMENTALS[self._index_tuple.DATA_CONTENT][0])

        self._int_order_vector_performance_segment_index = self._list_order_vector_segment_names.index(
            myOrderVectorDefinition.TUPLE_ORDER_VECTOR_PERFORMANCE[self._index_tuple.DATA_CONTENT][0])

    def reset_lists(self) -> None:

        self._list_order_ids = []

        self._list_performance_vector = []

        self._list_order_vectors = []

        self._list_working_days_from_order_list = []

        self._list_performance_change_from_order_list = []

        self._list_overall_score_change_from_order_list = []

        self._list_analyst_score_change_from_order_list = []

        self._list_derivate_score_change_from_order_list = []

        self._list_fundamentals_score_change_from_order_list = []

        self._list_performance_score_change_from_order_list = []

    def set_performance_vector(self, list_performance_vector: list) -> None:

        self._list_performance_vector = list_performance_vector

    def set_list_order_vectors(self, list_order_vectors: list) -> None:

        self._list_order_vectors = list_order_vectors

    def calc_order_vectors_working_days(self):

        if self._list_performance_vector.__len__() > 0:

            end_date = self._list_performance_vector[0][0]

        else:

            end_date = str(date.today())

        if  self._list_order_vectors.__len__() > 0:

            start_date = []

            id_ov_segment  = self._int_order_vector_header_segment_index

            for element in self._list_order_vectors:

                start_date.append(element[id_ov_segment][1])

            self._list_working_days_from_order_list = []

            for element in start_date:

                self._list_working_days_from_order_list.append(myAuxiliary.calc_business_days(element, end_date))

    def calc_order_vectors_total_performance(self):

        if self._list_order_vectors.__len__() > 0:

            self._list_performance_change_from_order_list = []

            id_ov_segment = self._int_order_vector_header_segment_index

            for element in self._list_order_vectors:

                self._list_performance_change_from_order_list.append(element[id_ov_segment][10])

    def calc_order_vectors_overall_score_change(self):
        # Standardwert setzen
        today_overall_score = 0

        id_ov_ranking = self._int_order_vector_ranking_segment_index

        # Schutz vor IndexError (len > 1, da auf Index 1 zugegriffen wird)
        if len(self._list_performance_vector) > 1:

            today_overall_score = self._list_performance_vector[id_ov_ranking][
                self._int_ranking_watch_list_overall_score_column_index
            ]

        # Lokale Cache-Variable für den langen Spaltenindex
        idx = self._int_ranking_watch_list_overall_score_column_index
        results = []

        # Pythonischer Check auf gefüllte Liste
        if self._list_order_vectors:

            for element in self._list_order_vectors:

                overall_score = element[id_ov_ranking][idx]

                if overall_score is None:

                    score_change = ''

                elif overall_score == 0:

                    score_change = 0

                else:

                    score_change = round(((today_overall_score - overall_score) / overall_score * 100), 2)

                results.append(score_change)

        self._list_overall_score_change_from_order_list = results

    def calc_order_vectors_analyst_change(self):
        # Standardwert setzen
        today_analyst_score = 0

        id_ov_ranking = self._int_order_vector_ranking_segment_index

        # Schutz vor IndexError (len > 1, da auf Index 1 zugegriffen wird)
        if len(self._list_performance_vector) > 1:

            today_analyst_score = self._list_performance_vector[id_ov_ranking][
                self._int_ranking_watch_list_analyst_score_column_index
            ]

            # Early Exit, falls der heutige Score fehlt
        if today_analyst_score is None:

            self._list_analyst_score_change_from_order_list = []

            return

        # Lokale Cache-Variable für den langen Spaltenindex
        idx = self._int_ranking_watch_list_analyst_score_column_index

        results = []

        # Pythonischer Check auf gefüllte Liste (leere Listen evaluieren zu False)
        if self._list_order_vectors:

            for element in self._list_order_vectors:

                analyst_score = element[id_ov_ranking][idx]

                if analyst_score is None:

                    score_change = ''

                elif analyst_score == 0:

                    score_change = 0

                else:

                    score_change = round(((today_analyst_score - analyst_score) / analyst_score * 100), 2)

                results.append(score_change)

        self._list_analyst_score_change_from_order_list = results

    def calc_order_vectors_derivate_change(self):
        # Standardwert setzen
        today_derivate_score = 0

        id_ov_ranking = self._int_order_vector_ranking_segment_index

        # Schutz vor IndexError (len > 1, da auf Index 1 zugegriffen wird)
        if len(self._list_performance_vector) > 1:

            today_derivate_score = self._list_performance_vector[id_ov_ranking][self._int_ranking_watch_list_derivate_score_column_index]

        # Early Exit, falls der heutige Score fehlt
        if today_derivate_score is None:

            self._list_derivate_score_change_from_order_list = []

            return

        # Index als sprechende Variable für bessere Lesbarkeit
        idx = self._int_ranking_watch_list_derivate_score_column_index

        results = []

        for element in self._list_order_vectors:

            derivate_score = element[id_ov_ranking][idx]

            if derivate_score is None:

                score_change = ''

            elif derivate_score == 0:

                score_change = 0

            else:

                score_change = round(((today_derivate_score - derivate_score) / derivate_score * 100), 2)

            results.append(score_change)

        self._list_derivate_score_change_from_order_list = results

    def calc_order_vectors_fundamentals_change(self):

        today_fundamentals_score = 0

        id_ov_ranking = self._int_order_vector_ranking_segment_index

        # Schutz vor IndexError (len > 1 statt > 0, da auf Index 1 zugegriffen wird)
        if len(self._list_performance_vector) > 1:
            today_fundamentals_score = self._list_performance_vector[id_ov_ranking][
                self._int_ranking_watch_list_fundamentals_score_column_index
            ]

        # Early Exit, falls der heutige Score fehlt
        if today_fundamentals_score is None:

            self._list_fundamentals_score_change_from_order_list = []

            return

        # Lokale Cache-Variable für den langen Spaltenindex
        idx = self._int_ranking_watch_list_fundamentals_score_column_index

        results = []

        for element in self._list_order_vectors:

            fundamentals_score = element[id_ov_ranking][idx]

            if fundamentals_score is None:

                score_change = ''

            elif fundamentals_score == 0:

                score_change = 0

            else:

                score_change = round(((today_fundamentals_score - fundamentals_score) / fundamentals_score * 100), 2)

            results.append(score_change)

        self._list_fundamentals_score_change_from_order_list = results

    def calc_order_vectors_performance_change(self):

        today_performance_score = 0

        id_ov_ranking = self._int_order_vector_ranking_segment_index

        if len(self._list_performance_vector) > 1:
            today_performance_score = self._list_performance_vector[id_ov_ranking][
                self._int_ranking_watch_list_performance_score_column_index
            ]

        if today_performance_score is None:

            self._list_performance_score_change_from_order_list = []

            return

        # List Comprehension für bessere Performance und Lesbarkeit
        idx = self._int_ranking_watch_list_performance_score_column_index

        results = []

        for element in self._list_order_vectors:

            performance_score = element[id_ov_ranking][idx]

            if performance_score is None:

                score_change = ''

            elif performance_score == 0:

                score_change = 0

            else:

                score_change = round(((today_performance_score - performance_score) / performance_score * 100), 2)

            results.append(score_change)

        self._list_performance_score_change_from_order_list = results


if __name__ == "__main__":

    my_performance_assessment = MyPerformanceAssessment()
