---
layout: post
current: post
cover: 'assets/images/embedded.jpg'
navigation: True
title: Micropython Nedir?
date: 13-11-2017 00:00:00
tags: micropython
class: post-template
subclass: 'post'
author: bisguzar
---

 Micropython'u tanımlamak çok kolay, okadar kolay ki tek bir cümle. 
> Micropython, C programlama dili ile yazılmış, Python 3 programlama dilinin görevini gömülü sistemler üzerinde yerine getiren bir yapıdır.[^1]

Bu tanımı kavrayabilmemiz için öncelikle anahtar kelimeler hakkında bilgi sahibi olmamız gerekiyor. Bu anahtar kelimelere tek tek bakalım.

# Gömülü Sistemler

Eğer teknoloji ile uzaktan yakından bir alakanız var ise -son kullanıcı olmaktan çıkıp, azıcık da olsa araştırma yaptıysanız- gömülü sistemler kavramını elbet duymuşsunuzdur.

Gömülü sistemler kavramı adının hakkını aslında veriyor, bir sistem eğer gömülüyor ise ona gömülü sistem diyebiliriz. Cevaplamamız gereken bir soru daha ortaya çıktı. Bir sistemin gömülmesi ne demek oluyor? Bu konu da aslında basit, sistemi bir işi gerçekleştirmek üzere tasarlıyor/programlıyoruz ve daha sonra o sistemi gömüyoruz. Yani çalışacağı ortama bırakıyoruz, sistemin tek işi ona verdiğimiz görevi gerçekleştirmek oluyor.

Bu konuyu daha iyi kavrayabilmeniz için örneklendirelim. 

Bir çamaşır makinesi düşünün. Ve tabii bu çamaşır makinasının otomatik olduğunu -günümüzde manuelleri kalmamış olsa da-. Deterjanı ve yumuşatıcıyı koyuyorsunuz, istediğiniz su sıcaklığını ve program uzunluğunu seçiyorsunuz. Daha sonra çamaşır makineniz program uzunluğu ve çalışma sıcaklığına göre gerekli ölçüde deterjan ve yumuşatıcı kullanarak görevini gerçekleştiriyor. Çünkü çamaşır makinasının içerisine **gömülen** sistemin görevi bu.

# Python

Ne olduğunu bilmemiz gereken bir diğer kavram ise Python. Programlama dillerine işiniz düştüyse, uygun dili ararken görmüş/adını duymuş olmanız muhtemel. Python, StackOverflow 2017 Geliştirici Anketine göre en çok aranan programlama dili.[^2]

# MicroPython

Gerekli kavramları öğrendik. Artık ilk aşamada yaptığımız tanıma tekrar baktığımızda daha anlamlı gelecek.  Şimdi MicroPython'un bize sunduğu avantajlara ve dezavantajlara bir bakalım.

## Avantajları

MicroPython, Python ile aynı sözdizimine -yani yazılış şeklinde, kod yapısına- sahip olduğu için Python'un sahip olduğu birçok avantaja sahip. Bunları aşağıdaki şekilde sıralayabiliriz.

* Kolay öğrenilebilir,
* Anlaması/yorumlaması kolay,
* Esnek, katı kuralları olmayan,
bir dil.

Ayrıca Python, StackOverflow'da en büyük 5. ve Meetup'da en büyük 3. topluluğa sahip. Github'da da en çok kullanılan 4. dil.[^3]


## Dezavantajları

Her alanda Python kullanmayı seven biri olarak gömülü sistemler alanında da MicroPython benim için en iyi seçenek. Daha kapsamlı olarak benim gibi Python severler için diyelim. Ancak bu durum MicroPython'un dört dörtlük bir seçenek olduğunu göstermiyor.

En bariz dezavantajının performans olduğunu rahatça söyleyebiliriz. Kıyaslama başlığında kullanıcılar tarafından yapılmış basit testlerle bunu rahatça göreceğiz.

# Kıyaslama

MicroPython'un farklı geliştirme kartları üzerindeki performansını ve diğer diller ile arasındaki performans farklarına bir göz atalım.

Tablodaki tüm kartlarda aynı işlem yapılıyor. Şöyle ki, tüm kartlarda 10 saniye boyunca çalışacak bir döngü oluşturuluyor. Döngü her tur attığında bir değişkenin değerini arttırıyor. Başka bir görevi yok, böylelikle 10 saniye boyunca olabildince dönmeyi hedefliyor. 

| Geliştirme Kartı | Programlama Dili | Clockspeed | Test Sonucu | Geliştirme Kartının Fiyatı |
|:----------------:|------------------|------------|-------------|----------------------------|
|    Teensy 3.1    |    MicroPython   |    96MHz   |  1,098,681  |           ~130₺*           |
|      Pyboard     |    MicroPython   |   168MHz   |  2,890,723  |            ~140₺           |
|    Teensy 3.1    |        C++       |    96MHz   |  95,835,923 |           ~130₺*           |
| Arduino Pro Mini |        C++       |    16MHz   |  4,970,227  |            ~12₺*           |

Tablodaki testler 2014 Haziran ayında yapılmış. Teknoloji sürekli ilerliyor, sonuçlar MicroPython sürümüne göre farklılık gösterebilir. Ama aşağı yukarı aynı olacaktır. [Testin orjinal adresine ulaşmak için tıklayın.](https://github.com/micropython/micropython/wiki/Performance)

Bu tabloyu biraz yorumlayalım. İlk iki satırdaki testler MicroPython'un farklı kartlar üzerindeki performansı. Burada yorumlayacak pek bir şey yok, özetle Pyboardın Teensy'e göre daha performanslı olduğunu söyleyebiliriz. 

1\. ve 3. Satırlardaki testlere baktığımız zaman aynı kart üzerinde farklı geliştirme dilleri ile test yapıldığını görüyoruz. Şimdi MicroPython'un performansını değerlendirmek için bir olanağımız var. Tamamen aynı donanım üzerinde C++ ve MicroPython ile yazılmış tamamen aynı işi yapan kodumuz var. Görüyoruz ki C++ ile yazılmış kodumuz görevini **95,835,923** puanla bitirirken MicroPython kodumuz görevini __1,098,681__ puanla bitirmiş. Bu da C++'ın MicroPython'a göre yaklaşık 87 kat daha hızlı olduğunu gösteriyor. Söylediğim gibi, MicroPython'un en büyük dezavantajı performans. 

Bir de ufaklığa, Arduino üzerinde yapılan teste bakalım. Teensy 3.1 geliştirme kartı Arduino Pro Mini kartına göre ciddi bir hızda çalışıyor. Buna rağmen C++ ile hazırlanmış örneği Arduino Pro Mini geliştirme kartında çalıştırdığımız zaman görüyoruz ki yine C++, MicroPython'a göre 4.5 kat daha hızlı. Söylememe gerek var mı bilmiyorum ama Arduino Pro Mini geliştirme kartı Teensy'nin yanında kaplumbağa gibi kalıyor. Ona rağmen sonuçlar böyle...

Peki bunun sebebi nedir? Aslında basit, şöyle ki Python yorumlanan bir dil. Peki yorumlanan bir dil ne demek ve bu neden performansta kayıp yaşatıyor?

Programınızın çalışabilmesi için tek bir yol var. O da yazdığınız kodun makinanın anlayacağı biçimde düzenlenmesidir. Bu düzenleme işlemi iki farklı aşamada yapılabiliyor. 

**Derleme**

Derleme (compile) olarak isimlendirilen işlem yazdığınız kodu makinada çalışacak forma getirme işlemidir. Tabii hangi makinada çalışacak ise -burada makinadan kasıt mikrodenetleyici/işlemcidir- ona göre derlenmesi gerekiyor. Yani X makinası için derlenen kodun Y makinasında çalışmama durumu olabilir. Ancak kodumuzu makinaya göndermeden önce onun anlayacağı dile çevirdiğimiz için makinamız artık anadilinde olan kodumuzu hızlıca okuyabilecek. Böylelikle makina performansının tamamını kodumuzu çalıştırmak için harcayacak.

**Yorumlama**

Yorumlanan (interpreted) dillerde durum biraz daha farklı. Bu diller ile biz kodumuzu yazarız daha sonra herhangi bir işlemden geçirmeden makinaya göndeririz makina kodumuzu çalıştırır. Peki nasıl, makinalar 'if'li 'for'lu şeyleri anlayamıyordu. Evet anlayamıyor, aslında yine bir derleme, kodumuzu makinanın anlayacağı formata çevirme işlemi var. Ancak bunu biz yapmıyoruz.

Yorumlanan dillerde derleme işini daha önceden makinamıza yüklediğimiz ve yorumlayıcı (interpreter) dediğimiz farklı bir katman yapıyor (Gömülü sistemlerde Python çalıştırmak için kullandığımız interpreterdir aslında MicroPython Firmware). Şöyle düşünebilirsiniz, araya bir tercüman girdi. Tercüman kodumuzu makinanın anlayacağı dile çevirecek ve makina da kodu çalıştıracak. Bu sırada tercüman, makinanın performansının bir kısmını gasp edecek.

Bir dilin derlenebilir olması demek çevirme işleminin çalışırken yapılacağı anlamına geliyor. Bu da bizim yazdığımız kodun derleyicinin çalıştığı tüm cihazlarda çalışacağı anlamına geliyor. Python ile yazdığınız kod -eğer işletim sistemine özgü bir şey kullanmadıysanız ve sürüm uyumsuzluğu yoksa-  Python'un kurulu olduğu tüm cihazlarda çalışacaktır.

# Sonuç

MicroPython'un avantajının genel olarak hızlı prototipleme ve dezavantajının da performans olduğunu öğrendik. Eğer performans gerektiren bir projeniz yoksa (saniyede 100.000'in altında işlem yapıyorsanız bu mikrodenetleyici için küçük bir değer diyebiliriz) MicroPython kullanarak projenizi hızlıca oluşturabilir, -burası tamamen kişisel görüş- kod yazarken alacağınız zevki doruklara çıkarabilirsiniz.

[^1]: https://en.wikipedia.org/wiki/MicroPython
[^2]: https://insights.stackoverflow.com/survey/2017#technology
[^3]: http://www.bestprogramminglanguagefor.me/why-learn-python
