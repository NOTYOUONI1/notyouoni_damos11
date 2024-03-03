"""name = input("name : ")
age = int(input("age : "))
price = float(input("price : "))

print("my name is", name, "my age", age,)"""

'''Hi = input("Hello :")
ki = input(input("ko :"))
na = input(input("ho :"))'''

#print("reply", Hi, "Reply", ki, "Reply", na,)
#name = input("name :")
#age = int(input("age :"))
#price = float(input("price"))

#print("my name is", name, "/" "my age", age,)
'''light = input("light color :")

if(light == "red"):
    print("stop")

elif(light == "blow"):
    print("slow")

elif(light == "orange"):
    print("kak")'''
'''marks = input("marks : ")

if(marks >= 90):
   print("A")

elif(marks >= 80 ):
    print("c")

elif(marks >= 70):
    print("B")

    print("D")
    print("this ragal is", marks) # type: ignore'''
'''age = int(input("age :"))
vote = ("yes","no") [age < 18]
print(vote)'''
'''b = 4
h = 9
print(b + h)'''
'''a = 2000
b = 2000
mun = 10
mim = mun * 100 #1000
print("mim :", mim)
d = input("what you :")
print("lolsa :", d)'''
'''a = int(input("Enter your number :"))
b = int(input("+ :"))

print("low :", a + b)'''
#a = int(input("Enter :"))
#b = int(input("Enter :"))
'''print("Hello\nWorld")
print('rakib\nWijv')
h = "lkjopfdglkjfglkmnfbglkjfbglkjfblkjfbgsffdsglj;mfbg\ngifigfjhfdjfvdkjnvfkjnvclknvclknxcvlkn"
print(h)
jj = "rakib"
print(jj[2:])'''
'''ri = "rakib"
print(i.count("ONI"))'''
'''p = "rakib ka sa ka sa ka sa"
print(p.count("k"))'''
#y = input("name :")
#print("my name is :", y)
"""i = input("rakib :")
if(i == "r"):
    print("s")
if(i == "y"):
    print("st")
if(i == "u"):
    print("sto")"""
"""if(maks < 70):
    print("c")
elif(maks < 80):
    print("b")
elif(maks < 90):
    print("A")
elif(maks < 100):
    print("A+")"""
"""maks = int(input("enter maks :"))
if(maks > 70):
    print("u")"""""""""
"""a = int(input("enter your number :"))#9
b = int(input("enter your number :"))#5
c = int(input("enter your number :"))#8
d = int(input("enter your number :"))#8
if(a > b and a < c):""""""
    print("rezalt :",a)
elif(b > c and b < d):
    print("rezalt ",b)
elif(c > d ):
    print("rezalt ",c)
else:
    print("no",d)"""
"""marks = [65,5454,4555636,346,56]
print(marks)
s = ["rakib",786,4325,"ONI"]
s[3] = "ONI"
print(s)
i = "rakib", 22,
print(i[1])"""
"""i = (535,739485676,6426333356072356,87)
print(type(i))
print(i[0])"""
"""a = input("cartoon name:")
b = int(input("ep :"))
c = input("DETALs :")
print("cartoon", a, "|" "BEST ep", b, "|" "DETAL", c)"""
"""li = [1,2,3]
l = li.copy()
l.reverse()
print(li, l)
if(li == l):
    print("h")
else:
    print("not")"""
"""pi = int(input("enter number :"))
p = int(input("enter number :"))
if(pi == p):
    print("h")
else:
    print("not")"""
"""p = ["C", "D", "A", "A", "B", "B", "A"]
l = p.sort()
print(p)"""
"""info = {
    "key" : "dec",
    "name" : "m",
    "learing" : "book"
}
print(info)"""
"""cl = int(input("Enter number :"))
cL = int(input("Enter :"))
c = int(input("Enter number"))
print(cl+cL+c)"""
"""def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")
    
    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() != "yes":
        break
"""
"""c = input("Enter number :")
C = input("enter number :")
print("-/+")
p = def(input("enter"))
if(p = +):
    print(c + C)
elif(p = -):
    print(c - C)"""
"""dict = {
    "name" :input("Name plese : "),
    "age" : 15,
}
print(dict)"""
"""dict = {
    "name 1" : "rakib",
    "name 2" : "sakib",
    "name 3" : "maruf",
    "name 4" : "doraemon",
    "fb" : {
        "fb" : "azira king",
        "tiktok" : "oni",
    }
}
l = {
    "name f" : "rakib",
    "name hg" : "sakib",
    "name p" : "maruf",
    "name o" : "doraemon",
    "fbr" : {
        "fbm" : "aziryfyua king",
        "tiktopk" : "otuoni",
    }
}
dict.update(l["fbr"])
print(dict)
"""
"""c = set()
c.add(1)
c.add(9)
c.add(4)
c.remove(4)
c.pop()
c.pop()
print(len(c))"""
"""u = {1,2,3}
i = {3,4,5}

print(i.union(u))"""
"""dict = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"
}
print(dict)
subject = {
    "python", "java", "c++", "c", "javasrip", "java", "c", "python"
}
print(len(subject))"""
"""marks = {}

x = int(input("java :"))
marks.update({"java" : x}),

x = int(input("english :"))
marks.update({"english" : x})

x = int(input("math :"))
marks.update({"math" : x})

print(marks)"""
""""""
"""i = 1
n = int(input("* number : "))
while (i <= 10):
    print(n*i)
    i += 1
"""
num = [1,20,60,433,644,4356,24243]
print(num[int])