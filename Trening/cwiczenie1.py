name = "Artur"
age = 41
days_in_year = 365
message = '%s is %d years old, so is about %d days old'

print(message %(name, age, age*days_in_year))


message2 = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message2.format(name, age, age * days_in_year))


name1 = input("podaj swoje imię: ")
age1 = int(input("podaj swój wiek: "))
message2 = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message2.format(name1, age1, age1 * days_in_year))

print(" 1234567890 divided by 12345 is ", 1234567890//12345, "and the rest is ", 1234567890 % 12345)