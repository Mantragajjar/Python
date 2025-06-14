intro = "My name is Mantra"
#index   0123456789.... position
print(intro[5])#this will print character at 5th index position from left side
print(intro[8])#this will print character at 8th index position from left side
print(intro[-2])#this will print character at 2nd index position from right side (2nd last position)
print(intro[0:5])#this will print character from 0 to 4nd index position from left side

another = intro[:]#this will assign whole string intro value to another
print(another)#this will print whole string another

name = "Charlie"
print(name[1:-1])#this will print character from 2nd position from left side to 2nd last position from the right side
# well the noticing part is that the index position of e is -1 but the characters will be printed until i , e will not be printed