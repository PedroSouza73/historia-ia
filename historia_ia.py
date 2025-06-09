import streamlit as st
import google.generativeai as genai  # ou qualquer outra IA, como OpenAI

# Configurar a chave da API (substitua pela sua se necessário)
api_key = st.secrets("API_KEY")
genai.configure(api_key=api_key)

# Função para gerar a história
def gerar_historia(nome, genero, local, frase):
    prompt = (
        f"Crie o início de uma história do gênero '{genero}' com o protagonista chamado '{nome}'. "
        f"A história começa em '{local}'. Incorpore a seguinte frase ou desafio no início: '{frase}'. "
        f"Escreva um ou dois parágrafos envolventes e criativos."
    )
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# Interface com o usuário
st.title("📚 Criador de Histórias Interativas com IA")

# 1. Nome do protagonista
nome_protagonista = st.text_input("Nome do Protagonista")

# 2. Gênero literário
genero = st.selectbox("Escolha o Gênero Literário", 
                      ["Fantasia", "Ficção Científica", "Mistério", "Aventura"])

# 3. Local inicial
local_inicial = st.radio("Escolha o Local Inicial da História", 
                         ["Uma floresta antiga", "Uma cidade futurista", "Um castelo assombrado", "Uma nave espacial à deriva"])

# 4. Frase de efeito ou desafio
frase_desafio = st.text_area("Adicione uma Frase de Efeito ou Desafio Inicial",
                             placeholder="Ex: E de repente, tudo ficou escuro.")

# 5. Botão de gerar história
if st.button("Gerar Início da História"):
    if nome_protagonista.strip() == "" or frase_desafio.strip() == "":
        st.warning("Por favor, preencha o nome do protagonista e a frase de desafio.")
    else:
        with st.spinner("Gerando sua história..."):
            historia = gerar_historia(nome_protagonista, genero, local_inicial, frase_desafio)
            st.subheader("📝 Início da História")
            st.write(historia)
