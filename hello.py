import sys

def repeat(s, exclaim):
    result = s + s + s

    if exclaim:
        result = result + "!!!"
    return result

def testin():
    squares = [ 1, 4, 9 , 16]
    summ = 0

    '''
    this function just prints out the sum of all the intergers in the list.
    the "in" value on its own is also an easy way to check if an element appear
    in a list

    '''

    #in is just an easy way to look at every elements in a list.
    for num in squares:
        summ += num
    print summ

    lis = ['Joe', 'Jackson', 'Bruno', 'Justin']

    if 'Joe' in lis:
        print "\n we found your name on the list sir\n"

    s = ['a', 'b', 'c', 'd', 'e', 'f']

    for ch in s:
        print ch
    '''
    rangen prints out the range, 0, 1,... n -1.
    therefore the range of a number a return a, upto a -1;
    ie range(100) return 0, 1, 2... 99.

    '''

    for i in range(100):
        print(i)
        
def listmethods():
    lst = ['joe','prince', 'joer', 'joel']
    #lst.append(elem) => adds elements to the end of the string
    lst.append('mkuu')
    #lst.insert(index, elem) => inserts elements at the given index shifting
    #elements to the right
    lst.insert(0, 'wohoo')
    print lst



def main():
    #print repeat("whoop whoop", True)
    #print repeat("whoop whoop", False)
    testin()
    listmethods()

if __name__ == '__main__':
    main()
