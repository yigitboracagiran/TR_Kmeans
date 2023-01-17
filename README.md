# TR_Kmeans
Not: Excel dosyası ile Python kodunun aynı dizinde olması gerekmektedir.

1- Veri seti okunarak Data Frame’e başarıyla aktarılmıştır.

2- Veriler, %30-%70 oranında olacak şekilde test ve eğitim verisine bölünmüştür.

3- Kategorik veriler, sayısal verilere dönüştürülmüştür.

4- Nan değerlere sahip satırlar silinmiştir.

5- Yapılan araştırmalar sonucunda listede işlemlerin daha hızlı yapılabileceği öğrenilmiştir. Bu nedenle
Data Frame’lerde tutulan test ve eğitim verileri listeye dönüştürülmüştür.

6- Kolaylık olması ve algoritmanın ilerleyişini daha rahat takip edebilmek için öncelikle rastgele 10
veri ile çalışılmıştır.

7- Eğitim verileri kümelerine göre ayrılmıştır ve bu indeksler listelerde tutulmuştur.

8- Verilerin birinci, ortasındaki ve sonuncuları başlangıçta belirlenen 3 küme merkezi seçilmiştir.

9- Öncelikle küme merkezleri değişmeyene kadar eğitim verileri ile model eğitilmiştir. Bunu yaparken
yeni küme merkezleri, belli kümeye ait verilerin ortalamaları ile hesaplanmıştır.

10- Ardından test verilerinin kümeleri tahmin edilmeye çalışılmıştır.

11- Küme merkezlerine uzaklıklar arasında en yakını seçilmiştir ve tahmin edilen küme bulunmuştur.

12- Tahmin edilen küme ile, test verisinin gerçek kümesi karşılaştırılmış, doğru veya yanlış tahmin
olarak kullanıcıya döndürülmüştür.

13- Tahminlerin yapılırken karmaşıklık matrisinin hesaplanması sağlanmıştır.

14- Karmaşıklık matrisinin indekslerindeki verileri kullanarak True Positive, True Negative, False
Positive ve False Negative değerleri hesaplanmıştır.

15- True Positive, True Negative, False Positive ve False Negative değerleri ile Doğruluk (Accuracy),
Kesinlik (Precision), Hassasiyet (Recall) ve F Score hesaplanmış ve ekrana yazdırılmıştır.

16- Algortimanın tamamlanması üzerine tüm veriler üzerinde hazırlanan algoritma
denenmiştir.

17- Yapılan eğitimin sonunda elde edilen doğruluk her nitelik için sırasıyla: %53.46534653465347,
%59.4059405940594 ve %18.811881188118812 olmuştur.

18- Test ve eğitim verisine ayrılırken random_state’in değiştirilmesi ile birçok farklı sonuç
elde edilmiştir. Aralarındaki en iyi sonuç ise yukarıda verilen sonuç olmuştur.
