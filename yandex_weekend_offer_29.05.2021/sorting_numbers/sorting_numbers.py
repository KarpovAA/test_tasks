#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Сортировка чисел

import sys
import requests


def parse_input():
    return [sys.stdin.readline().strip() for _ in range(4)]


def main():
    ip, port, a, b = parse_input()
    url = 'http://{}:{}'.format(ip, port)
    res = requests.get(url, params=dict(a=a, b=b))
    numbers = sorted(res.json())
    for num in numbers:
        print(num)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Execution is interrupted by pressing Control+C')
