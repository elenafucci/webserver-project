# CONSEGNA #
# Realizzazione di un Web Server minimale in Python e pubblicazione di un sito statico

## Obiettivo

Progettare un semplice server HTTP in Python (utilizzando il modulo `socket`) per servire un sito web statico realizzato in **HTML** e **CSS**, ispirato al design di un negozio di alta moda chiamato **Atelier 101**.

## Requisiti minimi

- Il server risponde su `localhost:8080`
- Serve almeno **3 pagine HTML statiche**
- Gestione delle richieste **GET** con risposta `200 OK`
- Risposta **404 Not Found** per file inesistenti

## Estensioni opzionali implementate

- Gestione dei **MIME types** (`.html`, `.css`, `.png`, ecc.)
- Logging delle richieste (timestamp, metodo, percorso, codice risposta)
- Layout responsive e animazioni CSS nel sito statico


**Per eseguire il server:**  
1. Avvia il server con:  
   ```bash
   python server.py
 2.	Apri il browser su: http://localhost:8080 o su http://127.0.0.1:8080
