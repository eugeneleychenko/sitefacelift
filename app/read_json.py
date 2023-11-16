import json

with open('/Users/eugeneleychenko/Downloads/sfl/sitefacelift/src/data.json') as json_file:
    data = json.load(json_file)
    structured_data = {key: value for key, value in data.items()}
    print(structured_data)


