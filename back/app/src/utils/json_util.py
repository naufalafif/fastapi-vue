import json
from typing import Dict


def is_valid_json(object_to_check: Dict) -> bool:
    """
    check is object is valid json.dumps object
    :param object_to_check:
    :return: Bool

    Example:
        >>> valid_object = {"name": "naufal", "age":23}
        >>> is_valid_json(valid_object)
        True
        >>> invalid_object = {"dict": Dict}
        >>> is_valid_json(invalid_object)
        False
    """
    try:
        json.dumps(object_to_check)
        return True
    except TypeError as err:
        return False


def sql_object_to_dict(sql_object) -> Dict:
    data = {}
    for column in sql_object.__table__.columns:
        data[column.name] = str(getattr(sql_object, column.name))

    return data
