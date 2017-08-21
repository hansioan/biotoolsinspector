# biotoolsinspector

### Miscellaneous utilities for bio.tools

##### Command line tool for checking tool descriptions

```text
usage: Provisional_detector_corrector.py [-h] [-m MODE] [-one-file]
                                         [-d DESCRIPTIONS] [-n NAMES]
                                         [-sentence SENTENCE_CHECKER]
                                         [-url URL_CHECKER] [-name NAME_CHECK]
                                         [-length LENGTH_CHECK]
                                         [-character CHARACTER_CHECK]
                                         [-char-fix CHARACTER_FIX]
                                         [-to-file FILE] [-filename FILE_NAME]


optional arguments:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  Mode of the checker: "full" - checks descriptions with
                        their names;"parial" - checks only the descriptions.
  -one-file, --one      Input descriptions and names from one file. Usable
                        only with mode "full".
  -d DESCRIPTIONS, --descriptions DESCRIPTIONS
                        File with descriptions.
  -n NAMES, --names NAMES
                        File with description names.
  -sentence SENTENCE_CHECKER, --sentence_checker SENTENCE_CHECKER
                        Check if descriptions start with a capital letter and
                        end with a dot. Options: "1" to use the argument, "0"
                        for skipping the argument. Default is 1.
  -url URL_CHECKER, --url_checker URL_CHECKER
                        Check if descriptions contain URLs. Options: "1" to
                        use the argument, "0" for skipping the argument.
                        Default is 1.
  -name NAME_CHECK, --name_check NAME_CHECK
                        Check if the description contains names. Options: "1"
                        to use the argument, "0" for skipping the argument.
                        Default is 1.
  -length LENGTH_CHECK, --length_check LENGTH_CHECK
                        Check if the description length is within the limits
                        and the descriptions is made of more than one word.
                        Options: "1" to use the argument, "0" for skipping the
                        argument. Default is 1.
  -character CHARACTER_CHECK, --character_check CHARACTER_CHECK
                        Check if the description contains unwanted characters
                        Options: "1" to use the argument, "0" for skipping the
                        argument. Default is 1.
  -char-fix CHARACTER_FIX, --character_fix CHARACTER_FIX
                        Check if the description contains unwanted characters
                        and remove them. Options: "1" to use the argument, "0"
                        for skipping the argument. Default is 1.
  -to-file FILE, --file FILE
                        Write all the output to a .csv file. Options: "1" to
                        use the argument, "0" for skipping the argument.
                        Default is 1.
  -filename FILE_NAME, --file_name FILE_NAME
                        Choose the output file name if the argument -to-file
                        is True. Default is "Warnings".



