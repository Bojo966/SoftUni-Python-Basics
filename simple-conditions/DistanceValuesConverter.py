inputDistance = float(input())
inputMetric = input()
outputMetric = input()

metrics = {'mm': 1000, 'cm': 100, 'mi': 0.000621371192, 'in': 39.3700787, 'km': 0.001, 'ft': 3.2808399, 'yd': 1.0936133, 'm': 1 }

middleDistanceInMeters = inputDistance / metrics[inputMetric]
outputDistance = middleDistanceInMeters * metrics[outputMetric]

print(outputDistance)




