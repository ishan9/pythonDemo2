# while loop
# 10= 10 div 2=5, 10 rem 2= 0 
# 5 = 5 div 2 =2, 5 rem 2 =1
# 2 = 2 div 2 =1, 2 rem 2 = 0
# 1 = 1 div 2 =0, 1 rem 2 =1
#2 raise n -1 == 10 .. 2^3 -1 = 7  2^ 4 - 1 = 15 2 raise to 7 128-1
n = 128
list1 = []
while n > 0:
    rem = n % 2
    list1.insert(0,rem)
    n = int(n / 2)

for x in list1:
    print(x)