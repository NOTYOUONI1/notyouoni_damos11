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
"""num = (1,20,60,433,644,4356,24243)
i = 1
while i <= 5:
    print("finding..")
    if(i == 4):
        break
    i += 1
print("total loop",i)"""
"""p = [1,4,9,16,25,36,49,64,81,100]
x = 36
for list in p:
    if list == x:
        print("yes")
    print(list)"""
"""i = 1
while i<= 100:
    print(i)
    i += 1"""
"""for i in range(100,0, -1):
    print(i)"""
"""
"""
"""def lenth(list):
    print(len(list), end="  ")

r = [1,2]
t = [6,6,0,3,9]
lenth(r)
lenth(t)
print()"""
"""i = input("enter your doller amount :")"""
"""def dod(i):
    tkk = i * 124
    print(i,"=doller", tkk,"=tk")
dod(l)
l = input("enter your amount :")"""
"""i = "$$$$"
print(i.count("$"))"""
""""""""
"""m = int(input("enter your mask :"))
if(m > 70 and m <80):
    print("c")
elif(m > 80 and m <90):
    print("b")
elif(m > 90 and m <100):
    print("a")
elif(m >101):
    print("a+")
"""
"""age = int(input("enter your age :"))
if(age < 18 ):
    if(age < 100):
        print("non")
    print("yes1")
elif(age > 18):
    print("no")
"""
"""a = int(input("enter your fast number : "))
b = int(input("enter your fast seceand : "))
c = int(input("enter your fast theard : "))
#i = int(input())
if( a > b and a > c):
    print("lerges number=",a)
elif(b > c):
    print("lerges number=",b)
else:
    print("lerges number=",c)"""
"""srang = [1,2,3,"rakib"]
srang[0] = 3
print(srang)"""
"""r = [20,593,'ralib',44]
r[0]=[609]
print(r[:2])"""
"""list = ["rakib","sakib,","maruf",213,743,882]
list1 = [4,74,97,654]
list.append(78)
print(list)"""
"""list = [8,6,1,2,3,4,5,6]
list.pop()
print(list)"""
"""tup = (5,9,8,8,8,)

print(tup.count(8))"""
"""i = [input("enter your first favourite movie :")]
y = [input("enter your second favourite drama :")]
print(i, "your first movie", y, "your secound drama")"""
"""p = [1,2,3]
l = [3,2,1]

copy_l = l.copy()
copy_l.reverse()

if(l == p):
    print("prandroom")
else:
    print("not prandroom")
print(copy_l)"""
"""dict = {
    "name" : "rakib",
    "name" : "rakib",
    "roll" : 67,
    "mask" : [12,74,90,91],
    "dict2" : {
        "name" : "rakib"
    }
}
#dict.update({"name" : "rf"})
gfddtu = set("123456789")
gfddtu.remove("2")
print(gfddtu)"""
"""dict = {
    "cat" : "animle",
    "table" : ["a place of futere","rakib"]
    
}
print(dict)

DICT = {}

#print(len(DICT))


#inp = input("enter your text :")
#ilp =int(input("ripit number :"))
""num = (1,2,3,4,5,6,7,8,9)
i = 1
while i < len(num):
    if num == 4 :
        print(4)
    print()"""
    
"""list = (1,2,3,52,3,55,74,84,87,89,90,55)
c = 55
idx = 0
for i in list:
    if i == c:
        print("number found at idx", idx)
    idx += 1"""
"""i = int(input("enter :"))
p = int(input("enter x :"))
l = 1
while l <=p:
    print(l*i,"", l)
    l+=1"""


"""def pla_rakib(a, b, t):
    ki = a+b+t
    ho = ki/3
    return(ho)

print(pla_rakib(1,2,3))
ko = pla_rakib(1,2,3)
print(ko)

print("rakib hassain", end=" ")
print("sakib ""\n""hassain")

def function_name(a=2, b=3):
    print(a*b)
function_name(5)"""
"""def no_line (l):
    for list in l:
        print(list,end="\n")

hiros = ["rakib", "sakib", "doraemon"]

no_line(hiros)"""
#o = input("enter your amuont :")
#h = int(input("enter doller price :"))
"""def doler(i):
    if(i == 1 or i == 0):
        return 1
    return doler(i-1) * i
         
#doler(5)
print(doler(5))
"""
"""f = open("jm.txt", "r")
line = f.read()
print(line)
f.close()"""
#with open("rakib.txt", "a") as f:
 #   data = f.write("Hi everyone\nWe are learning File I/O\nusing Java.\nl like programming in Java")
"""with open("rakib.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "python")

print(new_data)

with open("rakib.txt", "w") as f:
    data = f.write(new_data)"""

"""def data_find():
       word = "python"
       with open("rakib.txt", "r") as f:
           data = f.read()
           if(data == word):
                print("line 1")
           else:
                print("no hava this text")

def check_line():
     with open ("rakib.txt", "r") as f:
        data = f.readline()"""


"""with open("rakib.txt", "r") as f:
    data = f.read()
    print(data)"""

"""import qrcode as qr
img = qr.make(input("enter link :"))
img.save(input("png photo name :"))
"""
"""i = int(input('enter your number :'))
l = 1
while l <= 10:
    print(i*l, l)
    l += 1
"""
'''email_inputp = str(input("enter yur email addrese :"))

h = email_inputp.isalpha

print(h)'''
"""import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save(
    "scaled_qrcode.png",
    scale=50,
    light="lightblue"
    b
)"""
age =55
if age > 18:
    print("g")

print()

