text = 'veryz_large_word large_word'

# Indexing
print(text[0])
print(text[5])

print(text[-1])
print(text[-4])

# text slicing
# text[start: end: steps] --> here end is end-1

print(text[::]) # by default here start point is 0, end point is till last char and steps is 1
print(text[:]) # same for this by default here start point is 0, end point is till last char and steps is 1
print(text[::2]) # by default here start point is 0 and end point is till last char but steps is 2
print(text[5::1])
print(text[2:10:3])
print(text[2:4:2])