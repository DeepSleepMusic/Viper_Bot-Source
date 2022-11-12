def log_error(__error__: any):
    try:
        if __error__ is None:
            try:
                with open("Log.txt", "w") as __fileEmpty__:
                    __fileEmpty__.write(
                        str(
                            "No Error To Write."
                        )
                    )
            except Exception as en:
                print(
                    str(
                        en
                    )
                )
        else:
            pass
        with open("Log.txt", 'w') as __newFile__:
            __newFile__.write(
                f"{__error__}"
            )
            __newFile__.close()
        print(
            str(
                f"{__error__}"
            )
        )
    except Exception as en:
        print(
            str(
                en
            )
        )