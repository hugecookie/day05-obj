# 8-2-1 set()
# even_num = {0, 2, 4, 6, 8}
# odd_num ={1, 3, 5, 7, 9}
import random

# 8-2-2 set()
# print(set('letters'))  # 개수와 상관없고 종류만 출력, 순서 x
# print(set(('girl', 'woman', 'grandma')))
# print(set(['man', 'old man', 'child']))  # list와 tuple 둘 다 변환이 가능

# 8-2-3 len()
date = {1, 2, 3, 4, 5, 6, 7}
# print(len(date))

# 8-2-4~5 add(), remove()
# date = {1, 2, 3, 4, 5, 6, 7}
# date.add(8)
# print(date)
# date.remove(2)
# print(date)

# 8-2-6~7 for, in
# for i in date:
#     print(i)

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}}
# for name, contents in drinks.items():
#     if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
#         print(name)

# 8-2-8 Combination and Operators
# for name, contents in drinks.items():
#     if contents & {'vermouth', 'orange juice'}:
#         print(name)

# for name, contents in drinks.items():
#     if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
#         print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']

a = {1, 2}
b = {2, 3}
# print(a & b, a.intersection(b))
# print(bruss & wruss)
# print(a | b, a.union(b))
# print(a - b, a.difference(b))
# print(a ^ b, a.symmetric_difference(b))
# print(a <= b, a.issubset(b))
# print(a <= a, a.issubset(a))
# print(a < a)
# print(a >= b, a.issuperset(b))
# print(a > b)

# 8-2-9 set comprehension
a_set = {number for number in range(1, 6) if number % 3 == 1}
# print(a_set)

# 8-2-10 frozenset
# print(frozenset([3, 2, 1]))
# print(frozenset([2, 1, 3]))
# print(frozenset([2, 3, 1]))

fs = frozenset([3, 2, 1])
# fs.add(4)  # 불변 셋이라 더할 수 없다.

# 8-3 data structure so far
marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = ('Groucho', 'Chico', 'Harpo')
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}
marx_set = {'Groucho', 'Chico', 'Harpo'}  # 셋은 인덱스와 키가 없음.
# print( marx_list[2], marx_tuple[2], marx_dict['Harpo'])

# 8-4


# chap 9 function
# 9-1 def ~():
def do_nothing():
    pass


mamamoo = ['화사', '솔라', '휘인', '문별']
# print(mamamoo.pop())  # 삭제할 값 리턴 후 삭제
# print(mamamoo.remove('문별'))  # 삭제만 합. 따라서 print함수 none 출력
# print(mamamoo)
# 9-2 def
do_nothing()
# print(do_nothing())

def make_a_sound():
    print("quack")
# make_a_sound()

def agree():
    return True

# if agree():
#     print('splendid!')
# else:
#     print('That was unexpected')
import random

def calculate_fee(args):
    """
        놀이공원 요금 계산 프로그램
        :param: 사람 수 arg
        :total: {'num_of_people':전체 인원 수,
                 num_of_adults: 어른 수,
                 num_of_kids: 아이 수,
                 total_amounts:지불할 총 이용료
        """
    total = 0
    adults = 0
    kids = 0
    for i in args:
        if i > 19:
            total = total + 10000
            adults += 1
        else:
            total = total + 3000
            kids += 1
    return {'num_of_people': len(args), 'num_of_adults': adults, 'num_of_kids': kids, 'total_amounts': total}


# no_of_visitor = int(input('몇 분이세요? '))
# # print(calculate_fee().__doc__)
# ages = [random.randint(1, 60) for age in range(no_of_visitor)]
# print(ages)
# results = calculate_fee(ages)
# print(f"총 {results['num_of_people']}명이고 성인 {results['num_of_adults']}명, 아이 {results['num_of_kids']}명이 지원했으며, 총 {results['total_amounts']}원입니다.")

# print(calculate_fee(20, 30, 40))
# print(calculate_fee(45, 43, 10, 7))

def call_func(f):
    """
    :param f: 매개변수가 함수
    :return:
    """
    f()

def calculate():
    x = 1
    y = 2
    temp = 0
    def add_sub(n):
        nonlocal temp # 외부 변수를 끌어들임
        # x = 11
        temp = temp + x + n - y
        return temp
    return add_sub


c1 = calculate()
# for i in range(5):
#     print(c1(i))


# 9.7 lambda

import random

def process(num_list, f):
    for num in num_list:
        print(f(num))


# def squares(n):
#     """
#     :param n: integer
#     :return n: integer
#     """
#     return n**2


numbers = [random.randint(1, 100) for i in range(5)]
# process((numbers, squares)
process(numbers, lambda x: x * x) # lambda 함수는 간단한 함수를 빠르게 이용하기 위한 방법이다.













