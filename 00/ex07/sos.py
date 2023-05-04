import sys


def main():
    """Converts passed string to morse code then prints it

    Raises:
        AssertionError: in case of providing wrong arguments
    """
    NESTED_MORSE = {
		" ": "/ ",
		"A": ".- ",
		"B": "-... ",
		"C": "-.-. ",
		"D": "-.. ",
		"E": ". ",
		"F": "..-. ",
		"G": "--. ",
		"H": ".... ",
		"I": ".. ",
		"J": ".--- ",
		"K": "-.- ",
		"L": ".-.. ",
		"M": "-- ",
		"N": "-. ",
		"O": "--- ",
		"U": "..- ",
		"P": ".--. ",
		"R": ".-. ",
		"S": "... ",
		"T": "- ",
		"W": ".-- ",
		"Y": "-.-- ",
		"Z": "--.. ",
		"X": "-..- ",
		"Q": "--.- ",
		"V": "...- ",
	}
    try:
        arglist = sys.argv
        if len(arglist) != 2:
            raise AssertionError("the arguments are bad")
        string = str(arglist[1])
        result = ""
        for chara in string:
            try:
                result += NESTED_MORSE[chara.upper()]
            except KeyError:
                raise AssertionError("the arguments are bad")
        result.strip()
        print(result)
    except AssertionError as e:
        print(f"{e.__class__.__name__}: {e}")


if __name__ == "__main__":
    main()
