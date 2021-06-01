#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Перекладывание JSON

import sys
import json


def merge_fids(fids):
    comb_fids = list()
    for i in fids:
        for j in i['offers']:
            comb_fids.append(j)
    return sorted(comb_fids, key=lambda x: (x['price'], x['offer_id']))


def parse_input() -> [dict]:
    n_fids = int(sys.stdin.readline().strip())
    fids = []
    for _ in range(n_fids):
        fids.append(json.loads(sys.stdin.readline().strip()))
    return fids


def main():
    # '{"offers": [{"offer_id": "offer1", "market_sku": 10846332, "price": 499},
    #              {"offer_id": "offer2", "market_sku": 682644, "price": 499}]}'
    # '{"offers": [{"offer_id": "offer3", "market_sku": 832784, "price": 14000}]}'
    fids = parse_input()
    print(json.dumps({'offers': merge_fids(fids)}))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Execution is interrupted by pressing Control+C')
