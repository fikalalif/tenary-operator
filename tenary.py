# tenary operator
x = 4 
hasil = 'besar' if x > 5 else 'kecil'
print (hasil)

# operator logika
p = True
q = False

#Logika AND
print ("p AND q : ",p and q )
#OR 
print ("p OR q : ",p or q )
#NOT
print ("NOT p : ", not p)

bayar = True
absensi = 60

if bayar == True or absensi >= 70:
    print('boleh ujian')
else:
    print('tidak boleh ujian')

# operator is
x = 5 
y = 5
print (x is y)

a = [1,2,3]
b = [1,2,3]
print (a is b)

#operator keanggotaan
number = [1,2,3,4,5]
print (3 in number)
print (3 not in number)