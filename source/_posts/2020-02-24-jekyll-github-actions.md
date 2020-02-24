---
layout: post
current: post
cover: 'assets/images/github-actions.jpg'
navigation: True
title: Github Actions ve Jekyll
date: 24-02-2020 23:52:47
tags: devops
class: post-template
subclass: 'post'
author: bisguzar
---


Şu anda okuduğunuz bu yazının barındığı platforma (bloga) yıllık alan adı ücreti dışında bir ücret ödemiyorum. Çünkü zaten çok nadir yazdığım ve ziyaretçisinin de az olduğu bir platforma neden ücret ödeyeyim ki diye düşündüm. Getirisi (maddi olarak) olmayan şeyin götürüsü (yine maddi) de olmamalı. Bu yazıda da *Jekyll* ve *Github Actions* ile bu blogun yayına çıkma serüveninden bahsedeceğim.

# Statik Site Üreticileri

*Static page generators* diye tabir edilen bir yazılım ürünleri grubu var. Bu araçlar sizin verdiğiniz kaynak dosyaları derleyip HTML dosyaları üretiyorlar. Bu yazıyı okuduğunuza göre sizin de bildiğiniz ürünlerden biri olan *Wordpress* ise dinamik bir araçtır. Yani admin paneline girip yazınızda bir şeyi değiştirebilirsiniz, ve bu direk yazıya yansıyacaktır. Ancak statik üreticileri kullanarak bir şeyler elde ediyorsanız siz kaynağı düzenlemelisiniz ve bu üretici yazılımla kaynaktan bir derlenmiş sonuç elde etmelisiniz. Yani bir şeyleri elle yapmanız gerekiyor (şimdilik). 

Peki bu bize ne sunuyor? Aslında cevap çok basit, sitenizi sunmak için çok çok daha az kaynağa ihtiyacınız oluyor. Çünkü zaten siz önceden her şeyi yapıp nihai ürünü elde etmiş oluyorsunuz. Geriye sadece bunu sunmak kalıyor.

İşte bu noktada da sunucu maliyeti ortaya çıkıyor. Neyse ki *Github*'un *Github Pages* isimli bir çözümü var, statik dosyalarımızı (html, css, js) Github depomuzdan direk yayınlayabiliyoruz. Yani evet, sunucuya ücret ödemiyoruz. Ayrıca kaynağımızı Github yayınlıyor, yani güzel bir sağlayıcımız var diyebiliriz. Ayrıca kaynak zaten açık olduğu için bu yazıdaki bir yanlışlığı direk düzeltme şansınız bile oluyor. Hatta bu [yazının kaynağına giderek](https://github.com/bisguzar/bisguzar.github.io/blob/master/source/_posts/2020-02-24-jekyll-github-actions.md) bu yazı için bir pull request oluşturursanız (bir şeyi düzeltmeniz ya da eksik bir şeyi tamamlamanızı dilerim) direk bu blog üzerinde yazı güncellenecek. Dinamik olmayan dinamik bir blog burası.

Bu blog *Jekyll* adında bir statik site üreticisi tarafından derleniyor. Tema olarak da *Ghost* isimli bir CMS'in (Content Management System, Wordpress benzeri bir çözüm diyebiliriz) varsayılan temasının uyarlamasını kullanıyorum. Jekyll de Jasper de açık kaynaklı.

Bu yazıda sadece serüvenden bahsedeceğim. Bahsettiğim ürünler (jekyll, Github pages, ghost vb.) hakkında internette çok fazla kaynak zaten bulunuyor. 

# Yayına Alma

Github Pages bize birkaç farklı yöntem sunuyor aslında sitemizi yayınlamak için. Mesela *gh-pages* adında bir branch oluşturup dosyalarımızı orada tutmamızı sağlayabiliyor. Kendisi de oradan yayına alıyor. Ya da aynı şekilde *master* branch'ındaki **docs/** klasörüne bakabiliyor. Ya da direk *master* branchına bakıp ne gördüyse ordan yayına alabiliyor. Ben son bahsettiğim yöntemi kullanıyorum. Bunun çok basit bir sebebi var.

Aslında Github jekyll'i kendi içinde zaten destekliyor. Yani jekyll'i kendisi derleyip yayına alabiliyor ve bunun için sizin nerdeyse hiçbir şey yapmanıza gerek yok. Bu konu hakkında da internette yeterince kaynak var. E o zaman bu yazı neden var? Çünkü benim senaryomda Github'un direk desteklemesi ve kendisinin derleyip yayına alması yetersiz kaldı. Ben bazı ek Jekyll eklentileri kullanmak durumunda kaldım. Ve Github, Jekyll eklentilerini desteklemiyor :(. Ve ortaya çıkardığı sitede bazı sayfalar yanlış üretilebiliyor ya da hiç üretilmiyordu. Dolayısıyla benim bu üretme işlemini kendim yapmam gerekiyordu ama her yazı yayınladığımda bilgisayarımda derlemek de işkence olabiliyor. Çünkü farklı bir cihazdan bir şey yayınlamam gerekse önce Ruby'yi indirmem gerekecek (Jekyll'in geliştirildiği programlama dili) daha sonra bağımlı olduğu paketleri kurmam gerekecek. 

Github'un Jekyll'i tanımaması ve kendi kendine derlemeye çalışmaması için ana dizine **.nojekyll** adında bir dosya oluşturmamız gerekiyor. Bunu oluşturduğumuz zaman da sadece üçüncü seçenekte bahsettiğimiz gibi kullanmamıza izin veriyor Github Pages'i.

Tam bu işleri otomatize etmek için aslında CI/CD toollarını kullanıyoruz. Önce Travis'i kullanıyordum. Daha sonra Github, Actions isimli çözümünü piyasaya sürünce ona geçirmeyi düşündüm altyapıyı. Altyapı diyorsam da üç-beş komuttan ibaret her şey. Epey vakit geçtikten sonra bunu gerçekleştirdim. Github Actions hakkında Türkçe kaynaklar çok zengin değil ama Github'un kendi dökümanının giriş kısmını okusanız bile bu yazıyı yayına çıkarmak için hazırladığım Action'u anlayabilirsiniz. Actions'u bir eylem gerçekleştiğinde (mesela yeni bir yazı yazdığınızda) belli komutları (bizim önceden tanımladığımız) çalıştıran bir bilgisayar gibi düşünebilirsiniz.

Bize yazı yazdığımız zaman blogumuzu Jekyll ile üretecek ve daha sonrasında da bunu yine depoya gönderecek bir action lazım. Çünkü Github Pages yine depodan okuyacak ve yayınlayacak.

Burada parça parça inceleyeceğimiz action dosyamızın tamamına ve şu anda çalışan [güncel versiyonuna ulaşmak için tıklayınız](https://github.com/bisguzar/bisguzar.github.io/blob/master/.github/workflows/main.yml). (İleride action'u güncellersem burayı güncelleyeceğimin garantisini veremem...) 

Action dosyalarımız YAML formatında, dolayısıyla okumak kolay. Adım adım incelemeye başlayalım.

~~~yaml
name: Build Blog

on: 
  push:
    branches: master
    paths: 
      - "source/**"
~~~

Burada ilk satırda actionumuza bir isim veriyoruz. Bu action blogumuzu oluşturacağı için ben *Build Blog* dedim. Daha sonraki satırlarda da *push* işlemi gerçekleştiğinde, yani depoya bir şeyler geldiğinde çalışacağını belirtmişim. Ancak bu depoda sadece yazılar yok, bu action da blogu derliyorsa yazılar haricindeki değişikliklerde çalışmamalı. O yüzden biz de *branches* ve *paths* parametrelerini tanımlıyoruz ve sadece **master** branchındaki **source/** klasörüne dosya gönderilirse çalış diyerek kısıtlıyoruz. Burası tam da bizim blogumuzun kaynağının bulunduğu klasör.

~~~yaml
jobs:
  build:

    runs-on: ubuntu-latest

    steps:
~~~

Devam eden bu satırlarda da *jobs* yani actionumuzun görevlerini tanımlamaya başlıyoruz. Ben ilk göreve *build* adını vermişim. Ve bu görevin ubuntu ortamında çalışmasını istemişim. Actionsa bizim için komutlar çalıştıran bilgisayar diyebiliriz demiştik. Burada bizim bilgisayarımız ubuntu işletim sistemine sahip olsun istedik. Daha sonra da *steps* kısımında bu görevde çalışacak adımları teker teker tanımlayacağız.

~~~yaml
    - name: Install Ruby
      run:  sudo apt install ruby-full
    
    - name: Insall Bundler
      run: sudo gem install bundler
~~~

İlk iki adımımızı hazırladık, aslında bu iki adım da aynı amacı güdüyor. Bağımlılıkları kurmak. İlk adım ruby dilini sisteme kuruyor, ikinci adım da ruby için bir paket yöneticisi olan bundler'i kuruyor. Bunları tek adımda kurdurmak da mümkün tabi ancak actions'un akış diyagramında ayrı ayrı görmek ve bir hata alınırsa daha kolay müdahale edebilmek adına daha iyi oluyor. 

~~~yaml
    - name: Install dependencies
      run: |
        cd source
        bundle install  
~~~

3\. adımımızda da bundler ile ihtiyaç duyduğumuz paketleri kurduruyoruz (jekyll ve kullandığı diğer eklentileri). Bu adımımız farkettiyseniz iki ayrı komut içeriyor. Çünkü bundlerin kullanacağı Gemfile dosyamız source klasöründe. Dolayısıyla önce dizini değiştirmemiz gerekiyor.

~~~yaml
    - name: Build blog
      run: |
        cd source
        bundle exec jekyll build
~~~

Sonunda blogumuzun dosyalarını üreteceğimiz adıma geldik. Bu adımda da yine kaynak dosyalarının bulunduğu dizine geçtik ve bundler üzerinde *jekyll build* komutunu çalıştırdık. Bu komut çalıştıktan sonra Jekyll yine aynı dizinde *_site/* klasörü oluşturuluyor ve kaynaktan ürettiği dosyaları oraya koyuyor. Biz de bir sonraki adımlarda bu dosyaları Github Pages'e vereceğiz ki sitemiz yayına alınabilsin.

~~~yaml
    - name: Install SSH Client
      uses: webfactory/ssh-agent@v0.2.0
      with:
        ssh-private-key: ${{ secrets.ACTIONS_DEPLOY_KEY }}
~~~

Tabi ürettiğimiz dosyaları yine depoya göndereceğimiz için Github'a kendimizi tanıtmamız ve yetkili birisi olduğumuza kendisini ikna etmemiz gerekiyor. Bunun için hazırlanmış olan farklı bir actionu çağırıyoruz ve ilgili parametreyi veriyoruz. Bizim için o action gerekli işlemleri yapıyor. Evet, action-in-action.

~~~yaml
    - name: Initialize Git
      run: |
        git config --global user.email "bot@bisguzar.com"
        git config --global user.name "Deploy Bot"
~~~

Bu adımda da klasik git ayarlamalarımızı yapıyoruz. 

~~~yaml
    - name: Deploy Source
      run: |
        cp -r source/_site/* ./
        rm -r source/_site
        git add .
        git commit -m "🤖 Built and deployed automatically by actions." 
        git push
~~~

Blogumuzu yayına aldığımız asıl adı burası. Burada sırasıyla Jekyll'in ürettiği dosyaları ana dizine kopyaladık. Çünkü daha önce de bahsettiğim gibi, Github Pages ana dizinden yayına alıyor. Daha sonrasında üretilen dosyaları sildik, çünkü aynı anda iki yerde olmalarına ne gerek var? Bunlardan sonra da değişikliklerimizi git'e bildirdik, mesajımızı yazdık ve depoya gönderdik.

~~~yaml
    - name: Finish
      run: echo "All done!"
~~~

Evet, bu da son adımımız. Her şey bitti, sorun yaşamadık demek. Sadece ekrana "All done!" yazdırıyor.

[Bu yazı yayına çıkarken çalışan action'u adım adım incelemek için tıklayın, ve evet, bunu sonradan ekliyorum. Çünkü actionun çalışması için önce yazıyı göndermem gerekiyordu.](https://github.com/bisguzar/bisguzar.github.io/runs/465645033)

Cover photo by <a style="background-color:black;color:white;text-decoration:none;padding:4px 6px;font-family:-apple-system, BlinkMacSystemFont, &quot;San Francisco&quot;, &quot;Helvetica Neue&quot;, Helvetica, Ubuntu, Roboto, Noto, &quot;Segoe UI&quot;, Arial, sans-serif;font-size:12px;font-weight:bold;line-height:1.2;display:inline-block;border-radius:3px" href="https://unsplash.com/@yancymin?utm_medium=referral&amp;utm_campaign=photographer-credit&amp;utm_content=creditBadge" target="_blank" rel="noopener noreferrer" title="Download free do whatever you want high-resolution photos from Yancy Min"><span style="display:inline-block;padding:2px 3px"><svg xmlns="http://www.w3.org/2000/svg" style="height:12px;width:auto;position:relative;vertical-align:middle;top:-2px;fill:white" viewBox="0 0 32 32"><title>unsplash-logo</title><path d="M10 9V0h12v9H10zm12 5h10v18H0V14h10v9h12v-9z"></path></svg></span><span style="display:inline-block;padding:2px 3px">Yancy Min</span></a>