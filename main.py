#!/usr/bin/env python3
# coding=utf-8

from db import db
from report import report


def main():
    # db.init_db()
    # db.test()

    report_1 = report.get_total_reservations()


if __name__ == '__main__':
    main()
