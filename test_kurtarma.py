#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from kurtar import ara, dosya_no


class KurtarmaTest(unittest.TestCase):
    def test_kumanda_bulunmaz(self):
        t = ara(18, 3, "kayinpeder")
        self.assertFalse(t.kumanda_bulundu_mu)

    def test_dosya_numarasi(self):
        self.assertEqual(dosya_no(7, 1), "KAKKI-2026/07-01-KAYIP")

    def test_derin_koltuk_kapak_bulur_kumanda_bulmaz(self):
        t = ara(22, 1, "abla")
        self.assertIn("2014 yilina ait uzaktan kumanda kapagi", t.bulunanlar)
        self.assertFalse(t.kumanda_bulundu_mu)

    def test_negatif_ret(self):
        with self.assertRaises(ValueError):
            ara(-1, 1, "kimse")

    def test_bos_tanik_isimsiz(self):
        t = ara(5, 0, "   ")
        self.assertEqual(t.tanik, "isimsiz hane halki")
        self.assertGreaterEqual(t.ceza_ic_cekis, 1)


if __name__ == "__main__":
    unittest.main()
