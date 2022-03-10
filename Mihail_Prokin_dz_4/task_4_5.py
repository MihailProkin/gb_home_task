import sys
import task_4_3


if __name__ == "__main__":

    args = sys.argv[1:]

    for code in args:
        conv = task_4_3.currency_rates(code)
        if conv:
            cur, date = conv
            date = date.strftime("%d-%m-%Y")
            print(f"{cur}, {date}")
