import time
import datetime


def main():
    time_float = "{0:,.4f}".format(time.time())
    time_scientific = '{:.2e}'.format(time.time())
    print(f"Seconds since January 1, 1970: {time_float} or {time_scientific} in scientific notation")
    today = datetime.datetime.now()
    print(today.date().strftime("%b %d %Y"))


if __name__ == "__main__":
    main()
