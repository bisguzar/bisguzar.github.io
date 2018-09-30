---
layout: post
current: post
cover: 'assets/images/flask/blueprint.jpg'
navigation: True
title: Flask Blueprint Yapısı
date: 29-08-2018 13:41:03
tags: flask
class: post-template
subclass: 'post'
author: bisguzar
---

**İçerik Listesi**
1. TOC
{:toc}

<hr style="margin: 10px !important;">

# Blueprint Nedir?

Blueprint kelime olarak *taslak* anlamına geliyor. 

Eğer daha önce *Django* kullandıysanız *Django* projelerinin uygulamalardan (apps) oluştuğunu deneyimlemişsinizdir. Örneğin bir sosyal medya sitesi hazırlıyorsunuz, bu sitede üyelik işlemlerini (kayıt ol, giriş yap, profil) gerçekleştirmesi için bir alt-uygulama, ana yapı (dashboard) için bir uygulama oluşturabiliriz. Böylelikle büyük bir projeyi parçalara bölerek organizasyonu kolaylaştırıp modüler bir yapı elde edebiliriz. 

Aynı seneryoyu **Flask**da da yapabiliriz. Yani projemizi parçalar halinde oluşturabilir böylelikle proje yönetimini kolaylaştırabiliriz.


# İlk Blueprintimizi Oluşturalım

Flask proje klasörümüz içinde yeni bir dosya oluşturalım ve adını dashboard_core.py koyalım (siz kendinize göre isim verebilirsiniz tabiki, isimlendirme yaparken işlevini en net ve kısa şekilde belirtmesine dikkat etmeliyiz. ‘There are only two hard things in Computer Science: cache invalidation and naming things.’ - Phil Karlton).

~~~~python
from flask import Blueprint


dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/dashboard')
def homepage():
    return 'Şu an dashboard app\'ının içindeyim'
~~~~

Bu kadarcık tanımlamayla aslında bir app (*app* kelimesini projenin bir bölümü, alt uygulaması anlamında kullandığımızı hatırlayalım) oluşturabiliyoruz. Şimdi biraz bu satırları inceleyelim. Projemizi flask ile hazırladığımız için yine flask'ın app oluşturmak için kullandığımız kütüphanesi olan *Blueprint*'i projemize dahil ediyoruz.

4\. satırda ise projemize dahil ettiğimiz *Blueprint* sınıfının bir örneğini oluşturuyoruz. Aslında tam bu aşamada app'ımızı hazırlıyoruz. Verdiğimiz ilk değer app'ımızın adı. İkinci değer ise içe aktarılırken kullanılacağı parametre. Onun haricindeki tüm değerler tercihe bağlı olarak tanımlanabilir. Sonraki satırlar zaten flask kullanımından alışkın olduğumuz şey, bir fonksiyon tanımlayıp onu da bir adrese bağladık. Burada dikkat edilmesi gereken şey *route* decaratorünün oluşturduğumuz app örneğinden aldığımız (ben ana dosyadaki flask'ın Flask sınıfının örneğini de buraya aktarıp import loopa sokmuştum, sonra insan iki gün sorun ne diye arıyor).

Şu anda aslında bir app oluşturduk, oluşturduğumuz app'ı flask'a haber vermemiz gerekiyor. Bunun için ana flask sınıfının **register_blueprint** fonksiyonunu kullanacağız. Ana flask sınıfından kastım *app = Flask(_\_name__)* tanımlamasını yaptığımız dosya (değişkenin adını farklı belirlemiş olabilirsiniz). Bu dosyaya app'ımızı dahil ediyoruz. Eğer ikisinin app dosyamız ile bu dosyanın aynı dizinde olduğunu varsayarsak **from dashboard_core import dashboard** diyerek içe aktarma işlemimizi yapabiliriz. Daha sonrasında ise tanımlama işlemi kaldı. Onun için de **app.register_blueprint(dashboard)** dememiz yeterli.

Şimdi projenizi çalıştırıp /dashboard sayfasına girerseniz oluşturduğunuz app'ın içindeki fonksiyonun döndürdüğü değeri göreceksiniz. Buraya kadar herhangi bir hatayla karşılaşmadıysanız başarıyla bir uygulama (app) oluşturdunuz.


# Proje Dosya Yapısı

Eğer projemizi modüller halinde inşa edeceksek dosyalamayı da çok düzenli yapmalıyız, örneğin A app'ının template dosyaları B app'ının dizininde durmamalı. Onlarca app bulunan bir projede böyle bir durum çıkmaza yol açacaktır. Bunun için sizlere en çok tercih edilen iki yöntemi göstereceğim. Tabii siz kendi istediğiniz yapıyla da dosylama yapabilirsiniz. Ancak her zaman standartlaşmış yöntemleri kullanmak yararımıza olacaktır. En azından projeyi sonradan başka birisi geliştirmek durumunda kalırsa sizi daha az anacaktır.

Üç app'den oluşan bir projemiz olduğunu düşünelim. Sahip olduğumuz appler *userManagement*, *adminPanel* ve *dashboard* olsun. Aşağıdaki örnekleri de bu isimlendirmeleri kullanarak oluşturacağım.

## Fonksiyonel Yapı

Bu yapıda tüm applikasyon dosyalarınız ve bunların kullandığı statik (resim dosyaları, stil dosyaları vs.) dosyalar aynı dizinde bulunurken, applikasyonların tema dosyaları ise templates klasörü içinde kendi aralarında dosyalanmış şekilde bulunur. 


eşsizprojem/  
&emsp;\_\_init__.py  
&emsp;static/  
&emsp;templates/  
&emsp;&emsp;userManagement/  
&emsp;&emsp;adminPanel/  
&emsp;&emsp;dashboard/  
&emsp;views/  
&emsp;&emsp;\_\_init__.py  
&emsp;&emsp;userManagement.py  
&emsp;&emsp;adminPanel.py  
&emsp;&emsp;dashboard.py  
&emsp;models.py  

Proje dosyanız bu şekilde görünmeli, tabi eğer fonksiyonel dosyalama yapısını kullanmaya karar verdiyseniz. Bu durumda dashboard app'ını ele alalım. Bu app'ın back-end kodları, yani view kodları *dashboard.py* dosyasında olacak. Statik dosyları *static* klasöründe, tema/şablon dosyaları ise *templates/dashboard/* klasöründe olacak.

<p class="note">
Bu yazı hazırlandığı sıralarda flask'ın resmi sitesi de  (http://flask.pocoo.org) bu yapıyı kullanıyordu, hala kullanıyor da olabilir. <a href="https://github.com/pallets/flask-website/tree/master/flask_website">GitHub üzerinde</a> canlı görebilirsiniz.
</p>

## Bölünmüş Yapı

Bölünmüş yapıda applerin her birini tüm kendi alt dosyaları ile birlikte özel bir klasörde tutuyoruz. Çok karışık bir cümle oldu ama örnek üzerinde baktığınızda çok basit olduğunu göreceksiniz.

eşsizprojem/  
&emsp;\_\_init__.py  
&emsp;**userManagement**/  
&emsp;&emsp;\_\_init__.py  
&emsp;&emsp;views.py  
&emsp;&emsp;static/  
&emsp;&emsp;templates/  
&emsp;**adminPanel**/  
&emsp;&emsp;\_\_init__.py  
&emsp;&emsp;views.py  
&emsp;&emsp;static/  
&emsp;&emsp;templates/  
&emsp;**dashboard**/  
&emsp;&emsp;\_\_init__.py  
&emsp;&emsp;views.py  
&emsp;&emsp;static/  
&emsp;&emsp;templates/  
&emsp;models.py  

En üst seviyedeki *\_\_init__.py* dosyasında oluşturduğumuz Flask nesnesi ise bu tüm appleri kapsayacak ve projeyi bağlayıcı rol alacak.

## Hangisini Daha İyi?

Bu konu tamamen kişisel tercihlere bağlı. Yukarıda örneği bulunan iki yapı dışında da tamamen kendi oluşturacağınız bir yapıyı kullanarak bir proje inşa edebilirsiniz. Ancak ortak bir dil oluşturabilmek adına -tıpcıların latince kullanması gibi- benimsenmiş yapıları kullanmak her zaman daha avantajlı bir durum olacaktır. Bu yapılardan hangisini kullanacağınız ise sizin projenize hangisinin daha uygun olduğunu düşünmenize göre değişir.

Projeniz birden fazla ana parçadan oluşacaksa (yönetici paneli, kullanıcı paneli, ana sayfa) bölünmüş yapıyı kullanmanız ve her bölümün diğerlerinden tamamen bağımsız olmasını sağlamanız daha makul bir yol olacaktır. Ancak projenizdeki parçalar birbirinden kalın çizgilerle ayrılmıyorsa, örneğin applerinizin templateleri ortak bir stil dosyası (style.css) kullanıyorsa fonksiyonel dosyalama yapısı daha kullanışlı olabilir.

# İleri Seviye Kullanım

Flask'ın blueprint yapısı zaten yeterince kullanışlı değilmiş gibi ek olarak kullanabileceğimiz bazı özellikleri mevcut.

## URL Ön Eki

Blueprintimizi tanımlarken url_prefix niteliği tanımlamazsak bu değer varsayılan olarak / olacaktır. **profil** adında bir app oluşturduğumuz senaryosunu ele alalım. Bu app'ın alt sayfaları olarak ayarlar, resimler ve gonderiler sayfaları olmasını istiyoruz. Yani elimizde /profil, /profil/ayarlar, /profil/resimler, /profil/gonderiler seklinde 4 ayrı sayfa olmalı. Biz app'ın içinde sayfalarımızı tanımlarken urllerimizi bu şekilde tanımlayabileceğimiz gibi blueprinte bir URL ön eki verirsek kendimizi tekrarlamaktan kurtulmuş oluruz.

~~~~python
profil = Blueprint('profil', __name__, url_prefix='/profil')
~~~~

Şeklinde bir blueprint tanımlaması yaptığımızı düşünelim. Daha sonra da bu blueprintimizi kullanarak resimler sayfamızı oluşturalım.

~~~~python
@profil.route('/resimler')
def resimler():
    # Bir şeyler yap
    pass
~~~~

Bu şekilde oluşturduğumuz sayfamıza erişmek istediğimiz zaman sitemiz.uzantısı/profil/resimler adresine gitmemiz gerekiyor. Sebebi ise sayfamıza (diğer tanımlamayla fonksiyonumuza) /resimler URL'sini bağladık. Ancak sayfamızın dahil olduğu blueprint de /profil URL'sine bağlı. Bu durumda bu sayfaya erişmek isteyen bir kişi öncelike blueprintin bağlı olduğu noktaya erişecek sonrasında ise sayfaya erişecek diyebiliriz. Tabi olay tam olarak böyle işlemiyor, biz senaryolaştırıyoruz.

Şimdi durumu biraz daha karmaşıklaştıralım. Bu örneğimizi facebookdaki gibi bir duruma refactor edelim (tekrar düzenleyelim). Facebookda bu durum nasıl işliyor hatırlayalım. Örneğin johndoe kullanıcı adında biri oldun. Onun resimlerine girebilmek için facebook.com/profil/resimler adresine gitmiyoruz, bunun için kullanmamız gereken adres facebook.com/johndoe/resimler oluyor. Burada farkettiyseniz URL yapısı içerisinde bir kullanıcının kullanıcı adını kullandık. Yani orası değişkenlik gösterebiliyor demek bu. Orası aynı şekilde **joandoe** de olabilirdi. Bu yapıya dinamik URLler diyoruz. Orasını değişebilir kılıyoruz ve ne olduğunu da bir değişken olarak alıyoruz. Böyle bir yapıyı url_prefix niteliğini kullanmadan hazırlayalım hemen.


~~~~python
@profil.route('/<username>/resimler')
def resimler(username):
    # Bir şeyler yap
    pass
~~~~

Tekrarlıyorum, *url_prefix* tanımlaması yapılmadığını varsayıyoruz şu an bu nitelik varsayılan olarak / adresine tanımlı. Yani kısaca tanımlanmamış da diyebiliriz. Eğer tarayıcınızdan sitemiz.uzantısı/**johndoe**/resimler adresine giderseniz **resimler** adındaki fonksiyonumuzun username değeri 'johndoe'ye eşit olacak. Bunu da fonksiyon içerisinde herhangi bir yerde kullanabiliriz. 

Bu şekilde kullanımı ayarlar, resimler ve gönderiler sayfaları için teker teker uygulayabiliriz ancak kendimizi tekrarlamış oluruz. url_prefix niteliğini tanımlarken dinamik URL yapıları kullanabiliyoruz. Şimdi o şekilde kodumuzu yeniden düzenleyelim.


~~~~python
from flask import Blueprint, g

profil = Blueprint('profil', __name__, url_prefix='/<kadi>')

@profil.route('/resimler')
def resimler():
    pass
~~~~

Şu anda appımız bu şekilde. **kadi**'yi kullanıcı adının kısaltması olarak kullanıyorum. Gördüğünüz gibi bu sefer dinamik URL tanımlamasını blueprintimizi oluştururken url_prefix niteliğinde yaptık. O yüzden **resimler** fonksiyona bir parametre olarak gelmeyecek bu sefer. Ayrıca yakalamamız gerekecek. Bunun için blueprint sınıfının *url_value_preprocessor()* fonksiyonundan (decarator) yararlanabiliriz. Ayrıca farkettiyseniz bir üstteki örnekte **g** sınıfını da içeri aktardık, ona da birazdan değineceğim.

Şimdi de sayfa fonksiyonlarımız (örnekteki *resimler* fonksiyonu gibi) çalışmadan önce kullanıcıdan gelen URL'yi işleme tabii tutacak fonksiyonumuzu hazırlayalım. Böylelikle gelen dinamik veriyi tutup ayıklayabiliriz.

~~~~python
from flask import Blueprint, g

profil = Blueprint('profil', __name__, url_prefix='/<kadi>')


@profil.url_value_preprocessor
def url_ayiklayici(endpoint, values):
	g.kadi = values.pop('kadi')

@profil.route('/resimler')
def resimler():
    pass
~~~~

Hemen bu örneğimizi de açıklayıp bu başlığı da kapatalım. 7. satırda yeni bir fonksiyon tanımladık. 6. satır tamamen bu fonksiyonu kontrol etmesi için bir decarator çağırmaktan ibaret. Decarator yapısını ayrıca öğrenmenizi şiddetle tavsiye ediyorum. Bu tanımladığımız fonksiyon bazı parametreler alıyor (bu parametreler decarator tarafından veriliyor), ve bunlardan biri de URL'deki dinamik veriler. 8. satırda da bu parametrenin içinden istediğimiz veriyi alıp onu **g** nesnesinin **kadi** niteliğine eşitledik. Yani bir değişken tanımlaması yaptık diyebiliriz, ancak değişkeni **g** sınıfının içine tanımladık. [**g** sınıfı hakkında detaylı bilgi için tıklayın](http://flask.pocoo.org/docs/0.12/appcontext/#locality-of-the-context)


# Kaynaklar

* http://flask.pocoo.org/docs/1.0/blueprints/
* http://exploreflask.com/en/latest/blueprints.html