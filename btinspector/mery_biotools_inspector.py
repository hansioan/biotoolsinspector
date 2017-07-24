import json

def filter_jsonobj(json_file):
    """This function takes a single JSON object and returns a tuple
    of the name and description of the tool"""

    file = open(json_file, "r")
    string = file.read()
    parsed_json = json.loads(string)
    file.close()

    name = parsed_json["name"]
    description = parsed_json["description"]

    return([name,description])

#print(filter_jsonobj("json_test.json"))

