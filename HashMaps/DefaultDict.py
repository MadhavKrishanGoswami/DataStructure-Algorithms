from collections import defaultdict

city_map = defaultdict(list)
print(city_map)
cities = ["Delhi", "Lucknow"]
city_map["India"] += cities
print(city_map) 