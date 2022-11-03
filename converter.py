import csv, hashlib, json

CSV_FILE = 'data.csv'

new_csv_file = 'filename.output.csv'

f = open(new_csv_file, 'w')

writer = csv.writer(f)

writer.writerow(
    ['SerialNumber', 'Filename', 'Name', 'Description', 'Gender', 'Attributes', 'UUID', 'SHA256']
)

with open(CSV_FILE, 'r') as csv_file:
    read_csv = csv.reader(csv_file, delimiter=',')
    next(read_csv)
    
    data = []
    for a in read_csv:
        data.append(a)

    for item in data:
        series_number = item[0]
        filename = item[1]
        name= item[2]
        description= item[3]
        gender = item[4]
        attributes = item[5]
        uuid = item[6]

        chip007_format = {
            "format": "CHIP-0007",
            "name": name,
            "description": description,
            "minting_tool": "Team x",
            "sensitive_content": False,
            "series_number": series_number,
            "series_total": 420,
            "attributes": [
                {
                    "trait_type": "gender",
                    "value": gender
                }
            ],
            "collection": {
                "name": "Zuri NFT tickets for free lunch",
                "id": uuid,
                "attributes": [
                    {
                        "type": "description",
                        "value": "Rewards for accomplishments during HNGi9"
                    }
                ]
            },
        }

        # Creating a json file for each row in the csv file.
        json_item = json.dumps(chip007_format, indent=4) # Converting the json file to a string.
        with open(f'{filename}.json', 'w') as outfile:
            outfile.write(json_item)
        outfile.close()

        # Creating a hash of the json file and appending it to the csv file.
        hash_256 = hashlib.sha256(json_item.encode()).hexdigest()
        item.append(hash_256)
        writer.writerow(item)

# close the file
f.close()
