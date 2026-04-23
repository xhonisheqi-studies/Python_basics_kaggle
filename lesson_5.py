planaets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]

for planet in planaets:
    print(planet, end=' ') # end=' ' print all in the same lines

print("\n")

multiplicands = (1,2,3,4,5,6,7,8,9)
product = 1

for mult in multiplicands:
    product = product * mult
print(product)


a = 'come va la vita se conosci tutto quello che ti serve per essere felice e non pensarci'
msg = []

for char in a: 
    if char == 'a':
       msg.append(char)

print(len(msg)) 

for i in range(5):
    print("Doing important work. Task = " ,i)



i = 0

while i < 10:
    print(i, end= ' ')
    i+=1

print('\n')


# list comprehension

squares = [n ** 2 for n in range(10)]
print(squares)

short_planets = [planet for planet in planaets if len(planet) < 6]
print(short_planets)