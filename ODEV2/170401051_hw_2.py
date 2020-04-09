import sys,csv

my_list=[]
with open(sys.argv[1]+'input_hw_2.csv','r') as csv_file:
    for line in csv_file:
        my_list.append(int(line.split(";")[3].split("-")[1]))
print(my_list)

#listeyi bubble sort ile siralayip histograma atacagiz
def bubble_sort(my_list):
    n=len(my_list)
    #print(my_list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(my_list[j]<my_list[j+1]):
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp

    return my_list

sirali_list=bubble_sort(my_list)
#print(sirali_list)

#histogram listeyi alsin
def frequency_with_list_of_tuples(list_1):
    frequency_list=[]
    for i in range(len(list_1)):
        s=False
        for j in range(len(frequency_list)):
            if(list_1[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
            frequency_list.append([list_1[i],1])
    return frequency_list
hist_bilgi=frequency_with_list_of_tuples(sirali_list)

print(hist_bilgi)

#ayrilma bilgileri 1-12 sirali halde 
#dizinin her bolumunun 1.indislerini toplayalım
def medyan_bul():
    medyan_list=[]

    for i in range(0,len(hist_bilgi)):
        medyan_list.append(hist_bilgi[i][1])

    medyan_list.sort()
    #print(medyan_list)
    n = len(medyan_list)
    if n % 2 == 1:
        middle = int(n / 2) + 1
        median = medyan_list[middle - 1]

    else:
        middle_1 = int(n / 2) - 1
        middle_2 = middle_1 + 1
        median = (medyan_list[middle_1] + medyan_list[middle_2]) / 2

    return median

def art_ort():

    toplam = 0
    for i in range(0,len(hist_bilgi)):
        toplam+=hist_bilgi[i][1]     
    arit_ort = toplam / len(hist_bilgi)

    return arit_ort

print('aritmetik ort.', art_ort())
print('medyan',medyan_bulma())

dosya = open(sys.argv[2]+'180401049_hw_2_output.txt', 'w')
dosya.write("aritmetik ortalama=")
dosya.write(str(art_ort()))
dosya.write("\n")
dosya.write("medyan=")
dosya.write(str(medyan_bul()))
dosya.close()
