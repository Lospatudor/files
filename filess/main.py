import json


if __name__ == '__main__':
    file = open('input.json')
    data = json.load(file)

    for i in data['cars']:
        print(i)

    file.close()

    slow_cars = list(filter(lambda car: car["hp"] < 120, data["cars"]))
    for car in slow_cars:
        print(f"Slow cars : {car}")
        with open("slow_cars.json", "w") as outfile:
            json.dump(slow_cars, outfile)

    fast_cars = list(filter(lambda car: 120 <= car["hp"] < 180, data["cars"]))
    for car in fast_cars:
        print(f"Fast cars : {car}")
        with open("fast_cars.json", "w") as outfile:
            json.dump(fast_cars, outfile)

    sport_cars = list(filter(lambda car: car["hp"] >= 180, data["cars"]))
    for car in sport_cars:
        print(f"Sport cars : {car}")
        with open("sport_cars.json", "w") as outfile:
            json.dump(sport_cars, outfile)

    cheap_cars = list(filter(lambda car: car["Price"] < 1000, data["cars"]))
    for car in cheap_cars:
        print(f"Cheap cars : {car}")
        with open("cheap_cars.json", "w") as outfile:
            json.dump(cheap_cars, outfile)

    medium = list(filter(lambda car: 1000 <= car["Price"] < 5000, data["cars"]))
    for car in medium:
        print(f"Medium price cars : {car}")
        with open("medium_cars.json", "w") as outfile:
            json.dump(medium, outfile)

    expensive = list(filter(lambda car: car["Price"] >= 5000, data["cars"]))
    for car in expensive:
        print(f"Expensive cars : {car}")
        with open("expensive_cars.json", "w") as outfile:
            json.dump(expensive, outfile)
