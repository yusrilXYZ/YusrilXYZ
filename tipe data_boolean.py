data_boolean = "true atau false"
print (data_boolean)

# Deklarasi variabel boolean
is_true = True
is_false = False

# Mencetak nilai boolean
print(is_true)  # Output: True
print(is_false)  # Output: False

# Operasi logika
print(is_true and is_false)  # Output: False
print(is_true or is_false)  # Output: True
print(not is_true)  # Output: False

# Perbandingan
a = 10
b = 5

print(a > b)  # Output: True
print(a < b)  # Output: False
print(a == b)  # Output: False
print(a != b)  # Output: True

# Kondisi if-else
if a > b:
  print("a lebih besar dari b")
else:
  print("a tidak lebih besar dari b")  # Output: a lebih besar dari b

# Menggunakan boolean dalam fungsi
def is_even(number):
  return number % 2 == 0

print(is_even(4))  # Output: True
print(is_even(5))  # Output: False
