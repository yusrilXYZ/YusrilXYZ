string = "hello word"
print (string)
# Deklarasi string
my_string = "Hello, world!"

# Mengakses karakter dalam string
print(my_string[0])  # Output: H
print(my_string[7])  # Output: ,

# Mengiris string
print(my_string[7:12])  # Output: , wor
print(my_string[:5])  # Output: Hello
print(my_string[6:])  # Output: world!

# Menggabungkan string
string1 = "Hello"
string2 = "World"
combined_string = string1 + " " + string2
print(combined_string)  # Output: Hello World

# Mengulangi string
print(string1 * 3)  # Output: HelloHelloHello

# Memeriksa panjang string
print(len(my_string))  # Output: 13

# Mengubah kasus string
print(my_string.upper())  # Output: HELLO, WORLD!
print(my_string.lower())  # Output: hello, world!

# Memeriksa keberadaan substring
print("world" in my_string)  # Output: True
print("Python" in my_string)  # Output: False

# Mengganti substring
new_string = my_string.replace("world", "Python")
print(new_string)  # Output: Hello, Python!

# Memisahkan string
words = my_string.split(",")
print(words)  # Output: ['Hello', ' world!']

# Menggabungkan string dengan pemisah
joined_string = "-".join(words)
print(joined_string)  # Output: Hello- world!
