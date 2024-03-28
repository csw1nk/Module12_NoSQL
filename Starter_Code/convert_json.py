import json

input_path = 'Resources/establishments.json'
output_path = 'Resources/establishments_converted.jsonl'

# Read the original JSON file
with open(input_path, 'r') as json_file:
    data = json.load(json_file)

# Convert and save to a new .jsonl file
with open(output_path, 'w') as outfile:
    for entry in data:
        json.dump(entry, outfile)
        outfile.write('\n')