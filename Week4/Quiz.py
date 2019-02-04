def _reverse(some_list, start, end):
    if start > end:
        return
    else:
        temp = some_list[start]
        some_list[start] = some_list[end]
        some_list[end] = temp
        _reverse(some_list, start+1, end-1)

def reverse(some_list):
    _reverse(some_list, 0, len(some_list)-1)


name = ['E', 'r', 'i', 'c']

print(name)
reverse(name)
print(name)