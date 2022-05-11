from enum import Enum


class tokenTypes(Enum):
    URL = 1
    QR_CODE = 2
    WORD = 3
    EXCEL = 4
    ODT = 5
    BAT = 6
    SH = 7
    ODS = 8


if __name__ == "__main__":
    print(tokenTypes.URL.name)