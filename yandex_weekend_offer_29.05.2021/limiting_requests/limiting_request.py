#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ограничение запросов

import sys


def limit_requests(limits, requests):
    return 1


def parse_input() -> [dict]:
    # input_str = '2 5 5'
    input_str = sys.stdin.readline().strip()
    limits = [int(s) for s in input_str.split(' ')]
    requests = []
    while True:
        input_str = sys.stdin.readline().strip()
        if input_str == '-1':
            break
        requests.append([int(s) for s in input_str.split(' ')])
    return limits, requests


def output_response(responses):
    print(responses)


def main():
    limits, requests = parse_input()
    responses = limit_requests(limits, requests)
    output_response(responses)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Execution is interrupted by pressing Control+C')
