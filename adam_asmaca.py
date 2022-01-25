import random

while True:
    print("Adam asmaca oyununa hosgeldiniz...")
    print("Konseptimiz filmler.........")
    kelimeler = ["yüzüklerinefendisi","ölümcüldeney","örümcekadam","hızlıveöfkeli","buzdevri","çılgınhırsızlar","hababamsınıfı","tosunpaşa","korkuseansı","karayipkorsanları","görevimiztehlike","yahşibatı","batmankaraşövalye","harrypotter"]

    kelime = random.choice(kelimeler)
    tahminsayisi = 6

    harfler = [] #Kullanıcının girdiği tüm harfleri bu listeye ekledik.Bu sayede  tekrar aynı harf girilirse uyarı vereceğiz.
    x = len(kelime)
    z = list('_' * x)
    print(' '.join(z), end='\n')  # z listesinin elemanlarını birleştirdik(aralarda boşluk ile).
    
    while tahminsayisi > 0 :
        harf = input("Tahmin ettiginiz harfi giriniz :")
    
        if harf in harfler:
            print("Daha once tahmin etmediginiz bir harf giriniz.")
            continue
    
        elif len(harf) > 1:
            print("Lutfen sadece 1 harf giriniz.")
            continue
    
        elif harf not in kelime:
            tahminsayisi-= 1
            print("Yanlis tahmin yaptiniz. ")
            print("Kalan tahmin hakkiniz:",tahminsayisi)
        
        else:
            for i in range(len(kelime)):
                if harf == kelime[i]:
                    print("Dogru tahmin ettiniz.")
                    z[i] = harf
                    harfler.append(harf)
            print(' '.join(z), end='\n')
        
        cevap = input("Kelimenin tamamini tahmin etmek ister misin?(e-evet h-hayir) : ")
    
        if (cevap == 'e'):
            tahmin = input("Tahmininiz: ")
        
            if tahmin == kelime:
                print("Tebrikler kelimeyi bildiniz.......")
                break
        
            else:
                tahminsayisi-= 1
                print("Yanlis tahmin ettiniz.")
                print("Kalan tahmin hakkiniz: ",tahminsayisi)
                continue
        
        if tahminsayisi == 0:
            print("Tahmin hakkiniz kalmadi.Oyunu kaybettiniz...... :( :( :( ")
            break
            
    yanit = input("Tekrar oynamak ister misiniz? e-evet h-hayir : ")
    
    if yanit == 'e':
        continue
    
    else:
        break