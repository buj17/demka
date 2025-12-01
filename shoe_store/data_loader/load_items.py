import pathlib
import shutil
from typing import Sequence

import openpyxl

import config.settings
import database.models


def parse_items(
    source_xlsx_file: str | pathlib.Path,
) -> Sequence[database.models.Item]:
    workbook = openpyxl.load_workbook(source_xlsx_file)
    sheet = workbook.active

    rows = sheet.iter_rows()
    # Skip header
    next(rows)

    items = []
    for row in rows:
        if all(map(lambda cell: cell.value is None, row)):
            break

        values = list(map(lambda cell: cell.value, row))

        item = create_item(*values)
        items.append(item)

    return items


def create_item(
    article_number: str,
    name: str,
    measure: str,
    price: int,
    supplier: str,
    producer: str,
    category: str,
    current_discount: int,
    stock_quantity: int,
    description: str,
    image_filename: str | None = None,
) -> database.models.Item:
    # Replace nbsp char to common space
    description = description.replace(chr(160), ' ')

    kwargs = {
        'article_number': article_number,
        'name': name,
        'price': price,
        'supplier': supplier,
        'producer': producer,
        'category': category,
        'current_discount': current_discount,
        'stock_quantity': stock_quantity,
        'measure': measure,
        'description': description,
    }
    if image_filename is not None:
        shutil.copy(
            config.settings.BASE_DIR / 'import_data' / image_filename,
            config.settings.BASE_DIR / 'media',
        )
        kwargs['image_filename'] = image_filename

    return database.models.Item(**kwargs)


if __name__ == '__main__':
    parse_items(
        config.settings.BASE_DIR / 'import_data' / 'item_import.xlsx',
    )
