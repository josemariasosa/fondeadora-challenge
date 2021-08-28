#!/usr/bin/env python3
# coding=utf-8

from db import db
from op import op


def main():
    # db.init_db()
    # db.test()

    op.run_operations()


if __name__ == '__main__':
    main()
