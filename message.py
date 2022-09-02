import random

# User Message
shutDownMessage = ["kapan", "körüşürüz", "kendini kapat", "yok ol"]
dayMessage = ["bugün ne", "bugün günlerden ne","gün","hangi gündeyiz", "günlerden ne"]
whatTimeMessage = ["saat kaç","saati söylermisin","saat hakkında bilgi ver", "saati söyle"]
searchMessage = ["arama yap", "araştır","birşey araştırmanı istiyorum"]
uJokeMessage = ["beni güldür","bana şaka yap", "beni eğlendir","mutsuzum","moralim bozuk"]
songPlayMessage = ["şarkı aç","şarkı açarmısın","şu şarkıyı açarmısın","şarkı çal","şarkı oynat"]
wikiMessage = ["araştırma yap","benim için araştırırmısın","wikipedia da ara", "wikipedia"]
openLightMessage = ["ışıkları aç","ışıkları açarmısın","ışık aç","ışıkları yak"]
closeLightMessage = ["ışıkları kapat","ışıkları kapatırmısın","ışık kapat","ışıkları kapat"]


# Asistan message
exitMessage = ["Görüşürüz", "Kendine iyi bak", "Elveda", "Kapandım"]
helloMessage = ["Selam", "Hoşgeldin", "Merhaba", "Sanada Merhaba"]
timeMessage = ["Saat şuan", "Saati söylüyorum", "Saat", "Hemen bakıyorum saat"]
todayMessage = ["Bugün günlerden", "Bugün", "Günlerden"]
openMessage = ["Uyandım", "Selam", "Naber", "Aktifleştim"]
jokes = ["Gitme dur Niye ne oIdu Duracak mısın diye merak ettim şimdi git", "Alo Emin Ie görüşecektim yanlış numara Emin misin Evet Hani yanIış numaraydı", "Eti pufu açmaya çaIışırken cinnet geçirip pakete çatal bıçak Allah ne verdiyse dalanlar derneği hobaaa", "anne et varmı hayır hepsini windows 7"]
spotifyMessage = ["spotify ı başlat", "spotify ı aç"] 



# Rastgeleleştirme
jokes = random.choice(jokes)
openMessage = random.choice(openMessage)
todayMessage = random.choice(todayMessage)
timeMessage = random.choice(timeMessage)
helloMessage = random.choice(helloMessage)
exitMessage = random.choice(exitMessage)
