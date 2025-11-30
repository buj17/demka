import pathlib
from typing import Sequence

import openpyxl

import database.models


def parse_pickup_points(
    source_xlsx_file: str | pathlib.Path,
) -> Sequence[database.models.PickupPoint]:
    workbook = openpyxl.load_workbook(source_xlsx_file)
    sheet = workbook.active

    rows = sheet.iter_rows()

    pickup_points = []
    for row in rows:
        if all(map(lambda cell: cell.value is None, row)):
            break

        pickup_point = create_pickup_point(*map(lambda cell: cell.value, row))
        pickup_points.append(pickup_point)

    return pickup_points

def create_pickup_point(address: str) -> database.models.PickupPoint:
    return database.models.PickupPoint(
        address=address,
    )

