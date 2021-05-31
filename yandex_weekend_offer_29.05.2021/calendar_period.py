#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import calendar
import datetime as dt


def get_end_period(period: str, start_date: dt.datetime, end_date: dt.datetime) -> dt.datetime:
    """
    :param period:  WEEK — неделя с понедельника по воскресенье.
                    MONTH — месяц.
                    QUARTER — интервалы в три месяца: январь — март, апрель — июнь, июль — сентябрь, октябрь — декабрь.
                    YEAR — год c 1 января по 31 декабря.
                    REVIEW — периоды, за которые оцениваются достижения сотрудников Яндекса.
                             Летний период длится с 1 апреля по 30 сентября, зимний — с 1 октября по 31 марта.
    :param start_date: Дата начала периода
    :param end_date: Дата окончания периода
    :return:
    """
    if period == 'WEEK':
        pass
    if period == 'MONTH':
        pass
    if period == 'QUARTER':
        pass
    if period == 'YEAR':
        pass
    if period == 'REVIEW':
        pass
    return None


def parse_input():
    pass


def main():
    parse_input()
    get_end_period('WEEK', dt.datetime.now(), dt.datetime.now())


main()
