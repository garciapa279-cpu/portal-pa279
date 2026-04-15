import json
import os
import subprocess
from datetime import datetime

def enviar_para_github():
    try:
        # Garante que estamos na pasta certa para o Git
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Atualizacao Estilo G1 - {datetime.now().strftime('%d/%m %H:%M')}"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("🚀 SUCESSO: Portal atualizado e enviado para o ar!")
    except Exception as e:
        print(f"❌ Erro ao enviar para a internet: {e}")

def gerar_portal():
    print("🎨 Gerando Layout Profissional Estilo G1...")
    caminho_dados = '2_modulado/aprovadas.json'
    
    if not os.path.exists(caminho_dados):
        print("❌ Erro: O arquivo de notícias não foi encontrado!")
        return

    with open(caminho_dados, 'r', encoding='utf-8') as f:
        noticias = json.load(f)

    if not noticias:
        print("⚠️ Nenhuma notícia encontrada para exibir.")
        return

    # A primeira notícia vira o DESTAQUE PRINCIPAL
    destaque = noticias[0]
    outras_noticias = noticias[1:]

    html = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.tailwindcss.com"></script>
        <title>PÁ 279 | Portal de Notícias</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
            body {{ font-family: 'Inter', sans-serif; }}
        </style>
    </head>
    <body class="bg-gray-50 text-gray-900">
        
        <header class="bg-[#004a23] text-white py-6 shadow-md border-b-4 border-yellow-500">
            <div class="container mx-auto px-4 flex justify-between items-center">
                <div>
                    <h1 class="text-5xl font-black tracking-tighter">PÁ 279</h1>
                    <p class="text-xs uppercase tracking-widest font-bold opacity-80">O seu portal de notícias do Pará</p>
                </div>
                <div class="hidden md:block text-right">
                    <p class="text-sm font-bold">{datetime.now().strftime('%d de %B de %Y')}</p>
                </div>
            </div>
        </header>

        <main class="container mx-auto px-4 py-8">
            
            <section class="mb-12">
                <a href="{destaque['origem']}" target="_blank" class="group relative block w-full h-[500px] overflow-hidden rounded-xl shadow-2xl">
                    <img src="{destaque.get('imagem', 'https://images.unsplash.com/photo-1585829365234-781f3495d013?auto=format&fit=crop&q=80&w=1000')}" 
                         class="w-full h-full object-cover transition duration-500 group-hover:scale-105">
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent"></div>
                    <div class="absolute bottom-0 p-8 text-white">
                        <span class="bg-red-600 px-3 py-1 text-xs font-bold uppercase rounded">Destaque</span>
                        <h2 class="text-4xl md:text-5xl font-extrabold mt-4 leading-tight">{destaque['titulo']}</h2>
                        <p class="mt-4 text-gray-200 font-medium">Clique para ler a reportagem completa no portal de origem.</p>
                    </div>
                </a>
            </section>

            <h3 class="text-2xl font-black mb-6 border-l-8 border-[#004a23] pl-4 uppercase">Últimas Notícias</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
    """

    for noticia in outras_noticias:
        html += f"""
                <article class="bg-white rounded-lg shadow-lg overflow-hidden flex flex-col hover:shadow-2xl transition">
                    <img src="{noticia.get('imagem', 'https://via.placeholder.com/400x200')}" class="w-full h-48 object-cover">
                    <div class="p-5 flex-grow">
                        <h4 class="text-xl font-bold leading-snug mb-3 hover:text-green-800 transition">
                            <a href="{noticia['origem']}" target="_blank">{noticia['titulo']}</a>
                        </h4>
                    </div>
                    <div class="p-5 pt-0">
                        <a href="{noticia['origem']}" target="_blank" class="text-[#004a23] font-bold text-sm uppercase tracking-wider hover:underline italic">
                            Ler matéria →
                        </a>
                    </div>
                </article>
        """

    html += """
            </div>
        </main>

        <footer class="bg-gray-900 text-white py-10 mt-12">
            <div class="container mx-auto px-4 text-center">
                <p class="font-bold text-xl">PÁ 279</p>
                <p class="text-gray-500 text-sm mt-2">© 2026 - Todos os direitos reservados.</p>
            </div>
        </footer>

    </body>
    </html>
    """
    
    # Salva o arquivo final
    if not os.path.exists('3_final'):
        os.makedirs('3_final')
        
    with open('3_final/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("✅ Novo Layout G1 gerado com sucesso!")
    enviar_para_github()

if __name__ == "__main__":
    gerar_portal()