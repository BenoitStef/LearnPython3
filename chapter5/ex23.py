#-------------------------------------------------------------------------------
# Strings, Bytes & Char encodings - Learn Python 3 the hard way - page 110
# Author    : Benoit Stef
# Date      : 23.02.2019
#-------------------------------------------------------------------------------
import sys
script, inputEncoding, error = sys.argv

def main(languageFile, encoding, errors):
    line = languageFile.readline()

    if line:
        print_line(line, encoding, errors)
        return main(languageFile, encoding, errors)

def print_line(line, encoding, errors):
    nextLang = line.strip()
    rawBytes = nextLang.encode(encoding, errors=errors)
    cookedString = rawBytes.decode(encoding, errors=errors)

    print(rawBytes, "<===>", cookedString)

languages = open("languages.txt", encoding="utf-8")

main(languages, inputEncoding, error)
