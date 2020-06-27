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

    str = "person"

    # Cleaning.
    if len(argv) == 2 and argv[1] == '-c':
        scrape.clean()
        makeBrief.clean()
        exit(0)

    # Querying.
    if len(argv) >= 3:
        str = argv[2]
    if len(argv) >= 2:
        search_term = argv[1]
    else:
        print("I'm feeling lucky!")
        with open('adjectives.txt', 'r') as file:
            data = file.read().split("\n")
        search_term = data[randint(0, len(data) - 1)]

    driver_path = os.getenv('DRIVER_PATH')

    print("Performing search for \"" + search_term + " " + str + "\"")

    image_paths = scrape.search_and_download(search_term + " " + str, driver_path)

    makeBrief.create(search_term, image_paths)
    os.system(f"open pages/{search_term}.html")
