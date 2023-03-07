#boolean
a = True
b = False
print(a)
print(type(a))
print(b)
print(type(b))

#string
b = "Aku suka belajar bahasa pemrograman Python!"
print(b)
print(type(b))

#int
c = 55
print(c)
print(type(c))

#float
e = 3.14
f = -1.62
print(e)
print(f)
print(type(e))
print(type(f))

#hex
g = 1023
h = 255
print(hex(g))
print(hex(h))
print(type(g))
print(type(h))

#complex
i = 22j
print(i)
print(type(i))

#list
j = ["mobil", "motor", "kereta", "kapal"]
print(j)
print(j[1])
print(type(j))

#tuple
k = ("phi", 6.55, 7j)
print(k)
print(k[0])
print(type(k))

#dictionary
l = {"Mata kuliah" : "Praktikum Algoritma dan Pemrograman", "Kelas" : "D"}
print(l)
print(l["Mata kuliah"])
print(type(l))

#data type conversion
m = 10
n = 32
o = 89
print(type(m))
print(type(n))
print(type(o))
m_float = float(m)
n_str = str(n)
o_complex = complex(o)

print(m_float)
print(n_str)
print(o_complex)
print(type(m_float))
print(type(n_str))
print(type(o_complex))

#random
import random
i = random.random()
print(i)

#variabel
varbenar = "benar"
var_benar = "benar1"
_var_benar = "benar2"
varBenar = "Benar3"
VARBENAR = "benar4"
varbenar5 = "benar5"
print(varbenar)
print(var_benar)
print(_var_benar)
print(varBenar)
print(VARBENAR)
print(varbenar5)

#variabel global
r = "compiled language"

def myfunction():
    r = "interpreted language"
    print("Python adalah", r)
myfunction()
print("C adalah", r)

#keyword global
s = "mendengarkan musik"
def func():
    global s
    s = "membaca buku"
print("hobiku adalah", s)
func()
print("hobiku adalah", s)

#variabel ganda
t, u, v = "sawi", "bayam", "brokoli"

print("1.", t)
print("2.", u)
print("3.", v)

#operator aritmatika
w, x, y, z = 150, 25, 13, 7
#penjumlahan
print(w, "+", x, "=", w+x)
#pengurangan
print(y, "-", z, "=", y-z)
#perkalian
print(w, "*", z, "=", w*z)
#pembagian
print(w, "/", x, "=", w/x)
#modulus
print(x, "%", y, "=", x%y)
#perpangkatan
print(y, "^", 2, "=", y**2)
#pembagian bulat
print(w/z)
print("dibulatkan menjadi", w//z)

#operator perbandingan

#sama dengan
print(20 == 20)
#tidak sama dengan
print(34 != 34)
#lebih kecil dari
print(24 < 25)
#lebih besar dari
print(77 > 44)
#lebih kecil atau sama dengan
print(7<<5)
#lebih besar atau sama dengan
#print(19>=19)

#operator penugasan
z = 2
a = z #sama dengan
print(a)
b = 48
b += a #tambah sama dengan
print(b)
b -= 2 #kurang sama dengan
print(b)
b *= a #kali sama dengan
print(b)
b /= 8 #bagi sama dengan
print(b)
b %= 5 #sisa bagi sama dengan
print(b)
b **= 3 #pangkat sama dengan
print(b)
b //= 3 #pembagian bulat sama dengan
print(b)

#operator logika
bit, nibble, byte = 1, 4, 8
print("=======AND=======")
print(byte > nibble and nibble > bit)
print(nibble == byte and nibble == 4)
print(1 and 0)
print("=======OR=======")
print(byte < nibble or bit > byte)
print(nibble > bit or bit > nibble)
print(0 or 1)
print("=======NOT=======")
print(not(byte < nibble or bit > byte))
print(not(nibble > bit or bit > nibble))
print(not(0 or 1))

#operator bitwise
#XOR
a = 13
b = 0xF
print("bitwise operator XOR (^)")
print(format(a, "04b"))
print(format(b, "04b"))
print("--------XOR")
print(format(a ^ b, "04b"))
#>>
a = 13
b = 0xF
print("bitwise operator shifting right (>>)")
print(a, "\t=", format(a, "08b"))
a_shift_right = a >> 1
print(a_shift_right, "\t=", format(a_shift_right, "08b"))

#<<
a = 13
b = 0xF
print("bitwise operator shifting left (<<)")
print(a, "\t=", format(a, "08b"))
a_shift_left = a<< 1
print(a_shift_left, "\t=", format(a_shift_left, "08b")) 

#or
a = 13
b = 0xF
print("bitwise operator OR (|)")
print(format(a, "04b"))
print(format(b, "04b"))
print("--------OR")
print(format(a | b, "04b"))

#not
a = 5
b = 0xF
print("bitwise operator NOT (~)")
print(a, "\t=", format(a, "08b"))
a_not = ~a
print(a_not, "\t=", format(a_not, "08b"))

#and
a = 13
b = 0xF
print("bitwise operator AND (&)")
print(format(a, "04b"))
print(format(b, "04b"))
print("--------AND")
print(format(a & b, "04b"))

#membership
mobil = ["Volvo", "Hyundai", "Toyota"]
print("Volvo" in mobil)
print("Honda" in mobil)
print("Hyundai" not in mobil)
print("Mitsubishi" not in mobil)

#identity
x = "111"
y = "111"
z = "212"
w = x

print(x is y)
print(y is z)
print(x is not z)
print(w is x)




