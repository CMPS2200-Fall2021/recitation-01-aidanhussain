"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
import datetime
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):


    mid = (int((right-left) / 2)) + left
    print(mid)
    if right < left:
        return -1
    if key == mylist[mid]:
        return key
    elif key < mylist[mid]:
        print("smaller")
        _binary_search(mylist, key, 0, mid)
    else:
        print("bigger")
        _binary_search(mylist, key, mid+1, len(mylist)-1)
        
    
    
    
	

def test_binary_search():
    assert binary_search([1,2,3,4,5], 5) == 4
    assert binary_search([1,2,3,4,5], 1) == 0
    assert binary_search([1,2,3,4,5], 6) == -1
    assert binary_search([1,2,3,4,5], 2) == 1
    assert binary_search([1,2,3,4,5], 3) == 2
    


def time_search(search_fn, mylist, key):
    
    start = datetime.datetime.now()
    
    search_fn(mylist, key)
    
    stop = datetime.datetime.now()
    
    time = (stop - start ) * 1000
    
    
    return time

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	
    results = []
    
    for size in sizes:
        lst = list(range(size))
        
        linear_time = time_search(linear_search, lst, -1)
        binary_time = time_search(binary_search, lst, -1)
        
        result = (size, linear_time, binary_time)
        results.append(result)
    return results
            



def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
		headers=['n', 'linear', 'binary'],
		floatfmt=".3f",
		tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1
    
    
print(binary_search([1,2,3],3))
