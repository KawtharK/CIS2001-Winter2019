def countdown(number):
    if number <= 0:
        print(number)
    else:
        print(number)
        countdown(number-1)

#countdown(10)




#pretend we can't do this
#if 42 in numbers:

def _binary_search(sorted_collection, item_to_find, low_index, high_index):
    if low_index > high_index:
        return False

    mid = (low_index + high_index ) // 2
    if item_to_find == sorted_collection[mid]:
        return True
    elif item_to_find < sorted_collection[mid]:
        return _binary_search(sorted_collection,
                              item_to_find,
                              low_index,
                              mid-1)
    else:
        return _binary_search(sorted_collection,
                              item_to_find,
                              mid+1,
                              high_index)

def binary_search(sorted_collection, item_to_find):
    return _binary_search(sorted_collection,
                          item_to_find,
                          0,
                          len(sorted_collection)-1 )

def binary_search_iterative(sorted_collection, item_to_find):
    low_index = 0
    high_index = len(sorted_collection) - 1

    while( low_index <= high_index ):
        mid = ( low_index + high_index ) // 2
        if item_to_find == sorted_collection[mid]:
            return True
        elif item_to_find < sorted_collection[mid]:
            high_index = mid - 1
        else:
            low_index = mid + 1

    return False


def bad_fib(nth):
    if nth == 1 or nth == 2:
        return 1
    else:
        return bad_fib(nth-1) + bad_fib(nth-2)


def _better_fib(nth, current_nth, current, previous):
    if nth == current_nth:
        return current + previous
    else:
        return _better_fib(nth, current_nth+1, current + previous, current)

def better_fib(nth):
    if nth == 1 or nth == 2:
        return 1
    else:
        return _better_fib(nth, 3, 1, 1)


for nth in range(1,41):
    print(better_fib(nth))


