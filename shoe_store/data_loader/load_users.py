import pathlib
from typing import Sequence

import openpyxl

import database.models


def parse_users(
    source_xlsx_file: str | pathlib.Path,
) -> Sequence[database.models.User]:
    workbook = openpyxl.load_workbook(source_xlsx_file)
    sheet = workbook.active

    rows = sheet.iter_rows()
    # Skip header
    next(rows)

    users = []
    for row in rows:
        if all(map(lambda cell: cell.value is None, row)):
            break

        user = create_user(*map(lambda cell: cell.value, row))
        users.append(user)

    return users


def create_user(
    role: str,
    full_name: str,
    email: str,
    password: str,
) -> database.models.User:
    res_role = parse_role(role)
    last_name, first_name, surname = full_name.split()

    return database.models.User(
        user_role=res_role,
        last_name=last_name,
        first_name=first_name,
        surname=surname,
        email=email,
        password=password,
    )


def parse_role(role: str) -> database.models.UserRoleEnum:
    res_role = database.models.UserRoleEnum.EMPTY_ROLE
    match role:
        case 'Администратор':
            res_role = database.models.UserRoleEnum.ADMINISTRATOR
        case 'Менеджер':
            res_role = database.models.UserRoleEnum.MANAGER
        case 'Авторизированный клиент':
            res_role = database.models.UserRoleEnum.AUTHORIZED_CLIENT

    return res_role
