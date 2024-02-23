# numbers=int(input('Enter a number: '))
# sumEven=0
# sumOdd=0
# for i in range(1, numbers):
#
#     if i % 2==0:
#         sumEven=sumEven+i
#     else:
#         sumOdd+=i
#         print(sumEven,sumOdd)
# print('Sum of even',sumEven,'and odd',sumOdd)
#
try:
    numbers=int(input('Enter a number: '))
    sum_even = (list(range(0,numbers))[::2])
    print(sum_even)
    sum_even_num = sum(sum_even)
    print(sum_even_num)
    sum_odd = (list(range(0,numbers))[1::2])
    print(sum_odd)
    sum_odd_number = sum(sum_odd)
    print(sum_odd_number)
except(ValueError, TypeError) :
    print("invalid input")