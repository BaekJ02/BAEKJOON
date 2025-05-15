h, m = map(int, input().split())
add_time = int(input())

if h == 0:
    h = 24

new_h = ((h * 60 + m) + add_time) // 60
new_m = ((h * 60 + m) + add_time) % 60

if new_h >= 24:
    new_h -= 24
print(f'{new_h} {new_m}')

