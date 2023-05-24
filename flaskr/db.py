import os
import sqlite3

from scraper import europe_prices


def init_db():
    if not os.path.exists("instance"):
        os.makedirs("instance")

    # initializing database
    open("./instance/gasprices.db", "w+")
    connection = sqlite3.connect("./instance/gasprices.db")
    cursor = connection.cursor()

    # opening schematic file to create a table
    with open(os.path.abspath("../flaskr/schema.sql")) as db_schematic:
        cursor.executescript(db_schematic.read())

    europe_gas_prices = europe_prices()

    # trying to add the prices to database
    try:
        for country_prices in europe_gas_prices:
            cursor.execute(
                f"INSERT INTO europeprices (COUNTRY, GASOLINE, DIESEL, LPG) values ('{country_prices['name']}', '{country_prices['95']}', '{country_prices['diesel']}', '{country_prices['lpg']}')"
            )
        connection.commit()
    except Exception as error:
        print(f"An error has occured: {error}")


def get_europeprices_db(range=10, offset=0):
    connection = sqlite3.connect("./instance/gasprices.db")
    cursor = connection.cursor()

    # makes the request to database and returns info about prices in a list
    result = cursor.execute(
        f"SELECT country, gasoline, diesel, lpg FROM europeprices LIMIT {range} OFFSET {offset}"
    )
    list = []
    for row in result.fetchmany(range):
        country = row[0]
        gasprice = row[1]
        dieselprice = row[2]
        lpgprice = row[3]
        list.append(
            {
                "country": country,
                "gasolineprice": gasprice,
                "dieselprice": dieselprice,
                "lpgprice": lpgprice,
            }
        )
    return list


init_db()
