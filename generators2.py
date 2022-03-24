# interable
# iterate
# generators

# range is a generators which is an interable. Not the other way around, interable are not generators. 

# example 
# def generator_function(num):
#     for i in range(num):
#         yield i

# for item in generator_function(1000):
#     print(item)




# example 
def generator_function(num):
    for i in range(num):
        yield i*2

g = generator_function(100)
next(g)
# next(g)
print(next(g))

# example 
def generator_function(num):
    for i in range(num):
        yield i*2

g = generator_function(100)
next(g)
next(g)
print(next(g))


# example it will stop the interation as generator_function(1) is no more
def generator_function(num):
    for i in range(num):
        yield i

g = generator_function(1)
next(g)
next(g)
print(next(g))





# for item in generator_function(1000):
#     print(item)


# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result

# # my_list = make_list(100)
# # print(list(range(1000000)))

