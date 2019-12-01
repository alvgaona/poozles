# Print matrix column based on colum number

def print_column_with_for(matrix, column_number):
  for i in range(0,len(matrix)):
    print(a[i][column_number])
  print("Termino for")

def print_column_with_while(matrix, column_number):
  i = 0
  while(i < len(matrix)):    
    print(a[i][column_number])
    i = i + 1

a = [[1,2,3],[4,5,6]]

print_column_with_for(a,2)
print_column_with_while(a,2)
