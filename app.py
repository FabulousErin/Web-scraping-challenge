from flask import Flask, render_template
from flask_pymongo import PyMongo
import mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    listings = mongo.df
    return render_template("index.html", listings=listings)


@app.route("/scrape")
def scraper():
    listings = mongo.db.listings
    listings.delete_many({})
    listings_data = mars.table()
    listings.insert_many(listings_data)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
