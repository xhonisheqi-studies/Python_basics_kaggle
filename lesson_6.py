x = 'Pluto is a planet'
y = 'Pluto is a planet'
planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
x == y

# like for all the lists , you can access prosition by using [index] and also with range index
# you can use len() like for the list
# and you can also loop over strings

# the list like tuples are immutable you cannot change by specifying an index

s1 = "Xhoni"
print(s1.upper())

s2 = "XHONI"
print(s2.lower())

# you can search for an index with s.index("value")

# you can check if it ends with a specific word

s3 = "Ciao come va"
print(s3.endswith("va"))

# you can use .split(delimeter) to split a string into a list

z = x.split(' ') #based on sapce that is the default 

# you can also produce multiples variable from a string with split

date_of_birth = '1990-01-01'
year,month,day = date_of_birth.split("-")


# join to a string

new_date_format = '/'.join([day,month,year])
print(new_date_format)

# you can concatenate string by using + operator

concat  = x + y
print(concat)

# if you to concat a number or any other data types you have to process with a data conversion
n = 10
concat = x + y + " " + str(n) + " ahahha ho vinto"
print(concat)

# dictionaries 

# key:value pair
numbers = {'one': 1,'two': 2,'three': 3}

# print based on the key
print(numbers['one'])
# you can also change it 
numbers['two'] = 4-6
# you can also add , by adding a new key:value pair 
numbers['four'] = 4


intial_planets = {planet : planet[0] for planet in planets}
print(intial_planets)

