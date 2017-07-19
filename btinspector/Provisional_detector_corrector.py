# coding: utf-8

import csv
import re

# Collection of reporter functions
def dot_checker(text):
    ''' This function checks if the text ends with a dot '''
    if text[-1] != ".":
        return "Error: the description does not end with a dot"

def last_space_checker(text):
    ''' This function checks if the second last character of the text is a space '''
    if text[-2] == (" "):
        return "Error: the description previous last character is a space"

def space_checker(text):
    ''' This function checks that the text has at least one space in it '''
    if not (" ") in text:
        return "Error: the description is a single word"

def length_checker(text):
    ''' This function checks if the length of the text is less than 10 or more than 500 characters '''
    if len(text) < 10:
        return "Error: the length of the description is too short"
    elif len(text) > 500:
        return "Error: the length of the description is too long"

def url_checker(text):
    ''' This function checks if the text contains an URL '''
    url_regex = re.compile("http|www.")
    if url_regex.search(text):
        return "Error: the description contains an URL"

def names_checker(text, name):
    ''' This function checks if the text contains the tool name '''
    name_regex = re.compile(name)
    if name_regex.search(text):
        return "Error: the description contains a tool name"

def character_checker(text):
    ''' This function checks if the text contains some unwanted characters '''
    new_line_regex = re.compile("\n")
    carriage_return_regex = re.compile("↵")
    tab_regex = re.compile("\t")
    escape_regex = re.compile("\\bold")
    bullet_point_regex = re.compile("•")
    unknown_symbol_regex = re.compile("|�")

    error_list = []

    if new_line_regex.search(text):
        error_list.append("Error: the description contains new lines")
    if carriage_return_regex.search(text):
        error_list.append("Error: the description contains carriage returns")
    if tab_regex.search(text):
        error_list.append("Error: the description contains tabs")
    if escape_regex.search(text):
        error_list.append("Error: the description contains escape characters")
    if bullet_point_regex.search(text):
        error_list.append("Error: the description contains bullet points")
    if unknown_symbol_regex.search(text):
        error_list.append("Error: the description contains unknown symbols")

    return error_list


def fixer(text):
    ''' This function returns a capitalized description with an ending dot if it does not have one '''
    if dot_checker(text):
        return text[0].capitalize() + text[1:] + "."


def checker(text, name = None, dots_caps = True, last_space_check = True, space_check = True,
            length_check = True, url_check = True, names_check = True, character_check = True):
    ''' This function checks if the given text (tool description and tool name) is written according the requirements:

    If dots_caps is False, the text is not checked if it has an ending dot nor fixed
    If last_space_check is False, the text is not checked if its second last character is a space
    If space_check is False, the text is not checked if it has a space in it
    If length_check is False, the text is not checked if its length is out of limits
    If url_check is False, the text is not checked if it contains an URL
    If names_check is False, the text is not checked if it contains a tool name
    If character_check is False, the text is not checked if it contains unwanted characters '''

    name = "No name provided" if name is None else name

    # List of every errors in a description
    error = []

    # Corrected description if it misses a dot and/or a capitalized initial
    report = 0

    # If the condition is set to True in the main function, it checks that condition in the description,
    # adding the error report (if exists) to a list and outputting a corrected description
    if dots_caps:
        if dot_checker(text):
            error.append(dot_checker(text))
            report = fixer(text)

    if last_space_check:
        if last_space_checker(text):
            error.append(last_space_checker(text))

    if space_check:
        if space_checker(text):
            error.append(space_checker(text))

    if length_check:
        if length_checker(text):
            error.append(length_checker(text))

    if url_check:
        if url_checker(text):
            error.append(url_checker(text))

    if names_check:
        if name == "No name provided":
            print "Error: no names provided. Names cannot be checked"
        elif names_checker(text, name):
            error.append(names_checker(text, name))

    if character_check:
        if character_checker(text):
            error += character_checker(text)


    return name, error, report


with open("/home/juanma/Downloads/curation.tsv", "rb") as tsvin:
    with open("/home/juanma/Downloads/mergetest.tsv", "wb") as tsvout:
        tsvin = csv.reader(tsvin, delimiter="\t")
        tsvout = csv.writer(tsvout, delimiter="\t")

        # Iteration over all the tools in the input tsv
        for row in tsvin:
            tool = row[0]
            description = row[1]

            # Applying the checker function to every tool
            tsvout.writerow(checker(name = tool, text = description))