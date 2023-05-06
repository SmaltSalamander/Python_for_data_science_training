import sys


def main():
    """Counts the various categories of characters in a passed string

    Raises:
        AssertionError: in case of providing more than one argument
    """
    try:
        arglist = sys.argv
        if len(arglist) > 2:
            raise AssertionError("more than one argument is provided")
        if len(arglist) == 1:
            string = input("What is the text to count?\n")
        else:
            string = arglist[1]

        upper = sum(1 for c in string if c.isupper())
        lower = sum(1 for c in string if c.islower())
        punc = sum(1 for c in string if c in ",.\"\';:{}-!()?[]")
        spaces = sum(1 for c in string if c.isspace())
        digits = sum(1 for c in string if c.isnumeric())

        print(f"The text contains {len(string)} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punc} punctuation marks")
        print(f"{spaces} spaces")
        print(f"{digits} digits")
    except AssertionError as e:
        print(f"{e.__class__.__name__}: {e}")


if __name__ == "__main__":
    main()
