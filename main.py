#!/usr/bin/env python3
# coding=utf-8

from db import db


def main():
    db.init_db()
    db.test()


if __name__ == '__main__':
    main()
