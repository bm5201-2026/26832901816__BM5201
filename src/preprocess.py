"""Veri yükleme, durak kelime çıkarma ve kelime frekansı (Subtask 1 ön işleme)."""
from collections import Counter
from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data"
RESULTS = Path(__file__).resolve().parent.parent / "results"

STOP_WORDS = {
    'i','me','my','myself','we','our','ours','ourselves','you','your','yours','yourself','yourselves',
    'he','him','his','himself','she','her','hers','herself','it','its','itself','they','them','their',
    'theirs','themselves','what','which','who','whom','this','that','these','those','am','is','are',
    'was','were','be','been','being','have','has','had','having','do','does','did','doing','a','an',
    'the','and','but','if','or','because','as','until','while','of','at','by','for','with','about',
    'against','between','into','through','during','before','after','above','below','to','from','up',
    'down','in','out','on','off','over','under','again','further','then','once','here','there','when',
    'where','why','how','all','any','both','each','few','more','most','other','some','such','no',
    'nor','not','only','own','same','so','than','too','very','s','t','can','will','just','don',
    'should','now'
}

def load_train() -> pd.DataFrame:
    return pd.read_csv(DATA / "train.csv")

def clean_text(text: str) -> str:
    return ' '.join(w for w in str(text).lower().split() if w not in STOP_WORDS)

def main():
    RESULTS.mkdir(exist_ok=True)
    df = load_train()
    print("Satır, sütun:", df.shape)
    print("Sütunlar:", list(df.columns))
    print("Eksik değer:\n", df.isna().sum().to_string())
    df['cleaned_prompt'] = df['prompt'].apply(clean_text)
    print(df[['prompt', 'cleaned_prompt']].head().to_string())
    counts = Counter()
    for t in df['cleaned_prompt']:
        counts.update(t.split())
    top = pd.DataFrame(counts.most_common(10), columns=['kelime', 'frekans'])
    print(top.to_string(index=False))
    top.to_csv(RESULTS / "top10_kelime.csv", index=False, encoding="utf-8")
    df[['id', 'prompt', 'cleaned_prompt']].to_csv(RESULTS / "temizlenmis_train.csv", index=False, encoding="utf-8")

if __name__ == "__main__":
    main()
