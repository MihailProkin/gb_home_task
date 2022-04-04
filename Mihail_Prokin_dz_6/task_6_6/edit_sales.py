PRICE_FILE = "./bakery.csv"

if __name__ == "__main__":

    import sys

    if len(sys.argv[1:]) != 2:
        sys.exit(1)

    pos = sys.argv[1]
    new_price = sys.argv[2]

    if not (pos.isdigit() and new_price.replace(".", "").isdigit()):
        sys.exit(1)

    pos = int(pos)
    new_price = float(new_price)

    with open(PRICE_FILE, "r+", encoding="utf-8") as price_list:

        skip_chars = 0

        for (i, line) in zip_longest(range(1, pos), price_list):

            if i is None:
                break

            if line:
                skip_chars += len(line)
            else:
                print("out of index")
                sys.exit(1)

        price_list.seek(skip_chars)
        price_list.writelines(f"{new_price:100.2f}")
