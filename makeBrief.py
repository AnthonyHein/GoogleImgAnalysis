#-------------------------------------------------------------------------------
# File:     makeBrief.py
# Author:   Anthony Hein
#
# Description: Compiles scraped images into an easy to digest html page.
#-------------------------------------------------------------------------------

from string import Template
import os
import glob

# Read in a file as a template, which enables substitution.
def _readTemplate():
    with open("briefTpl.html", 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def create(search_term="", modifier="", image_paths=[], target_path='./pages'):
    images_html = ""
    for image in image_paths:
        images_html += "<img src=\"." + image + "\" alt=\"" + search_term + "\" style=\"height:300px;width:auto;\"><br>"

    f = open(f"{target_path}/{search_term}.html", "w")
    tpl = _readTemplate()
    html = tpl.substitute(SEARCH=search_term.upper() + " " + modifier.upper(), IMAGES=images_html)
    f.write(html)
    f.close()

    print("SUCCESS - Made briefing.")

def clean(target_path='./pages'):
    target_folder = os.path.join(target_path)
    files = glob.glob(target_folder + "/*.html", recursive=True)

    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))

    print("SUCCESS - Cleaned html filetree.")
