import pandas #DataFrame icin...
import numpy #Kucukten buyuge yazdirmak icin...
from sklearn.model_selection import train_test_split #test ve egitim verilerini ayirmak icin...
import statistics #ortalama almak icin...
from tabulate import tabulate #karmasiklik matrisini yazdirmak icin...

def Hesaplama(x):
    kumeMerkezi1, kumeMerkezi2, kumeMerkezi3
    sonuc1=0
    sonuc2=0
    sonuc3=0
    for i in range(6): #6 nitelik icin 3 kume merkezine uzaklik...
        sonuc1+=(x[i]-kumeMerkezi1[i])**2
        sonuc2+=(x[i]-kumeMerkezi2[i])**2
        sonuc3+=(x[i]-kumeMerkezi3[i])**2
    return((sonuc1**0.5), (sonuc2**0.5), (sonuc3**0.5))

csvVerileri=pandas.read_csv('penguins_size.csv') #Excel dosyasi okunuyor.

csvVerileri=csvVerileri.dropna(axis=0) #Null degerler atiliyor.

csvVerileri['species'].replace(['Adelie', 'Chinstrap', 'Gentoo'], [1, 2, 3], inplace=True) #kategorik degiskenler, sayisal yapiliyor.
csvVerileri['island'].replace(['Torgersen', 'Biscoe', 'Dream'], [1, 2, 3], inplace=True)
csvVerileri['sex'].replace(['MALE', 'FEMALE', '.'], [1, 2, 3], inplace=True)

y=csvVerileri["species"] #y olusturuluyor.
x=csvVerileri.drop(columns="species") #y sutunu siliniyor ve x olusturuluyor.

(xEgitimVerisi, xTestVerisi, yEgitimVerisi, yTestVerisi)=train_test_split(x, y, random_state=0, test_size=0.3) #Test ve egitim verileri ayriliyor.

yEgitimVerisiListesi=yEgitimVerisi.tolist() #Test ve egitim verileri daha hizli islem yapilmasi icin liste formuna donusturuluyor.
yTestVerisiListesi=yTestVerisi.tolist()
xEgitimVerisiListesi=xEgitimVerisi.values.tolist()
xTestVerisiListesi=xTestVerisi.values.tolist()

kumeMerkezi1=xEgitimVerisiListesi[0] #Baslangicta 3 tane rastgele kume merkezi seciyoruz.
kumeMerkezi2=xEgitimVerisiListesi[int(len(xEgitimVerisiListesi)/2)]
kumeMerkezi3=xEgitimVerisiListesi[len(xEgitimVerisiListesi)-1]

kumeMerkezi1Indeksler=[]
kumeMerkezi2Indeksler=[]
kumeMerkezi3Indeksler=[]

dict={0: 1, 1: 2, 2: 3}
while(1): #Kume merkezleri degismeyene kadar sonsuz dongu...
    for i in range(len(xEgitimVerisiListesi)):
        sayi=Hesaplama(xEgitimVerisiListesi[i])
        indeksler=numpy.argsort(sayi) #Kucukten buyuge siralandiginda hangi indekse hangi indeskteki sayilarin donecegi bulunuyor.
        tahminEdilenKume=dict[indeksler[0]] #En yakin kume merkezi bulunuyor.
        yEgitimVerisiListesi[i]=dict[indeksler[0]]
        if yEgitimVerisiListesi[i]==1: #Kumelerin elemanlarinin indekslerini tutuyor.
            kumeMerkezi1Indeksler.append(i)
        elif yEgitimVerisiListesi[i]==2:
            kumeMerkezi2Indeksler.append(i)
        elif yEgitimVerisiListesi[i]==3:
            kumeMerkezi3Indeksler.append(i)
    yeniKumeMerkezi1=[]
    yeniKumeMerkezi2=[]
    yeniKumeMerkezi3=[]
    for j in range(6):
        yeniKumeMerkezi1.append((statistics.mean([xEgitimVerisiListesi[i][j] for i in kumeMerkezi1Indeksler]))) #Niteliklerin aritmatik ortalamalari k=1 icin
        yeniKumeMerkezi2.append((statistics.mean([xEgitimVerisiListesi[i][j] for i in kumeMerkezi2Indeksler]))) #k=2 icin
        yeniKumeMerkezi3.append((statistics.mean([xEgitimVerisiListesi[i][j] for i in kumeMerkezi3Indeksler]))) #k=3 icin
    if(kumeMerkezi1!=yeniKumeMerkezi1) or (kumeMerkezi2!=yeniKumeMerkezi2) or (kumeMerkezi3!=yeniKumeMerkezi3): #Kume merkezi degistiyse...
        print("Kume Merkezleri Degisti!")
        kumeMerkezi1=yeniKumeMerkezi1
        kumeMerkezi2=yeniKumeMerkezi2
        kumeMerkezi3=yeniKumeMerkezi3
        kumeMerkezi1Indeksler=[]
        kumeMerkezi2Indeksler=[]
        kumeMerkezi3Indeksler=[]
    else:
        print("Kume Merkezleri Degismedi!")
        break

karmasiklikMatrisi=[[1, 0, 0, 0], [2, 0, 0, 0], [3, 0, 0, 0]] #Karmasiklik Matrisimiz
def KarmasiklikMatrisi(sayi1, sayi2): #Karmasikilik Matrisini Guncelleme
    global karmasiklikMatrisi
    karmasiklikMatrisi[sayi1][sayi2]+=1

dogru=0 #dogru tahmin sayisi
yanlis=0 #yanlis tahmin sayisi
for i in range(len(xTestVerisiListesi)): #Test verilerini yukarida egitilen kume merkezleri ile deniyoruz.
    sayi=Hesaplama(xTestVerisiListesi[i])
    indeksler=numpy.argsort(sayi) #Kucukten buyuge siralandiginda hangi indekse hangi indeskteki sayilarin donecegi bulunuyor.
    tahminEdilenKume=dict[indeksler[0]]  #En yakin kume merkezi bulunuyor.
    if yTestVerisiListesi[i]==tahminEdilenKume:
        print("Kume dogru tahmin edildi! Tahmin Edilen Kume: ", tahminEdilenKume, "Gercek Kume: ", yTestVerisiListesi[i])
        KarmasiklikMatrisi(tahminEdilenKume-1, tahminEdilenKume)
        dogru+=1
    else:
        print("Kume yanlis tahmin edildi! Tahmin edilen Kume: ", tahminEdilenKume, "Gercek Kume: ", yTestVerisiListesi[i])
        KarmasiklikMatrisi(tahminEdilenKume-1, yTestVerisiListesi[i])
        yanlis+=1
    print("Dogru: ", dogru, "Yanlis: ", yanlis)

print("Karmasiklik Matrisi")
sutunBasliklari=["Kume", "1", "2", "3"]
print(tabulate(karmasiklikMatrisi, sutunBasliklari)) #Karmasiklik Matrisi Yazdiriliyor.

birTP=karmasiklikMatrisi[0][1] #TP, TN, FN ve FP degerleri her nitelik icin hesaplaniyor.
birTN=karmasiklikMatrisi[1][2]+karmasiklikMatrisi[1][3]+karmasiklikMatrisi[2][2]+karmasiklikMatrisi[2][3]
birFN=karmasiklikMatrisi[0][2]+karmasiklikMatrisi[0][3]
birFP=karmasiklikMatrisi[1][1]+karmasiklikMatrisi[2][1]

ikiTP=karmasiklikMatrisi[1][2]
ikiTN=karmasiklikMatrisi[0][1]+karmasiklikMatrisi[0][3]+karmasiklikMatrisi[2][1]+karmasiklikMatrisi[2][3]
ikiFN=karmasiklikMatrisi[1][1]+karmasiklikMatrisi[1][3]
ikiFP=karmasiklikMatrisi[0][2]+karmasiklikMatrisi[2][2]

ucTP=karmasiklikMatrisi[2][3]
ucTN=karmasiklikMatrisi[0][1]+karmasiklikMatrisi[0][2]+karmasiklikMatrisi[1][1]+karmasiklikMatrisi[1][2]
ucFN=karmasiklikMatrisi[2][1]+karmasiklikMatrisi[2][2]
ucFP=karmasiklikMatrisi[0][3]+karmasiklikMatrisi[1][3]

birDogruluk=(birTP+birTN)/(birTP+birFN+birFP+birTN) #Dogruluk, Kesinlik, Duyarlilik ve F1-Score degerleri 3 nitelik icin de hesaplaniyor ve yazdiriliyor.
birKesinlik=birTP/(birTP+birFP)
birDuyarlilik=birTP/(birTP+birFN)
if (birKesinlik+birDuyarlilik)!=0:
    birFScore=2*((birKesinlik*birDuyarlilik)/(birKesinlik+birDuyarlilik))
else:
    birFScore="tanimsiz"
ikiDogruluk=(ikiTP+ikiTN)/(ikiTP+ikiFN+ikiFP+ikiTN)
ikiKesinlik=ikiTP/(ikiTP+ikiFP)
ikiDuyarlilik=ikiTP/(ikiTP+ikiFN)
if (ikiKesinlik+ikiDuyarlilik)!=0:
    ikiFScore=2*((ikiKesinlik*ikiDuyarlilik)/(ikiKesinlik+ikiDuyarlilik))
else:
    ikiFScore="tanimsiz"
ucDogruluk=(ucTP+ucTN)/(ucTP+ucFN+ucFP+ucTN)
ucKesinlik=ucTP/(ucTP+ucFP)
ucDuyarlilik=ucTP/(ucTP+ucFN)
if (ucKesinlik+ucDuyarlilik)!=0:
    ucFScore=2*((ucKesinlik*ucDuyarlilik)/(ucKesinlik+ucDuyarlilik))
else:
    ucFScore="tanimsiz"

print("Dogruluk: ", birDogruluk, "Kesinlik: ", birKesinlik, "Duyarlilik:", birDuyarlilik, "F1 Score:", birFScore)
print("Dogruluk: ", ikiDogruluk, "Kesinlik: ", ikiKesinlik, "Duyarlilik:", ikiDuyarlilik, "F1 Score:", ikiFScore)
print("Dogruluk: ", ucDogruluk, "Kesinlik: ", ucKesinlik, "Duyarlilik:", ucDuyarlilik, "F1 Score:", ucFScore)