---
layout: post
current: post
cover: 'assets/images/flask_python.jpg'
navigation: True
title: Flask ile Blog Yapalım
date: 02-08-2018 17:09:00
tags: flask
class: post-template
subclass: 'post'
author: bisguzar
---

**İçerik Listesi**
1. TOC
{:toc}

<hr style="margin: 10px !important;">

# Giriş

Bu yazıda web temelli uygulamalar geliştirmek için hazırlanmış olan python kütüphanesi Flask'ı kullanarak kendi blogumuzu geliştireceğiz. Bunu yaparken birkaç farklı alanda temel seviyede bilgi edinmiş olacağız. Bu alanları listelemek gerekirse;

1. Web temelleri hakkında bilgi edineceğiz, bir web sitesinin nasıl çalıştığını öğreneceğiz
2. PIPENV'i kullanmayı öğreneceğiz
3. Flask'ı tanıyacağız
4. HTML ve CSS kullanarak kendi temalarımızı tasarlayacağız, Jinja2 tema motorunu kullanmayı öğreneceğiz
5. Veritabanı modellerimizi hazırlarken ORM yapısını göreceğiz, peewee ORM kütüphanesini kullanacağız
6. Blogumuzun istekleri karşılayan ve yanıt üreten (terimsel olarak back-end) kısımını hazırlayacağız, tarayıcı oturumlarına değineceğiz
7. Hazırladığımız blogu yayına alacağız, pythonanywhere kullanmayı öğreneceğiz

Yine web temelli uygulamalar geliştirmek için hazırlanmış olan bir başka Python kütüphanesi *Django* ile blog geliştirmek için benzer bir döküman mevcut. Hem o döküman, hem bu döküman sizlere temel seviyede bilgi verip bu konuları araştırma heyecanı oluşturmak için hazırlandı. [djangogirls.org üzerindeki o Türkçe dökümana gitmek için tıklayın](https://tutorial.djangogirls.org/tr/){:target="_blank"}. Fırsat bulursanız DjangoGirls çalışmalarından birine katılmanızı da öneririm. 

Ancak biz Flask'ı kullanarak bu dökümanda ilerleyeceğiz. Birçok şeyi kendimiz yapmak durumunda kalacağız. Djangoda birçok kullanıma hazır yapı bulunurken Flask için ek kütüphaneler kullanarak ilerleyeceğiz. Ayrıca içerik listesinde de gördüğünüz (ya da göremediğiniz) bu dökümanda Python öğrenmeyeceğiz. Hali hazırda iyi kötü bir Python bilginizin olması gerekiyor. Djangogirls'ün hızlandırılmış Python dökümanına [ulaşmak için tıklayın](https://tutorial.djangogirls.org/tr/python_introduction/).

Ayrıca bu yazı boyunca oluşturacağımız tüm dosyalar Github'daki **[bisguzar/flask-blog](https://github.com/bisguzar/flask-blog){:target='_blank'}** deposunda bulunuyor. Oradan da takip edebilirsiniz.

# İnternet Siteleri Nasıl Çalışır

İnternet sitelerinin çalışmasını anlamak için bu senaryoyu hikayeleştirelim. Öncelikle Ahmet #TODO isminde bir karakterimiz olsun ve bakkala girip bir kase yoğurt istediğini varsayalım. Böyle bir durumda gerçekleşecek bir sonraki olay bakkalın Ahmet'e istediği yoğurtu dolaptan çıkarıp vermesi olacak. Olay çok basitti. Ahmet bir yoğurt istedi ve istediğini aldı. 

Web siteleri de aynen böyle çalışıyor. Ancak web siteleri yoğurttan oluşmuyor tabikide, kaynak dosyalarını -yani html,css,js gibi dosyaları- da buzdolabında tutamıyoruz. Bu dosyaların saklanması gerekiyor, çünkü istek geldiği zaman isteği yapan kişiye gönderilmesi gerekiyor ki senaryomuz tamamlansın. Bu saklama işlemini ise sunucu dediğimiz güçlü bilgisayarlar üzerinde yapıyoruz. Bu bilgisayarlara biz web sitemizi oluşturan dosyaları yüklüyoruz ve sitemize bir ziyaretçi girdiği zaman -ziyaretçi sitemize girdiği zaman aslında sunucumuza *'ben bu web sitesini görmek istiyorum'* şeklinde bir istek gönderiyor- kaynak dosyaları kendisine gönderip sitemizi görüntülemesini sağlıyoruz.

Yani siz github.com adresini tarayıcınızın bağlantı çubuğuna girdiğiniz zaman tarayıcınız github.com adresine bir istek gönderiyor. Ozaman github.com bir sunucu mu? Aslında hem evet hem hayır. Github.com bir temsili isim. Github.com aslında bir sunucunun IP adresini belirtiyor, ancak tarayıcıya *192.30.253.112* yazmayı mı yoksa *github.com* yazmayı mı tercih edersiniz? Daha okunaklı olabilmesi için domain ismi verilen bu yönlendirici yapılar kullanılıyor.

Bu oluşturduğumuz senaryoyu unutmayın, ilerleyen konuları işlerken de bu senaryo üzerinden örneklendirmeler yapacağız.

# Pipenv Kurulumu ve Kullanımı

Eğer işletim sisteminiz Linux ise Python'un kurulu geldiğini farketmişsinizdir. Çünkü Linux dağıtımlarının bir çoğunda Python yoğun olarak kullanılıyor. Dolayısıyla bazı kütüphaneler de sisteminizde zaten kurulu durumda. Siz de projenizde o kütüphaneyi hemen kullanmaya başlayabilirsiniz. Böyle bir durumda herhangi bir sorun yok gibi görülüyor. Ancak durum malesef öyle değil, örnek vererek ilerleyelim. Ubuntu kullananların tanıyacağı "apt-add-repository" paketini sisteminize kurmak istediğinizi varsayalım. Bu paket python-requests kütüphanesini kullanıyor. Ancak paketin kullandığı kütüphane sürümü 1.5. Aynı zamanda geliştirdiğiniz bir uygulamanın da python-requests kütüphanesi kullandığını varsayalım. Doğal olarak son sürümü kullanıyor olacaksınız. Şuanda kütüphanenin son sürümü 2.19.1. Sistemde zaten 'apt-add-repository' kurulumundan dolayı bulunan bu kütüphanesi son sürüme güncellerseniz 'apt-add-repository' paketi çalışamaz duruma gelecek. Çünkü python-requests kütüphanesinde 1.5 sürümünden bu yana köklü değişiklikler yapıldı. Bu tarz uygulamalar arası uyum sorunlarını çözmek için sanal yöntemler kullanıyoruz.

Pipenv ise bu sanallaştırma için şuanda en fazla önerilen yöntem. Alternatifi olarak virtualenv gösterilebilir ancak pipenv de zaten temelde virtualenv'i kullanıyor. Sadece daha basitleştiriyor işlemleri.

Ruby'nin paket yöneticisi bundle veya nodejs'in paket yöneticisi npm kullandıysanız zaten çok kolay adapte olabileceğiniz bir yapısı var.

Sisteminizde zaten python ve pip'in kurulu olduğunu varsayarak pipenv'i kurmak için pip'i kullanabiliriz.

~~~
pip3 install pipenv
~~~

Şimdi projemizi geliştireceğimiz bir klasör oluşturalım. Ben masaüstünde *flask-blog* adında bir kütüphane oluşturuyorum. Daha sonra terminali açıp (eğer windows kullanıyorsanız cmd'yi) bu klasörün içine girelim. Şimdi burada pipenv için bir ortam oluşturmalıyız. Eğer bir paket kurmak istersek ve orada pipenv ortamı yoksa ilk kurulumu pipenv bizim için yapacak. pipenv kullanarak Flask kütüphanesini *flask-blog* klasörümüzün içinde kuralım.

~~~
pipenv install flask
~~~

Mevcut bir pipenv ortamı olmadığı için bir ortam oluşturacak. Burası biraz zaman alabilir, beklememiz gerekiyor.

Eğer herhangi bir sorunla karşılaşmadıysak aşağıdaki gibi bir çıktı almış olmalıyız. (çıktıyı biraz kısalttım)

~~~posh
Creating a virtualenv for this project...
Pipfile: C:\Users\bisguzar\Pipfile
Using c:\users\bisguzar\appdata\local\programs\python\python37-32\python.exe (3.7.0) to create virtualenv...
Already using interpreter c:\users\bisguzar\appdata\local\programs\python\python37-32\python.exe
Using base prefix 'c:\\users\\bisguzar\\appdata\\local\\programs\\python\\python37-32'
.
.
Adding flask to Pipfile's [packages]...
Pipfile.lock not found, creating...
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
Updated Pipfile.lock (662286)!
Installing dependencies from Pipfile.lock (662286)...
  ================================ 6/6 - 00:00:02
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
~~~

Sadece **pipenv install** komutunu çalıştırarak içinde hiçbir kütüphane kurulmamış, temiz bir pipenv ortamı da kurabiliriz. Ancak zaten biz Flask'ı kuracaktık. İki işlemi bir arada yapmış olduk.

Kurduğumuz kütüphane aslında sisteme kurulmadı. O yüzden python'u çalıştırıp *import flask* dersek hata almamız olası (eğer sisteme daha önceden Flask kurmadıysak!). Bunu test etmek için terminale *python* yazarak Python'un etkileşimli kabuğuna girelim ve *import flask* komutunu verelim.

~~~~python
C:\Users\bisguzar\Desktop\flask-blog
λ python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import flask
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'flask'
~~~~

Evet, bir hata aldık. Çünkü sistemde Flask kütüphanesi kurulu değil. Ama biz az önce bir şeyler kurmuştuk, o nerede?
exit() diyerek etkileşimli kabuktan çıkalım ve proje dosyamızın içinde **pipenv run python** komutunu vererek Python'u bu sefer sanal ortamımızın içinde çalıştıralım ve tekrar Flask'ı içe aktarmayı deneyelim.

~~~~python
C:\Users\bisguzar\Desktop\flask-blog
λ pipenv run python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import flask
>>>
~~~~

Olması gerektiği gibi oldu ve herhangi bir hata almadık, çünkü sanal ortamımızın içinde Flask kütüphanesi kuruluydu. Neden sanal ortamlar kullanmalı ve sistem genelinde paket kurulumları yapmamalı konularını anladığımıza göre yazımıza devam edebiliriz.

# Flask Kullanmaya Başlayalım

Zaten oluşturduğumuz *flask-blog* klasöründe olduğumuzu varsayarak burada *app.py* adında yeni bir dosya oluşturalım. Burada kısa bir bilgilendirme geçmek istiyorum, hangi metin editörünü kullandığınızın bir önemi yok. Terminal tabanlı bir editör olan vim de kullanabilirsiniz, Python için geliştirilmiş en donanımlı IDE'lerden biri olan PyCharm da. Tamamen size kalmış bir durum. Ben sublime-text kullanarak bu yazıyı hazırlıyorum, belki merak eden olmuştur :D

Şimdi oluşturduğumuz *app.py* dosyasını tercih ettiğimiz editör (ya da IDE) ile açalım. Üzerinde çalışacağımız ilk satırlarımızı yazalım ve daha sonrasında üstüne konuşalım.

*app.py*
~~~~python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__": 
    app.run(debug=True)
~~~~

Burada ilk satırda *flask* kütüphanesinin içindeki **Flask** sınıfını projemize dahil ettik. Yani aslında flask kütüphanesinin içinden sadece bir parçayı kullanacağımızı, onu projemizin içine çekmesini söyledik Python Bey'e.  
İkinci satırda ise içeriye aktardığımız sınıf ile bir nesne oluşturduk. Sınıf, nesne terimleri biraz *Nesne Tabanlı Programlama* başlığı altına giriyor. Biz o kadar detaylı ilgilenmiyoruz şuanlık. NTP detayları için [buraya tıklayabilirsiniz. (Türkçe)](https://belgeler.yazbel.com/python-istihza/nesne_tabanli_programlama1.html).

Daha sonraki satırlarda ise bir fonksiyon tanımladık ve bu fonksiyon 'Hello, World!' diye bir yazı döndürüyor. Basit seviyede Python bilen herkes bunu anlayabilir ama peki ya fonksiyonun üstündeki *@* ile başlayan alan? Pythonda bu kullanıma *decarator* deniyor. Aslında o da bir fonksiyon. Farkı, üzerine yazıldığı fonksiyon üzerinde işlem yapması. Bu konu da biraz detaya giriyor. Biz bu konuyla da ilgilenmeyeceğiz. Ama ben öğrenmek istiyorum şuan derseniz [buraya tıklayarak](https://wiki.python.org/moin/PythonDecorators) PythonWiki'ye gidebilirsiniz (İngilizce).

*app.route* decaratorünü projemizde bol bol kullanacağız. Burada yaptığı iş aslında fonksiyonumuzun Flask projemizin bir parçası olmasını sağlamak. app objemize (2. satırda oluşturmuştuk) fonksiyonumuzu bağlıyor. Aynı zamanda kendisi bazı değerler de alabiliyor. Şuanlık gördüğümüz gibi '/' değerini almış. Bu değer fonksiyonu hangi adrese bağlayacağını gösteriyor. Yani biz oraya '/' yerine *'/selam'* yazsaydık sitemizi yayına aldığımızda *site_adresimiz.com/selam* adresini bizim fonksiyonumuza bağlayacaktı. O adrese bir ziyaretçi gelip istek gönderdiği zaman bizim fonksiyonumuzun cevabı oraya ulaşacaktı.

Şimdi bakkal ile Ahmet'in senaryosuna geri dönelim ve #TODO Ahmet'in bakkaldan yine yoğurt istediğini düşünelim ama busefer Pınar yoğurt istiyor olsun. Yani busefer bir ailenin içinden (yoğurt ailesi :D) Pınar markalı olanı istiyor. İstediği şey yine yoğurt. Bu örneği kendi durumumuzla ilişkilendirmemiz gerekirse biz yine siteyi görmek istiyoruz, ancak busefer belli bir noktasındaki dosyayı görmek istiyoruz. Peki '/' ne anlama geliyor? Çünkü burada herhangi bir ibare bulunmuyor, hangi adresi belirtiyor diye düşünüyor olabilirsiniz. '/' ifadesi ana noktayı belirtiyor. Yani hiçbir şeyi. Buda demek oluyor ki *site_adresimiz.com* adresine giren biri bağlantı noktası '/' olan fonksiyonumuz tarafından cevap alacak.

Gelelim son iki satırımıza. İlkinin bir karşılaştırma satırı olduğunu görüyoruz. Bu kısım eğer dosyanın kendisini çalıştırmışsak anlamına geliyor. Bu biraz karışık gelmiş olabilir. Ama bazı durumlarda *app.py* dosyamızı başka bir .py dosyasının içine aktarmamız gerekebiliyor. Bu durumlarda da projemizin çalışmaması için sadece app.py'nin kendisini çalıştırdığımızda projenin ayağa kalkmasını[^1] istediğimizi belirtiyoruz. Son satır da kendisini belli ettiği üzere projemizi çalıştırıyor. debug parametresini de True yaparak olası hatalarda tam bir hata mesajı göstermesini sağlıyoruz.

Şimdi projemizi çalıştırıp tarayıcıda görüntüleyebiliriz! Ama unutmayın, projemizi sanal ortam içinde çalıştırmamız -yani pipenv ile- gerekiyor.

~~~~
pipenv run python app.py
~~~~

Eğer herhangi bir hata almadıysak tarayıcımızdan http://127.0.0.1:5000 adresine gidince bizi ilk sayfamız karşılıyor olmalı!

![]({{ "/assets/images/flask_document/hello_world.jpg" | absolute_url }})

# Site İskeletini Oluşturalım

Websiteniz arkaplanda şahane teknolojiler kullanıyor olabilir, dünyada bir ilki gerçekleştiriyor bile olabilir. Ama malesef siteye giren ziyaretçi için bu hiçbir şey ifade etmiyor. Çünkü ziyaretçiler ne arkada çalışan sunucuyu görüyor ne de Flask fonksiyonlarınızdan haberi var. Onlar sadece kendilerine ulaşan html ve html'i güzelleştiren css dosyalarını görüyor. O yüzden web sitemizin iskeletini -yani tasarımını- elimizden geldiğince güzel tutmalıyız. Tabiki bu hızlandırılmış bir döküman olduğu için çok basit çalışacağız, gerisi size ve yaratıcılığınıza kalmış.

Öncelikle iskelet dosyalarımızın (html) barınacağı bir klasör oluşturmamız gerekiyor. *flask-blog* klasörünün içine *templates* klasörü oluşturuyoruz. Aslında bu klasör isimlerini kendi istediğimiz gibi yapabiliriz ancak kabul görmüş standartları kullanmak her zaman bizim ve projemizi okuyacak kişilerin yararına olacaktır. Daha sonra da *templates* klasörü içine *base.html* adında bir html dosyası oluşturuyoruz. Bu aşamada proje dosyamızın içeriği aşağıdaki gibi olacak.

flask-blog  
├───templates  
│   └───base.html  
├───app.py  

Şimdi neden base.html isiminde bir dosya oluşturduğumuza deneyelim. Base kelime anlamı olarak 'baz, temel' anlamına geliyor. Yani bu temel iskeletimiz olacak. Oluşturacağımız diğer iskeletler base.html iskeletimizi kullanacak böylelikle genel yapıyı her dosya için tekrar yazmaktan kurtulacağız ve aynı zamanda blogumuzun tüm sayfalarının benzer şemada olmasını sağlayıp bütünlük sağlayabileceğiz. HTML' etiketlerden oluştuğu konusunda bir bilginiz vardır elbet. Açılan her etiket kapatılır. <etiket> </etiket> örneğinde gördüğünüz gibi kapatırken taksim kullanılır. Bu bilgi açıklamaları okumanızı kolaylaştıracaktır. Bu aşamadan itibaren iskelet dosyalarını oluştururken izleyeceğimiz adımlar tamamen tercihe bağlıdır. Örnek vermek gerekirse siz h1 etiketi yerine h2 etiketi kullanarak daha küçük bir yazı elde edebilirsiniz. Kendi zevkinize göre bu kısımı özelleştirmeyi unutmayın! Neticede bu sizin blogunuz :) Eğer bu dökümanı bir workshopda takip ediyorsanız zaten size yardımcı olacak birisi var demektir. Hata yapmaktan korkmayın.

~~~~html
<!DOCTYPE html>
<html>
<head>
	<title>Benim Blogum</title>
</head>
<body>

</body>
</html>
~~~~

base.html içeriğimizi bu şekilde oluşturalım. Burası çok da özelleştirebileceğimiz bir alan değil, HTML'nin standart ve olması gereken etiketleri bunlar.
Burada açıklamak istediğim iki etiket var. Öncelikle *title* etiketi, bu etiketin içerisine yazdığımız yazı tarayıcılar tarafından site adı olarak yorumlanacak ve sekmede görünecek. *body* etiketine yazdığımız kodlarımız ise tarayıcı tarafından site içeriği olarak yorumlanacak ve kullanıcıya gösterilecek. 

Bu aşamada biraz tema motorlarından bahsetmek istiyorum. Tema motorları (template engines) iskelet dosyalarımızı dinamik yapmamıza yardımcı oluyor. Yani örnek vermek gerekirse ana sayfada başka, profil sayfasında başka site başlığı belirleyebiliyoruz. Yapmamız gereken bu alanlara bir blok geleceğini belirtmek ve daha sonra ilgili fonksiyonların içinde blokları veya değişkenleri doldurmak. Bu kısımı tam anlayamamış olabilirsiniz, örnekler üzerinde daha iyi anlayacağınızı düşünüyorum. Şimdi base.html dosyamızı biraz düzenleyip ilgili alanlara işaretlemeler yapalım.

~~~~html
{% raw %}<!DOCTYPE html>
<html>
<head>
	<title>Benim Blogum - {% block title %}{% endblock %}</title>
</head>
<body>

<header>
	<main>Benim Blogum</main>
</header>
<main>
	<nav>giriş yap</nav>
	<content>
		{% block main %}{% endblock %}
	</content>
</main>

</body>
</html>{% endraw %}
~~~~

Yaptığımız değişikleri açıklayalım. *title* etiketinin içine adı yine *title* olan bir block oluşturduk. Bunu yaparken {% raw %}{% %}{% endraw %} şeklinde bir etiket yazdık. Bu etiketler Flask'ın tema motoru olan Jinja2 tarafından okunup yorumlanacak ve sonra ortaya düzenlenmiş bir html dosyası çıkacak. Bu düzenlenmiş yani render edilmiş dosya da siteyi görmek için istek gönderen ziyaretçiye iletilecek. Böylelikle ziyaretçi için özel bir cevap hazırlamış olacağız. *title* etiketindeki block kısımını ziyaretçinin görmek istediği sayfaya göre sayfa başlığını değiştirebilmek için kullanacağız.

*main* etiketinde de adı yine *main* olan bir blockumuz daha var. Daha önce base.html dosyamızın başka iskeletler tarafından temel alınıp üzerine inşa edileceğinden bahsetmiştik. Bu kısıma o iskelet dosyalarının içeriği gelecek. Böylelikle temel HTML etiketlerimizi her dosya için yazmayacağız.

Bunlar dışında *header* ve *nav* olmak üzere iki yeni etiket ekledik. Bunlar da sitemizin diğer ilgili alanlarını oluşturuyor. *header* etiketi sitemizin başlığını, üst kısımını, *nav* etiketi ise menüsünü belirtiyor. *content* etiketi ise tamamen alanı belirtmek için.

Şimdi *templates* dosyamızın içine bir de index.html dosyası oluşturup sitemizin '/' adresine gelen isteklere cevap verecek ana sayfa iskeletimizi oluşturalım.

~~~~html
{%raw%}{% extends 'base.html' %}

{% block title %} Ana Sayfa {% endblock %}

{% block main %}
	'Dünya, naber?'
{% endblock %}{%endraw%}
~~~~

index.html dosyamızın içeriği bu şekilde, şuanlık. Bir html dosyası oluşturduk ama içine hiç html etiketi yazmadık diye düşünüyor olabilirsiniz. Evet, yazmadık, yazacağız ama yazmadan önce burayı biraz açıklamak istiyorum.

İlk satırda *extends* ifadesi kullandık. Extend kelime anlamı olarak **genişletmek** anlamına geliyor. Yani index.html dosyamızın aslında *base.html* dosyasının genişletilmiş hali olduğunu belirtiyoruz. Daha önce kullandığımız değişle base.html dosyasını temel almasını söylüyoruz. Daha sonra burada da block etiketlerini kullandığımızı görebilirsiniz. Burada kullandığımız block etiketleri arasına yazdığımız her şey temel aldığımız base.html dosyasındaki ilgili yere gidecek. Hemen bu durumu canlı canlı görelim.

*app.py* dosyamıza dönelim ve hello_world fonksiyonumuzdaki **return 'Hello, World!'** satırını **return render_template('index.html')** ile değiştirelim daha sonra projemizi başlatalım. Projemizi pipenv ile başlatmamız gerektiğini unutmayalım![^2]

Projeyi çalıştırdıktan sonra tarayıcıdan açtığımız zaman **NameError: name 'render_template' is not defined** hatasıyla karşılaşacağız. Bu çok normal. Sizlere Flask'ı tamamen içeri aktarmadığımızı, sadece Flask'ın Flask sınıfını (bilgisayar bilimlerinde en zor konulardan birinin isimlendirme olduğu gerçeğini tekrar anlıyoruz) içeri aktardığımızdan bahsetmiştik. render_template fonksiyonu da Flask'ın içinde olmasına rağmen onu dahil etmediğimiz için kendisini bulamadık şeklinde hata alıyoruz. request_template fonksiyonunu da içeri aktararak sorunu çözebiliriz. Yani app.py'deki import kısımını aşağıdaki şekilde düzenleyip projeyi tekrar çalıştıralım.

~~~~python
from flask import Flask, render_template
~~~~

Şimdi sitemizi çalıştırdığımız zaman değişikliklerin geçerli olduğunu görebiliriz.

![]({{ "/assets/images/flask_document/template_helloworld.jpg" | absolute_url }})

Devam etmeden önce şimdiye kadar yaptıklarımızı kısa bir özetleyelim. '/' adresine bağlı fonksiyonumuz artık cevap olarak bir iskeleti (template'yi) döndürüyor. Bu döndürdüğü template'de olmamasına rağmen 'Giriş Yap' yazısının yinede sitede bulunmasının sebebinin de aslında index.html dosyasının base.html dosyasını kullanarak bir bütün oluşturması ve cevap olarak bu oluşan bütünü göndermesi olduğunu biliyoruz.

Biz bir blog sitesi yapıyoruz ve ana sayfada blog yazılarını göstermek istiyoruz. Oyüzden şimdilik temsilen iki yazıyı elimizle varmış gibi gireceğiz. Daha sonra fonksiyonları yazarken bu kısımları otomatikleştireceğiz. 

index.html dosyamızın içeriğini aşağıdaki gibi düzenleyelim.

~~~~html
{%raw%}{% extends 'base.html' %}

{% block title %} Ana Sayfa {% endblock %}

{% block main %}
	
	<div>
		<h2>Hello World!</h2>
		<p>Bu birinci yazımızın kısa bir önizlemesi olsun. Devamı daha sonra :)</p>
		<a href='#'>Devamını Oku</a>
	</div>

	<div>
		<h2>Bir Diğer Yazı!</h2>
		<p>Bu da ikinci yazımızın kısa bir önizlemesi olsun. Devamı daha sonra :)</p>
		<a href='#'>Devamını Oku</a>
	</div>

{% endblock %}{%endraw%}
~~~~

Bu şimdilik böyle kalsın, daha sonra tekrar döneceğiz index.html şablonumuza. Editörlerin giriş yapabilmesi için login.html şablonuna ihtiyacımız var. O yüzden templates klasörüne login.html dosyası oluşturalım. Bu şablonda da extends etiketi ile base.html'i kullanması gerektiğini belirteceğimizi ve title ile main blocklarını kullanacağımızı biliyoruz. O yüzden benim vereceğim örneğe bakmadan önce kendiniz oluşturmaya çalışın şablonu, içine oluşturacağımız formu beraber yaparız yine :)


~~~~html
{%raw%}{% extends 'base.html' %}
{% block title %} Giriş Yap {% endblock %}
{% block main %}
	<form method="POST" action="/girisyap">
		
		<table>
			<tr>
				<th><label for="username">Kullanıcı Adı:</label></th>
				<th><input type="text" name="username" required=""></br></th>
			</tr>
			<tr>
				<td><label for="password">Şifre:</label></td>
				<td><input type="password" name="password" required=""></td>
			</tr>
			<tr>
				<td><button type="submit">Giriş Yap</button></td>
			</tr>
		</table>
	</form>
{% endblock %}{%endraw%}
~~~~

login.html şablonumuzun içeriğini bu şekilde hazırlayabiliriz. Editörler bu sayfadan giriş yapacağı için bir giriş formu oluşturmamız gerekiyor. *form* etiketinin *action* özelliğine girdiğimiz adresi görüyorsunuz. Bu adresi daha sonra oluşturacağız, şablonumuzda şimdiden bir yönlendirme eklememizde sakınca yok. Aynı şekilde base.html iskeletimizdeki *'giriş yap'* yazısına da html'nin **a** etiketini kullanarak aynı adrese link verelim. 
~~~~html
<a href="/girisyap">giriş yap</a> 
~~~~
Son olarak bu şekilde görünüyor olacak.

Şimdi yine blog sitelerinin gereksinimlerinden biri olan yeni yazı ekleme sayfamızı hazırlayalım. Buraya kadar Jinja2 (hatırlayalım: Jinja2, Flask'ın tema motorudur) etiketlerini ve form yapısını öğrenmiş olmalıyız. Siz yine hazır olan örneğe bakmadan önce **newpost.html** adında içinde bir form barındıran şablon oluşturmaya çalışın. Yapabildiğiniz kadar yapın, daha sonra buradaki örnek ile kıyaslayıp eksiklerini/hatalarını düzeltin. Kopyala yapıştır ile öğrenmek malesef mümkün değil.

~~~~html
{%raw%}{% extends 'base.html' %}
{% block title %} Yeni Yazı {% endblock %}
{% block main %}
	<form method="POST" action="/yaziekle">
		
		<table>
			<tr>
				<th><label for="title">Yazı Başlığı:</label></th>
				<th><input type="text" name="title" require></br></th>
			</tr>
			<tr>
				<td><label for="content">Yazı İçeriği:</label></td>
				<td><textarea name="content" required></textarea></td>
			</tr>
			<tr>
				<td><button type="submit">Yazı Ekle</button></td>
			</tr>
		</table>
	</form>
{% endblock %}{%endraw%}
~~~~

Sonuç olarak newpost.html dosyamız da buna benziyor olmalı. Şimdi devam edebiliriz.

## Şablonlarımızı Güzelleştirelim

Şablonları oluştururken tamamen benimle aynı şeyleri yapamamanızı, biraz yaratıcılık katmanızı rica etmiştim. Şimdi o kısıma geliyoruz. Şablonlarımızı güzelleştirirken kendi yazı büyüklüklerinizi, arkaplan ve yazı renklerinizi kullanmaktan çekinmeyin. Malesef css kodlarını çok fazla açıklayamayacağım. Ancak css'yi basit seviyede öğrenmek için birkaç döküman okumanız yeterli.

İlk paragraftan da anlaşıldığı üzere şablonlarımızı güzelleştirirken CSS'den yararlanacağız. CSS için özetle, HTML etiketlerinin şekilleri üzerinde oynamalar yapmamızı sağlayan bir dil diyebiliriz. CSS dosyaları eğer HTML dosyalarının içinde belirtilmemişse malesef çalışamıyor. Bu aşamada işin içine static dosyalar dediğimiz durum giriyor. Statik bir websitesi geliştirirken (yani html dosyasından oluşan, herhangi bir özelliği olmayan, düz site) html dosyasının içine direk olarak css dosyasının yolunu belirtebilirdik. Ancak biz Flask kullanarak dinamik bir site geliştirdiğimiz için malesef bu çok mantıklı bir yöntem olmayacaktır. Hem şablonlar ile diğer dosyaların farklı lokasyonlarda tutuluyor olması hem de proje büyüdükçe oluşacak dosya kalabalığında her dosya için elimizde adres vermek mantıklı bir çözüm olmuyor. Burada yardımımıza static dosyalar yetişiyor. Bunun için *flask-blog* klasörüne yani projenin ana klasörüne bir de static klasörü oluşturalım.

Sonuç olarak proje klasörümüzün içeriği aşağıdaki gibi olmalı.

flask-blog  
├───static  
├───templates  
│   └───base.html  
│   └───index.html  
│   └───login.html  
├───app.py 

Şimdi stil dosyamızı oluşturacağız. Biz bir dosya oluşturacağız, ama yine de standartlara uymak için static klasörümüzün içine *css* adında yeni bir klasör açıyoruz. Stil dosyalarımızı bu klasöre kaydedeceğiz. Aynı şekilde resim dosyalarını da static klasörünün içindeki *images*, JavaScript dosyalarımızı da static klasörü içindeki *js* klasörüne kayıt etmeliyiz. Daha önce de söylediğim gibi, dosya isimlerini siz de belirleyebilirsiniz. Hatta dosyaları işlevlerine göre sınıflandırmak yerine hepsini direkt *static* klasörü içine de oluşturabilirsiniz. Ancak genel kabul görmüş standartları kullanmak ve bunlara alışmak sizin için daha iyi olacaktır. 

Oluşturduğumuz *css* klasörümüzün içine *style.css* adında bir dosya oluşturalım ve bu dosyamızı düzenlemek üzere açalım. Bu aşamada klasör yapımız şu şekilde olacak.

flask-blog  
├───static  
│   └───css  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└───style.css  
├───templates  
│   └───base.html  
│   └───index.html  
│   └───login.html  
├───app.py 


Bu aşamada style.css dosyasını tamamen kendi zevkinize göre oluşturmalısınız. Ancak bu dökümanda -Orhun Yazıtları'na benzememesi için- *CSS* kullanımına değinmeyeceğiz. Eğer bir workshopda bu dökümanı takip ediyorsanız hazır örnek üzerinde değişiklikler yapabilirsiniz. *style.css* dosyamızı oluşturmaya başlamadan önce bu dosyamızı *base.html* dosyamızda içeri aktaralım. Bunun için *head* HTML etiketinin içine, *title* etiketinden sonra aşağıdaki gibi bir satır ekleyeceğiz.

~~~~html
{%raw%}<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">{%endraw%}
~~~~

Eklediğimiz etiketin *href* özelliğine de bir tema motoru etiketi yazdığımızı görüyorsunuz. Bu etiket ziyaretçiye gönderilecek HTML dosyası oluşturulmadan önce istediğimiz dosyanın -ki bu örnekte css içindeki style.css dosyası- tam adresini oluşturup o kısıma ekleyecek. İsterseniz blogunuzu pipenv ile başlatıp sayfa kaynağını görüntüleyerek kontrol edebilirsiniz.

~~~~css
body,html {
  margin:0;
  padding:0;
}

main{
	width: 50%;
	margin: 0 auto;
}

header{
	background-color: orange;
	font-size: 32px;
}

main div:not(:last-child){
	border-bottom: 2px dotted black;
}
~~~~

Ben *style.css* dosyamı bu şekilde hazırladım. Evet tasarım anlayışımın çok kısıtlı olduğunun farkındayım, sizlerin çok daha güzellerini yapacağınıza eminim. Hazırladığınız style.css dosyalarını bana mail olarak gönderirseniz buradaki basit örnekle değiştirmeyi çok isterim :) Şuanda ana sayfamın son hali aşağıdaki gibi.

![]({{ "/assets/images/flask_document/styled.jpg" | absolute_url }})

Tasarım için bukadar vakit ayırdığımız yeter. Şimdi işin eğlenceli kısımlarına dönelim.

# Veritabanı Modelleri

Bir blog sitesi hazırladığımızı tekrar düşünürsek bu blogun verilerini -editör bilgileri, yazılar- tutması için bir depoya ihtiyacı var. İşte bu yüzden bir veritabanı kullanmamız gerekiyor. Veritabanı olarak sqlite kullanacağız. Şuanda basit bir şey yaptığımız ve çok fazla veritabanı sorgusu oluşturmayacağımız için sqlite bize yetecektir. Veritabanı ile Flask fonksiyonlarımızı *sql* adındaki bir dil ile haberleştirebiliriz. Ancak biz bu yöntemi kullanmak yerine *ORM* adı verilen ve veritabanı sorgu işlerimizi kolaylaştıran yardımcı ara katmanlardan birini kullanacağız. ORM kütüphanesi olarak bu dökümanda PeeWee kullanmaya karar verdim, o yüzden pipenv ile oluşturduğumuz sanal ortama peewee kütüphanesini de kurmamız gerekiyor. Pipenv ile bu işi kolayca yaptığımızı hatırlayabiliriz. Bir terminal ile proje klasörümüze girip (flask-blog) **pipenv install peewee** komutunu vermemiz yeterli.

Peewee'yi kurduğumuza göre kullanmanın vaktidir! *app.py* dosyamıza girelim ve en başa **from peewee import \*** komutunu ekleyerek peewee'yi içe aktaralım. Şimdi veritabanı işlemlerimizi yapabilmemiz için tanımlanmış bir veritabanına ihtiyacımız var. Bu bağlantıyı da oluşturduğumuzda app.py dosyamızın ilk satırları aşağıdaki gibi görünecek.

~~~~python
from flask import Flask, render_template
from peewee import *

app = Flask(__name__)
database = SqliteDatabase('database.sql')
~~~~

Sıradaki yapmamız gereken iş ise modellerimizi oluşturmak. Modeller, veritabanındaki tabloların (verilerin tutulduğu yerlerin) oluşturulması, yönetilmesini sağlayacağımız araçlar olacak. Bizim ihtiyacımız olan iki model var, birincisi editörün kullanıcı adı ve şifre verisinin tutulacağı **Editor** modeli bir diğeri ise blog yazılarının tutulacağı **Post** modeli. Modellerimizi *database* tanımlamamızdan hemen sonra tanımlayacağız. Onları da oluşturup üzerine konuşalım. 

~~~~python
class Editor(Model):
    class Meta:
        database = database

    username = TextField()
    password = TextField()

class Post(Model):
    class Meta:
        database = database

    title = TextField()
    content = TextField()
~~~~

Bu ikişer satırlık iki tablo (her model databasedeki bir tabloyu temsil ediyorve her ikisi de iki farklı satıra/değere sahip) projemizin şu aşamasında bize yeterli. Projemiz genişledikçe tablolarımızı da genişletebilir, yeni tablolar ekleyebiliriz. **app.py** dosyamızı kaydedelim ve hazırladığımız modellerin veritabanımızda da oluşmasını sağlayalım. Bunun için yine bir terminal açıp proje dizinimize girelim ve **pipenv run python** komutu ile sanal ortamımız içinde bir python çalıştıralım. Daha sonra yapacaklarımız ise app.py dosyasını içeri aktarmak ve daha sonra oradaki mevcut database değişkenimiz üzerinde hazırladığımız modelleri oluşturmak olacak.

~~~~shell
C:\Users\bisguzar\Desktop\flask-blog
λ pipenv run python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from app import *
>>> database.create_tables([Editor, Post])
~~~~

Yazdığımız iki satıra bakacak olursanız yukarıda belirttiğim işlemleri yaptığımızı görebilirsiniz. Herhangi bir hata oluşmadı ise hiçbir çıktı almamış olmalısınız. Daha sonra proje dosyanızı kontrol ettiğinizde orada *database.sql* adında bir dosya oluştuğunu görebilirsiniz. Bu dosya peewee'nin üzerinde çalışacağı ve verilerimizin tutulacağı veritabanımız.

Şimdi hazır veritabanı tablolarımızı oluşturmuşken terminalimizi kapatmayalım ve ilk editörümüzü de oluşturalım. Ama burada dikkat etmemiz gereken bir nokta var. Editörümüz için gireceğimiz bilgiler kullanıcı adı ve parola. Peki şifreyi düz metin olarak veritabanında saklamak mantıklı mı? Şuan biz lokalde çalıştığımız için aslında evet diyebilirsiniz, yanlışayamam da. Ama daha geniş bir projede birçok kullanıcının şifresinin bulunduğunu varsayarsak ve kötü amaçlı birilerinin veritabanınıza erişim sağladığını düşünürsek bu felaket olur. O yüzden bazı şifreleme yöntemleri ile parolayı şifreleyip [(şifre ile parola arasındaki fark için tıklayın)](https://eksisozluk.com/sifre-ile-parola-arasindaki-fark--1132529){:target='_blank'} saklayacağız. 

Parolayı şifrelemek için Flask ile birlikte zaten kurulmuş olan **werkzeug** kütüphanesinin **security** sınıfından **generate_password_hash** fonksiyonunu kullanacağız. Biraz uzun bir cümle olduğunun farkındayım ama yaparken çok kolay olduğunu göreceksiniz :D. Bu fonksiyona bir metin veriyoruz -ki bu bizim kullanmak istediğimiz parola oluyor- ve fonksiyon bize bu parolanın şifrelenmiş halini veriyor. Hadi bunu zaten açık olan terminalimizde deneyelim. 

~~~~shell
>>> from werkzeug.security import generate_password_hash
>>> generate_password_hash('123')
'pbkdf2:sha256:50000$QiivRF34$ae92386b5de080073206455bc7384f42c83e70d313cac2f76b2b9d991671114b'
~~~~

Önce gerekli fonksiyonumuzu içe aktardık, daha sonra fonksiyonumuza şifrelemesi için '123' verisini verdik ve o da bize şifrelenmiş halini döndürdü. Şifrelenmiş hali gördüğünüz gibi çok karmaşık bir yapı. Bu yapının geri döndürülmesi mümkün değil. Peki biz giriş yaparken nasıl şifreleri karşılaştıracağız? Kullanıcının giriş yaparken belirttiği parolayı da şifreleyip veritabanındaki ile karşılaştıracağız. Yani biz kullanıcının parolası ile ilgilenmeyeceğiz. Şimdi buradan şifrelenmiş parolamızı kopyalayalım (tırnak işaretleri hariç) ve bir kenara not edelim, hemen birazdan lazım olacak.

Yine açık olan terminalimizde bir editör kaydı oluşturalım.

~~~~python
>>> Editor.create(username='bisguzar', password='pbkdf2:sha256:50000$QiivRF34$ae92386b5de080073206455bc7384f42c83e70d313cac2f76b2b9d991671114b')
<Editor: 1>
~~~~

Zaten app.py dosyamızdaki her şeyi içeri aktarmıştık, yani Editor modelimiz de çalıştırdığımız etkileşimli kabukta mevcuttu. Biz de onu kullanarak yeni bir kayıt oluşturduk. Username ve password değerlerini kendinizinkilerle değiştirmeyi unutmayın!

Modellerle işimiz şimdilik bukadar. Şimdi blogumuzun tüm hamallığını yapacak olan arka tarafı yazmaya başlayabiliriz.

# Back-end'i Hazırlayalım

Aslında şimdiye kadar birçok şeyi hallettik, bundan sonra yapacağımız işlemler sitemizi hazırlamak için son adımlar. Öncelikle her sayfayı farklı bir fonksiyonun ve bağlantı noktasının hazırladığından bahsetmiştik. O yüzden sayfalarımız için yeni fonksiyonlar oluşturmalıyız. Şu anda zaten '/' adresine bağlı *hello_world* adında bir fonksiyonumuz mevcut. Hadi fonksiyonumuzun adını *hello_world* değil de *index* olarak değiştirelim. Websitelerinde ana bağlantı noktasını karşılayan her şeye **index** diyoruz. Hatırlarsanız şablonunun adını da *index.html* koymuştuk. Fonksiyonumuz şu aşamada son olarak aşağıdaki gibi görünecek.

~~~~python
@app.route('/')
def index():
    return render_template('index.html')
~~~~

## Fonksiyonlarımızı Oluşturalım

Ancak bizim blogumuz sadece index'den -yani ana sayfadan- ibaret değil. Editörlerin giriş yapabileceği ve yazı ekleyebileceği iki ayrı sayfamız daha var. Onlar için de birer fonksiyon oluşturup decaratör ile bağlantı adreslerini ayarlamamız gerekiyor. Hadi şimdi adı **login** olan ve **/girisyap** bağlantı noktasına bağlanmış bir fonksiyon oluşturalım. Ve aynı zamanda bu fonksiyonumuz da değer olarak bir temayı döndürecek, *login.html* temasını. 

~~~~python
@app.route('/girisyap')
def login():
    return render_template('login.html')
~~~~

Aynen bu şekilde görünüyor olmalı. Sanırım fonksiyon adı, bağlantı noktası ve şablon döndürme konularını anladık. O zaman sıra sizde. Şimdi de adı **newpost** olan, **/yaziekle** adresine bağlı ve **newpost.html** şablonunu döndüren bir fonksiyon oluşturun. Daha sonra buradaki örnek ile kıyaslayın. Hata yapmaktan korkmayın.

~~~~python
@app.route('/yaziekle')
def newpost():
    return render_template('newpost.html')
~~~~

Son eklediğimiz fonksiyon da böyle görünüyor olmalı. Şimdi yaptığımız tüm değişikliklerden sonra *app.py* dosyamız nasıl görünüyor ona bir bakalım, eğer aralarda bir şeyleri kaçırmışsanız düzenleme şansınız olsun.

~~~~python
from flask import Flask, render_template
from peewee import *

app = Flask(__name__)
database = SqliteDatabase('database.sql')


class Editor(Model):
    class Meta:
        database = database

    username = TextField()
    password = TextField()


class Post(Model):
    class Meta:
        database = database

    title = TextField()
    content = TextField()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/girisyap')
def login():
    return render_template('login.html')


@app.route('/yaziekle')
def newpost():
    return render_template('newpost.html')


if __name__ == "__main__":
    app.run(debug=True)
~~~~
 
Sırasıyla import (içe aktarma) işlemlerimizi yaptık, tanımlamalarımızı yaptık, modellerimizi hazırladık, fonksiyonlarımızı hazırladık ve son olarak projemizi çalıştırma komutumuzu yazdık.

## Giriş/Çıkış Yapısını Hazırlayalım

Her şey çok güzel görünüyor, bir /yaziekle sayfamız var. Ama bu sayfaya sadece siteye giriş yapmış editörlerin erişebilmesi gerekiyor. Yoksa siteye giriş yapan tüm ziyaretçiler yeni yazı ekleyebilir ve bunu pek istemeyiz. Aslında belki isteyebiliriz, ziyaretçi defteri yapmış oluruz. Ama bu seferlik istemediğimizi varsayarak ilerleyelim. Bunun için öncelikle üye girişi sayfamızı hazırlamamız gerekiyor. Zaten *login* fonksiyonumuz mevcut onun üzerinde çalışabiliriz. Ama bundan önce http metodları hakkında biraz bilgi sahibi olmamız gerekiyor. Açıklayacağım iki farklı metod var ve bu metodları kabaca inceleyeceğiz.

**GET**  
GET metodumuz aslında veri isterken kullanılır. Burada referans noktamız ziyaretçi. Yani ziyaretçi bizden veri isterken GET metodunu kullanacaktır. Veri istemekten kastımız Ahmet'in bakkaldan yoğurt istemesi gibi ziyaretçinin html verisini istemesidir. GET kelime anlamı olarak da almak, edinmek anlamlarına gelir.

**POST**  
POST metodumuz ise yine ziyaretçimizin bizden veri istemek yerine bize veri göndermesi için kullanılır. Bu sefer veriyi yakalayan biz, gönderen ziyaretçi olacaktır. POST da kelime anlamı olarak posta, mektup anlamlarına gelir.

Biz aslında fonksiyonlarımızı oluştururken fonksiyonların kabul edeceği HTTP metodlarını da belirtiyoruz. decaratöre nasıl bağlantı noktasını belirtiyorsak **methods=['METOD1', 'METOD2']** diyerek fonksiyonun kabul edeceği metodları da belirtebiliyoruz. Eğer belirtmezsek Flask bizim için sadece *GET* metodunu kabul edecek şekilde düzenliyor fonksiyonlarımızı. Ancak biz *login* metodumuzda bir form aracılığıyla veri almak istiyoruz ziyaretçiden. O yüzden POST metodunu da kabul etmemiz gerekiyor. O zaman hadi decaratörümüzü düzenleyelim ve son haline bir bakalım.

~~~~python
@app.route('/girisyap', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
~~~~

Bu görünümü aldı fonksiyonumuz ve onun decaratörü. POST metodunu formdan gelen verileri kabul edebilmek için ekledik ama aynı zamanda kullanıcı veri gönderebilmek için formu görebilmeli. Yani bize veriyi *POST* etmeden önce form yapısını *GET* edebilmeli. Biliyorum plaza ağzı gibi oldu, ama yapacak bir şey yok :(. Mantık şöyle işliyor; ziyaretçi /girisyap sayfasına girer ve önüne bir form çıkar (burada GET metodu ile bizden veri aldı), formu doldurur ve gönder butonuna basar (burada da POST metodu ile veriyi bize gönderdi).

Eğer böyle bir durum varsa biz bir fonksiyonda birden fazla iş yapacağız demektir. Eğer form verisi geldiyse (yani method POST ise) giriş işlemlerini yapacağız ve şifreyi kontrol edeceğiz, eğer böyle bir durum yoksa ziyaretçi formu görmek istemiş demektir o zaman da form göstereceğiz. Bunları yaparken Flask'ın request sınıfını kullanacağız. O yüzden onu da importlarımız arasına ekleyelim. Ancak onunla beraber farklı yapılar da kullanacağız. O yüzden farklı sınıfları/fonksiyonları da ekliyoruz, ilerleyen zamanlarda onları da açıklayacağım.

~~~~python
from flask import (Flask, render_template, request,
                   redirect, url_for)
~~~~

Son olarak durum böyle. Şimdi *login* fonksiyonumuzu yazalım. Ben hazırlayıp geliyorum, üzerinde konuşalım.

~~~~python
@app.route('/girisyap', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for('index'))

    return render_template('login.html')
~~~~

Son durumu bu olan login fonksiyonumuza neler eklemişiz bir bakalım. Açıklamaya geçmeden hemen önce Python hakkında bir bilgi vermek istiyorum. Her fonksiyon bir tane değer döndürebilir. Yani bir şey aynı zamanda hem elma hem de armut olamaz. O yüzden eğer bir fonksiyon oluşturup için birden fazla return ifadesi yazıp çalıştırırsanız ilk değerin döndürüldüğünü, sonraki değerlerin ise çalışmadığını göreceksiniz. Çünkü Python döndürecek bir değer bulduğu zaman o fonksiyon ile işi bittiğini düşünür ve sonrakilere bakmaz bile. Bu aklımızda kalsın, çünkü hazırladığımız fonksiyonda da böyle bir durum söz konusu.

Hadi şimdi inceleyelim. 3. satırda bir şart koşmuşuz. Şartımız ziyaretçimizin *POST* metodunu kullanmış olması. Eğer metod POST ise bu şartımızdaki kodlarımız çalışacak. Ama eğer metodumuz POST değilse -ki bu durumda metod kesinlikle GET'dir. çünkü fonksiyonumuz diğer metodları şuanda kabul etmiyor. listeye eklemedik- 9. satır çalışacak ve ziyaretçiye form bilgisini döndürecek. 

Varsayalım ki kullanıcı POST metodunu kullandı, yani formu doldurup butona bastı ve bize veri postaladı, gönderdi. Şimdi şartımızın içindeki kodlarımız çalışacak, 4. ve 5. satırlarda kullanıcının doldurduğu formdaki *'username'* ve *'password'* verilerini aldık ve yine aynı isimlerdeki değişkenlere atadık. Şifre karşılaştırması yaparken bunlara ihtiyacımız olacak. Daha sonra ise ilk kez gördüğünüz fonksiyonları kullanarak bir şeyler yaptık. Aslında burada yaptığımız şey çok basit, *redirect* fonksiyonunu ziyaretçiyi yönlendirmek istediğimiz zaman kullanıyoruz. Ancak bu fonksiyon tam bir adres istiyor yönlendirmek için, yani argüman olarak bir URL istiyor. Biz de bu URL'yi *url_for* fonksiyonu ile oluşturuyoruz. Bu fonksiyon da metin olarak yönlendirme yapmak istediğimiz fonksiyonun adını alıyor ve onun için bir URL oluşturup döndürüyor. Yani orada zincirleme fonksiyon tamlaması gibi bir şey var :D.

Şimdi elimizde kullanıcı adı ve şifre verileri de olduğuna göre kullanıcıyı giriş yaptırabiliriz. Bunun için yine Flask sınıfı olan **session**'u içeri aktarmamız gerekiyor.

~~~~python
from flask import (Flask, render_template, request,
                   redirect, url_for, session)
~~~~

Session'lar nedir? Sessionlar sunucu tarafında tutulan değerlerdir. HTTP methodlarından bahsetmiştik. Farkettiyseniz her seferinde bir istek-cevap mantığı ile çalışıyor. Yani bir süreklilik yok. İstek gönderiliyor, cevap alınıyor ve iletişim kesiliyor. Her istek için yeniden iletişim kuruluyor. Bu yüzden bazı verileri bizim farklı yöntemler ile tutmamız gerekiyor. Sessionlar da bu yöntemlerden biri. Sessionların sunucu tarafında tutuluyor olması da cookilerden en büyük farkıdır. Cookiler client tarafında, yani ziyaretçinin tarayıcısında tutulur ve değiştirilebilirlerdir. Güvenlik önlemi olarak değiştirilebilir bir şey kullanmak çok da mantıklı değil gibi. Aynı zamanda sessionlar şifrelenir, bu şifrelemede sizin belirlediğiniz bir metin kullanılır. O yüzden gelin öncelikle şifreleme metinimizi tanımlayalım. Unutmamanız gereken şeylerden biri de bu metinin gizli kalması gerektiği ve olabildiğince karmaşık olması gerekiyor.

*app.py* dosyamızı açalım ve app değişkenini tanımladıktan sonra onun **secret_key** değerini değiştirelim. Siz kendinize özel bir metin belirlemeyi unutmayın ve kimseyle paylaşmayın.

~~~~python
from flask import (Flask, render_template, request,
                   redirect, url_for, session)
from peewee import *

app = Flask(__name__)
app.secret_key = 'çok_gizli_ve_karmaşık_metin'
database = SqliteDatabase('database.sql')
~~~~

Sonuç olarak *app.py* dosyamızın başı buna benzer görünüyor olmalı. Şimdi tekrar *login* fonksiyonumuza dönebiliriz, birazdan bu session konusuna tekrar geleceğiz. Bu sadece ön hazırlıktı.

Şimdi kullanıcının girdiği username ve password verilerini kullanarak bilgileri doğrulamamız gerekiyor. Peki bunu nasıl yapacağız? Mantığımız basit, kullanıcının girdiği kullanıcı adına sahip satırı veritabanımızdaki *editor* tablosundan çekeceğiz ve yine kullanıcının girdiği parolanın şifrelenmiş hali ile bu satırdaki kayıtlı şifrenin aynı olup olmadığını kontrol edeceğiz. Bu şifre karşılaştırması için yine *werkzeug* kütüphanesinden yararlanacağız o yüzden ilgili satırı sayfamızın başındaki import'ların arasına ekleyelim.

~~~~python
from werkzeug.security import check_password_hash
~~~~

Bu fonksiyon düz parolayla şifrelenmiş parolayı kıyaslamak için kullanacağımız fonksiyon. Bu da bir kenarda dursun, az sonra kullanacağız kendisini. Önce girilen kullanıcı adını içinde barındıran satırı veritabanından çekmeliyiz. 

~~~~python
database_record = Editor.select().where(Editor.username == username)[0]
encrypted_password = database_record.password
~~~~

Bu kod bloğuyla veritabanındaki verilerin içinde *'username'* sütunu kullanıcının girdiğiyle aynı olan satırları çektik (öyle bir satır veritabanında bir tane olsa bile dönen veri çoğul olacaktır. O yüzden dönen verinin de ilkini aldık.) ve o satırın *'password'* değerini alıp bir değişkene atadık. Şimdi fonksiyonumuzun içinde geriye kalan kısımları da hazırlayıp üzerine konuşalım.

~~~~python
@app.route('/girisyap', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        database_record = Editor.select().where(Editor.username == username)[0]
        encrypted_password = database_record.password

        if check_password_hash(encrypted_password, password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

    return render_template('login.html')
~~~~

Burada öncelikle 10. satıra bir koşul bloğu ekledik. Burada kullanıcının girdiği parola ile veritabanında kayıtlı olan şifresini karşılaştırdık. Eğer doğruysa 11. satırda sessionlara kullanıcının kullanıcı adını ekledik. Giriş doğrulaması yaparken yine sessionlar üzerinde kontrol yapacağız. 12. satırda ise giriş yapmış kullanıcıyı ana sayfaya yönlendirdik çünkü artık burası ile işi kalmadı. 14. satırda da kullanıcı adı ve şifresi eşleşmeyen kullanıcıyı tekrar giriş yapma sayfasına yönlendirdik.

Ancak burada şöyle bir durumu kaçırdık, giriş yapmış kullanıcının artık giriş yapma sayfasına erişememesi lazım, çünkü bir işi yok. Kullanıcının giriş yapıp yapmadığını sessionlar üzerinden kontrol edeceğiz demiştik. Eğer 'username' bilgisi sessionlarda yoksa kullanıcı giriş yapmamış demektir, varsa giriş yapmış demektir. Hadi düzenleyelim ve giriş yapmış kullanıcıları ana sayfaya yönlendirelim.

~~~~python
@app.route('/girisyap', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        database_record = Editor.select().where(Editor.username == username)[0]
        encrypted_password = database_record.password

        if check_password_hash(encrypted_password, password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

    return render_template('login.html')
~~~~

Yeni eklediğimiz 3. ve 4. satırda kullanıcı giriş yapmışsa onu direkt olarak ana sayfaya yönlendirdik. Giriş yapmış her kullanıcının çıkış da yapabiliyor olması gerekiyor. O yüzden bağlantı noktası '/cikis' olan yeni bir fonksiyon oluşturalım. Fonksiyonumuzun adı da logout olsun. Bu fonksiyonun yapacağı şey çok basit, eğer kullanıcı giriş yapmışsa (yani sessionlarda 'username' verisi varsa) sessiondan o veriyi silmeli ve kullanıcıyı ana sayfaya yönlendirmeli. Eğer bu veri yoksa kullanıcıyı giriş yapma sayfasına yönlendirmeli. Çünkü giriş yapmadan çıkış yapılamaz. Hadi bunu yazmaya çalışın, yazabiliyor olduğunuzu biliyorum. Ben yine de örneği hemen alt satıra bırakıyorum.

~~~~python
@app.route('/cikis')
def logout():
    if 'username' in session:
        session.pop('username')
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))
~~~~

Tüm fonksiyon bundan ibaret. Herhangi bir şablon döndürmesine ya da veri girilmesine gerek yok. Yaptığı iş çok basit. Eğer 'username' verisi sessionlarda varsa onu siliyor (yani kullanıcı çıkış yapmış oluyor) ve kullanıcıyı ana sayfaya yönlendiriyor. Aksi durumda da zaten giriş yapmış olmadığı için çıkış da yapamıyor ve giriş sayfasına yönlendiriyor.

Aslında şu anda giriş/çıkış yapısını oluşturduk ama düzenlememiz gereken ufak bir nokta daha kaldı. Hatırlarsanız base.html dosyamızda *giriş yap* diye bir alan oluşturmuştuk. Artık kullanıcılarımız giriş yapabiliyor, ama giriş yapan kullanıcılar da aynı yazıyı görüyor. Giriş yapan biri daha ne kadar/nereye kadar giriş yapabilir ki? :/. Onu giriş yapmış kullanıcılar için *çıkış yap* olarak değiştirmeliyiz ve bağlantı adresini de /cikis olarak ayarlamalıyız. Bunu yapmak da aynı mantığa dayanıyor. Sessionları kontrol edeceğiz. Bu işlemi Jinja2 sayesinde html dosyalarının içinde yapabiliyoruz. Hemen base.html dosyasını düzenleyelim.

~~~~html
{%raw%}<!DOCTYPE html>
<html>
<head>
    <title>Benim Blogum - {% block title %}{% endblock %}</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
<header>
    <main>Benim Blogum</main>
</header>
<main>
    <nav>
        {% if 'username' in session %}
            <a href="/cikis">çıkış yap</a>
        {% else %}
            <a href="/girisyap">giriş yap</a>
        {% endif %}
    </nav>
    <content>
        {% block main %}{% endblock %}
    </content>
</main>
</body>
</html>{%endraw%}
~~~~

*base.html* dosyasını bu şekilde düzenledim. Gördüğünüz gibi html dosyalarının içinde de koşul blokları oluşturabiliyoruz. Sözdizimi biraz farklı oluyor ancak yapabiliyoruz. Bu sayede artık giriş yapmış kullanıcılar *giriş yap* butonu yerine *çıkış yap* butonunu görüyor ve çıkış yapabiliyor. Şimdi pipenv ile projenizi başlatıp test edebilirsiniz. Bununla oynamak çok zevkli ^^.

## Yazı Ekleme Sayfasını Ayarlayalım

*newpost* adında bir fonksiyonumuz daha var oluşturduğumuz. Hadi şimdi bu fonksiyonumuzu hazırlayalım ve editörlerimiz yeni yazılar eklemeye başlayabilsin. Ama önce bir güvenlik önlemi hazırlamamız gerekiyor, çünkü giriş yapmamış kullanıcılar bu sayfaya erişememeli. Fonksiyonumuzun içinde öncelikle session kontrolu yapalım eğer giriş yapılmamışsa giriş yapma sayfasına yönlendirelim, giriş yapılmışsa yapacaklarımıza sonra geleceğiz.

~~~~python
@app.route('/yaziekle')
def newpost():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('newpost.html')
~~~~

Şu anda fonksiyonumuzun durumu bu. Yaptığımız şey ise eğer kullanıcı giriş yapmamışsa ana sayfaya yönlendirmek, eğer giriş yapmışsa ise koşul bloğumuz çalışmayacağı için kullanıcı *newpost.html* şablonumuzu görecek. Şimdi ise form'dan gelen verileri yakalamamız gerekiyor. Hatırlarsanız form'dan verileri yakalarken *POST* metodunu kullanıyorduk. Bu da demek oluyor ki bu fonksiyonumuzun kabul ettiği metodları da değiştirmeliyiz.

~~~~python
@app.route('/yaziekle', methods=['GET', 'POST'])
~~~~

Fonksiyonumuzun decaratör satırını bu şekilde düzenlememiz yeterli. Şimdi giriş kontrolünden sonra bir de methodu kontrol edelim ve method POST ise formdan gelen verileri yine aynı isimdeki değişkenlere atayalım.

~~~~python
if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
~~~~

Şimdi ise elimizdeki bu verileri kullanarak veritabanına yeni yazı kaydı eklememiz gerekiyor. Benzer bir işlemi ilk editör kaydını oluştururken yapmıştık, çok yabancı olduğumuz bir konu değil yani.

~~~~python
Post.create(title=title, content=content)
~~~~

Diyerek kullanıcıdan aldığımız title ve content bilgileriyle bir veritabanı kaydı oluşturduk. Bu işlemden sonra kullanıcıyı tekrar ana sayfaya yönlendirebiliriz. Fonksiyonumuz son olarak aşağıdaki gibi görünüyor olacak.

~~~~python
@app.route('/yaziekle', methods=['GET', 'POST'])
def newpost():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        Post.create(title=title, content=content)
        return redirect(url_for('index'))

    return render_template('newpost.html')
~~~~

Şimdi de giriş yapmış kullanıcıların yazı ekleme sayfasına erişebilmesi için *base.html*'deki nav etiketine bir ekleme daha yapalım ve bu sayfanın adresini verelim.

~~~~html
{%raw%}<nav>
    {% if 'username' in session %}
        <a href="/cikis">çıkış yap</a>
        <a href="/yaziekle">yazı ekle</a>
    {% else %}
        <a href="/girisyap">giriş yap</a>
    {% endif %}
</nav>{%endraw%}
~~~~

base.html dosyamızdaki *nav* etiketinin son durumu böyle oldu. Son olarak hadi ilk yazımızı ekleyelim. Ben kısacık bir teşekkür içeren bir yazı ekleyeceğim, siz de istediğiniz herhangi bir konuda bir şeyler yazabilirsiniz. Neticede bu sizin blogunuz :).

## Ana Sayfayı Düzenleyelim

*index.html* (yani ana sayfa) şablonumuzu hazırlarken hatırlarsanız iki tane temsili yazı eklemiştik. Şimdi o yazıları temsili olmaktan çıkaralım ve gerçek yazılarımızı ana sayfada göstermeye başlayalım. Bunun için öncelikle *index* fonksiyonumuzda yazıları listelememiz ve onu Jinja2'ye göndermemiz gerekiyor. Hadi önce bunu çözelim.

~~~~python
@app.route('/')
def index():
    posts = Post.select()
    return render_template('index.html', posts=posts)
~~~~

Burada 3. satırda tüm yazıları veritabanından çektik ve 4. satırda da bu yazıları Jinja2'ye gönderdik. Çünkü index.html şablonumuzda kullanacağız bunları. Hatta madem verileri o tarafa gönderme işlemini hallettik, biz de o tarafa geçelim ve gelen verileri alıp parçalayalım. Yapacaklarımızı bi özetleyeyim şimdiden. Gelen verileri alıp bir döngü oluşturacağız. Çünkü şuan bir tane olsa bile ileride yazı ekledikçe birden fazla yazımız olacak. Her yazıyı yazdırmak istiyoruz biz, döngü kullanarak bunu yapabiliriz. Daha sonra döngünün içinde gelen her yazı için yeni bir alan oluşturup onu yazdıracağız. Şimdi düzenleyelim ve üzerine konuşalım.

~~~~html
{%raw%}{% extends 'base.html' %}

{% block title %} Ana Sayfa {% endblock %}

{% block main %}

    {% for post in posts %}
        <div>
            <h2>{{ post.title }}</h2>
            <p>{{ post.content|safe }}</p>
        </div>
    {% endfor %}

{% endblock %}{%endraw%}
~~~~

Farkettiyseniz önceden iki üç tane HTML etiketi vardı, şimdi neredeyse onlar da kalmadı :D. Çünkü bizim yerimize Jinja2 o etiketleri oluşturuyor ve ziyaretçinin isteğine cevap vermek üzere Flask'a iletiyor. 7. satırda bir döngü oluşturduk ve 9-10. satırlarda bu döngüden gelen yazının içeriğini yazdırdık. Her şey bundan ibaret. Farkettiyseniz Jinja etiketlerini {%raw%}*{% %}*{%endraw%} kullanarak yazıyorduk ama 9-10. satırlarda {%raw%}*{{ }}*{%endraw%} yapısını kullandık. Jinja'da bir şeyi ekrana yazdırmak istediğimizde ikili süslü parantez kullanıyoruz, eğer kod yazıyorsak süslü parantezlerle birlikte yüzde işareti kullanıyoruz. Genelde tema motorlarının çoğunda bu yapı aynıdır.

Ben hızımı alamadım, bir yazı daha ekleyip geliyorum.

![]({{ "/assets/images/flask_document/son_hali.jpg" | absolute_url }})

Şu anda blogumuzun son hali böyle. Farkettiyseniz ikinci yazı birinciden daha okunaklı. Çünkü yazılarımız HTML kullanmamıza izin veriyor ve ben de HTML ile birkaç satır boşluk bırakarak paragraflara ayırdım. Aklınızda olsun bu özellik de.

Şuana kadar oluşturuğumuz tüm dosyların Github'daki **[bisguzar/flask-blog](https://github.com/bisguzar/flask-blog){:target='_blank'}** deposunda bulunduğunu hatırlatmak istiyorum. Yani blogumuzun son hali orada da var ^^ Geri bildirimlerinizi iletmekten çekinmeyin.

# Devam Etmek İsteyenler İçin

Bu yazı Flask için çok hızlandırılmış bir yazıydı. Ancak ona rağmen session yönetimi, Jinja2 tema motoru, HTTP metodları, ORM yapısı gibi temel ve önemli konular hakkında fikir edindik. Öğrendik diyemiyorum çünkü bu konular çok kapsamlı, öğrenmek malesef öyle kolay değil. O yüzden ben de araştırmaya ve öğrenmeye devam etmek isteyenler için buraya bazı adresler bırakıyorum. Kesinlikle kurcalamanızı öneriyorum! 

Not: Tüm adresler İngilizce.

* https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works
* https://docs.pipenv.org/
* http://flask.pocoo.org/
* http://jinja.pocoo.org/docs/2.10/
* http://docs.peewee-orm.com/en/latest/
* http://werkzeug.pocoo.org/
* https://www.tutorialspoint.com/http/http_methods.htm

[^1]: Bu tabir biraz garip. Yabancıların 'run' etmek tabirini biz ayağa kaldırmak olarak kullanıyoruz. Yani çalışır duruma gelmesi.
[^2]: pipenv run python app.py
