#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ограничение запросов

import sys
from collections import deque, defaultdict


class Limiter:
    def __init__(self, limit: int, duration: int):
        self._limit = limit
        self._duration = duration
        self._queue = deque()

    def check_push(self, time):
        if (len(self._queue) >= self._limit) and (self._queue[0] >= time - self._duration):
            return False
        return True

    def push(self, time):
        if not self.check_push(time):
            return False

        if len(self._queue) >= self._limit:
            self._queue.popleft()
        self._queue.append(time)
        return True


def limiter_requests(limits, requests):
    user_limit, service_limit, time_duration = limits
    user_limiter = defaultdict()
    service_limiter = Limiter(service_limit, time_duration)
    responses = []
    for time, user in requests:
        if not user_limiter.get(user):
            user_limiter[user] = Limiter(user_limit, time_duration)

        response_user_limiter = user_limiter[user].check_push(time)
        response_service_limiter = service_limiter.check_push(time)

        if response_user_limiter and response_service_limiter:
            response_service_limiter = service_limiter.push(time)
            user_limiter[user].push(time)

        if not response_user_limiter:
            response = '429'
        elif not response_service_limiter:
            response = '503'
        else:
            response = '200'
        responses.append(response)
    return responses


def parse_input():
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
    sys.stdout.flush()
    for s in responses:
        sys.stdout.write(s)
        sys.stdout.write('\n')

def main():
    limits, requests = parse_input()
    # limits = [2, 5, 5]
    # requests = [[1, 100], [1, 100], [2, 100], [2, 200], [2, 300], [2, 400], [2, 500], [3, 500], [5, 200], [6, 100],
    #             [7, 200]]
    responses = limiter_requests(limits, requests)
    output_response(responses)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Execution is interrupted by pressing Control+C')

