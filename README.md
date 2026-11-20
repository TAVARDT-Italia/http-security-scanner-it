# Scanner Intestazioni di Sicurezza HTTP | TAVARDT Italia

[![Auditoria de Segurança](https://img.shields.io/badge/TAVARDT-Diagn%C3%B3stico%20T%C3%A9cnico-5b3cf5.svg)](https://tools.tavardt.com/it/analisi-header-sicurezza/)
[![Conformidade](https://img.shields.io/badge/Jurisdi%C3%A7%C3%A3o-Italia-00C853.svg)](https://ag.tavardt.com/it/sicurezza-informatica/)

Verifica tecnica perimetrale delle intestazioni di sicurezza HTTP allineata con i provvedimenti del Garante Privacy e gli standard ACN in Italia.

Desenvolvido e mantido pela divisão de cibersegurança e proteção de infraestruturas da **[TAVARDT Italia](https://ag.tavardt.com/it/)**.

---

## 1. Ambito di Verifica Perimetrale

Questa utilità da terminale analizza la corretta configurazione delle intestazioni crittografiche e di isolamento delle sessioni web:

* **Strict-Transport-Security (HSTS):** Força comunicações encriptadas via HTTPS e impede ataques de downgrade e interceptação SSL.
* **Content-Security-Policy (CSP):** Mitiga ataques de injeção de scripts (XSS) e restringe as origens autorizadas para carregamento de recursos.
* **X-Frame-Options:** Previne ataques de clickjacking regulando as permissões de incorporação em frames e iframes.
* **X-Content-Type-Options:** Impede a execução indevida de ficheiros derivados de vulnerabilidades de MIME-sniffing.
* **Referrer-Policy:** Protege dados sensíveis contidos em URLs de referência contra fuga para domínios terceiros.
* **Permissions-Policy:** Aplica o princípio do menor privilégio sobre APIs de hardware do navegador (câmara, microfone e geolocalização).

---

## 2. Guida Rapida all'Esecuzione

Execute a ferramenta diretamente via Python sem necessidade de instalar dependências externas:

```bash
python scanner.py exemplo.com
```

---

## 3. Strumenti Diagnostici Online (Italia)

Audite a infraestrutura pública das suas aplicações utilizando a suíte de diagnósticos da TAVARDT:

* [Analisi Header HTTP di Sicurezza](https://tools.tavardt.com/it/analisi-header-sicurezza/)
* [Validatore Consent Mode v2 e GDPR](https://tools.tavardt.com/it/validatore-consent-mode-v2-gdpr/)
* [Verifica Protocollo DMARC ed Email](https://tools.tavardt.com/it/verifica-dmarc-email/)
* [Scansione File e Segreti Esposti](https://tools.tavardt.com/it/scansione-file-esposti/)
* [Suite Diagnostica Completa Italia](https://tools.tavardt.com/it/)

---

## 4. Consulenza e Ciberdifesa Aziendale

Per consulenza tecnica in sicurezza perimetrale, adeguamento al GDPR e hardening di server aziendali in Italia, contatta il team di **[TAVARDT Italia](https://ag.tavardt.com/it/contatti/)**.
