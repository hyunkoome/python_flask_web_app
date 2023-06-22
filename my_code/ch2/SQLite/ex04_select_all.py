# Install sqlitebrowser with GUI for Ubuntu (Stable release)
# For Ubuntu and derivatives, @deepsidhu1313 provides a PPA with the latest release here:
# https://launchpad.net/~linuxgndu/+archive/ubuntu/sqlitebrowser
# To add this PPA just type in this command in terminal:#
# $ sudo add-apt-repository -y ppa:linuxgndu/sqlitebrowser
# Then update the cache using:#
# $ sudo apt-get update
# Install the package using:#
# $ sudo apt-get install sqlitebrowser

import sqlite3
from sqlite3 import Error
import typing


def connect_sqlite():
    try:
        con = sqlite3.connect('../apps/db/db.db')
        return con
    except Error:
        print(Error)


def create_table(con: sqlite3.Connection) -> None:
    cursor_db = con.cursor()
    being_table = check_table_existence(con=con, table_name='chechup')
    if not being_table:
        cursor_db.execute(
            "CREATE TABLE chechup(id integer PRIMARY KEY, Name text, Height real, Weight real, Measured_data text)")
        con.commit()


def insert_one(con: sqlite3.Connection, one_data: typing.Tuple) -> None:
    cursor_db = con.cursor()
    cursor_db.execute("INSERT INTO chechup(id, Name, Height, Weight, Measured_data) VALUES (?, ?, ?, ?, ?)", one_data)
    con.commit()


def check_table_existence(con: sqlite3.Connection, table_name: str) -> bool:
    cursor_db = con.cursor()
    sql_cmd = "SELECT count(*) as count FROM sqlite_master WHERE type='table' AND name='{}'".format(table_name)
    cursor_db.execute(sql_cmd)
    result = cursor_db.fetchone()
    return bool(result[0])  # 1: existence, 0: not existence


def update_one(con: sqlite3.Connection, table_name: str, search_id: int, search_field_name: str, update_value: str):
    cursor_db = con.cursor()
    sql_cmd = "UPDATE {} SET {} = '{}' where id = {}".format(table_name, search_field_name, update_value, search_id)
    cursor_db.execute(sql_cmd)
    con.commit()

def search_all(con: sqlite3.Connection, table_name: str):
    cursor_db = con.cursor()
    sql_cmd = "SELECT * FROM {}".format(table_name)
    cursor_db.execute(sql_cmd)
    raw_datas = cursor_db.fetchall()
    for one_data in raw_datas:
        print(one_data)


if __name__ == '__main__':
    con = connect_sqlite()
    search_all(con=con, table_name='chechup')
