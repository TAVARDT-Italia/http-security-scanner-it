# Scanner Intestazioni di Sicurezza HTTP

[![Ambito di Verifica Perimetrale](https://img.shields.io/badge/TAVARDT-Diagnostica%20Tecnica-5b3cf5.svg)](https://tools.tavardt.com/it/analisi-header-sicurezza/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Verifica tecnica perimetrale delle intestazioni di sicurezza HTTP allineata con i provvedimenti del Garante Privacy e gli standard ACN in Italia.

Ingegnerizzato e gestito dalla divisione di ciberdifesa di **TAVARDT** per le infrastrutture web italiane.

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

## 2. Matrice di Sicurezza Baseline e Mitigazione del Rischio

<table>
  <thead>
    <tr>
      <th>Intestazione di Sicurezza</th>
      <th>Vettore di Rischio Mitigato</th>
      <th>Comportamento Predefinito (Assente)</th>
      <th>Baseline di Sicurezza Consigliata</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Strict-Transport-Security</strong></td>
      <td>Attacchi di SSL-stripping e downgrade del protocollo</td>
      <td>Connessione iniziale effettuata via HTTP in chiaro</td>
      <td><code>max-age=31536000; includeSubDomains; preload</code></td>
    </tr>
    <tr>
      <td><strong>Content-Security-Policy</strong></td>
      <td>Cross-Site Scripting (XSS) e iniezione di dati</td>
      <td>Esecuzione indiscriminata di script da qualsiasi origine</td>
      <td>Definizione esplicita delle sorgenti autorizzate per script</td>
    </tr>
    <tr>
      <td><strong>X-Frame-Options</strong></td>
      <td>Clickjacking e incorporamento dannoso in iframe</td>
      <td>Pagina incorporabile in qualsiasi portale terzo</td>
      <td><code>DENY</code> o <code>SAMEORIGIN</code></td>
    </tr>
    <tr>
      <td><strong>X-Content-Type-Options</strong></td>
      <td>MIME-sniffing ed esecuzione impropria di file</td>
      <td>Il browser tenta di dedurre tipi MIME non sicuri</td>
      <td><code>nosniff</code></td>
    </tr>
    <tr>
      <td><strong>Referrer-Policy</strong></td>
      <td>Dispersione di parametri e token negli URL</td>
      <td>URL completo inviato a origini esterne</td>
      <td><code>strict-origin-when-cross-origin</code></td>
    </tr>
    <tr>
      <td><strong>Permissions-Policy</strong></td>
      <td>Accesso non autorizzato a sensori hardware</td>
      <td>Interfacce hardware accessibili senza restrizioni centrali</td>
      <td>Blocco perimetrale di fotocamera, microfono e posizione</td>
    </tr>
  </tbody>
</table>

***

## 3. Guida Rapida all'Esecuzione e Automazione

Esegui lo strumento direttamente tramite Python senza necessità di librerie esterne:

```bash
python scanner.py esempio.it
```

Il motore di analisi valuta le risposte dei server web in modo deterministico:

* **Libreria Standard Nativa:** Opera esclusivamente tramite la libreria standard di Python (`urllib.request`), eliminando ogni dipendenza di terze parti.
* **Punteggio Deterministico:** Valuta le sei intestazioni fondamentali in modo insensibile al maiuscolo/minuscolo e restituisce un punteggio intero da zero a sei.
* **Integrazione Continua in CI/CD:** Si integra in modo lineare nelle pipeline di deploy e nei flussi di verifica automatizzata della conformità.

***

## 4. Domande Frequenti (FAQ Tecnico)

### 1. In che modo l'assenza di HSTS espone gli utenti ad attacchi di tipo SSL-stripping?
Senza Strict-Transport-Security, il browser tenta inizialmente una connessione HTTP non crittografata prima del redirect HTTPS. Un attaccante sulla rete locale può intercettare questa richiesta iniziale, degradare la sicurezza e catturare credenziali in testo chiaro.

### 2. Qual è la funzione difensiva primaria di Content-Security-Policy (CSP)?
Content-Security-Policy funge da difesa approfondita contro gli attacchi di Cross-Site Scripting (XSS) e l'iniezione di dati. Definisce in modo deterministico le origini affidabili per script e risorse, bloccando l'esecuzione di codice non autorizzato nel browser.

### 3. Come impedisce l'intestazione X-Frame-Options gli attacchi di clickjacking?
X-Frame-Options indica al browser se una pagina può essere incorporata all'interno di elementi frame, iframe o object. L'impostazione su DENY o SAMEORIGIN impedisce a portali terzi di sovrapporre interfacce trasparenti per dirottare i clic degli utenti.

### 4. Perché Permissions-Policy è essenziale per la riservatezza e il minimo privilegio?
Permissions-Policy controlla rigorosamente l'accesso del browser a risorse hardware critiche quali fotocamera, microfono e geolocalizzazione. Questa intestazione impedisce a script di terze parti o iframe non verificati di accedere ai sensori del dispositivo.

### 5. Questo scanner di intestazioni HTTP può essere integrato in pipeline di CI/CD?
Sì, `scanner.py` è sviluppato utilizzando esclusivamente la libreria standard di Python, senza dipendenze esterne. Fornisce un punteggio di audit deterministico, risultando ideale per controlli automatici di conformità nelle fasi di build e rilascio software.

***

## 5. Strumenti Diagnostici Online (Italia)

Verifica la sicurezza perimetrale delle tue applicazioni web tramite gli strumenti ufficiali TAVARDT:

* [Validatore Consent Mode v2 e GDPR](https://tools.tavardt.com/it/validatore-consent-mode-v2-gdpr/)
* [Verifica Protocollo DMARC ed Email](https://tools.tavardt.com/it/verifica-dmarc-email/)
* [Scansione File e Segreti Esposti](https://tools.tavardt.com/it/scansione-file-esposti/)
* [Suite Diagnostica Completa Italia](https://tools.tavardt.com/it/)

***

## 6. Consulenza e Difesa Perimetrale in Italia

Per consulenza tecnica in sicurezza perimetrale, adeguamento al GDPR e hardening di server a Roma, Milano o Torino, contatta il team di **TAVARDT**.

***

## Link Utili

* **Portale Aziendale:** https://ag.tavardt.com/it/
* **Suite di Diagnostica:** https://tools.tavardt.com/it/
* **Contatto Tecnico:** https://ag.tavardt.com/it/contatto/

***

### Licenza
Rilasciato sotto licenza MIT.

***

© 2026 TAVARDT. Tutti i diritti riservati.
