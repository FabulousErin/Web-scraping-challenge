#from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd


def init_browser():
    executable_path = {"executable_path": "C:\\Users\\erinn\\Documents\\WashU\\chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    listings = []

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


def table():
    mars_facts_webpage = 'https://space-facts.com/mars/'
    table = pd.read_html(mars_facts_webpage)
    print(table)
    return table



#!jupyter nbconvert --to python mission_to_mars.ipynb