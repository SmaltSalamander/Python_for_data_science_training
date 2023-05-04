import sys


def main():
    try:
        arglist = sys.argv
        if len(arglist) == 1:
            return
        if len(arglist) > 2:
                raise AssertionError("more than one argument is provided")
        try:
            number = int(arglist[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
        if str(number) != arglist[1]:
            raise AssertionError("argument is not an integer")
        if number % 2 == 0:
            print("I'm Even")
        else:
            print("I'm Odd")
    except AssertionError as e:
        print(f"{e.__class__.__name__}: {e}")
        return



if __name__ == "__main__":
    main()
