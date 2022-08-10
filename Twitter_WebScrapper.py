# Import Dependencies
import re
import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from msedge.selenium_tools import Edge, EdgeOptions
from selenium import webdriver
from selenium.webdriver.common.by import By

# create instance of web driver #call microsoft edge
options = EdgeOptions()
options.use_chromium = True
driver = webdriver.Edge()

# navigate to login screen
driver.get('https://www.twitter.com/login')
driver.maximize_window()
subject = "Netflix Controversy"

# Setup the log in
sleep(3)
username = driver.find_element(By.XPATH, "//input[@name='text']")
username.send_keys("esg_artemis")
next_button = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
next_button.click()

sleep(3)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys('artemis.esg1')
log_in = driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]")
log_in.click()

# Search item and fetch it
sleep(3)
search_box = driver.find_element(By.XPATH, "//input[@data-testid='SearchBox_Search_Input']")
search_box.send_keys(subject)
search_box.send_keys(Keys.ENTER)

sleep(3)
latest = driver.find_element(By.XPATH,
                             '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div['
                             '2]/nav/div/div[2]/div/div[2]/a/div/span')
latest.click()

sleep(3)
Usernames = []
TimeStamps = []
Tweets = []
Replies = []
Retweets = []
Likes = []

articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
while True:
    for article in articles:
        Username = driver.find_element(By.XPATH, ".//div[@data-testid='User-Names']").text
        TimeStamp = driver.find_element(By.XPATH, ".//time").get_attribute('datetime')
        Tweet = driver.find_element(By.XPATH, ".//div[@data-testid='tweetText']").text
        Reply = driver.find_element(By.XPATH, ".//div[@data-testid='reply']").text
        Retweet = driver.find_element(By.XPATH, ".//div[@data-testid='retweet']").text
        Like = driver.find_element(By.XPATH, "//div[@data-testid='like']").text

        if Username not in Usernames:
            Usernames.append(Username)
            TimeStamps.append(TimeStamp)
            Tweets.append(Tweet)
            Replies.append(Reply)
            Retweets.append(Retweet)
            Likes.append(Like)

    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(3)
    articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
    Tweets2 = list(set(Tweets))
    if len(Tweets2) > 5:
        break


# importing pandas as pd
import pandas as pd


# dictionary of lists
dataframe = {'UserName': Usernames, 'TimeStamps': TimeStamps, 'Tweets': Tweets, 'Replies': Replies, 'Retweets': Retweets, 'Likes': Likes,}

df = pd.DataFrame(dataframe)

# saving the dataframe
df.to_csv('Netflix.csv')
