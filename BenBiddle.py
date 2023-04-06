# def my_generator(n):

#     # initialize counter
#     value = 0

#     # loop until counter is less than n
#     while value < n:

#         # produce the current value of the counter
#         yield value

#         # increment the counter
#         value += 1

# # iterate over the generator object produced by my_generator
# for value in my_generator(3):

#     # print each value produced by generator
#     print(value)
def genName():
    value = 0
    nameList = ["Barlowe",
                    "Caddel",
                    "Hart",
                    "Katz",
                    "Laurier",
                    "Madden",
                    "Elrod",
                    "Whitlock",]
    while value <= len(nameList):
        
        yield nameList[value]
        value +=1   
        print(value)
households = genName()
print(next(households))
print(next(households))
print(next(households))