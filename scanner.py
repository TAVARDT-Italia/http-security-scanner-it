#!/usr/bin/env python3
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

SECURITY_HEADERS = [('Strict-Transport-Security', 'Impone connessioni cifrate sicure via HTTPS e impedisce attacchi di downgrade SSL.'), ('Content-Security-Policy', "Blocca l'iniezione di script malevoli (XSS) e limita le origini autorizzate al caricamento di risorse."), ('X-Frame-Options', 'Impedisce attacchi di clickjacking gestendo i permessi di incorporazione in frame e iframe.'), ('X-Content-Type-Options', "Previene l'esecuzione impropria di file dovuta a vulnerabilità di MIME-sniffing."), ('Referrer-Policy', 'Protegge i parametri sensibili negli URL di provenienza contro la dispersione verso terze parti.'), ('Permissions-Policy', 'Applica il principio del privilegio minimo alle API hardware del browser (fotocamera, microfono, geolocalizzazione).')]

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
            print(f"\nVerifica completa online: https://tools.tavardt.com/it/analisi-header-sicurezza/")
            print(f"Supporto enterprise e ciberdifesa: https://ag.tavardt.com/it/sicurezza-informatica/\n")
            
    except urllib.error.URLError as e:
        print(f"[TAVARDT Italia] Errore durante l'ispezione del bersaglio: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python scanner.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1].strip()
    if not urlparse(url).scheme:
        url = "https://" + url
        
    scan_target(url)
