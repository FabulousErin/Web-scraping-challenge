from bs4 import BeautifulSoup
import pandas as pd
from splinter import Browser


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

def scrapeNew():
    browser = init_browser()
    listings = []
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    news_title = soup.find_all("div", {"class": "content_title"})
    print(news_title[1].get_text())

    news_title.pop(0)

    clean_titles = []

    for title in news_title:
        title_dictionary = {
            "title": title.get_text()
        }
        clean_titles.append(title_dictionary)

    print(clean_titles)
    return clean_titles

    


def table():
    mars_facts_webpage = 'https://space-facts.com/mars/'
    table = pd.read_html(mars_facts_webpage)
    print(table)
    return table



#!jupyter nbconvert --to python mission_to_mars.ipynb