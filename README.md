# nfthash

This console script takes the CSV you provide it and generates a CHIP-0007 compatible json, calculates the sha256 of the json file and append it to each line in the csv.

## How to

Clone this repo:
```
git clone https://github.com/Pythonian/nfthash.git
```

Change into the cloned directory
```
cd nfthash
```

Copy your CSV file into the directory.

Open the `converter.py` file in your favorite text editor.

Go to line 3 and enter the path to your csv file for the **CSV_FILE**

Open your terminal and run the command:
```
python converter.py
```

A new CSV file **filename.output.csv** will be generated and a json file for each nft will also be created.
