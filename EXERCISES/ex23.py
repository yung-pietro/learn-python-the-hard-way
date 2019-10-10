import sys
script, input_encoding, error = sys.argv
#the argv's that the script requires


def main(language_file, encoding, errors):
    #creates function, main, with three inputs, language_file, encoding, and errors.  But where do these come from?
    line = language_file.readline()
#not sure
    if line:
        #if statement related to the line variable above. In this case, we are checking the first line to see if it contains anything.
        #? How is he testing that this line has something in it?
        print_line(line, encoding, errors)
        #print_line appears to be a native function.  Indeed it is.
        return main(language_file, encoding, errors)
        # This is calling main, which jumps to the top, creating a loop.  The if line statement breaks the loop, when it reaches a blank line.



def print_line(line, encoding, errors):
    next_lang = line.strip()
    #strip() removes the leading and trailing blank space from the line, assigning it to next_lang.  In this case removes the \n
    raw_bytes = next_lang.encode(encoding, errors=errors)
    #I pass to encode() the encoding I want and how to handle errors.
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    # This line decodes the raw bytes, passing to decode the encoding I want and how to handle errors.  This just basically
    # re-assembles (decodes) the raw bytes back into a string
    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
