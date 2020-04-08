formats = {
    "ymd": "{d.year}-{d.month}-{d.day}",
    "mdy": "{d.month}/{d.day}/{d.year}",
    "dmy": "{d.day}/{d.month}/{d.year}",
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        fmt = formats[code or "ymd"]
        return fmt.format(d=self)


if __name__ == "__main__":
    d = Date(2020, 4, 7)
    print(
        format(d),
        format(d, "mdy"),
        "The date is {:mdy}".format(d),
        "The date is {:dmy}".format(d),
        "The date is {:ymd}".format(d),
        sep="\n",
    )
