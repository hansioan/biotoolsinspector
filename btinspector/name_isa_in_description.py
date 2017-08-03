import sys

if len(sys.argv) != 2:
    print ("Argument error: the programm accepts only one argument.")
    print ("Usage: python name_fixer.py <filename>")
    exit()


def description_with_name_is_a(description, name):
    # Check if name at the beginning of description and if
    # description looks like: <toolname> is a / is an bla
    # and removes the tool name and is a / is an part
    # and capitalizes the first character in
    # the description.

    # Returns corrected description if it contains is a
    # and the name at the beginning.

    # Returns corrected description if it contains the
    # name at the beginning, but not is a.

    is_a  = "is a "
    is_an = "is an "
    which = None

    i_name = description.lower().find(name.lower())

    i_is = description.lower().find(is_a)
    if i_is >= 0:
        which = is_a
    else:
        i_is = description.lower().find(is_an)
        if i_is >= 0:
            which = is_an

    if i_is == -1 and i_name == -1:
        return description

    if i_is >= 0 and i_name == 0 and i_is > i_name:
        index = (description.lower().find(which) + len(which))
        description = description[index:]

        #capitalize first letter only and leave the rest unchanged
        return description[0].upper() + description[1:]

    if i_is == -1 and i_name == 0:
        # add a plus one because of the extra whitespace after the name
        # which also needs to be removed
        index = len(name) + 1
        description = description[index:]

        #capitalize first letter only and leave the rest unchanged
        return description[0].upper() + description[1:]

    # If none of the conditions above apply,
    # just return the non-modified description
    return description

# bullshit commands to get python2 to work with Unicode characters
# which can be found in descriptions.
reload(sys)
sys.setdefaultencoding('utf8')

with open(sys.argv[1]) as f:
    for line in f:
        line = line.lstrip()
        e_array = line.split("\t")
        name = e_array[0]
        #.decode('UTF-8') needed to deal with the weird Unicode characters
        description = e_array[1].decode('UTF-8')
        sys.stdout.write(description_with_name_is_a(description, name))
