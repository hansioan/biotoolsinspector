import csv

# This script reads the original problem file as a .tsv ("curation.tsv") and writes a new .csv file ("corrections.csv")
# with a column of descriptions, capitalizing the initial letters of those which are not originally capitalized and
# adding an ending dot to those descriptions which do not have one. This column will be manually pasted to the
# original .tsv file in the "fixed_tool" description column

with open("/home/juanma/Downloads/curation.tsv", "rb") as tsvin:
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

