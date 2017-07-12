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
    escape_regex = re.compile("\\bold")
    unknown_symbol_regex = re.compile("|�")
    bullet_point_regex = re.compile("•")
    error_list = []
    if new_line_regex.search(text):
        error_list.append("Error: the text contains new lines")
    if carriage_return_regex.search(text):
        error_list.append("Error: the text contains carriage returns")
    if tab_regex.search(text):
        error_list.append("Error: the text contains tabs")
    if escape_regex.search(text):
        error_list.append("Error: the text contains escape characters")
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

    if character_check is False, it is not checked if the text contain unwanted characters

    if create_dataframe is False, the output is a dictionary, not a dataframe'''

    name = "No name provided" if name is None else name
    error = []
    if length_check:
        error.append(length_checker(text))
    if url_check:
        error.append(url_checker(text))
    if names_check:
        if name == "No name provided":
            print "Error: no name provided. Name can't be checked"
        else:
            error.append(names_checker(text, name))
    if character_check:
        error += character_checker(text)
    error_dict = {name: error}
    return error_dict


def data_iterator(texts, names=None, url_checking=True, names_checking=True,
            length_checking=True, character_checking=True, to_file=True):
    '''a function for iteration over the data frame and
    applying checker function

    if url_checking is False, it is not checked if URL is included in the text

    if names_checking is False, it is not checked if tool name is included in the text

    if length_checking is False, it is not checked if the length of text is more than
    10 characters and less than 500

    if character_checking is False, it is not checked if the text contain unwanted characters

    if to_file is False, the output is not written to the file and just returned as a list of tuples'''
    error_list = []
    # checking if the names are given to the function
    if names is not None:
        # checking if the length of text list and name list is the same
        # if not, an error is raised
        if len(texts)==len(names):
            # iterating over the text list and applying checker function
            for i in range(len(texts)):
                checker_dict = checker(texts[i], names[i], url_check=url_checking,
                              names_check=names_checking, length_check=length_checking,
                              character_check=character_checking)
                # adding the checker function results from the dictionary to the list
                error_list += checker_dict.items()
            # creating a dataframe from a full list of checker function results from all the items
            error_df = pd.DataFrame(error_list, columns=["Name", "Error"])
            # if to_file is True, results are written to the file
            if to_file:
                error_df.to_csv("Errors.csv")
            # othewise, results are returned as a list of tuples with
            # the tool name and errors which occurred
            else:
                return error_df
        else:
            raise Exception("The length of two lists is different")
    # if names are not provided
    else:
        # iterating over the text list and applying checker function
        for i in range(len(texts)):
            checker_dict = checker(texts[i], url_check=url_checking,
                          names_check=names_checking, length_check=length_checking,
                          character_check=character_checking)
            # adding the checker function results from the dictionary to the list
            error_list += checker_dict.items()
        # creating a dataframe from a full list of checker function results from all the items
        error_df = pd.DataFrame(error_list, columns=["Name", "Error"])
        # if to_file is True, results are written to the file
        if to_file:
            error_df.to_csv("Errors_no_names.csv")
        # othewise, results are returned as a list of tuples with the errors which occurred
        else:
            return error_df

data_iterator(descriptions, tool_names)
# print checker(descriptions[1778], tool_names[1778])
# data_iterator(descriptions)

