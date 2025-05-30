# use filter(): filter out even num from a list of int (1 to 100):

def filter_even():

    return list(filter(lambda x: x % 2 == 0, range(1, 101)))


print(filter_even())


   
