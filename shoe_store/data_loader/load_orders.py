import datetime
import pathlib
from typing import Sequence

import openpyxl
from sqlalchemy.orm import Session

import database.models


def parse_orders(
    source_xlsx_file: str | pathlib.Path,
    session: Session,
    *,
    user_dict: dict[str, database.models.User],
    item_dict: dict[str, database.models.Item],
    pickup_points: Sequence[database.models.PickupPoint],
):
    workbook = openpyxl.load_workbook(source_xlsx_file)
    sheet = workbook.active

    rows = sheet.iter_rows()
    # Skip header
    next(rows)

    orders = []

    for row in rows:
        if all(map(lambda cell: cell.value is None, row)):
            break

        values = list(map(lambda cell: cell.value, row))
        (
            _,
            items_article_numbers,
            order_date,
            deliver_date,
            pickup_point_number,
            user_full_name,
            get_code,
            order_status,
            *_,
        ) = map(lambda cell: cell.value, row)

        order = create_order(
            order_date,
            deliver_date,
            get_code,
            order_status,
        )
        session.add(order)
        session.flush()
        order.user = user_dict[user_full_name]
        order.pickup_point = pickup_points[pickup_point_number - 1]

        items_article_numbers_iter = iter(items_article_numbers.split(', '))
        for article_number, item_count in zip(
            items_article_numbers_iter,
            items_article_numbers_iter
        ):
            ordered_item = database.models.OrderedItem(
                item_count=int(item_count)
            )
            session.add(ordered_item)
            session.flush()
            ordered_item.order = order
            ordered_item.item = item_dict[article_number]
        session.flush()


def create_order(
    order_date: datetime.datetime,
    deliver_date: datetime.datetime,
    get_code: int,
    order_status: str,
) -> database.models.Order:
    return database.models.Order(
        order_date=order_date,
        deliver_date=deliver_date,
        get_code=get_code,
        order_status=order_status,
    )



if __name__ == '__main__':
    parse_orders()
