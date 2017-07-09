# coding: utf-8

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
        return "Error: the length of description is not right"

def url_checker(text):
    '''a function for checking if the text contains URL'''
    url_regex = re.compile("http|www.")
    if url_regex.search(text):
        return "Error: the description contains URL"

def names_checker(text, name):
    '''a function for checking if the text contains the tool name'''
    name_regex = re.compile(name)
    if name_regex.search(text):
        return "Error: the description contains a tool name"

def character_checker(text):
    '''a function for checking if the text contains unwanted characters'''
    new_line_regex = re.compile("\n")
    carriage_return_regex = re.compile("↵")
    tab_regex = re.compile("\t")
    # escape_regex = re.compile("\e")
    unknown_symbol_regex = re.compile("|�")
    bullet_point_regex = re.compile("•")
    error_list = []
    if new_line_regex.search(text):
        error_list.append("Error: the text contains new lines")
    if carriage_return_regex.search(text):
        error_list.append("Error: the text contains carriage returns")
    if tab_regex.search(text):
        error_list.append("Error: the text contains tabs")
    # if escape_regex.search(text):
    #     error_list.append("Error: the text contains escape charecters")
    if bullet_point_regex.search(text):
        error_list.append("Error: the text contains bullet points")
    if unknown_symbol_regex.search(text):
        error_list.append("Error: the text contains unknown symbols")
    return error_list

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
    error = []
    if length_check:
        error.append(length_checker(text))
    if url_check:
        error.append(url_checker(text))
    if names_check:
        if name == "No name provided":
            print "Error: no names provided. Names can't be checked"
        else:
            error.append(names_checker(text, name))
    if character_check:
        error += character_checker(text)
    error_dict = {name:error}
    error_df = pd.DataFrame.from_dict(error_dict)
    error_df.to_csv("Errors.csv", mode="a")
    # return error_df



def data_iterator(texts, names=None):
    '''a function for iteration over the data frame and
    applying checker function'''
    if names is not None:
        if len(texts)==len(names):
            for i in range(len(texts)):
                checker(texts[i], names[i])
        else:
            raise Exception("The length of two lists is different")
    else:
        for i in range(len(texts)):
            checker(texts[i])


print data_iterator(descriptions, tool_names)
# print data_iterator(descriptions)

