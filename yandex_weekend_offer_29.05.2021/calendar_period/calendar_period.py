#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Модуль разбиения на интервалы дат

import sys
import calendar
import datetime as dt


def get_latest_date_of_period(period: str, start_date: dt.datetime) -> [dt.datetime, None]:
    """
    :param period:  WEEK — неделя с понедельника по воскресенье.
                    MONTH — месяц.
                    QUARTER — интервалы в три месяца: январь — март, апрель — июнь, июль — сентябрь, октябрь — декабрь.
                    YEAR — год c 1 января по 31 декабря.
                    REVIEW — периоды, за которые оцениваются достижения сотрудников Яндекса.
                             Летний период длится с 1 апреля по 30 сентября, зимний — с 1 октября по 31 марта.
    :param start_date: Дата начала периода
    :return:
    """
    if period == 'WEEK':
        return start_date + dt.timedelta(days=6 - start_date.weekday())     # последний день недели

    if period == 'MONTH':
        days_in_month = calendar.monthrange(start_date.year, start_date.month)[1]   # количество дней в месяце
        return dt.datetime(start_date.year, start_date.month, days_in_month)        # последний день месяца

    if period == 'QUARTER':
        n_month = (start_date.month // 3 + 1) * 3                         # последний месяц текущего квартала
        days_in_month = calendar.monthrange(start_date.year, n_month)[1]  # кол-во дней в последнем месяце квартала
        return dt.datetime(start_date.year, n_month, days_in_month)       # последний день квартала

    if period == 'YEAR':
        return dt.datetime(start_date.year, 12, 31)                       # последний день текущего года

    if period == 'REVIEW':
        if 4 <= start_date.month <= 9:
            month = 9
            year = start_date.year
        else:
            month = 3
            year = start_date.year + 1
        days_in_month = calendar.monthrange(year, month)[1]
        return dt.datetime(year, month, days_in_month)                    # последний день ревью

    return None


def split_date_intervals(period: str, start: dt.datetime, end: dt.datetime) -> [int, list]:
    start_date = start
    n_period = 0
    list_periods = []
    while start_date < end:
        n_period += 1
        end_date = get_latest_date_of_period(period, start_date)
        if end_date > end:
            end_date = end
        list_periods.append([str(start_date.date()), str(end_date.date())])
        start_date = end_date + dt.timedelta(days=1)
    return n_period, list_periods


def parse_input():
    period = sys.stdin.readline().strip()
    start_period, end_period = sys.stdin.readline().strip().split(' ')
    return period, dt.datetime.strptime(start_period, '%Y-%m-%d'), dt.datetime.strptime(end_period, '%Y-%m-%d')


def main():
    period, start_period, end_period = parse_input()
    n_period, list_periods = split_date_intervals(period, start_period, end_period)
    print(n_period)
    for i in list_periods:
        print(i[0], i[1])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Execution is interrupted by pressing Control+C')
