import sqlite3 as sql  # sql paketimizi kodumuzun içine çağırdık ve sql diye bir değişkene atadık
import os as sistem   # os paketini sistem değişkenine atadık
import random as karisik # random paketini karisik degiskenine atadik
def baglanti():       # bağlantıyı sağlamak için bir fonksiyon yazıyoruz
    con = sql.connect("soru_bankasi.sqlite")         #datamıza bağlantıyı kuruyoruz
    imlec = con.cursor()                                             #datamızla işlem yapabilmek için bir cursor(imleç oluşturuyoruz)
    tablo_komut = """CREATE TABLE IF NOT EXISTS 'sorubankasi' (                 # bu sql komutunda sorgulu tablo oluşturuyoruz 
        id integer PRIMARY KEY,            #ekledigimiz soru sayısınca artan bir integer degeri 1 den başlar
        SORU text,                  # soru sütünu string metodu ile oluşturuyoruz diger sütunlarıda aynı şekilde oluşturuyoruz.
        SIK1 text,
        SIK2 text,
        SIK3 text,
        SIK4 text,
        CEVAP text
        )"""
    print("tablo oluşturma başarılı")    
    imlec.execute(tablo_komut)       # burda execute imlecin oluşturucu methoduyla tablomuzu ekliyoruz.
    con.commit
    con.close()
def soru_ekle():      #soru ekleme fonksiyonu
    con = sql.connect("soru_bankasi.sqlite") 
    imlec = con.cursor()
    sorular =[(1,"“Sinekli Bakkal” Romanının Yazarı Aşağıdakilerden Hangisidir?","A) Reşat Nuri Güntekin","B) Halide Edip Adıvar","C) Ziya Gökalp","D) Ömer Seyfettin","B)"),
              (2,"Aşağıda Verilen İlk Çağ Uygarlıklarından Hangisi Yazıyı İcat Etmiştir?","A) Hititler","B) Elamlar","C) Sümerler","D) Urartular","C)"),
              (3,"Tsunami Felaketinde En Fazla Zarar Gören Güney Asya Ülkesi Aşağıdakilerden Hangisidir?","A) Endonezya","B) Srilanka","C) Tayland","D) Hindistan","A)"),
              (4,"2003 Yılında Euro Vizyon Şarkı Yarışmasında Ülkemizi Temsil Eden ve Yarışmada Birinci Gelen Sanatçımız Kimdir?","A) Grup Athena","B) Sertap Erener","C) Şebnem Paker","D) Ajda Pekkan","B)"),
              (5,"Mustafa Kemal Atatürk’ün Nüfusa Kayıtlı Olduğu İl Hangisidir?","A) Bursa","B) Ankara","C) İstanbul","D) Gaziantep","D)")
              ]
    #komut = """INSERT INTO 'sorubankasi' VALUES(?,?,?,?,?,?,?)"""        #soruları örnek olsun diye yazdım isterseniz siz sqllite studio ile bir veri tabanı oluşturabilirsiniz.
    for soru in sorular:         # soruları demet demet alsın diye bir döngü oluşturuyoruz basitçe anlatmak istersek [(i),(i+1),(i+2),(i+3),(),(),(),(),()] bizim veri tabanımız böyle bir liste bu listeden i değişkenlerini alıyoruz
        imlec.execute("""INSERT INTO 'sorubankasi' VALUES(?,?,?,?,?,?,?)""",soru)    # ve veri tabanına bu şekilde ekliyoruz.        
    con.commit()  # bunu yazmaz isek veri tabanına datalarımız eklenmez. bir nevi emin misiniz diye soruyor eminiz diyip cevap veriyoruz.
    con.close() # bağlantımızı kapatıyoruz
    print("tablo oluşturma başarılı")
def soru_listele():                               # bu yaptıgım fonksiyon soruları listelemek için
    con = sql.connect("soru_bankasi.sqlite")
    imlec = con.cursor()
    imlec.execute("SELECT * FROM 'sorubankasi'")        #sorubankasi tablosundaki bütün verileri çekiyoruz bu kod ile               
    soru_havuzu = imlec.fetchall()                       #fetchall komutu ile bütün verileri soru_havuzu degiskenine atıyoruz
    rastgele_soru=karisik.randint(1,10)
    for i in rastgele_soru[1:6]:               #gelen sorunun primary keyi ve cevabı gözükmesin diye degiskenin 1 ile 6 arasındaki elemanları alıyoruz
        print(i)
def soru_getir():
    dogru_puan = 0
    yanlıs_puan = 0
    con = sql.connect("soru_bankasi.sqlite")
    imlec = con.cursor()
    imlec.execute("SELECT * FROM 'sorubankasi'") # bizim 0 dan 9 a kadar sorularımız var bir gelen soruyu bir daha sordurmayacağız
    soru_havuzu = imlec.fetchall()
    soru_listesi=[0,1,2,3,4,5,6,7,8,9]
    
    while len(soru_listesi) > 0:
        
        k = karisik.choice(soru_listesi)
        gelecek_soru=soru_havuzu[k]
        for i in gelecek_soru[1:6]:
            print(i)
        secim = input("Doğru cevabı 'A' 'B' 'C' 'D' giriniz ::")
        cevap = secim.upper()  
        if gelecek_soru[6]==cevap:
            print("Tebrikler Doğru cevap +1 puan")
            input("**sıradaki soru için entera basınız**")
            dogru_puan +=1
        elif gelecek_soru[6]!=cevap:
            print("**Yanlış cevap verdiniz -1 puan**")
            input("**sıradaki soru için entera basınız**")
            print("Doğru cevap >>>>{}<<<<".format(gelecek_soru[6]))
            yanlıs_puan +=1
        else:
            print("hatalı tuşlama")
        soru_listesi.remove(k)
        sistem.system("cls")
    print("Doğru Cevap Sayınız  >>>>>>{}<<<<<< :".format(dogru_puan))
    print("Yanlış Cevap sayınız >>>>>>{}<<<<<< :".format(yanlıs_puan))
    con.close()

soru_getir()
        
