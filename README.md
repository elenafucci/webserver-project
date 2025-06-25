# Realizzazione di un Web Server minimale in Python e pubblicazione di un sito statico #

## Obiettivo del progetto  
Realizzare un semplice server HTTP utilizzando Python e il modulo `socket`. Il server serve un sito web statico con pagine **HTML** e **CSS** che riprendono il design e i contenuti di un negozio di alta moda chiamato Atelier 101, rispondendo alle richieste HTTP GET con le pagine richieste o con una pagina di errore 404 se il file non è presente.

## Struttura e tecnologie utilizzate  
- **Linguaggio:** Python 3.x  
- **Modulo:** `socket` per gestire le connessioni TCP/IP  
- **`server.py`**: server HTTP minimale in Python  
- **Cartella `www/`:** contiene i file statici (HTML, CSS, immagini)  
- **Porta di ascolto:** localhost sulla porta 8080

## Funzionalità implementate  
- Ascolto delle **richieste HTTP** in locale sulla porta 8080  
- Gestione delle richieste HTTP **GET**  
- Risposta con codice **200** e contenuto del file richiesto, se presente  
- Risposta con codice **404** e pagina di errore se il file non esiste  
- Supporto ai **MIME types** più comuni (`.html`, `.css`, `.png`)  
- **Logging** semplice delle richieste (timestamp, metodo, risorsa, codice risposta)

## Contenuti del sito statico  
La cartella `www/` include almeno 3 pagine HTML, ad esempio:  
- `index.html` (pagina principale)  
- `about.html` (pagina informativa)  
- `contact.html` (pagina di contatto)  
È presente anche un file CSS (`style.css`) per la formattazione.

## Funzionamento del server  
1. Riceve una richiesta GET e ne estrae il percorso della risorsa  
2. Cerca il file nella cartella `www/`  
3. Se il file esiste, invia risposta HTTP 200 con il contenuto e header MIME corretti  
4. Se il file non esiste, invia risposta HTTP 404 con pagina di errore  
5. Registra la richiesta con data, metodo, risorsa e codice risposta

## Esempio di log generati
[2025-06-25 09:52:27] GET /index.html -> 200
[2025-06-25 09:52:27] GET /css/style.css -> 200
[2025-06-25 09:52:27] GET /img/maglie.png -> 200
[2025-06-25 09:52:29] GET /img/maglie/maglia1.png -> 200
[2025-06-25 09:52:32] GET /maglie/maglia1.html -> 404

## Risultati  
Il server risponde correttamente alle richieste GET e serve le pagine con gli stili CSS applicati. Le pagine inesistenti restituiscono l’errore 404 personalizzato.

**Per eseguire il server:**  
```bash
python server.py
