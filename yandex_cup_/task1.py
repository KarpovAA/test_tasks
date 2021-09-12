import sys
import json
from collections import defaultdict


orders = list()

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
            }
          ]
for order in data:
    if order['status'] == 'OK':
        if order['order_id'] in orders:
            orders[order['order_id']][order['item_id']] += order['count']
        else:
            orders[order['order_id']][order['item_id']] = order['count']
    else:
        if order['order_id'] in orders:
            orders[order['order_id']][order['item_id']] -= order['count']
        else:
            orders[order['order_id']][order['item_id']] = - order['count']
        pass
# for k, v in orders.items():
#     print(k, v)
print(orders)
print(orders[1][1])