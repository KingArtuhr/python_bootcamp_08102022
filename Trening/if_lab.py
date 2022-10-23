#1
muscle_pain = False
fever = False
weakness = True

#2
if muscle_pain and fever and weakness:
    print("suspicious of influenca")
else:
    print("the flue is unlikely")

#3
if muscle_pain and fever and weakness:
    print("suspicious of influenca")
elif not (muscle_pain and fever) and weakness:
    print("Just take a rest!")
else:
    print("You may be cold")

#4 i 5
is_man = True

if muscle_pain and fever and weakness or is_man and(muscle_pain or fever or weakness):
    print("suspicious of influenca")
elif not (muscle_pain and fever) and weakness:
    print("Just take a rest!")
else:
    print("You may be cold")

#6

check_is_completed = False

print("Check is colpeted" if check_is_completed else "check not done yet")


