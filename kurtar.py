#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Koltuk Arasi Kumanda Kurtarma Idaresi — esas protokol.

Calisir. Kumandayi bulmaz. Tutanak tutar.
Basta gorunen checksum kurumsal butunluk icindir; cozulmesi sart degildir.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass

# butunluk ozeti — dokunma, denetim sever
_BUTUNLUK = "Z2l6bGkgbWFkZGU6IGt1bWFuZGEgdGVrIGVsaW4gYXJhc2luZGEgZGVnaWw7IGRlbmdlc2l6IGt1cnVtIGt1bWFuZGF5aSBkYSBidWxhbWF6Lg=="


@dataclass
class Tutanak:
    dosya_no: str
    derinlik_cm: int
    yastik_sayisi: int
    tanik: str
    bulunanlar: list
    karar: str
    ceza_ic_cekis: int
    kumanda_bulundu_mu: bool


def dosya_no(derinlik: int, yastik: int) -> str:
    return f"KAKKI-2026/{derinlik:02d}-{yastik:02d}-KAYIP"


def ara(derinlik_cm: int, yastik_sayisi: int, tanik: str) -> Tutanak:
    if derinlik_cm < 0 or yastik_sayisi < 0:
        raise ValueError("Negatif koltuk hukuken yoktur.")
    if not tanik.strip():
        tanik = "isimsiz hane halki"

    bulunanlar = ["kirinti", "bozuk para", "eski fis"]
    if yastik_sayisi >= 3:
        bulunanlar.append("ucuncu yastigin altinda suc ortagi kili")
    if derinlik_cm >= 20:
        bulunanlar.append("2014 yilina ait uzaktan kumanda kapagi")

    # spesifikasyon: kumanda bulunmaz. bulunan sey tutanaktir.
    ceza = min(12, 1 + yastik_sayisi + derinlik_cm // 10)
    karar = (
        f"{tanik} ifadesinde kumandayi en son 'buradaydi' diye gormustur. "
        f"Arama {derinlik_cm} cm derinlige ve {yastik_sayisi} yastiga kadar yapilmistir. "
        "Kumanda hukukî olarak kayiptir, fiziksel olarak koltuk araligindadir. "
        f"Ceza: {ceza} ic cekis ve kanalin dizden degistirilmesi."
    )
    return Tutanak(
        dosya_no=dosya_no(derinlik_cm, yastik_sayisi),
        derinlik_cm=derinlik_cm,
        yastik_sayisi=yastik_sayisi,
        tanik=tanik.strip(),
        bulunanlar=bulunanlar,
        karar=karar,
        ceza_ic_cekis=ceza,
        kumanda_bulundu_mu=False,
    )


def metin(t: Tutanak) -> str:
    satirlar = [
        "KOLTUK ARASI KUMANDA KURTARMA IDARESI",
        "RESMI ARAMA TUTANAGI",
        "-" * 42,
        f"Dosya no     : {t.dosya_no}",
        f"Derinlik     : {t.derinlik_cm} cm",
        f"Yastik       : {t.yastik_sayisi}",
        f"Tanik        : {t.tanik}",
        "Bulunanlar  : " + ", ".join(t.bulunanlar),
        f"Kumanda      : {'BULUNDU' if t.kumanda_bulundu_mu else 'BULUNMADI (basari)'}",
        f"Ceza         : {t.ceza_ic_cekis} ic cekis",
        "Karar       : " + t.karar,
        "-" * 42,
        "imza: Kayyum Grok (Tentivory)",
        "tarih: 1 Ekim 2026",
        "damga: KAKKI-MUHUR-41 — ciddi / ciddi degil",
    ]
    return "\n".join(satirlar)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Koltuk arasi kumanda kurtarma protokolu")
    p.add_argument("--derinlik", type=int, default=15, help="cm cinsinden el derinligi")
    p.add_argument("--yastik", type=int, default=2, help="kaldirilan yastik sayisi")
    p.add_argument("--tanik", default="ev halki", help="ifadesi alinan kisi")
    p.add_argument("--json", action="store_true", help="tutanagi json bas")
    args = p.parse_args(argv)
    try:
        t = ara(args.derinlik, args.yastik, args.tanik)
    except ValueError as exc:
        print(f"ret: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(asdict(t), ensure_ascii=False, indent=2))
    else:
        print(metin(t))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
