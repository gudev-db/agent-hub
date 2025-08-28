import streamlit as st
import os

# Configuração da página
st.set_page_config(
    page_title="Hub de Agentes Macfor",
    page_icon="assets/page-icon.png",
    layout="centered"
)

# Logo da Macfor (da pasta assets)
if os.path.exists("assets/macLogo.png"):
    st.image("assets/macLogo.png", width=200)
else:
    st.title("🚀 Hub de Agentes Macfor")

st.header("Central de acesso aos agentes especializados")

# Agentes
agents = [
    {
        "name": "Agente Broto",
        "description": "Agente especializado em soluções para Broto",
        "url": "https://agente-broto.streamlit.app/",
        "icon": "🌱"
    },
    {
        "name": "Agente Holambra",
        "description": "Agente especializado em soluções para Holambra",
        "url": "https://agente-holambra.streamlit.app/",
        "icon": "🌸"
    },
    {
        "name": "Positivo Empresas",
        "description": "Agente especializado em Positivo empresas",
        "url": "https://agente-positivo-empresas.streamlit.app/",
        "icon": "🏢"
    },
    {
        "name": "Positivo Tecnologia",
        "description": "Agente especializado em Positivo Tecnologia",
        "url": "https://agente-positivo-tec.streamlit.app/",
        "icon": "💻"
    }
    ,
    {
        "name": "Eurochem",
        "description": "Agente especializado em Eurochem",
        "url": "https://agente-eurochem.streamlit.app/",
        "icon": "💻"
    }
]


# Exibir agentes de forma simples
for agent in agents:
    st.subheader(f"{agent['icon']} {agent['name']}")
    st.write(agent['description'])
    
    # Link como markdown
    st.markdown(f"[Acessar Agente]({agent['url']})")
    st.write("---")

# Rodapé
st.write("---")
st.caption("Macfor Marketing Digital - Todos os direitos reservados")
