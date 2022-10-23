hello_message = 'Hello %s!'
print( hello_message % ("Kris"))
print( hello_message % ("Kate"))

hello_message2 = "Hello {0:s}!"
print(hello_message2.format("Kris"))
print(hello_message2.format("Kate"))

hello_message3 = "%s has %d %s"
print(hello_message3 % ("Kate", 1, "animal"))
print(hello_message3 % ("Kris", 10000, "$"))

hello_message4 = "{0:s} has {1:d} {2:s}"
print(hello_message4.format("Kate", 1, "animal"))
print(hello_message4.format("Kris", 100000, "$"))

line = "{0:20s} costs {1:6d} €"

print(line.format('ICE CREAM', 3))
print(line.format('TRIP TO VENICE', 119))
print(line.format('PIZZA HAWAI', 6))

line2 = '{0:s} {1:d}'
print(line2.format('ICE CREAM', 3))
print(line2.format('TRIP TO VENICE', 3))
print(line2.format('PIZZA HAWAI', 3))

