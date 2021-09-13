import sys
import json
from collections import defaultdict


orders = defaultdict(defaultdict)
item = {'id': None, 'count': 0}
items = list(item)

# data = json.load(sys.stdin
data = [
            {"event_id": 1,
            "order_id": 1,
            "item_id": 1,
            "count": 1,
            "return_count": 0,
            "status": "OK"
            },
            {
            "event_id": 2,
            "order_id": 1,
            "item_id": 1,
            "count": 1,
            "return_count": 0,
            "status": "CANCEL"
            },
            {
            "event_id": 3,
            "order_id": 1,
            "item_id": 2,
            "count": 1,
            "return_count": 0,
            "status": "OK"
            }
        ]


def item_update(order_id, item_id, item_count):

    pass


for order in data:
    if order['status'] == 'OK':
        orders[order['order_id']][order['item_id']] = orders[order['order_id']][order['item_id']] + order['count'] - order['return_count']
    else:
        orders[order['order_id']][order['item_id']] = orders[order['order_id']][order['item_id']] - order['count'] - order['return_count']
for order_id, order in orders.items():
    for item_id, item_count in order.items():
        print('order_id:', order_id, 'item_id:', item_id, 'item_count:', item_count)
# print(orders)
# print(orders[1][1])