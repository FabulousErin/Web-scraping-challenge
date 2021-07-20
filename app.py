from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars



app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
   # listings = mongo.df

    single_title = mongo.db.mars_titles.find_one()
    
    return render_template("index.html", dbperson=single_title)


@app.route("/scrape")
def scraper():
    db = mongo.db.mars_titles
    all_titles = mars.scrapeNew()
    db.update({}, all_titles[0], upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
