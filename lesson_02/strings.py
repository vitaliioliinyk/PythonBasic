# Лапки
s1 = "string"
s2 = 'string'
s3 = '2'
s4 = "string with 'single quotes'"
s5 = 'string with "double quotes"'
s6 = '''Three single quotes'''
s7 = """Three 
double quotes"""
print(s1, s2, s3, s4, s5)

# Конкатенація
concatenate = s3 + '3'
print(concatenate) # => 23
# concatenate = s3 + 3 # TypeError: can only concatenate str (not "int") to str

# Форматування
s = f"s3 value is {s3}"
print(s)
s = "s3 value is {}".format(s3)
print(s)

# Управляючі послідовності основні
#   \n
print("Hello\nWorld!")
#   \t
print("Hello World! Hello\tWorld!")
#   \\
print("Backslash symbol \\")
#   \'
print('Single \'quotes\'')

# Методи рядків
s = "Hello World!"
replace = s.replace("World!", "Python!")
print(replace)

s = "hello World!"
print(s.upper(), s.lower(), s.capitalize())

print("Count 'o': ", s.count('o'))

s_lenght = len(s)
print(f"Length of {s} is {s_lenght}")

# Індекси та зрізи
s = "Hello World!"
print("First symbol -", s[0])
print("Last symbol -", s[-1])
print("First 2 symbols -", s[0:3])
print("Entile string -", s[0:len(s)])
print("Symbols with step 2 -", s[0:12:2])
print("Symbols with step 3 -", s[0:12:3])
print("String reverse -", s[::-1])
