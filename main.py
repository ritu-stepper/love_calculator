print("welcome to love calculator!!")
print("this has been made by ritu raj for my Harshita")
name1=input("what is your name?\n")
name2=input("what is your name?\n")
final_name = (name1+name2).lower()
t=final_name.count("t")
r=final_name.count("r")
u=final_name.count("u")
e=final_name.count("e")
true=(t+r+u+e)
l=final_name.count("l")
o=final_name.count("o")
v=final_name.count("v")
e=final_name.count("e")
love=(l+o+v+e)
true_love=f"{true}{love}"
true_love=int(true_love)
if 10<true_love<90:
    print(f"your score is{true_love},you are in cook and hooked relationship")
elif 40<true_love<50:
    print(f"your score is{true_love},you are good relation")
else:
    print(f"your score is{true_love} ")