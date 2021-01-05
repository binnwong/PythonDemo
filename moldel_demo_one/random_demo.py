# coding=utf-8
import random


# print(random.randint(1, 5))
# print(random.randrange(0, 51, 5))

# print(random.random())
# print(random.uniform(2, 5))

# choice_str = 'python'
# print(random.choice(choice_str))
# choice_list = [i for i in range(1, 6)]
# print("choice_list: ", choice_list)
# print(random.choice(choice_list))
# choice_tuple = (10, 20, 30, 40, 50)
# print(random.choice(choice_tuple))
# choice_set = {"name", "job", "age"}
# print(random.choice(choice_set))
# choice_dict = {"name": "wuyazi", "job": "ceo", "age": 18}
# print(random.choice(choice_dict))

# choice_list = [i for i in range(1, 6)]
# print("choice_list: ", choice_list)
# print(random.choices(choice_list))
# choice_tuple = (10, 20, 30, 40, 50)
# print(random.choices(choice_tuple, k=2))
# choice_str = 'python'
# print(random.choices(choice_str, weights=[0.5, 0, 0.5, 0, 0, 0], k=7))
# print(random.choices(choice_str, cum_weights=[0, 0.5, 0.5, 1, 1, 1], k=7))
# print(random.choices(choice_str, weights=[1, 0, 0, 0, 0, 0], cum_weights=[1, 1, 1, 1, 1, 1], k=2))

# sample_list = [i for i in range(1, 6)]
# print("sample_list: ", sample_list)
# print(random.sample(sample_list, 1))
# sample_tuple = (10, 20, 30, 40, 50)
# print(random.sample(sample_tuple, 2))
# sample_str = 'python'
# print(random.sample(sample_str, 3))

cards = ['%s-%s' % (a, b) for a in ['Spade', 'Heart', 'Diamond', 'Club'] for b in
         ([str(i) for i in range(3, 11)] + [j for j in 'JQKA2'])] + ['Black joker', 'Red joker']
print("Before: ", cards)
random.shuffle(cards)
print("After: ", cards)
