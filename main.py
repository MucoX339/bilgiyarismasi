import sqlite3 as sql
import os as sistem
import random as karisik
def baglanti():
    con = sql.connect("soru_bankasi.sqlite")
    imlec = con.cursor()
    tablo_komut = """CREATE TABLE IF NOT EXISTS 'sorubankasi' (
        id integer PRIMARY KEY,
        SORU text,
        SIK1 text,
        SIK2 text,
        SIK3 text,
        SIK4 text,
        CEVAP text
        )"""
    print("tablo oluşturma başarılı")
    imlec.execute(tablo_komut)
    con.commit
    con.close()
def soru_ekle():
    con = sql.connect("soru_bankasi.sqlite")
    imlec = con.cursor()
    sorular =[(1,"“Sinekli Bakkal” Romanının Yazarı Aşağıdakilerden Hangisidir?","A) Reşat Nuri Güntekin","B) Halide Edip Adıvar","C) Ziya Gökalp","D) Ömer Seyfettin","B)"),
              (2,"Aşağıda Verilen İlk Çağ Uygarlıklarından Hangisi Yazıyı İcat Etmiştir?","A) Hititler","B) Elamlar","C) Sümerler","D) Urartular","C)"),
              (3,"Tsunami Felaketinde En Fazla Zarar Gören Güney Asya Ülkesi Aşağıdakilerden Hangisidir?","A) Endonezya","B) Srilanka","C) Tayland","D) Hindistan","A)"),
              (4,"2003 Yılında Euro Vizyon Şarkı Yarışmasında Ülkemizi Temsil Eden ve Yarışmada Birinci Gelen Sanatçımız Kimdir?","A) Grup Athena","B) Sertap Erener","C) Şebnem Paker","D) Ajda Pekkan","B)"),
              (5,"Mustafa Kemal Atatürk’ün Nüfusa Kayıtlı Olduğu İl Hangisidir?","A) Bursa","B) Ankara","C) İstanbul","D) Gaziantep","D)")
              ]
    #komut = """INSERT INTO 'sorubankasi' VALUES(?,?,?,?,?,?,?)"""
    for soru in sorular:
        imlec.execute("""INSERT INTO 'sorubankasi' VALUES(?,?,?,?,?,?,?)""",soru)
    con.commit()
    con.close()
    print("tablo oluşturma başarılı")
def soru_listele():
    con = sql.connect("soru_bankasi.sqlite")
    imlec = con.cursor()
    imlec.execute("SELECT * FROM 'sorubankasi'")
    soru_havuzu = imlec.fetchall()
    rastgele_soru=karisik.sample(soru_havuzu,2)
    for i in rastgele_soru[1:6]:
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
        
