#!/usr/bin/env python3
# coding=utf-8

from db import db
from report import report


def main():
    db.init_db()
    db.test()

    print('\n ------------------ Reports: ------------------\n')

    report_1 = report.get_total_reservations(date_from="2020-01-01",
                                             date_to="2020-01-31")
    print('Report 1: Total confirmed and pending reservations, total rents and average time per rent (in secs).')
    print(report_1, '\n')


    report_2 = report.get_vehicle_current_location()
    print('Report 2: Vehicle current location.')
    print(report_2, '\n')


if __name__ == '__main__':
    main()
