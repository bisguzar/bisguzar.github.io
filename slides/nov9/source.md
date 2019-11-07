name: inverse
layout: true
class: center, middle, inverse
---
name: last-page
template: inverse

# whoami
### Backend Developer @InfinitumIT
  
  
### @bugraisguzar
### github/bisguzar
### ben@bisguzar.com

???
**ben kimim?**

paramediğim, aynı zamanda infinitumIT şirketinde backend geliştirici olarak çalışıyorum. şu sıralar python ile IoT projeleri ve  Flask web framework ile REST apiler üzeinde çalışıyorum.
---
## ✈️
## Ready to Flight
???
başlayalım
---
## What we want to do?
???
**ne yapmak istedik?**

temelde web sitelerinin aktiflik (uptime) durumlarını ölçmeyi hedefledik. bunu farklı lokasyonlardan küçük makinalarla yapmakk istedik. saniyede 1 milyon anektodu da bu minik servislerin toplam işlem kabiliyetinden geliyor. 

bugün de bu projemizi senaryolaştırıp basit kod örnekleri ile örneklendireceğiz. ve performans iyileştirmesini nasıl yaptığımıza deyineceğiz
---
template: inverse

## Sync

???
ilk kodumuzu her projenin hello-world'u sayabileceğimiz formatta, senkron biçimde hazırladığımızı düşünelim, 
---
layout: false
.left-column[
  ## Sync
]
.right-column[

```python
from requests import get

def do_request(target: str):
    return get(target)

if __name__ == "__main__":
    while True:
        do_request("www.google.com")
```

Blocks during the response of http request
]
???
bu şekilde hazırladığımız kodda tüm işleyiş bir isteiğimiz cevaplanana kadar bloklanıyor olacak. dolayısıyla bir işlem bitmeden diğerine başlanmayacak ve tüm sistemimiz network bağlantısına bağlı olarak yavaş çalışacak.

dolayısıyla network hızımız CPU hızımızdan yavaş kalıyor ise CPU'muzun tamamını kullanamıyor olacak, bir kısmını israf ediyor olacağız. (ki networkumuz cpumuzdan daha hızlı olamayacağı için bir şekilde  bu israfı engellememiz gerekiyor)
---
template: inverse

## Improved Sync

???
bu israfı engellemenin birkaç yöntemi var. israfa sebep olan faktörlerden en önemlisi gereksiz işlemci gücü harcayan faktörleri ortadan kaldırmak. mesela bu basit senaryonun ilk örneğinde 3. parti bir kütüphane olan **requests** kütüphanesini kullandık. bu kütüphane temelinde pyhton'un **httplib** kütüphanesini kullanıyor. dolayısıyla biz araya gereksiz bir katman koymuş olduk. 

öncelikle bu katmanı aradan kaldırarak CPU'ya yüklediğimiz fazlalık yükü kaldırarak performansda ve dolayısıyla istek sayısında iyileştirme yapabiliriz.
---
.left-column[
  ## Sync
  ## Improved Sync
]
.right-column[
- Use low-level APIs instead high-level

```python
from http.client import HTTPSConnection

def do_request(target: str)
    session = HTTPSConnection(target)
    session.request('GET', '/')
    return session.getresponse()

if __name__ == "__main__":
    while True:
        do_request("https://www.google.com")
```

]

???
kodumuzu iyileştirdiğimiz bu versionda **requests** kütüphanesi yerine direk python3'ün **http.client** modülünden **httpsconnection** sınıfını çekerek ara katmanı ortadan kaldırdık. çok minimal bir düzeyde de olsa performansımızda iyileştirme olduğunu görebiliriz
---
template: inverse

## Threaded
???
ancak yine bu senaryomuzda da işlemcimizin tamamını, tam kapasitesini kullanabiliyor olmayacağız. 

işlemcimizin tam kapasitesini kullanamıyor olmamızın asıl sebebi HTTP üzerinden yptığımız **GET** isteiğinin sonucunu beklerken bizim bir işlem yapmamamız  ve uzak sunucudan cevap beklememiz. dolayısıyla bu esnada CPU'muz cevabı bekleyecek ve herhangi bir işlem yapmayacaktır.

Multithreading yapısına geçerek python'un tek çekirdek üzerinde birden fazla fonksiyonu (aynı fonksiyon olabilir) sahte bir şekilde paralel çağırmasını sağlayarak performansımızı bir tık iyileştirebiliyoruz.

ancak bu paralelizm sahte. yani aslında bu fonksiyonlar aynı anda çalışmayacaklar. python'un **threading** kütüphanesi bu threadler arasında geçiş yapacak ve aynı anda sadece birisinin çalışmasını sağlayabilecek. ancak bu geçişler çok hızlı olduğu için sahte de olsa gerçek zamanlı çalıştıkları hissine kapılacağız.
---
.left-column[
  ## Sync
  ## Improved Sync
  ## Threaded
]
.right-column[
- Use low-level APIs instead high-level
- Use threading

```python
from http.client import HTTPSConnection
from threading import Thread

def do_request(target: str):
    session = HTTPSConnection(target)
    session.request('GET', '/')
    return session.getresponse()

if __name__ == "__main__":
    while True:
        thread = Thread(
            target=do_request, 
            args=('google.com',)
            )

        thread.start()
```
]
???
bu kod örneğimizde python'un threading kütüphanesini içe aktardık ve sonsuz bir döngü içinde fonksiyonumuzu sürekli yeni threadler içinde çağırarak sahtecikten de olsa paralelizm yapısı elde etmiş olduk. 

dolayısıyla duruma bağlı olarak bir thread uzak sunucudan cevap beklerken bir başka threadın yeni bir istek başlatmasını sağlamış olduk. 
---
template: inverse

## Async

???
ancak bir önceki **threading** çözümümüzde threadler arası geçişi biz sağlıklı bir şekilde yönetemediğimiz için tam anlamıyla istediğimiz şeyi elde edemedik.

bize lazım olan **uzak sunucudan yanıt beklediğimiz süre boyunca** farklı bir işlem yapmaktı. çünkü biliyoruz ki uzak sunucudan yanıt beklediğimiz süre boyunca bizim sistemimiz kilitleniyor ve bir israfa yol açıyor.

tam bu noktada async devreye giriyor.
---
.left-column[
  ## Sync
  ## Improved Sync
  ## Threaded
  ## Async
]
.right-column[


```python
import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'https://google.com')
        return html

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```
]
???
bu örneğimizde **aiohttp ve asyncio** kütüphaneleri ile birlikte await ve async deyimlerini kullandığımızı görüyoruz.

buradaki await deyimi bu işlem olana kadar başka işlemler yapabilirsin anlamına geliyor. dolayısıyla programımız await deyimini gördüğü noktada bir işaret bırakacak ve o işlem tamamlanana kadar başka işlemleri yürütmeye devam edecek.

peki bu diğer işemler neler? sonsuz döngüye girdiğimiz için istek tamamlanana kadar yeni bir istek oluşturabileceğiz. Dolayısıyla 1. isteğimizin 10 saniye sürdüğünü varsayalım. her bir isteği de 1 saniyede oluşturduğumuzu. 1. isteğin sonucunu bekleyene kadar 10 yeni istek daha oluşturmuş olacağız.

peki 1. isteğin sonucu gelince ne olacak? programımız bıraktığı işaret noktasına gidecek ve aslında o aralıkta faklı işlemler yapmamış, senkron çalışıyormuş gibi çalışmasına devam edecek.


bu sayede threading'in threadler arası değişimini daha kontrol edilebilir, istediğimiz noktada kırılabilir bir forma getirmiş, daha doğrusu getirilmiş bir formunu kullanmaya başladık.
---
name: last-page
template: inverse

# Then?
???
peki isteğimiz bu noktada bitiyor mu?

hayır...

bu sonuçların listelenip farklı mikroservisler tarafından depo edilmesi,,, daha faklı mikroservisler tarafından yorumlanması, farklı mikroservisler tarafından alarm oluşturulması, farklı mikroservisler tarafından alarmların uygun kanallar üzerinden gönderilmesi gerekiyor.

tüm bu akışı KAFKA üzerinden ilerletiyoruz. confluent_kafka kütüphanesinin async clienti ile bahsettiğimiz gibi asenkron işlemler yapabiliyor, bir isteğin cevabını beklerken farklı bir işlem yapabiliyoruz.