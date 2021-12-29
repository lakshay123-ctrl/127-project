from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome(r"C:/Users/Lenovo/Desktop/python/127project/chromedriver")
browser.get(START_URL)
time.sleep(10)


def scrape():
    headers = ["VMag","name","designation","distance","spectral class","mass","radius","luminosity"]
    star_data = []

    for i in range(0,1):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for tr_tag in soup.find_all("tr",attrs = {"class","headerSort"}):
            td_tags = tr_tag.find_all("td")
            temp_list = []
            for index,td_tag in enumerate(td_tags):
               if index == 1:
                 temp_list.append(li_tag.find_all("a")[1].contents[1])
               else:
                    try:
                      temp_list.append(td_tag.contents[1])
                    except:
                      temp_list.append("")
            star_data.append(temp_list)
    with open("scrapper.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)                    


scrape()           
