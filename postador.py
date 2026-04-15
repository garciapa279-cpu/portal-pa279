import json
import os

# Função para garantir que os links de imagem fiquem bonitos
def formatar_imagem(url):
    if not url or url == "" or url == "None":
        return "https://via.placeholder.com/400x250?text=P%C3%A1+279+Informa%C3%A7%C3%A3o"
    return url

def gerar_portal_final():
    print("🚀 Gerando o novo portal Pá 279 com vida e notícias...")
    
    # Caminhos
    caminho_aprovadas = '2_modulado/aprovadas.json'
    caminho_politica = '1_bruto/politica_para.txt'
    
    # Se não tiver notícias, não gera
    if not os.path.exists(caminho_aprovadas):
        print("❌ Nenhuma notícia aprovada encontrada! Vá ao painel e publique.")
        return

    with open(caminho_aprovadas, 'r', encoding='utf-8') as f:
        noticias = json.load(f)

    # Lê a política ou usa o padrão
    texto_politica = "Escreva sua análise no painel..."
    if os.path.exists(caminho_politica):
        with open(caminho_politica, 'r', encoding='utf-8') as f:
            texto_politica = f.read().replace('\n', '<br>')

    html = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Portal Pá 279 | Regional</title>
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; background: #e9ecef; margin: 0; padding: 0; }}
            
            /* Cabeçalho Verde Moderno */
            header {{ background: linear-gradient(135deg, #1b5e20, #388e3c); color: white; padding: 30px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.2); }}
            header h1 {{ margin: 0; font-size: 2.5rem; }}

            /* CONTAINER PRINCIPAL (GRID) */
            .container {{ max-width: 1200px; margin: 20px auto; display: grid; grid-template-columns: 1.5fr 2.5fr; gap: 20px; padding: 10px; }}

            /* --- COLUNA ESQUERDA: POLÍTICA (OCUPA 40% APROX.) --- */
            .politica-container {{
                background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.9)), url('https://upload.wikimedia.org/wikipedia/commons/e/ea/Estacao_das_docas_belem.jpg');
                background-size: cover;
                background-position: center;
                border-radius: 12px;
                padding: 25px;
                color: white;
                height: fit-content;
                border-top: 10px solid #ffca28; /* Faixa amarela de destaque */
                box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            }}
            
            .politica-container h2 {{ color: #ffca28; margin-top: 0; display: flex; align-items: center; gap: 10px; }}
            .politica-container p {{ font-size: 1.1rem; line-height: 1.6; }}

            /* --- COLUNA DIREITA: GRID DE NOTÍCIAS --- */
            .noticias-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }}
            
            /* Estilo dos Cards de Notícia */
            .card {{ background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 3px 8px rgba(0,0,0,0.1); transition: transform 0.3s; }}
            .card:hover {{ transform: translateY(-5px); }}
            
            .card img {{ width: 100%; height: 180px; object-fit: cover; display: block; }}
            
            .card-content {{ padding: 15px; }}
            .card-content h3 {{ font-size: 1.1rem; margin: 0 0 10px; color: #333; height: 55px; overflow: hidden; }}
            .card-content a {{ text-decoration: none; color: #1b5e20; font-weight: bold; font-size: 0.9rem; }}
        </style>
    </head>
    <body>
        <header>
            <h1>PÁ 279</h1>
            <p>Integração Regional: Xinguara até Marabá</p>
        </header>
        
        <div class="container">
            <div class="politica-container">
                <h2>🏛️ POLÍTICA DO ESTADO</h2>
                <p>{texto_politica}</p>
            </div>
            
            <div class="noticias-grid">
    """

    for n in noticias:
        img_url = formatar_imagem(n.get('imagem'))
        html += f"""
                <div class="card">
                    <img src="{img_url}">
                    <div class="card-content">
                        <h3>{n['titulo']}</h3>
                        <a href="{n['origem']}" target="_blank">Ler reportagem completa →</a>
                    </div>
                </div>
        """

    html += """
            </div>
        </div>
        <footer style="text-align:center; padding: 20px; color: #777;">Portal Regional Pá 279</footer>
    </body>
    </html>
    """

    # Cria a pasta e salva
    if not os.path.exists('3_final'): os.makedirs('3_final')
    with open('3_final/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ Site gerado com Política em destaque e Notícias em Grid!")

if __name__ == "__main__":
    gerar_portal_final()