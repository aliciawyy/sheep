import os
import sys
import time

import requests


POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'http://flupy.org/data/flags'

DEST_DIR = os.path.expanduser('~/Downloads/flags')


def save_flag(image, filename):
    fullname = os.path.join(DEST_DIR, filename)
    with open(fullname, "wb") as f:
        f.write(image)


def get_flag(country):
    url = f"{BASE_URL}/{country}/{country}.gif"
    req = requests.get(url)
    return req.content


def show(country):
    print(country, end=" ")
    sys.stdout.flush()


def download_flag(country):
    image = get_flag(country)
    save_flag(image, f"{country}.gif")
    show(country)
    return country


def download_flags(countries):
    return len(list(map(download_flag, countries)))


def main(download_many):
    if not os.path.isdir(DEST_DIR):
        os.mkdir(DEST_DIR)
    start_time = time.time()
    count = download_many(sorted(POP20_CC))
    print(
        "\nDownloaded {} flags in {}s.".format(count, time.time() - start_time)
    )


if __name__ == "__main__":
    main(download_flags)
