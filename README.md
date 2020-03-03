# Face and eye identification with Viola-Jones algorithm

Bu projemizde Viola-Jones algoritmasını kullanarak ressimlerde, videoda, kamera erişimi ile yüz ve göz tespiti yapacağız.

aşamalar:

1-) Eğitim

2-) Tanıma 

Biz bu uygulamada tanıma kısmını yapacağız.

* En iyi performans yüz kameraya dönükken olur.
* İşlemlerden geçirmeden önce resmi veya videoyu siyah beyaz yaparız.
* Sol üst kısımdan aramaya başlar ve kareyi sağa doğru ilerletir.

![Screenshot_2020-03-03_19-00-12](https://user-images.githubusercontent.com/54184905/75805520-0c877100-5d93-11ea-8fd7-6fc31953c503.png)

![Screenshot_2020-03-03_19-02-40](https://user-images.githubusercontent.com/54184905/75805818-8f103080-5d93-11ea-8258-116f36031bfb.png)


# HAAR - LİKE Özellikler

![Screenshot_2020-03-03_19-06-42](https://user-images.githubusercontent.com/54184905/75805935-ced71800-5d93-11ea-95aa-692151a54f73.png)

![Screenshot_2020-03-03_19-10-00](https://user-images.githubusercontent.com/54184905/75806137-28d7dd80-5d94-11ea-9160-b493ae18b136.png)


* Aydınlık ve karanlık bölgelerin ayrı ayrı ortalamaları alınır.
* Karanlık - aydınlık = ideal olarak 1 e yaklaşmalı

![Screenshot_2020-03-03_19-11-17](https://user-images.githubusercontent.com/54184905/75806204-4c9b2380-5d94-11ea-822a-d762f64f126f.png)

# İntegral resmi

Pixelleri toplarken hız kazanmak ve minimum güç harcamak amaçlı kullandığımız yöntem.

![Screenshot_2020-03-03_19-23-54](https://user-images.githubusercontent.com/54184905/75806504-d6e38780-5d94-11ea-9304-b0eebd32a3e8.png)

Bu örnekte 12 kareyi toplayıp işlem yapacağımıza 4 işlem ile alanı toplayabildik.

# Eğitim

Projemizde opencv2 Cascade lerini kullandık (hazır eğitilmiş veriler)

* Resim 24x24 boyutuna küçültülür
* Resimde Haar - Like özellik aranır.
* Bol veri ile beslenmiş algoritma daha iyi çalışır.
veya data augmentation ile yeni veriler üretebilirsiniz.(veri arttırma, veri setinden sentetik veriler üretiriz.)
* Berilerin içersine yüz olmayan verilerde eklenir böylece her ihtimale karşı algoritmamımızı hazırlarız.
* Büyük resimler algoritmayı yavaşlatır.

![Screenshot_2020-03-03_19-27-46](https://user-images.githubusercontent.com/54184905/75807095-dc8d9d00-5d95-11ea-8f87-798ef8b2748b.png)

# Adaptive Boosting (Adaboost)

24x24 ressimde Haar - Like özelliklerin olma ihtimali +18.000 den fazladır. Bu kadar ihtimali hesaplamak bizi yavaşlatır
bunun için Adaboost yöntemini kullanacağız.



