lowername1 = name1.lower()
lowername2 = name2.lower()
totalname = lowername1 + lowername2
t = totalname.count("t")
r = totalname.count("r")
u = totalname.count("u")
e = totalname.count("e")
totalTrue = t + r + u + e
l = totalname.count("l")
o = totalname.count("o")
v = totalname.count("v")
e = totalname.count("e")
totalLove = l + o + v + e
result = int(str(totalLove) + str(totalTrue))
print(f"your love result is {result}")
if result < 10 and result > 90:
    print("you go togather like coke and mentos")
   
elif result >= 40 and result <= 50:
    print("you are well togather")
