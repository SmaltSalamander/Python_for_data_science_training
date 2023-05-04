import sys
from ft_filter import ft_filter


def word_len_checker(length):
    return lambda word: len(word) > length


def main():
    """Prints a list of words longer than provided length within the string

    Raises:
        AssertionError: in case of providing wrong arguments
    """
    try:
        arglist = sys.argv
        if len(arglist) != 3:
            raise AssertionError("the arguments are bad")

        string = str(arglist[1])
        try:
            length = int(arglist[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        if str(length) != arglist[2]:
            raise AssertionError("the arguments are bad")
        if any([not str.isalnum(chara) and not
                str.isspace(chara) for chara in string]):
            raise AssertionError("the arguments are bad")
        word_filter = word_len_checker(length)
        longer_words = ft_filter(word_filter, string.split())
        print(longer_words)
    except AssertionError as e:
        print(f"{e.__class__.__name__}: {e}")


if __name__ == "__main__":
    main()
