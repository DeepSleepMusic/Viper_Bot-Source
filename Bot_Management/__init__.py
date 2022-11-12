def log_error(__error__: any):
    try:
        __error__ = __error__ if __error__ is not None else "No Error To Write."
        try:
            with open("Log.txt", "w") as __fileEmpty__:
                __fileEmpty__.write(f"{__error__}")
        except Exception as en:
            print(en)
    except Exception as en:
        print(en)
