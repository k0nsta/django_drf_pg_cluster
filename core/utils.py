import csv
from collections import deque
from typing import Any, List, Tuple, Iterable, Generator


def sorted_fields(fields: list, order: list, reverse=False) -> List:
    """Sorting model fields by given order

    Args:
        fields (list): Unsorted list of model field names (str).
        order (list): Sorted list elements in natural squence.
        end_order (bool, optional): If set `True`, then the `fields` sorted
        from the end list. Defaults to False.

    Returns:
        None
    """
    if reverse:
        [fields.sort(key=lambda x: x == i) for i in order]
    else:
        [fields.sort(key=lambda x: x == i, reverse=True) for i in reversed(order)]


class CsvSerializer:

    class EchoBuffer:
        def write(self, value):
            return value

    def __init__(self, buffer: Any = None):
        self.buffer = buffer or self.EchoBuffer()

    def perform(self, db_models: Tuple) -> deque:
        data = deque()
        for model in db_models:
            col_name = model.get_sorted_fields()
            rows = deque(model.objects.values_list(*col_name))
            delimiter_row = tuple('')
            rows.appendleft(col_name)
            rows.append(delimiter_row)
            data += rows
        return data

    def yield_rows(self, data: Iterable[Any]) -> Generator:
        writer = csv.writer(self.buffer)
        return (writer.writerow(row) for row in data)
