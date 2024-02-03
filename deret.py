#membuat deret bilangan
#1,2,4,7,14,18
#u1 = 1, u2 = 2

list_seq =[1,2]
a = 1
j = 2
n = int(input('Tampilkan deret suku ke - = '))
for i in range (0,n):
    if a % 2 != 0:
        elemen = 2* list_seq[a]
        a += 1
    else:
        elemen = list_seq[a] + j
        a +=1
        j +=1
    list_seq.append(elemen)
print(list_seq)
print(f'Sum of the element in the list = {sum(list_seq)}')

#membuat deret bilangan yang satu maju yg satu dibagi
#3,5,4,8,6,14,11
#menampilkan deret angka, dimana suku ganjil memberikan +2 dgn
#---- u = 2 , memenuhi rumus j = j * 2
#
list_set = [3,5]
a = 1
j = 2
c = 1
n = int(input('Masukkan suku yang ingin diketahui '))
for i in range(0,n):
    if a % 2 == 0:
        elemen = list_set[a] + j * 2
        a += 1
        j *= 2
    else:
        elemen = list_set[a] - c
        a += 1
        c += 1
    list_set.append(elemen)
print(list_set)
#gimana cara ngejumlahin list di python?
print(f'Sum of the element in the second list is ={sum(list_set)}')
#gimana kalo deret pascal, taylor dan deret yang lain 
