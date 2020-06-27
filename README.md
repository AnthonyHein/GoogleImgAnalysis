# GoogleImgAnalysis

This program scrapes images from Google based on an adjective that the user enters.
The point is to see if there exists biases in the images that are returned by Google
searches. At this point, it is unknown to the program what connotations adjectives carry
so this is not possible. Additionally, the program cannot recognize faces (or races). These
are all features I hope to implement in the future.

The results of the scrape will be output to an html file and opened after each execution.

NOTE: Assumes the existence of a webdriver in a sibling folder.

## Acknowledgements

Adjectives taken from Ashley Bovan (http://www.ashley-bovan.co.uk/words/partsofspeech.html).

Scraping taken from Fabian Bosler (https://towardsdatascience.com/image-scraping-with-python-a96feda8af2d).

## Usage

$ python3 client.py [ search term ] [ modifier]

e.g.
$ python3 client.py uneducated person
$ python3 client.py unprofessional
$ python3 client.py # will automatically generate an adjective.

Clean with:
$ python3 client.py -c
