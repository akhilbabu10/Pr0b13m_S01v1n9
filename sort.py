print(‘enter values in a single line separated by spaces:’)
a= list(map(int, input().split()))
for i in range(len(a)):
#starting nested loop from 1 index ahead of i
    for j in range(i + 1, len(a)):
    # checking if current element is greater than elements ahead of it 
       if a[i] >= a[j]:
          # if current element is greater, current element as element at position j are exchanged
          a[i], a[j] = a[j], a[i]
print (a)