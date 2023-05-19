from collections import defaultdict, Counter
from typing import List


def displayTable(orders: List[List[str]]) -> List[List[str]]:
    desk = defaultdict(Counter)
    meal = set()
    for _, table, food in orders:
        meal.add(food)
        desk[table][food] += 1
    foods = sorted(meal)
    result = [['Table'] + [food for food in foods]]
    
    for table in sorted(desk, key=int):
        result.append([table] + [str(desk[table][food]) for food in foods])
    return result

    


orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"], ["Adam","4","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
a = displayTable(orders)
print(a)