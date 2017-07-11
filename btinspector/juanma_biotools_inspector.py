import csv

def biotools_inspector(input_tsv):
    '''This function takes a .tsv file and writes it as a .tsv output file, correcting the second column (descriptions)
       by capitalizing the initial letter of the descriptions and adding an ending dot if they do not have one'''

    with open(input_tsv, "rb") as tsvin:
        with open("/home/juanma/Downloads/corrections.tsv", "wb") as tsvout:
            tsvin = csv.reader(tsvin, delimiter = "\t")
            tsvout = csv.writer(tsvout, delimiter = "\t")

            for tool in tsvin:
                description = tool[1]
                fixed_description = tool[6]

                # Capitalization and ending dot criteria evaluation
                if description[0].isupper() and description.endswith("."):
                    fixed_description = description
                    tsvout.writerow(tool)
                elif not description.endswith("."):
                    fixed_description = description[0].capitalize() + description[1:] + "."
                    tsvout.writerow(tool)
                else:
                    fixed_description = description[0].capitalize() + description[1:] + "."
                    tsvout.writerow(tool)


biotools_inspector(input_tsv = "/home/juanma/Downloads/curation.tsv")
