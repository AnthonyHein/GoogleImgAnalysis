#-------------------------------------------------------------------------------
# File:     client.py
# Author:   Anthony Hein
#
# Description: Using functions from scrapeImages.py
#-------------------------------------------------------------------------------

# Environment variables.
from dotenv import load_dotenv
import os

from sys import argv

import scrapeImages as scrape
from random import randint

load_dotenv()

if __name__ == "__main__":

    if len(argv) == 2:
        search_term = argv[1] + " people"
    else:
        print("I'm feeling lucky!")
        with open('adjectives.txt', 'r') as file:
            data = file.read().split("\n")
        search_term = data[randint(0, len(data) - 1)] + " people"

    driver_path = os.getenv('DRIVER_PATH')

    print("Performing search for \"" + search_term + "\"")

    scrape.search_and_download(search_term, driver_path)

    os.system("open brief.html")
