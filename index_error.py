#INDEX ERROR
import sys

a = "abcde"
n = input()
print(a[n])  #BUG, IndexError
print(a[-7]) #BUG, IndexError

print(sys.argv[0])
print(sys.argv[1]) #BUG, IndexError

a_list = ['a', 'b', 'mpilgrim', 'z', 'example']
print(a_list[-6])  #BUG, IndexError
print(a_list[-3])

a_list.append(['c','d','e'])
print(a_list[5][3])  #BUG, IndexError , two dimensional

a_list.pop(-1)  #BUG, IndexError
