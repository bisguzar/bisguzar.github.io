---
layout: post
current: post
cover: 'assets/images/embedded.jpg'
navigation: True
title: Adafruit MicroPython Tool - AMPY Nedir?
date: 2017-12-10 00:00:00
tags: micropython
class: post-template
subclass: 'post'
author: bisguzar
---

Bir projede MicroPython kullanmaya karar verdikten ve biraz araştırma yaptıktan sonraki soru "İyi, güzel, hoş da biz kodlarımızı nasıl bu karta yüklüyoruz" oluyor. En azından benim için bu süreç tam olarak böyle ilerledi. Adafruit MicroPython Tool ya da kısaca AMPY tam olarak bu konuda yardımınıza koşan [açık kaynak](https://github.com/adafruit/ampy) bir çalışma.

Öncelikle MicroPython'a en saf şekilde nasıl kodlarımızı yükleyebileceğimize biraz değinelim. MicroPython firmware yüklü olan bir geliştirme kartına bağlandığınızda sizi REPL karşılıyor. Burada bi durup firmware ve REPL kavramlarına yakından bakalım, daha önce duymamış olabilirsiniz.

# Firmware

En basit tanımıyla firmware dosyaları, donanıma (burada söz konusu olan donanım, geliştirme kartıdır) işlevini önceden bildiren dosyalardır. 
MicroPython firmwaresini donanımınıza yüklediğinizde firmware donanıma MicroPython'un nasıl çalıştığını anlatıyor diyebiliriz.

Bilgisayarlarımızda Python uygulamalarını çalıştırabilmemiz için Python'un kurulu olması gerekiyor çünkü Python yorumlanan bir dildir. Bu konuya [MicroPython Nedir?](https://bisguzar.me/micropython-nedir/) başlıklı yazımda değinmiştim. Gömülü donanımımızda da yorumlama görevini önceden yüklemiş olduğumuz firmware dosyamız üstleniyor.

# REPL

REPL, eğer Python ile **Hello World** yazdırdıysanız kesinlikle karşılaşmış olduğunuz bir kavram. REPL'i açarak inceleyelim. Çünkü kendisi dört aşamadan oluşuyor.

**R**ead  
**E**valuete  
**P**rint  
**L**oop

Yani Python'da "etkileşimli kabuk" olarak ifade ettiğimiz şey REPL ekranı. Öncelikle bir kod girmemiz isteniyor ki bu **read** aşaması oluyor. Daha sonra girdiğiniz kod **evaluete** aşaması gereği işleniyor. **Print** aşamasında kodunuzun sonucu ekrana yazdırılıyor ve son aşama olan **loop** aşamasında tekrar **read** aşamasına dönülüyor, yani sonsuz döngüye giriyor.

# MicroPython'a Kodumuzu Yüklemek

REPL'in ne olduğunu da öğrendik. Eğer MicroPython yüklü bir geliştirme kartına seri bağlantı ile bağlanırsanız sizi bir REPL ekranı karşılayacaktır. Bu ekran üzerinde Python'un dosya işlemleri komutunu kullanarak kodumuzu bir dosyaya yazdırabiliriz. Bir örnek veremem gerekirse:

~~~python
with open('boot.py', 'w') as dosya:
        dosya.write('print("Anne ben boot oldum!")')
~~~

MicroPython ilk çalıştığında yürürlüğe girecek olan boot.py dosyamıza bir print fonksiyonu yazdırdık. Peki yüzlerce, belki de binlerce satır koddan oluşan projelerimizde bu yolu izlemek nekadar mantıklı? Şuan için başka çaremiz malesef ki yok. Ama AMPY kullanarak bu işlevleri basitleştirebiliyoruz.

# AMPY

Öncelikle sistemimize AMPY'i kurmamız gerekiyor. **pip** paket yöneticisini kullanarak basit bir şekilde kurabiliriz.

    pip3 install adafruit-ampy

Kurulumu gerçekleştirdikten sonra AMPY'nin güzelliklerinden yararlanabiliriz. Şimdi AMPY üzerinde kullanabileceğimiz komutlara kısaca bakalım.

Komutlarımızı aşağıdaki formatta kullanacağız.

    ampy -p KART_PORTU [ÖZELLİKLER] KOMUT [ARGÜMAN]
    

Eğer her ampy komutu çalıştırırken geliştirme kartımızın bağlı olduğu portu belirtmek istemiyorsak portu önceden tanımlayabiliriz.

\*nix tabanlı işletim sistemlerinde: 

    export AMPY_PORT=[KART_PORTU]
    ampy KOMUT

Windows üzerinde (test edilmemiş):
    
    set AMPY_PORT=COM4
    ampy KOMUT
    

## get
Geliştirme kartımızan herhangi bir dosyayı bilgisayarımıza getirmemizi sağlar. İki farklı kullanımı var, birincisinde dosya içeriğini sadece yazdırırken diğerinde kartımızdaki dosyayı içeriği ile birlikte kendi bilgisayarımıza çeker.

İçeriği görmek için:
    
    ampy get dizin/karttaki_dosya_adı.py
    
İçeriği kendi bilgisayarımıza çekmek için ise:

    ampy get dizin/karttaki_dosya_adı.py <local_dosya_adı.py>
    
## ls
Geliştirme kartındaki dosya içeriğini yazdırmamızı sağlar. Eğer bir dizin belirtmeden kullanırsak öntanımlı olarak '/' yani kök dizinin içeriğini yazdıracaktır.

    ampy ls </benim/dosya/dizinim>
    
## mkdir
Geliştirme kartımız üzerinde bir klasör oluşturmamızı sağlar. 

    ampy mkdir dosya_adı
    
## put
Kendi bilgisayarımızdaki bir dosyayı geliştirme kartımıza göndermek için kullanılır. 

    ampy put bilgisayardaki/dosya/yolu.py <karttaki/dosya/yolu.py>
    
Eğer kartta nereye gönderileceğini belirtmezseniz dosya kök dizine gönderilir.

## reset

Geliştirme kartımıza yazılımsal reset atar.

    ampy reset
    
## rm

Geliştirme kartı kartındaki bir dosyayı silmemizi sağlar.

    ampy rm karttaki/dosya/yolu.py
    
## rmdir

Geliştirme kartı üzerindeki bir klasörü silmemizi sağlar.

    ampy rmdir karttaki/klasör
    
## run

Bilgisayarımızdaki bir dosyayı geliştirme kartına göndermeden çalıştırmamızı sağlar. Kodumuz geliştirme kartına gider, çalışır ve sonucu bilgisayarımızda ekrana yazdırılır. Ama kodumuz geliştirme kartına kaydedilmez.

    ampy run bilgisayardaki/dosya.py <--no-output>
    
Eğer **--no-output** parametresi kullanılırsa çalıştırılan dosyanın çıktısı ekranda gösterilmez.
