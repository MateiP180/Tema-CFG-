# 🎯 CFG String Generator & Derivation Validator

Acest proiect Python explorează modul în care **gramaticile independente de context (Context-Free Grammars - CFG)** pot fi utilizate pentru a genera și valida șiruri. Programul permite atât **crearea de șiruri valide** conform unei gramatici, cât și **verificarea** dacă un șir aparține limbajului definit de aceasta, oferind în același timp și o **derivare pas cu pas** a șirului, dacă este posibilă.

---

## 🧾 Descriere detaliată

### 🔍 Ce este o gramatică independentă de context?

O **gramatică independentă de context (CFG)** este o structură formală utilizată pentru a descrie limbaje formale. Este formată din:
- un set de **simboluri terminale** (caractere din șiruri finale),
- un set de **simboluri non-terminale** (simboluri care pot fi înlocuite),
- un **simbol de start**,
- un set de **reguli de producție** care descriu cum pot fi înlocuite simbolurile non-terminale.

Gramatica CFG definită este:
- **Non-terminal:** `S`
- **Terminale:** `a`, `b`
- **Simbol de start:** `S`
- **Producții:**
  - `S → aSb`
  - `S → ε` (vid) -> notat in cod cu "~"

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
