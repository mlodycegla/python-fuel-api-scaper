import sqlite3, os
from scraper import europe_prices


def init_db():
    if not os.path.exists("instance"):
        os.makedir("instance")

    # initializing database
    open("./instance/gasprices.db", "w+")
    connection = sqlite3.connect("./instance/gasprices.db")
    cursor = connection.cursor()

    # opening schematic file to create a table
    with open("schema.sql") as db_schematic:
        cursor.executescript(db_schematic.read())

    europe_gas_prices = europe_prices()

    # trying to add the prices to database
    try:
        for country_prices in europe_gas_prices:
            cursor.execute(
                f"INSERT INTO europeprices (COUNTRY, GASOLINE, DIESEL, LPG) values ('{country_prices['name']}', '{country_prices['95']}', '{country_prices['diesel']}', '{country_prices['lpg']}')"
            )
        connection.commit()
    except Exception as e:
        print(f"An error has occured: {e}")


init_db()
