#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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


def parse_input():
    period = sys.stdin.readline().strip()
    start_period, end_period = sys.stdin.readline().strip().split(' ')
    return period, dt.datetime.strptime(start_period, '%Y-%m-%d'), dt.datetime.strptime(end_period, '%Y-%m-%d')


def main():
    period, start_period, end_period = parse_input()
    print('Окончание периода: ', str(get_latest_date_of_period(period, start_period).date()))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Execution is interrupted by pressing Control+C')

