# coding: utf-8

import csv
import re

# Compilation of reporter functions

def dot_checker(text):
    ''' This function checks if the text ends with a dot '''
    if text[-1] != ".":
        return "Error: the description does not end with a dot"

def capitalize_checker(text):
    ''' This function checks if the initial letter of the text is capitalized '''
    if text[0].islower():
        return "Error: the description initial letter is not capitalized"

def last_space_checker(text):
    ''' This function checks if the second last character of the text is a space '''
    if text[-2] == (" "):
        return "Error: the description previous last character is a space"

def beyond_dot_checker(text):
    ''' This function checks if the text has any text after the ending dot '''
    ending_regex = re.compile("\..+")
    if ending_regex.search(text):
        return "Error: the description has characters after the ending dot"

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
    '''This function checks if the text contains some unwanted characters'''
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


# Compilation of corrector functions

def dot_fixer(text):
    ''' This function returns a description with an ending dot if it does not have one '''
    if text[-1] != ".":
        return [text + "."]

def capitalize_fixer(text):
    ''' This function returns an initial-capitalized description if it is not '''
    if text[0].islower():
        return text[0].capitalize() + text[1:]

def dot_capitalize_fixer(text):
    ''' This function returns an initial-capitalized and ending dot description if it is not '''
    if text[0].islower() and text[-1] != ".":
        return [text[0].capitalize() + text[1:] + "."]



def biotools_inspector(input_tsv):
    ''' This function takes a .tsv file and writes it as a .tsv output file, correcting the second column (descriptions)
       by capitalizing the initial letter of the descriptions and adding an ending dot if they do not have one '''

    with open(input_tsv, "rb") as tsvin:
        with open("/home/juanma/Downloads/corrections.tsv", "wb") as tsvout:
            tsvin = csv.reader(tsvin, delimiter="\t")
            tsvout = csv.writer(tsvout, delimiter="\t")

            # Iteration over every row in the csv, defining the problematic description in the second column
            for tool in tsvin:
                description = tool[1]

                # If the description is not initial-capitalized and it does not have an ending dot
                if dot_checker(description) and capitalize_checker(description):
                    tsvout.writerow(dot_capitalize_fixer(description))

                # If the description does not have an ending dot
                elif dot_checker(description):
                    tsvout.writerow(dot_fixer(description))

                # If the description is not initial-capitalized
                elif capitalize_checker(description):
                    tsvout.writerow(capitalize_fixer(description))

                else:
                    pass

biotools_inspector(input_tsv = "/home/juanma/Downloads/curation.tsv")