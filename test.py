numbers=[1,2,3,4,5]
num=[]

for item in numbers:
        num.append(item*2)
print(num)   

def my_fun(num):
    return num*2

result1=map(my_fun,numbers)  
print(list(result1))  

result2=map(lambda x:x*3 ,numbers) 
print(list(result2))