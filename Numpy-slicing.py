import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]
                  ])
print('print the matrix in reverse order ',array[::-1])# form  to
print('print the matrix with skipping every 2 rows ',array[::2])
#array[stars:end:step]
print('print the first two rows',array[:2])
print(array[0,])
# :2 print from to -take first two rows-
# ::2 print 0 2 4
print(array[:,0])#print every index at 0
print("momo",array[:,1:3])#from  1 to 3
print("loly",array[:,::-2])#reverse-starts from the ends - with every second columns-from to-
print('joy',array[0:2,0:2])# rows from 0 to 2 ,  columns form 0 to 2
#print the rows from to , print the colums form to
print("i did it!",array[2:,0:2])# from row 2 to the end row , from column to column
# last two rows , first two columns
