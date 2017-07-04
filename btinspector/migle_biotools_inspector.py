import pandas as pd
import re

# reading in the data as a data frame
data = pd.read_table("problematic_descriptions_migle.tsv")

# storing only the tool description column
descriptions = data.tool_description

# storing only the tool name column
tool_names = data.tool_name

def length_checker(text):
    '''a function for checking if the length of text is more than
    10 characters and less than 500'''
    if len(text) < 10 or len(text) > 500:
        print "Error: the length of description is not right"

def url_checker(text):
    '''a function for checking if the text contains URL'''
    url_regex = re.compile("http|www.")
    if url_regex.search(text):
        print "Error: the description contains URL"

def names_checker(text, name):
    '''a function for checking if the text contains the tool name'''
    name_regex = re.compile(name)
    if name_regex.search(text):
        print "Error: the description contains a tool name"

def character_checker(text):
    '''a function for checking if the text contains unwanted characters'''
    character_regex = re.compile("\\bold|\n|\r|\t")
    if character_regex.search(text):
        print "Error: the text contains unwanted symbols"

def checker(text, name=None, url_check=True, names_check=True,
            length_check=True, character_check=True):
    '''a function for checking if the given text (e.g. tool description,
    tool name, etc.) is written according to all the requirements

    if url_check is False, it is not checked if URL is included in the text
    if names_check is False, it is not checked if tool name is included in the text
    if length_check is False, it is not checked if the length of text is more than
    10 characters and less than 500
    if character_check is False, it is not checked if the text contain unwanted characters'''
    name = "No name provided" if name is None else name
    print name
    if length_check==True:
        length_checker(text)
    if url_check==True:
        url_checker(text)
    if names_check==True:
        if name is "No name provided":
            print "Error: no names provided. Names can't be checked"
        else:
            names_checker(text, name)
    if character_check==True:
        character_checker(text)


def data_iterator(texts, names=None):
    '''a function for iteration over the data frame and
    applying checker function'''
    names = "No names provided" if names is None else names
    if names is not "No names provided":
        if len(texts)==len(names):
            for i in range(len(texts)):
                checker(texts[i], names[i])
        else:
            print "The length of two lists is different"
    else:
        for i in range(len(texts)):
            checker(texts[i])



data_iterator(descriptions, tool_names)
# data_iterator(descriptions)

