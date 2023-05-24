from flask import Flask, render_template, request
from multiprocessing import Process, Value
import schedule
import time
import sys

sys.path.append("../flaskr")
import db

app = Flask(
    __name__, static_url_path="", static_folder="static", template_folder="templates"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/europe")
def europe():
    return render_template("europeprices.html")


@app.route("/api/europe", methods=["GET"])
def europeprices():
    # getting url parameters and getting prices from database
    range = request.args.get("range", default=10, type=int)
    offset = request.args.get("offset", default=0, type=int)
    return db.get_europeprices_db(range, offset)


# activates every day at 2am - scrapes prices from website and updates the database within "db" file
def updatedb():
    schedule.every().day.at("02:00").do(db.init_db)
    while True:
        schedule.run_pending()
        time.sleep(3600)


# starts flask and while loop on different processes
if __name__ == "__main__":
    recording_on = Value("b")
    p = Process(target=updatedb)
    p.start()
    app.run()
    p.join()
