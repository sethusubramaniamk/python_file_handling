This script is to extract the value of a key from a list of JSON files and store them in a CSV file

**Example Format:**

  _sudo python3 json_to_csv.py -d ./directory -k keyname -s output.csv_

Note:
 
1. For more information, type in the following command,

  _sudo python3 json_to_csv.py --help_

2. If the CSV output filename is not specified, the values of the respective JSOn key only will be printed and not stored in a file.

3. If the target directory is not specified, the current working directory will be taken as default.
