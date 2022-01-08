#variable :la mot vung khong gian duoc dat ten.

age = 18
name = "meta"
pow = 1000
print("my name is : " + name) 
print("my age: "+ str(age)) #noi chuoi va ep kieu so age thanh string typecast
# kiem tra kieu du lieu
# print(type(name))
# print(type(age))
#noi suy trong string.fomat
str = "my name is {} , my age {}"
print(str.format(name, age))
str2 = "myname is {0} my age : {1} , i have {1} , balaa {2} w"
print(str2.format(name, age, pow))
#onway decision : quyet dinh if 