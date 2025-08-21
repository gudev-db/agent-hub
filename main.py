import streamlit as st
import os

# Configuração da página
st.set_page_config(
    page_title="Hub de Agentes Macfor",
    page_icon="assets/page-icon.png",
    layout="centered"
)

# CSS personalizado
st.markdown("""
<style>
    .header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #0e3b92 0%, #2a5caa 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .agent-card {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    .agent-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    .link-button {
        background-color: #0077b5;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        text-decoration: none;
        display: inline-block;
        margin-top: 0.5rem;
        transition: background-color 0.3s ease;
    }
    .link-button:hover {
        background-color: #005582;
        color: white;
    }
    .logo-container {
        text-align: center;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Logo da Macfor (da pasta assets)
if os.path.exists("assets/macLogo.png"):
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    st.image("assets/macLogo.png", width=200)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="header"><h1>🚀 Hub de Agentes Macfor</h1></div>', unsafe_allow_html=True)

# Cabeçalho
st.markdown('<div class="header"><h2>Central de acesso aos agentes especializados</h2></div>', unsafe_allow_html=True)

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
        "description": "Agente especializado em soluções empresariais Positivo",
        "url": "https://agente-positivo-empresas.streamlit.app/",
        "icon": "🏢"
    },
    {
        "name": "Positivo Tecnologia",
        "description": "Agente especializado em soluções técnicas Positivo",
        "url": "https://agente-positivo-tec.streamlit.app/",
        "icon": "💻"
    }
]

# Exibir cards dos agentes
for agent in agents:
    st.markdown(f"""
    <div class="agent-card">
        <h3>{agent['icon']} {agent['name']}</h3>
        <p>{agent['description']}</p>
        <a href="{agent['url']}" target="_blank" class="link-button">Acessar Agente</a>
    </div>
    """, unsafe_allow_html=True)

# Rodapé
st.markdown("---")
st.markdown("<p style='text-align: center; color: #666;'>Macfor Marketing Digital - Todos os direitos reservados</p>", unsafe_allow_html=True)
