h, m = map(int, input().split())

if h == 0:
    h = 24

new_h = ((h * 60 + m) - 45) // 60
new_m = ((h * 60 + m) - 45) % 60

if new_h == 24:
    new_h = 0

print(f'{new_h} {new_m}')

