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

