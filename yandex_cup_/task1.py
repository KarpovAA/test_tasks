import sys
import json
from collections import defaultdict


# data = json.load(sys.stdin)
data = [
        {
            "event_id": 2,
            "order_id": 2,
            "item_id": 1,
            "count": 3,
            "return_count": 1,
            "status": "OK"
        },
        {
            "event_id": 1,
            "order_id": 1,
            "item_id": 1,
            "count": 2,
            "return_count": 0,
            "status": "OK"
        },
        {
            "event_id": 3,
            "order_id": 3,
            "item_id": 1,
            "count": 2,
            "return_count": 2,
            "status": "OK"
        }
    ]
# data = [
#             {"event_id": 1,
#             "order_id": 1,
#             "item_id": 1,
#             "count": 1,
#             "return_count": 0,
#             "status": "OK"
#             },
#             {
#             "event_id": 2,
#             "order_id": 1,
#             "item_id": 1,
#             "count": 1,
#             "return_count": 0,
#             "status": "CANCEL"
#             },
#             {
#             "event_id": 3,
#             "order_id": 2,
#             "item_id": 2,
#             "count": 1,
#             "return_count": 0,
#             "status": "OK"
#             }
#         ]


orders = defaultdict(defaultdict)

for order in data:
    if order['order_id'] not in orders:
        orders[order['order_id']] = defaultdict(int)
        orders[order['order_id']][order['item_id']] = 0

    if order['status'] == 'CANCEL':
        orders[order['order_id']][order['item_id']] = 0
    else:
        orders[order['order_id']][order['item_id']] += order['count'] - order['return_count']
    pass

result = list()
for k, v in orders.items():
    list_items = [{'id': item_id, 'count': item_count} for item_id, item_count in v.items() if item_count > 0]
    if list_items:
        result.append({'id': k, 'items': list_items})

sys.stdout.write(json.dumps(result))
