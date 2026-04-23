primes = [2,3,5,7]
panaets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]

# list of list

hands_bj = [
    ['J','A'],
    ['5','6','K'],
    ['9','6','K']
]

# you could write a list of list also in a single line by separeting with a coma
# list could contain a mix of data types

list_of_mixed_data_types = ["my_var",primes,hands_bj,45]
print(list_of_mixed_data_types)

# you can access list position by using the index, can go also - backwords and also with 0:3 ranges
print(panaets[2])
print(panaets[:3])
print(panaets[0:3])
print(panaets[3:])
print(panaets[1:-1])

# by accessing the index you can also change the list content 
list_of_mixed_data_types[-1] = 69

# to know the lenght of list
print(len(panaets))

# and you can also sort a list
print(sorted(panaets))

# to make a complex number you can use 'j'
a = 12 + 3j
print(a.imag) # imag is the immaginary part of complex numbers 

# you could also print the bit of the variable
#print(a.bit_length())


# list methods 

# append to the list
primes.append(13)
# pop --> the last element of a list
primes.pop()


# to get the index in a list

print(panaets.index("Earth"))


# use the in interrogation 

print('Earth' in panaets)

# tuples -- differentrly from list are immutable
example_of_a_tupla = (1,2,3)
# you cannot access it like this ...[] cuz is immutable and values cannot change

# method of float

x = 0.258
print(x.as_integer_ratio()) # return a tupla with numerator and a denominator 


   
