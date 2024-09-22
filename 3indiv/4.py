data = {1: 200, 2: 30, 3: 0, 4: 999, 5: 923, 6: 87, 7: -2}
top3 = sorted(data, key=data.get, reverse=True)[:3]
print(top3)