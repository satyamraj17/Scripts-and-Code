# Scrap the songs list from www.notationsworld.com, a site which post the sargam and flute notes of songs.

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def calculate_total_pages(driver):
    total_pages = driver.find_elements(By.XPATH, '//a[@class="page-numbers"]')[1].text
    return total_pages.split("\n")[1]

def scrapper(song_list, url_type):
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    driver.get(url_type+str(1))
    sleep(3)
    total_pages = calculate_total_pages(driver=driver)
    for i in range(2,int(total_pages)+1):
        sleep(3)
        names = driver.find_elements(By.XPATH, "//a[@rel='bookmark']")
        for name in names:
            s = name.text
            s = s.split('–')
            song_list.append(f"Page {i-1} {s[0]}")
        sleep(3)
        driver.get(url_type+str(i))


def hindi_songs(song_list):
    url = "https://www.notationsworld.com/category/hindi-songs/page/"
    scrapper(song_list=song_list, url_type=url)
    with open("hindi_song_list.txt", 'w') as f:
        for name in song_list:
            f.write(name)
            f.write('\n')

def english_songs(song_list):
    url = "https://www.notationsworld.com/category/western-song/page/"
    scrapper(song_list=song_list, url_type=url)
    with open("western_song_list.txt", 'w') as f:
        for name in song_list:
            f.write(name)
            f.write('\n')


song_names = list()
song_type = input("Enter the type of songs you want to extract: Hindi or Western/English: ")

if (song_type.lower()=="hindi"):
    hindi_songs(song_list=song_names)
elif (song_type.lower()=="english" or song_type.lower()=="western"):
    english_songs(song_list=song_names)
else:
    print("Please enter among the available options!")

