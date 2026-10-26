"""myDecisionEngine.py."""

__title__: str = "myDecisionEngine"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
import json
import operator
from typing import Optional
from myfilebase import myFileBase

STR_WORKING_DIRECTORY: str = '/Users/oliverrudow/PycharmProjects/Data'
STR_JSON_FILE_NAME: str = 'rules.json'


@dataclasses.dataclass(init=False)
class MyDecisionEngine():
    """

    """

    _str_working_directory: str = dataclasses.field(init=False, default_factory=str)

    _str_json_file_name: str = dataclasses.field(init=False, default_factory=str)

    # FileBase
    _my_file: myFileBase.MyFileBase = dataclasses.field(repr=False, default_factory=type(myFileBase.MyFileBase))

    _json_rules: list | dict = dataclasses.field(repr=False, default_factory=dict)

    _operators: dict = dataclasses.field(repr=False, default_factory=dict)

    def __init__(self, str_working_directory: Optional[str] = None, str_json_file_name: Optional[str] = None) -> None:

        # init FileBase w/o Config
        self._my_file = myFileBase.MyFileBase()

        if str_working_directory is not None:

            self._my_file.set_directory(str_working_directory)

        else:

            self._my_file.set_directory(STR_WORKING_DIRECTORY)

        self._str_working_directory = self._my_file.get_directory_name

        if str_json_file_name is not None:

            self._my_file.set_file_name(str_json_file_name)

        else:

            self._my_file.set_file_name(STR_JSON_FILE_NAME)

        self._str_json_file_name = self._my_file.get_entire_file_name

        self._json_rules = self._load_rules(self._str_json_file_name)

        self._operators = {
            ">=": operator.ge,
            "<=": operator.le,
            ">": operator.gt,
            "<": operator.lt,
            "==": operator.eq
        }

        print(self._json_rules)

    def _load_rules(self, str_file_name: str) -> list | dict:
        """Lädt die Regeln aus der JSON-Datei."""
        try:

            with open(str_file_name, 'r', encoding='utf-8') as f:

                return json.load(f)

        except FileNotFoundError:

            print(f"----Fehler: Datei {str_file_name} nicht gefunden.")

            return []

    def evaluate(self, market_data):
        """
        Überprüft alle Regeln gegen die aktuellen Marktdaten.
        market_data: Dictionary mit aktuellen Werten, z.B. Verlusten über Zeiträume.
        """
        triggered_actions = []

        for rule in self._json_rules:
            cond_type = rule["condition"]
            op_str = rule["operator"]
            p1 = rule["param_1"]  # Schwellenwert (z.B. 5%)
            p2 = rule["param_2"]  # Zeitraum (z.B. 1 Werktag)

            # Prüfen, ob der passende Operator existiert
            if op_str not in self._operators:
                continue

            op_func = self._operators[op_str]

            # Dynamische Auswertung basierend auf dem Zeitraum (param_2)
            # Wir holen uns aus den Marktdaten den realen Wert für diesen Zeitraum
            actual_value = market_data.get(cond_type, {}).get(p2)

            if actual_value is not None:
                # Hier passiert die Magie: z.B. op_func(5.5, 5.0) -> 5.5 >= 5.0 -> True
                if op_func(actual_value, p1):
                    triggered_actions.append({
                        "rule_id": rule["id"],
                        "rule_name": rule["name"],
                        "action": rule["action"],
                        "message": rule["text"],
                        "actual_value": actual_value
                    })

        return triggered_actions

if __name__ == "__main__":

    my_decision_engine = MyDecisionEngine()
