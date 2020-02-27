import csv
from flower_generator import create_file


def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file
  create_file(filename)

  # Open the file
  with open(filename) as f:
    # Read the rows of the file into a dictionary
    flowers = csv.DictReader(f)
    print(flowers)
    # Process each item of the dictionary
    for row in flowers:
      print(row)
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string


print(contents_of_file('flowers.csv'))
