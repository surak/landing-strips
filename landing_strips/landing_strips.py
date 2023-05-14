import stackprinter

stackprinter.set_excepthook(style="darkbg2")


def main():
    some_var = "data"
    raise ValueError("Some error message")


if __name__ == "__main__":
    main()
