# Scanner Intestazioni di Sicurezza HTTP

[![Ambito di Verifica Perimetrale](https://img.shields.io/badge/TAVARDT-Diagnostica%20Tecnica-5b3cf5.svg)](https://tools.tavardt.com/it/analisi-header-sicurezza/)
Verifica tecnica perimetrale delle intestazioni di sicurezza HTTP allineata con i provvedimenti del Garante Privacy e gli standard ACN in Italia.

Sviluppato e gestito dalla divisione di sicurezza informatica e protezione infrastrutture di **TAVARDT**.

***

## 1. Ambito di Verifica Perimetrale

Questa utilità da terminale analizza la corretta configurazione delle intestazioni crittografiche e di isolamento delle sessioni web:

* **Strict-Transport-Security (HSTS):** Impone connessioni cifrate sicure via HTTPS e impedisce attacchi di downgrade SSL.
* **Content-Security-Policy (CSP):** Blocca l'iniezione di script malevoli (XSS) e limita le origini autorizzate al caricamento di risorse.
* **X-Frame-Options:** Impedisce attacchi di clickjacking gestendo i permessi di incorporazione in frame e iframe.
* **X-Content-Type-Options:** Previene l'esecuzione impropria di file dovuta a vulnerabilità di MIME-sniffing.
* **Referrer-Policy:** Protegge i parametri sensibili negli URL di provenienza contro la dispersione verso terze parti.
* **Permissions-Policy:** Applica il principio del privilegio minimo alle API hardware del browser (fotocamera, microfono, geolocalizzazione).

***

## 2. Guida Rapida all'Esecuzione

Esegui lo strumento direttamente tramite Python senza necessità di librerie esterne:

```bash
python scanner.py esempio.it
```

***

## 3. Strumenti Diagnostici Online (Italia)

Verifica la sicurezza perimetrale delle tue applicazioni web tramite gli strumenti ufficiali TAVARDT:

* Analisi Header HTTP di Sicurezza
* [Validatore Consent Mode v2 e GDPR](https://tools.tavardt.com/it/validatore-consent-mode-v2-gdpr/)
* [Verifica Protocollo DMARC ed Email](https://tools.tavardt.com/it/verifica-dmarc-email/)
* [Scansione File e Segreti Esposti](https://tools.tavardt.com/it/scansione-file-esposti/)
* [Suite Diagnostica Completa Italia](https://tools.tavardt.com/it/)

***

## 4. Consulenza e Ciberdifesa Aziendale

Per consulenza tecnica in sicurezza perimetrale, adeguamento al GDPR e hardening di server aziendali in Italia, contatta il team di **TAVARDT**.

***

## Link Utili

* **Portale Aziendale:** https://ag.tavardt.com/it/
* **Suite di Diagnostica:** https://tools.tavardt.com/it/
* **Contatto Tecnico:** https://ag.tavardt.com/it/contatto/

***

© 2026 TAVARDT. Tutti i diritti riservati.
