# def fatorial(num):
#     if num <= 1:
#         return 1
#     else:
#         return(num * fatorial(num -1))

# print(fatorial(5))

# def fatorial(n):
#     n = n if n> 1 else 1
#     j =1 
#     for i in range(1 , n+1):
#         j = j * i
#     return j

# for i in range(1,6):
#     print(str(i) +'->' + str(fatorial(i)))

def fib(n):
    if n> 1:
        return fib(n - 1) + fib(n-2)
    else:
        return 1

for i in [1,2,3,4,5]:
    print(str(i) + ' => ' + str(fib(i)))
