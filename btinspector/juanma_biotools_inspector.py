import csv

def biotools_inspector(input_tsv):
    '''This function takes a .tsv file and writes its second column (descriptions) to a .csv output file,
             capitalizing the initial letter of the descriptions and adding an ending dot'''
    with open(input_tsv, "rb") as tsvin:
        with open("/home/juanma/Downloads/corrections.csv", "wb") as csvout:
            tsvin = csv.reader(tsvin, delimiter = "\t")
            csvout = csv.writer(csvout)

            for row in tsvin:
                description = row[1]

                # Capitalization and ending dot criteria evaluation
                if description[0].isupper() and description.endswith("."):
                    csvout.writerow([description])
                else:
                    fixed_description = description[0].capitalize() + description[1:] + "."
                    csvout.writerow([fixed_description])


biotools_inspector(input_tsv = "/home/juanma/Downloads/curation.tsv")
