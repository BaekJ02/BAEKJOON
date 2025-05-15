total_price = int(input())
total_quantity = int(input())
tmp = 0

for i in range(total_quantity):
    item_price, item_quantity = map(int, input().split())
    tmp += item_price * item_quantity 

if (total_price == tmp):
    print("Yes")
else:
    print("No")