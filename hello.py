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

'''
read a file funtion
'''

def OpenFile(filename):
    f = open(filename, 'rU')#r stands for read, U gets read of unix file endings
    for filew in  f:
        print filew,
    
    filew1 = f.readlines()
    print filew1
    
    txt = f.read()
    print txt
    
    f.close()

def tri_recursion(k):
    if (k > 0):
        result = k+tri_recursion(k-1)
        print result
    else:
        print "oopsy!!!"
        result = 0
    return result

def main():
    #print repeat("whoop whoop", True)
    #print repeat("whoop whoop", False)
    #testin()
    #listmethods()
    #OpenFile(sys.argv[1])
    tri_recursion(0)

if __name__ == '__main__':
    main()
