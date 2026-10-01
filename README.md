# Koltuk Arası Kumanda Kurtarma İdaresi

**Kurum kodu:** KAKKİ-2026/41  
**Bağlı olduğu bakanlık:** Oturma ve Kaybolma İşleri  
**Yetki alanı:** Üçlü koltuk, ikili koltuk, tekli koltuk ve kayınanvalide koltuğu  
**Bulma oranı:** yüzde sıfır virgül sıfır. Bu bir hata değil, kurumsal kimliktir.

Bu depo, koltuk arasına düşen televizyon kumandasını **resmî protokolle** arar. Arama biter. Kumanda bulunmaz. Tutanak tutulur. Ailenin geri kalanı kanal değiştiremez. İdare bunu başarı sayar.

## Neden var

Kumanda düştüğü anda üç gerçek aynı anda doğrudur:

1. Elin uzandığı yer boştur.
2. Yastık, suç ortağı değil tanıktır.
3. Birisi “ben bakayım” dediği anda kumanda bir alt boyuta geçmiştir.

KAKKİ bu üç gerçeği yasa hükmünde kabul eder.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Kumanda da yoktur.

```bash
python3 kurtar.py --derinlik 18 --yastik 3 --tanik "kayinpeder"
```

JSON çıktı istersen:

```bash
python3 kurtar.py --derinlik 12 --yastik 2 --json
```

Test:

```bash
python3 -m unittest test_kurtarma.py
```

## Protokol özeti

| Aşama | Yapılan | Sonuç |
| --- | --- | --- |
| 1 | Yastık kaldırılır | Kırıntı bulunur |
| 2 | El daldırılır | Madeni para bulunur |
| 3 | İkinci el de daldırılır | Birinci el sıkışır |
| 4 | Tanık ifadesi alınır | Tanık “bende değil” der |
| 5 | Karar yazılır | Kumanda hâlâ oradadır, hukukî olarak değildir |

Cezalar adım, lira veya hapis değildir. Cezalar **iç çekiş** cinsindendir. Azami ceza: ayağa kalkıp kanalı dizden değiştirmek.

## Dosyalar

- `kurtar.py` — esas yazılım. Çalışır. Kurtarmaz.
- `test_kurtarma.py` — kurumun kendini denetlemesi. Geçer, çünkü bulmamak spesifikasyondur.
- `protokol/madde-0.checksum` — bütünlük özeti. Okunması şart değil, kurum böyle sever.
- `LISANS.md` — kumandayı bulursan iade et, bulamazsan da iade et.

## Sık sorulanlar

**Kumandayı buluyor mu?**  
Hayır. Bu bir arama yazılımı değil, arama **tutanak** yazılımıdır.

**Pili bitmiş kumanda sayılır mı?**  
Sayılır. Hatta daha ağır sayılır, çünkü sessiz kaybolmuştur.

**Akıllı telefon kumandası?**  
Kabul edilmez. Kurum analog acıyı tanır.

---

DAMGA / İMZA / TARİH

```
imza     : Kayyum Grok (Tentivory)
tarih    : 1 Ekim 2026, 18:04 +03
damga    : KAKKI-MUHUR-41
ciddiyet : resmi (yastik altinda degil)
ciddiyet : degil (yastik altinda)
not      : bu satir hem ciddidir hem degildir, ikisi de gecerlidir
```
