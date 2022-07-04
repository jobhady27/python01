fruits = ["apple","banana","cherry","orange"]
print(fruits[0])
#เปลี่ยนค่าในlist
fruits[1]="blackcurrent"
print(fruits)
fruits[1:3]=["banana","kiwi","melon"]
print(fruits)
fruits[1:3]=["blackcurrent"]
print(fruits)
#เพิ่มค่าในlist
fruits.append("kiwi")
print(fruits)
fruits.append("banana")
print(fruits)
tropical = ["mango","pineapple","papaya"]
fruits.extend(tropical)
print(fruits)
#ลบค่าในlist
fruits.remove("pineapple")
print(fruits)
fruits.pop(3)
print(fruits)
#del fruits ลบตัวแปรlistทิ้งไปจากระบบ
#เรียงค่าในlist
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
#รวมlist
vege=["carrot","potato","cucamber"]
all= fruits+vege
print(all)
#วรรณวิภา ดอนจวง  6/11 เลขที่ 43