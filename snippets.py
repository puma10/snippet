import sys
import argparse
import logging
import csv

# Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)

def put(name, snippet, filename):
    #Store a snippet with an associated name in the CSV file
    logging.info("Writing {}:{} to {}".format(name, snippet, filename))
    logging.debug("Opening file")
    #added "U" for universal to make interacting with spreadsheet less brittle
    with open(filename, "a") as f:
        writer = csv.writer(f)
        logging.debug("Writing snippet to file".format(name, snippet))
        writer.writerow([name, snippet])
    logging.debug("Write sucessful")
    return name, snippet

def get(name):
    #Retrieve a snippet with an associated name

    logging.info("Searching for {}".format(name))
    logging.debug("Opening file")
    #added "U" for universal to make interacting with spreadsheet less brittle
    with open("snippets.csv", "rU") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == name:
                snippet = row[1]

    return snippet


#add parsing arguments
def make_parser():
    """ Construct the command line parser """
    logging.info("Constructing parser")
    description = "Store and retrieve snippets of text"
    parser = argparse.ArgumentParser(description=description)

    #will need to walk through this to full understand how this all
    #command = arguments.pop("command")
    #what does "dest" argument do ?
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")
    put_parser.add_argument("filename", default="snippets.csv", nargs="?",
                            help="The snippet filename")


    # Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="retrieve a snippet")
    get_parser.add_argument("name", help="The name of the snippet")

    #what is contained in this parser object that is being returned?
    #how can we access variables? parser.argurment?
    return parser

def main():
    """ Main function """
    logging.info("Starting snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(**arguments)
        print "Stored '{}' as '{}'".format(snippet, name)

    if command == "get":
        snippet = get(**arguments)
        print "Retrieved '{}' ".format(snippet)

if __name__ == "__main__":
    main()
