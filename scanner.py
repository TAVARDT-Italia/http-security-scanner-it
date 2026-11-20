#!/usr/bin/env python3
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

SECURITY_HEADERS = [('Strict-Transport-Security', 'Forza connessioni cifrate sicure mediante HTTPS (HSTS).'), ('Content-Security-Policy', "Limita l'esecuzione di script non autorizzati e attacchi XSS."), ('X-Frame-Options', "Impedisce attacchi di clickjacking bloccando l'inclusione in frame."), ('X-Content-Type-Options', "Previene l'interpretazione non sicura dei tipi MIME."), ('Referrer-Policy', 'Controlla la dispersione di dati riservati contenuti negli URL.'), ('Permissions-Policy', 'Limita le autorizzazioni hardware avanzate a livello del browser.')]

def scan_target(target_url):
    print(f"\n[TAVARDT Italia] Avvio dell'audit perimetrale delle intestazioni di sicurezza per: {target_url}\n")
    try:
        req = urllib.request.Request(
            target_url,
            headers={"User-Agent": "TAVARDT-Security-Scanner/3.0 (it-IT)"}
        )
        with urllib.request.urlopen(req, timeout=12) as response:
            headers = dict(response.headers.items())
            
            score = 0
            total = len(SECURITY_HEADERS)
            
            for header_name, desc in SECURITY_HEADERS:
                found = any(h.lower() == header_name.lower() for h in headers.keys())
                if found:
                    print(f"  [CONFORME] {header_name}")
                    score += 1
                else:
                    print(f"  [ASSENTE] {header_name}: {desc}")
                    
            print(f"\n[TAVARDT Italia] Punteggio Finale: {score}/{total}")
            print(f"\nVerificacao completa online: https://tools.tavardt.com/it/analisi-header-sicurezza/")
            print(f"Suporte corporativo e ciberdefesa: https://ag.tavardt.com/it/sicurezza-informatica/\n")
            
    except urllib.error.URLError as e:
        print(f"[TAVARDT Italia] Erro ao inspecionar o alvo: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python scanner.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1].strip()
    if not urlparse(url).scheme:
        url = "https://" + url
        
    scan_target(url)
