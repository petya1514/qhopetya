print ("What should I do (recover/study)?")
activity = input ()
if activity == "recover":
    act1 = input ("do you want to sleep or socialize")
    if act1 == "sleep":
        print ("zzzz")
    else:
        print("I will meet a friend")
else:
    print(" I will study")
    study1 = input("what subject do you want to study?(network/cyber")
    if study1 ==network:
        print("study intro to networks")
    else:
        print("study intro to Cyber")

print ("activity complete")