people = [
{"name":"Alex", "house":"Burgos"},
{"name":"Pamela", "house":"Xochitepec"},
 {"name":"Daniel", "house":"Burgos"} 

]
"""
def f(person):
    return person["name"]
people.sort(key=f)
"""

people.sort(key = lambda person: person["name"])
print(people)