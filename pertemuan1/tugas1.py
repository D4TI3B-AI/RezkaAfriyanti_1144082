import time
start_time = time.time()
print("menghitung nilai rumus matematika menggunakan bahasa padang")
r = raw_input("Masukan Nilai 1: ")
e = raw_input("Masukan Nilai 2: ")
s = raw_input("Masukan Nilai 3: ")
k = raw_input("Masukan Nilai 4: ")
a = raw_input("Masukan Nilai 5: ")

if r == 'cie':
	r=1

if r == 'duo':
	r=2

if r == 'tigo':
	r=3

if r == 'ampe':
	r=4

if r == 'limo':
	r=5

if r == 'anam':
	r=6

if r == 'tujuh':
	r=7

if r == 'delapan':
	r=8

if r == 'sambilan':
	r=9

if r == 'nol':
	r=0


if e == 'cie':
	e=1

if e == 'duo':
	e=2

if e == 'tigo':
	e=3

if e == 'ampe':
	e=4

if e == 'limo':
	e=5

if e == 'anam':
	e=6

if e == 'tujuh':
	e=7

if e == 'delapan':
	e=8

if e == 'sambilan':
	e=9

if e == 'nol':
	e=0

if s == 'cie':
	s=1

if s == 'duo':
	s=2

if s == 'tigo':
	s=3

if s == 'ampe':
	s=4

if s == 'limo':
	s=5

if s == 'anam':
	s=6

if s == 'tujuh':
	s=7

if s == 'delapan':
	s=8

if s == 'sambilan':
	s=9

if s == 'nol':
	s=0


if k == 'cie':
	k=1

if k == 'duo':
	k=2

if k == 'tigo':
	k=3

if k == 'ampe':
	k=4

if k == 'limo':
	k=5

if k == 'anam':
	k=6

if k == 'tujuh':
	k=7

if k == 'delapan':
	k=8

if k == 'sambilan':
	k=9

if k == 'nol':
	k=0


if a == 'cie':
	a=1

if a == 'duo':
	a=2

if a == 'tigo':
	a=3

if a == 'ampe':
	a=4

if a == 'limo':
	a=5

if a == 'anam':
	a=6

if a == 'tujuh':
	a=7

if a == 'delapan':
	a=8

if a == 'sambilan':
	a=9

if a == 'nol':
	a=0


jumlah =(r*e)+(s/k-a)
print ("hasil" , jumlah)
print("time : %s detik " % (time.time() - start_time))
