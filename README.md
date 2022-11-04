# ihaKiralamaPlatformu

Bu proje BAYKAR Teknoloji'nin Vaka Çalışması için hazırlanmıştır.

Öncelikle Postgresql kullanarak lokal makinenizde 'ihaKiralamaDB' isimli bir veritabanı oluşturmanız gerekmektedir. Projede, veritabanı kullanıcı adı default olarak 'postgres' olarak belirlenmiştir. Eğer postgres dışında başka bir kullanıcı olarak bağlanmak istiyorsanız o kullanıcıyı tanımlamalı daha sonra da kullanıcı şifrenizi ve adınızı ihaKiralamaPlatformu/ihaKiralamaPlatformu/settings.py ve docker-compose.yml dosyalarında değiştirmelisiniz. Tüm bunlar gerçekleştirildikten sonra proje docker'dan çalıştırılmaya hazır hale gelecektir.

Projeyi Docker ile çalıştırmak için:

```
docker-compose build
```
ve ardından
```
docker-compose run 
```
komutlarını kullanabilirsiniz.

Eğer build ile ilgili bir sıkıntı yaşarsanız:
```
docker-compose -f docker-compose.yml up --build -d
```
komutuyla container'ı baştan build etmeyi deneyin.
