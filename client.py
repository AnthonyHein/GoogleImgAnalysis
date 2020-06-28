#-------------------------------------------------------------------------------
# File:     client.py
# Author:   Anthony Hein
#
# Description: Using functions from scrapeImages.py, finds URLs, downloads
# images, makes brief, opens brief, deletes images.
#-------------------------------------------------------------------------------

# Environment variables.
from dotenv import load_dotenv
import os

from sys import argv, exit

import scrapeImages as scrape
from random import randint
import makeBrief

load_dotenv()

if __name__ == "__main__":

    driver_path = os.getenv('DRIVER_PATH')
    search_term = "smart"
    modifier = "person"
    num = 10

    while True:

        print("---------------------------------------------------------------")

        temp = input("Clean?: ")
        if temp != "":
            scrape.clean()
            makeBrief.clean()
            continue

        temp = input("Search term: ")
        if temp != "":
            search_term = temp
        else:
            with open('adjectives.txt', 'r') as file:
                data = file.read().split("\n")
            search_term = data[randint(0, len(data) - 1)]

        temp = input("Modifier: ")
        if temp != "":
            modifier = temp

        temp = input("Number: ")
        if temp != "":
            num = int(temp)

        print("Performing search for \"" + search_term + " " + modifier + "\"")

        image_paths = scrape.search_and_download_faces(search_term + " " + modifier, driver_path, number_images=int(num))

        makeBrief.create(search_term, modifier, image_paths)
        os.system(f"open pages/{search_term}.html")
