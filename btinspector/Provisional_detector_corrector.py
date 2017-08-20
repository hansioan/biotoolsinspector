# coding: utf-8
import re
import pandas as pd


def dot_checker(text):
    ''' This function checks if the text ends with a dot '''
    if not text.endswith("."):
        return "Warning: the description does not end with a dot"
    elif text.endswith(" .") or text.endswith("..") or text.endswith(". "):
        return "Warning: the description does not end properly"

def capitalize_checker(text):
    ''' This function checks if the initial letter of the text is capitalized '''
    if text[0].islower():
        return "Warning: the description initial letter is not capitalized"

def length_checker(text):
    ''' This function checks if the length of the text is less than 10 or more than 500 characters '''
    if len(text) < 10:
        return "Warning: the length of description is shorter than 10 characters"
    if len(text) > 500:
        return "Warning: the length of description is longer than 500 characters"
    if len(text) >= 10 and len(text) <= 500 and " " not in text:
        return "Warning: the description contains only one word"

def url_checker(text):
    ''' This function checks if the text contains an URL '''
    url_regex = re.compile("http|www.")
    if url_regex.search(text):
        return "Warning: the description contains an URL"

def names_checker(text, name):
    ''' This function checks if the text contains the tool name '''
    if "+" in name:
        name = name.replace("+", "\+")
    if "*" in name:
        name = name.replace("*", "\*")
    if "(" in name:
        name = name.replace("(", "\(")
    if ")" in name:
        name = name.replace(")", "\)")
    if "[" in name:
        name = name.replace("[", "\[")
    if "]" in name:
        name = name.replace("]", "\]")
    name_regex = re.compile(name, re.IGNORECASE)
    if name_regex.search(text):
        return "Warning: the description may contain the tool name"

def character_checker(text):
    ''' This function checks if the text contains some unwanted characters '''
    new_line_regex = re.compile("\n")
    carriage_return_regex = re.compile("↵")
    tab_regex = re.compile("\t")
    bullet_point_regex = re.compile("•")
    unknown_symbol_regex = re.compile("|�")

    error_list = []

    if new_line_regex.search(text):
        error_list.append("Warning: the description contains new lines")
    if carriage_return_regex.search(text):
        error_list.append("Warning: the description contains carriage returns")
    if tab_regex.search(text):
        error_list.append("Warning: the description contains tabs")
    if bullet_point_regex.search(text):
        error_list.append("Warning: the description contains bullet points")
    if unknown_symbol_regex.search(text):
        error_list.append("Warning: the description contains unknown symbols")

    return error_list

def dot_fixer(text):
    ''' This function calls dot_checker and returns a description with an ending dot if condition is TRUE '''
    if dot_checker(text):
        if text.endswith(" .") or text.endswith("..") or text.endswith(". "):
            return text.replace("..", ".").replace(" .", ".").replace(". ", ".")
        else:
            return text + "."

def capitalize_fixer(text):
    ''' This function calls capitalize_checker and returns an initial-capitalized description if condition is TRUE '''
    if capitalize_checker(text):
        return text[0].upper() + text[1:]

def character_fixer(text):
    ''' This function checks if the text contains some unwanted characters and removes them if needed'''
    new_line_regex = re.compile("\n")
    carriage_return_regex = re.compile("↵")
    tab_regex = re.compile("\t")
    bullet_point_regex = re.compile("•")
    unknown_symbol_regex = re.compile("|�")

    error_list = []

    if new_line_regex.search(text):
        text = text.replace("\n", " ")
    if carriage_return_regex.search(text):
        text = text.replace("↵", " ").replace("  ", " ")
    if tab_regex.search(text):
        text = text.replace("\t", " ").replace("  "," ")
    if bullet_point_regex.search(text):
        text = text.replace("•", ", ").replace("  "," ")
    if unknown_symbol_regex.search(text):
        text = text.replace("", "").replace("�", "")

    return text


def checker(text, name = None, dots_caps = True, length_check = True, url_check = True,
            names_check = True, character_check = True, character_fix=True):
    ''' This function checks if the given text (tool description and tool name) is written according the requirements:

    If dots_caps is False, the text is not checked /nor fixed if it has an ending dot and/or a capitalized initial
    If length_check is False, the text is not checked if its length is out of limits and the descriptions
    is made of more than one word
    If url_check is False, the text is not checked if it contains an URL
    If names_check is False, the text is not checked if it contains a tool name
    If character_check is False, the text is not checked if it contains unwanted characters '''

    name = "No name provided" if name is None else name
    # List of every errors in a description
    error = []
    if dots_caps:
        if dot_checker(text):
            error.append(dot_checker(text))
            text = dot_fixer(text)
        if capitalize_checker(text):
            error.append(capitalize_checker(text))
            text = capitalize_fixer(text)
    if length_check:
        if length_checker(text):
            error.append(length_checker(text))
    if url_check:
        if url_checker(text):
            error.append(url_checker(text))
    if names_check:
        if name == "No name provided":
            print "Warning: no names provided. Names cannot be checked"
        else:
            error.append(names_checker(text, name))
    if character_check:
        error += character_checker(text)
    if character_fix:
        text = character_fixer(text)
    # If no errors are reported, the empty list is returned
    if None in error:
        error.remove(None)
    return name, error, text


def data_iterator(texts, names=None, dot_caps_checking=True, url_checking=True, names_checking=True,
            length_checking=True, character_checking=True, character_fixing=True, to_file=True, file_name="Warnings"):
    '''This function iterates over the data frame/list/etc. and
    applies the checker function

    If dots_caps_cheking is False, the text is not checked /nor fixed if it has an ending dot and/or a capitalized initial
    If length_checking is False, the text is not checked if its length is out of limits and the descriptions
    is made of more than one word
    If url_checkomg is False, the text is not checked if it contains an URL
    If names_checking is False, the text is not checked if it contains a tool name
    If character_checking is False, the text is not checked if it contains unwanted characters
    If character_fixing is False, unwanted characters are not removed from the text
    If to_file is False, the output is not written to the file and just returned as a list of tuples'''
    error_list = []
    # checking if the names are given to the function
    if names is not None:
        # checking if the length of text list and name list is the same
        # if not, an error is raised
        if len(texts)==len(names):
            # iterating over the text list and applying checker function
            for i in range(len(texts)):
                checker_results = checker(texts[i], names[i], dots_caps=dot_caps_checking, url_check=url_checking,
                              names_check=names_checking, length_check=length_checking,
                              character_check=character_checking, character_fix=character_fixing)
                # adding the checker function results from the dictionary to the list
                error_list += [checker_results]
            # creating a dataframe from a full list of checker function results from all the items
            error_df = pd.DataFrame(error_list, columns=["Name", "Warning", "Fixed capitalized/dotted description"])
            # if to_file is True, results are written to the file
            if to_file:
                error_df.to_csv(file_name+".csv")
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
            checker_results = checker(texts[i], dots_caps=dot_caps_checking, url_check=url_checking,
                          names_check=names_checking, length_check=length_checking,
                          character_check=character_checking, character_fix=character_fixing)
            # adding the checker function results from the dictionary to the list
            error_list += [checker_results]
        # creating a dataframe from a full list of checker function results from all the items
        error_df = pd.DataFrame(error_list, columns=["Name", "Warning", "Fixed capitalized/dotted description"])
        # if to_file is True, results are written to the file
        if to_file:
            error_df.to_csv(file_name+"_no_name.csv")
        # othewise, results are returned as a list of tuples with the errors which occurred
        else:
            return error_df


def __number2bool(number):
    if number==1:
        return True
    else:
        return False

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description = "Command line tool for checking tool descriptions")
    parser.add_argument("-m", "--mode", help="Mode of the checker: \"full\" - checks descriptions with their names;" \
                                            "\"parial\" - checks only the descriptions.")
    parser.add_argument("-one-file", "--one", help="Input descriptions and names from one file. "
                                                   "Usable only with mode \"full\".",
                        required=False, action = 'store_true')
    parser.add_argument("-d", "--descriptions", help="File with descriptions.")
    parser.add_argument("-n", "--names", help="File with description names.")
    parser.add_argument("-sentence", "--sentence_checker", help="Check if descriptions start with a capital letter and end"
                                                                " with a dot. Options: \"1\" to use the argument,"
                                                                " \"0\" for skipping the argument. Default is 1.",
                        type=int, required=False, default=True)
    parser.add_argument("-url", "--url_checker", help="Check if descriptions contain URLs. Options: \"1\" to use the argument, "
                                                      "\"0\" for skipping the argument. Default is 1.",
                        type=int, required=False, default=True)
    parser.add_argument("-name", "--name_check", help="Check if the description contains names. Options: \"1\" to use the argument, "
                                                      "\"0\" for skipping the argument. Default is 1.",
                        type=int, required=False, default=True)
    parser.add_argument("-length", "--length_check", help="Check if the description length is within the limits and "
                                                          "the descriptions is made of more than one word. "
                                                          "Options: \"1\" to use the argument, \"0\" for skipping the argument. "
                                                          "Default is 1.",
                        type=int, required=False, default=True)
    parser.add_argument("-character", "--character_check", help="Check if the description contains unwanted characters "
                                                                "Options: \"1\" to use the argument, \"0\" for skipping "
                                                                "the argument. Default is 1.",
                        type=int, required=False, default=True)
    parser.add_argument("-char-fix", "--character_fix", help="Check if the description contains unwanted characters and "
                                                             "remove them. Options: \"1\" to use the argument, \"0\" for "
                                                             "skipping the argument. Default is 1.",
                        type=int, required=False, default=True)
    parser.add_argument("-to-file", "--file", help="Write all the output to a .csv file. Options: \"1\" to use the argument, "
                                                   "\"0\" for skipping the argument. Default is 1.",
                        type=int, required=False, default=True)
    parser.add_argument("-filename", "--file_name", help="Choose the output file name if the argument -to-file is True. "
                                                         "Default is \"Warnings\".",
                        type=str, required=False, default="Warnings")

    args = vars(parser.parse_args())

    if args["mode"] == "full":
        if args["one"]:
            descriptions_names = pd.read_table(args["descriptions"], header=None, index_col=None)
            names = descriptions_names[0]
            descriptions = descriptions_names[1]

            print data_iterator(descriptions, names,
                                dot_caps_checking=__number2bool(args["sentence_checker"]),
                                url_checking=__number2bool(args["url_checker"]),
                                names_checking=__number2bool(args["name_check"]),
                                length_checking=__number2bool(args["length_check"]),
                                character_checking=__number2bool(args["character_check"]),
                                character_fixing=__number2bool(args["character_fix"]),
                                to_file=__number2bool(args["file"]),
                                file_name=args["file_name"])
        else:
            descriptions = pd.read_table(args["descriptions"], header=None, index_col=None)
            names = pd.read_table(args["names"], header=None, index_col=None)
            names = names[0]
            descriptions = descriptions[0]
            print data_iterator(descriptions, names,
                          dot_caps_checking=__number2bool(args["sentence_checker"]),
                          url_checking=__number2bool(args["url_checker"]),
                          names_checking=__number2bool(args["name_check"]),
                          length_checking=__number2bool(args["length_check"]),
                          character_checking=__number2bool(args["character_check"]),
                          character_fixing=__number2bool(args["character_fix"]),
                          to_file=__number2bool(args["file"]),
                          file_name=args["file_name"])
    elif args["mode"] == "partial":
        descriptions = pd.read_table(args["descriptions"], header=None, index_col=None)
        descriptions = descriptions[0]
        print data_iterator(descriptions,
                      dot_caps_checking=__number2bool(args["sentence_checker"]),
                      url_checking=__number2bool(args["url_checker"]),
                      names_checking=__number2bool(args["name_check"]),
                      length_checking=__number2bool(args["length_check"]),
                      character_checking=__number2bool(args["character_check"]),
                      character_fixing=__number2bool(args["character_fix"]),
                      to_file=__number2bool(args["file"]),
                      file_name=args["file_name"])
    else:
        print "Mode Error: The mode is wrong." \
              "\nUsage: python btcorrector.py <mode> <description file> <name file>" \
              "\n<mode>: \"full\" or \"partial\""

