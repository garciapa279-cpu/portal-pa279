import requests
from bs4 import BeautifulSoup
import json
import os

sites = [
    "https://correiodecarajas.com.br/",
    "https://pebinhadeacucar.com.br/",
    "https://www.zedudu.com.br/"
]

def buscar_e_salvar_completo():
    print("📸 Coletando notícias e imagens para o Portal Pá 279...")
    todas_noticias = []
    
    for url in sites:
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            resposta = requests.get(url, headers=headers, timeout=10)
            sopa = BeautifulSoup(resposta.text, 'html.parser')
            
            # Procura blocos de notícias (manchetes)
            artigos = sopa.find_all(['article', 'div'], class_=['post', 'noticia', 'entry'], limit=5)
            
            if not artigos: # Se não achar por classe, tenta por tags comuns
                artigos = sopa.find_all('h3', limit=5)

            for art in artigos:
                titulo = art.get_text().strip()
                link_img = ""
                
                # Tenta achar uma imagem dentro do bloco da notícia
                img_tag = art.find('img')
                if img_tag:
                    link_img = img_tag.get('src') or img_tag.get('data-src')

                if len(titulo) > 30:
                    todas_noticias.append({
                        "origem": url,
                        "titulo": titulo,
                        "imagem": link_img
                    })
        except:
            continue

    with open('1_bruto/noticias_do_dia.json', 'w', encoding='utf-8') as f:
        json.dump(todas_noticias, f, ensure_ascii=False, indent=4)
    
    print(f"✅ Sucesso! {len(todas_noticias)} notícias com imagens salvas.")

if __name__ == "__main__":
    buscar_e_salvar_completo()