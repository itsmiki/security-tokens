from enum import Enum


class tokenTypes(Enum):
    URL = 1
    QR_CODE = 2


if __name__ == "__main__":
    print(tokenTypes.URL.name)