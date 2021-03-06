#!/usr/local/bin/python3

from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import sys

# TODO: undoing a creation


def seperate_pdf(file):
    print("Seperating pdf command triggered")

    print("Initializing new directory...")
    parent = os.getcwd()
    directory = "pdf-output"
    path = os.path.join(parent, directory)
    os.mkdir(path)
    print("Directory '{}' created".format(path))

    filename = file[:-4]

    print("Seperating {}...".format(file))
    input = PdfFileReader(open(file, "rb"))

    for i in range(input.numPages):
        output = PdfFileWriter()
        output.addPage(input.getPage(i))
        with open("{}/{}-p{}.pdf".format(path, filename, i), "wb") as outputStream:
            output.write(outputStream)
    print("Done.")


def pdf(arguments):
    action = arguments[0]

    if action == "split":
        if len(arguments) != 2:
            raise Exception(
                "Invalid arguments. Usage: jarvis pdf split [filename.pdf]")

        seperate_pdf(arguments[1])
    else:
        raise Exception("Invalid command. Possible commands: jarvis pdf split")


if __name__ == "__main__":
    num_args = len(sys.argv)

    # Get command
    command = sys.argv[1]

    if command == "pdf":
        pdf(sys.argv[2:])
    else:
        print("Invalid command. Please try again")
