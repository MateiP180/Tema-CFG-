# 🎯 CFG String Generator & Derivation Validator

Acest proiect Python lucrează cu **gramatici independente de context (CFG)** pentru a genera și valida șiruri. În mod special, se ocupă de o gramatică simplă care generează șiruri echilibrate de forma `aⁿbⁿ`. Util pentru studenți, pasionați de teoria limbajelor formale sau automatizare.

---

## 📚 Descriere

Gramatica CFG definită este:
- **Non-terminal:** `S`
- **Terminale:** `a`, `b`
- **Simbol de start:** `S`
- **Producții:**
  - `S → aSb`
  - `S → ε` (vid)

### 🔁 Ce face programul?
- Generează **aleator 10 șiruri** bazate pe această gramatică.
- Verifică dacă un șir dat aparține limbajului generat de gramatică.
- Afișează **pașii derivației** pentru un șir dat, dacă există o derivare validă.

---

## 🛠️ Tehnologii folosite

- Python 3.x
- Modulul `random`

---

## 🚀 Rulare

### 1. Clonare și rulare locală
```bash
git clone https://github.com/username/proiect-cfg.git
cd proiect-cfg
python main.py
