data = [5, 10, 15, 20, 25, 30]
print(data[1:5])
data = [5, 10, 15, 20, 25, 30]
print(data[-3:])
data = [5, 10, 15, 20, 25, 30]
print(data[::2])
data = [5, 10, 15, 20, 25, 30]
print(data[4:2])
data = [5, 10, 15, 20, 25, 30]
print(data[::-2])

"""Write Your Own Functions"""


def get_first_n(items, n):
    """
    返回列表的前 n 个元素。
    如果列表长度不足 n，则返回整个列表。
    如果 n=0，则返回空列表。
    """
    return items[:n]

def get_every_second(items):
    """
    返回列表中索引为 0, 2, 4... 的元素。
    """
    return items[::2]


get_first_n([10,20,30,40], 2)	
get_first_n([10,20], 5)	
get_first_n([10,20], 0)	
get_every_second([1,2,3,4,5])	
get_every_second([])