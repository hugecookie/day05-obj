8-11
set_com = {number for number in range(10) if number % 2 == 1}
# print(set_com)

8-12
gen = (f'got {i}' for i in range(10))
# for i in gen:
#     print(i)


8-13
key = ('optimist', 'pessimist', 'troll')
values = ('The glass is full', 'The glass if half empty', 'How did you get a glass')
dic = {key[0]: values[0], key[1]: values[1], key[2]: values[2]}

8-14
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a mon ster', 'A hunted yarn shop']

movies = {titles[0]: plots[0], titles[1]: plots[1]}
# print(movies)

9-1
def good():
    harry = ['Harry', 'Ron', 'Hermione']
    return harry

9-2
def get_odds():
    a = []
    count = 0
    for i in range(1,10):
        if i % 2 == 1:
            count += 1
            a.append(i)
    return a
a = get_odds()
print(a[2])

9-3