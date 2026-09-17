force = input("ENter a force in Newtons:")
distance = input("Enter a distance in meters:")
work = float(force) * float(distance)
print("work:", work)
print(type(work))

time = 6
power = work / time
print("power:", power)
print(type(power))
