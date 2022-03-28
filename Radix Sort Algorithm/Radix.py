#çalışma zamanlarını hesaplamak için time kütüphanesini ekliyorum

from datetime import datetime

#Bucket Sort yerine Counting Sort ile yapıyorum.
def countingSort(array, place):

    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        array[i]=int(array[i])
        index = array[i] // place
        count[index % 10] += 1
        

    for i in range(1, 10):
        count[i] += count[i - 1]
        
    # liste içersindeki elemanları sıralıyorum
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
    #sıralanmış diziyi başka bir diziye aktarıyorum
    for i in range(0, size):
        array[i] = output[i]
        
        

#float değerleri sıralamaya almak için , sonrası ifadeleri kaldırmak için önce çarpıp sonra bölüyorum.     
def convert(array):
    size=len(array)
    for i in range(0,size):
        array[i]=float(array[i])
        array[i]=array[i]/10000

def radixSort(array):
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10

dizi=[]
#kodun olduğu dosyadan dosya yolu belirtmeden okunacak dosyayı açıyorum    
liste=open("10lukliste.txt")
for i in range(0,10):
    veri=float(liste.readline())
    #float değerleri değiştirmek için çarpıyorum
    veri=veri*10000
    veri=int(veri)
    dizi.append(veri)
start=datetime.now()
radixSort(dizi)
print("Sıralı onluk dizi")
convert(dizi)
print(dizi)
stop=datetime.now()
time=stop-start
print("Onluk Dizi Çalışma Zamanı :" ,time) 
liste.close()
liste_1=open("100lukliste.txt")
for i in range(0,100):
    veri=liste_1.readline()
    veri=float(veri)
    veri=veri*10000
    veri=int(veri)
    dizi.append(veri)
start=datetime.now()
radixSort(dizi)
print("Sıralı yüzlük dizi")
convert(dizi)
print(dizi)
stop=datetime.now()
time=stop-start
print("Yüzlük Dizi Çalışma Zamanı :" ,time)    
liste_1.close()
liste_2=open("100000likliste.txt")
for i in range(0,100000):
    veri=liste_2.readline()
    veri=float(veri)
    veri=veri*10000
    veri=int(veri)
    dizi.append(veri)
start=datetime.now()
radixSort(dizi)
print("Sıralı yüzbinlik dizi:")
convert(dizi)
print(dizi)
stop=datetime.now()
time=stop-start
#çalışma zamanlarını ekrana yazıyorum   
print("Yüzbinlik Dizi Çalışma Zamanı :" ,time)   
liste_2.close()
input()

