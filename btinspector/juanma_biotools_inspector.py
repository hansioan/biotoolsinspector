import csv

def dot_checker(text):
    ''' This function checks if the text ends with a dot '''
    if text[-1] != ".":
        return "Error: the description does not end with a dot"

def capitalize_checker(text):
    ''' This function checks if the initial letter of the text is capitalized '''
    if text[0].islower():
        return "Error: the description initial letter is not capitalized"


def dot_fixer(text):
    ''' This function returns a description with an ending dot if it does not have one '''
    if text[-1] != ".":
        return [text + "."]

def capitalize_fixer(text):
    ''' This function returns an initial-capitalized description if it is not '''
    if text[0].islower():
        return text[0].capitalize() + text[1:]

def dot_capitalized_fixer(text):
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
                    tsvout.writerow(dot_capitalized_fixer(description))

                # If the description does not have an ending dot
                elif dot_checker(description):
                    tsvout.writerow(dot_fixer(description))

                # If the description is not initial-capitalized
                elif capitalize_checker(description):
                    tsvout.writerow(capitalize_checker(description))

                # For everything else, mastercard
                else:
                    pass

biotools_inspector(input_tsv = "/home/juanma/Downloads/curation.tsv")