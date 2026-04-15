import streamlit as st
import json
import os

st.set_page_config(page_title="Pá 279 - Painel", layout="wide")
st.title("🚜 Central de Redação - Portal Pá 279")

# ÁREA DE POLÍTICA EM DESTAQUE (TAMANHO GRANDE)
st.subheader("🏛️ Coluna de Política do Estado")
texto_politica = st.text_area("Escreva aqui os bastidores e análises da política do Pará:", height=400)
if st.button("💾 Salvar Coluna de Política"):
    if not os.path.exists('1_bruto'): os.makedirs('1_bruto')
    with open('1_bruto/politica_para.txt', 'w', encoding='utf-8') as f:
        f.write(texto_politica)
    st.success("Texto de política salvo com sucesso!")

st.markdown("---")

# ÁREA DE NOTÍCIAS ABAIXO
caminho = '1_bruto/noticias_do_dia.json'
if os.path.exists(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        noticias = json.load(f)
    
    st.subheader("📋 Selecionar Notícias Regionais")
    aprovadas = []

    for i, n in enumerate(noticias):
        with st.expander(f"Notícia {i+1}: {n['titulo'][:50]}..."):
            col1, col2 = st.columns([1, 2])
            with col1:
                img = n.get('imagem') if n.get('imagem') else "https://via.placeholder.com/300x200?text=Sem+Imagem"
                st.image(img)
            with col2:
                novo_tit = st.text_input(f"Editar Título", n['titulo'], key=f"t_{i}")
                opc = st.radio("Ação:", ["Analisar", "Aprovar ✅", "Excluir 🗑️"], key=f"s_{i}")
                if opc == "Aprovar ✅":
                    aprovadas.append({"titulo": novo_tit, "imagem": n.get('imagem'), "origem": n['origem']})

    if st.button("🚀 PUBLICAR TUDO NO PORTAL"):
        if not os.path.exists('2_modulado'): os.makedirs('2_modulado')
        with open('2_modulado/aprovadas.json', 'w', encoding='utf-8') as f:
            json.dump(aprovadas, f, indent=4)
        st.success("Tudo pronto! Agora rode o postador.py no VS Code.")
else:
    st.error("Rode o 'python coletor.py' primeiro.")