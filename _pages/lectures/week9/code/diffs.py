a = [0, 1, 2, 3, 4, 5, 6, 7, 7, 9, 10, 11, 12, 13, 14, 16, 15, 17, 18, 18]
b = list(range(20))


def listdiff(a, b):
    assert len(a) == len(b), "Lists are of different lengths."
    difflist = []
    for i in range(len(a)):
        if a[i] != b[i]:
            difflist.append(i)
    return difflist

x = [3, 4, 5]
y = [2, 4]
#difference = listdiff(x,y) this will throw an assertion error
difference = listdiff(a,b)
print(difference)