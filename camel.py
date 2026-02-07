def camelcase(sentence):
    """convert sentence to camelcase, for example, "display all boos" to "DisplayAllBooks"
    """
    title_case = sentence.title() # upper case first letter of each words
    upper_camel_cased = title_case.replace(' ', '') #remoe spaces
    #lower case first letter, join with the rest of the string
    #slices don't produce index out of boundary error
    # so this still works on empty strings, strings of length
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def main():
    sentence = input('Enter your sentence:')
    output = camelcase(sentence)
    print(output)

if __name__ == '__main__':
    main()


