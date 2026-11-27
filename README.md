# SemEval-2027'nin Task 3: Semantic Change Across Multiple Time Periods
# Subtask 1: Diachronic Word Sense Induction (ders uygulaması)

Bu repo, veri madenciliği dersi için basit bir metin temizleme ve kelime frekansı analizi içerir.

## Yapı
- `data/` : train.csv, dev.csv, sample_submission.csv (kopyalar)
- `src/preprocess.py` : veri yükleme, durak kelime çıkarma, kelime frekansı
- `results/` : üretilen çıktılar
- `requirements.txt` : gerekli kütüphaneler

## Çalıştırma
```bash
pip install -r requirements.txt
python src/preprocess.py
```


