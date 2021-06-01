#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Сортировка чисел

import sys
import json


def parse_input():
    addr_ip = sys.stdin.readline().strip()
    addr_port = sys.stdin.readline().strip()
    return addr_ip, addr_port


def main():
    ip, port = parse_input()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Execution is interrupted by pressing Control+C')
