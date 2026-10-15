
# kiosk/reports.py

from kiosk.data import sales_log


def unique_goods_sold():
    unique_goods = set()

    for goods, quantity, total in sales_log:
        unique_goods.add(goods)

    print()
    print("Unique goods sold:")

    if not unique_goods:
        print("No goods have been sold yet.")
    else:
        for goods in sorted(unique_goods):
            print(goods)
