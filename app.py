import streamlit as st
from dataclasses import dataclass
from typing import List

# Configuração da página
st.set_page_config(
    page_title="Leonardo Braga | Ciência de Dados e IA",
    page_icon="◽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS customizado para aproximar do design React
st.markdown("""
<style>
    /* Reset e estilos globais */
    .main {
        background-color: #f9fafb;
    }
    
    @media (prefers-color-scheme: dark) {
        .main {
            background-color: #020617;
        }
    }
    
    /* Header fixo */
    header[data-testid="stHeader"] {
        background-color: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(8px);
        border-bottom: 1px solid #e2e8f0;
    }
    
    @media (prefers-color-scheme: dark) {
        header[data-testid="stHeader"] {
            background-color: rgba(15, 23, 42, 0.9);
            border-bottom: 1px solid #1e293b;
        }
    }
    
    /* Remover padding extra */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }
    
    /* Títulos */
    h1 {
        font-weight: 800;
        color: #0f172a;
        line-height: 1.2;
    }
    
    @media (prefers-color-scheme: dark) {
        h1 {
            color: #ffffff;
        }
    }
    
    /* Cards de projeto */
    .project-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 0.5rem;
        padding: 1.5rem;
        height: 100%;
        display: flex;
        flex-direction: column;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        transition: box-shadow 0.3s ease;
    }
    
    .project-card:hover {
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    @media (prefers-color-scheme: dark) {
        .project-card {
            background: #0f172a;
            border-color: #1e293b;
        }
    }
    
    /* Tags */
    .tag {
        display: inline-block;
        padding: 0.25rem 0.5rem;
        background: #f1f5f9;
        color: #475569;
        font-size: 0.75rem;
        border-radius: 0.25rem;
        margin: 0.25rem;
        font-weight: 500;
    }
    
    @media (prefers-color-scheme: dark) {
        .tag {
            background: #1e293b;
            color: #94a3b8;
        }
    }
    
    /* Badge de tipo */
    .badge-hf {
        background: #fef3c7;
        color: #92400e;
        border: 1px solid #fde68a;
        padding: 0.125rem 0.5rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 500;
    }
    
    .badge-streamlit {
        background: #fee2e2;
        color: #991b1b;
        border: 1px solid #fecaca;
        padding: 0.125rem 0.5rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 500;
    }
    
    @media (prefers-color-scheme: dark) {
        .badge-hf {
            background: rgba(251, 191, 36, 0.2);
            color: #fbbf24;
            border-color: #92400e;
        }
        
        .badge-streamlit {
            background: rgba(239, 68, 68, 0.2);
            color: #ef4444;
            border-color: #991b1b;
        }
    }
    
    /* Skill pills */
    .skill-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.375rem 0.75rem;
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 0.375rem;
        font-size: 0.875rem;
        font-weight: 500;
        color: #334155;
        margin: 0.375rem;
    }
    
    @media (prefers-color-scheme: dark) {
        .skill-pill {
            background: #0f172a;
            border-color: #1e293b;
            color: #cbd5e1;
        }
    }
    
    /* Timeline */
    .timeline-item {
        position: relative;
        padding-left: 2rem;
        margin-bottom: 2rem;
    }
    
    .timeline-dot {
        position: absolute;
        left: -0.6rem;
        top: 0.25rem;
        width: 1.25rem;
        height: 1.25rem;
        background: #2563eb;
        border: 4px solid #f9fafb;
        border-radius: 50%;
    }
    
    @media (prefers-color-scheme: dark) {
        .timeline-dot {
            background: #3b82f6;
            border-color: #020617;
        }
    }
    
    /* Botões */
    .stButton > button {
        background: #0f172a;
        color: white;
        border: none;
        border-radius: 0.375rem;
        padding: 0.5rem 1rem;
        font-weight: 500;
        width: 100%;
        transition: background 0.2s;
    }
    
    .stButton > button:hover {
        background: #1e293b;
    }
    
    @media (prefers-color-scheme: dark) {
        .stButton > button {
            background: #f1f5f9;
            color: #0f172a;
        }
        
        .stButton > button:hover {
            background: #e2e8f0;
        }
    }
    
    /* Cards de educação e certificação */
    .edu-card, .cert-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 0.5rem;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    
    @media (prefers-color-scheme: dark) {
        .edu-card, .cert-card {
            background: #0f172a;
            border-color: #1e293b;
        }
    }
    
    /* Article card */
    .article-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 0.5rem;
        padding: 1.25rem;
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }
    
    .article-card:hover {
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transform: translateY(-2px);
    }
    
    @media (prefers-color-scheme: dark) {
        .article-card {
            background: #0f172a;
            border-color: #1e293b;
        }
    }
    
    /* Links sociais */
    .social-link {
        color: #64748b;
        transition: color 0.2s;
        text-decoration: none;
        font-size: 1.25rem;
    }
    
    .social-link:hover {
        color: #2563eb;
    }
    
    /* Gradient text */
    .gradient-text {
        background: linear-gradient(to right, #2563eb, #4f46e5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    @media (prefers-color-scheme: dark) {
        .gradient-text {
            background: linear-gradient(to right, #60a5fa, #818cf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
    }
</style>
""", unsafe_allow_html=True)

# Data classes
@dataclass
class Project:
    title: str
    description: str
    tags: List[str]
    link: str
    type: str

@dataclass
class Experience:
    role: str
    company: str
    period: str
    description: List[str]

@dataclass
class Education:
    institution: str
    degree: str
    period: str
    details: str

@dataclass
class Certification:
    name: str
    issuer: str
    year: str

@dataclass
class Article:
    title: str
    link: str

# Dados do perfil
PROFILE = {
    "name": "Leonardo Borges Silva Braga",
    "role": "Oracle Certified Professional",
    "location": "Brasília, Brasil",
    "email": "leoborgesprofissional@gmail.com",
    "summary": "Estudante de Ciência de Dados e IA com experiência prática em projetos reais de integração e migração de dados (SAP, Pentaho, BBDD) e desenvolvimento de aplicações com LLMs. Certificado pela Oracle em Generative AI Professional e Data Science Professional. Forte atuação em construção de pipelines, prototipação rápida, aplicações conversacionais e produtos orientados a dados.",
    "social": {
        "linkedin": "https://www.linkedin.com/in/leonardo-borges1",
        "github": "https://github.com/Leo-bsb",
        "huggingface": "https://huggingface.co/leo-bsb",
        "medium": "https://medium.com/@leonardoborges6947",
        "email": "mailto:leoborgesprofissional@gmail.com"
    }
}

PROJECTS = [
    Project(
        title="Sistema de Extração de Documentos Jurídicos",
        description="Sistema modular para análise de PDFs jurídicos em larga escala. Processamento em lote otimizado para documentos de 200MB+ com persistência SQLite e validação de esquema.",
        tags=["LLM", "Python", "Streamlit", "Polars", "SQLite"],
        link="https://huggingface.co/spaces/leo-bsb/legal-extraction-system",
        type="Hugging Face"
    ),
    Project(
        title="IA Generativa para Avaliações de Restaurantes",
        description="Modelo generativo que gera respostas empáticas e contextuais a avaliações de restaurantes. Desenvolvido em fluxo interativo com IA para otimização.",
        tags=["LLMs", "Google Gemini", "NLP", "Análise de Sentimento", "Gradio"],
        link="https://huggingface.co/spaces/leo-bsb/bot-for-restaurant-reviews",
        type="Hugging Face"
    ),
    Project(
        title="Gerador de Descrições de Pratos",
        description="Agente inteligente que gera descrições persuasivas de pratos de delivery, personalizadas por estilo. Prototipado em ciclo ágil com IA generativa, integrando engenharia de prompt e ajustes manuais.",
        tags=["LLMs", "Google Gemini", "NLP", "Gradio", "Polars"],
        link="https://huggingface.co/spaces/leo-bsb/generative-ai-for-persuasive-dish-descriptions",
        type="Hugging Face"
    ),
    Project(
        title="Assistente de IA para SAP Data Services",
        description="Chatbot RAG personalizado para usuários do SAP BODS. Integra busca semântica e classificação de intenção para suporte preciso e contextualizado em português.",
        tags=["RAG", "FAISS", "Streamlit", "SAP BODS", "NLP"],
        link="https://sap-bot.streamlit.app/",
        type="Streamlit"
    ),
    Project(
        title="Preditor Inteligente de Tempo de Entrega",
        description="Preditor de tempo de entrega com alta precisão (82%) usando XGBoost. Aplicação de SHAP para explicabilidade do modelo e insights acionáveis.",
        tags=["XGBoost", "SHAP", "Scikit-learn", "Gradio"],
        link="https://leo-bsb-delivery-time-predictor.hf.space/",
        type="Hugging Face"
    ),
    Project(
        title="Recomendação Inteligente de Livros",
        description="Motor de recomendação híbrido combinando aprendizado profundo com filtragem colaborativa usando PyTorch para sugestões personalizadas.",
        tags=["PyTorch", "Redes Neurais", "Deep Learning"],
        link="https://huggingface.co/spaces/leo-bsb/book-recomendation",
        type="Hugging Face"
    ),
    Project(
        title="Dashboard de Nascidos Vivos SINASC 2023",
        description="Plataforma de análise visual para dados de saúde pública brasileira. Interface intuitiva para explorar nascimentos registrados no Brasil com filtros dinâmicos e visualizações interativas.",
        tags=["Streamlit", "Plotly", "Pandas", "Análise de Dados"],
        link="https://dashboard-nascidos-vivos-2023.streamlit.app/",
        type="Streamlit"
    ),
    Project(
        title="Ferramentas de EDA Rápida",
        description="Dashboards de análise exploratória instantânea usando PyGWalker e Polars para processamento eficiente de grandes volumes de dados.",
        tags=["PyGWalker", "Polars", "Plotly", "Streamlit"],
        link="https://huggingface.co/spaces/leo-bsb/Fast_Eda",
        type="Hugging Face"
    )
]

EXPERIENCE = [
    Experience(
        role="Estagiário em Data Migration",
        company="First Decision",
        period="Abr 2025 – Atual",
        description=[
            "Responsável pela migração completa do módulo SAP Quality Management da Neugebauer, entregando o ETL 40% antes do prazo.",
            "Desenvolvimento de pipelines usando SAP Data Services, SAP Cockpit e Pentaho.",
            "Atendimento e comunicação com clientes corporativos (Natura, Neugebauer) para alinhamento técnico e validação de entregas.",
            "Tratamento e integração de grandes volumes de dados corporativos."
        ]
    ),
    Experience(
        role="Membro / Consultor",
        company="DatAí Tecnologia EJ",
        period="Jul 2024 – Jul 2025",
        description=[
            "Coleta, limpeza e análise de dados de fontes públicas e privadas.",
            "Criação de dashboards interativos com Python, SQL e Excel.",
            "Estruturação e armazenamento de dados em bancos SQL."
        ]
    )
]

EDUCATION = [
    Education(
        institution="IESB",
        degree="Bacharelado em Ciência de Dados e Inteligência Artificial - (6º Semestre)",
        period="2023 – 2026",
        details="Disciplinas relevantes: Machine Learning, Mineração de Dados, Estatística Aplicada, Modelagem e Inferência Estatística, Processamento de Dados Massivos, EDA e Visualização."
    )
]

CERTIFICATIONS = [
    Certification(name="Oracle Certified Professional: Generative AI", issuer="Oracle", year="2025"),
    Certification(name="Oracle Certified Professional: Data Science", issuer="Oracle", year="2025"),
    Certification(name="OCI Foundations: AI Foundations", issuer="Oracle", year="2025"),
    Certification(name="OCI Foundations: Data Platform", issuer="Oracle", year="2025"),
    Certification(name="OCI Foundations: Cloud Infrastructure", issuer="Oracle", year="2025"),
    Certification(name="Databricks Accreditation: Fundamentals", issuer="Databricks", year="2025"),
    Certification(name="Databricks Accreditation: Generative AI Fundamentals", issuer="Databricks", year="2025"),
]

CERTIFICATIONS_IN_PROGRESS = [
    "Oracle Multicloud Architect Professional (previsão: 12/2025)",
    "Oracle DevOps Professional (previsão: 12/2025)"
]

ARTICLES = [
    Article(
        title="Como Construí um Sistema de Predição de Tempo de Entrega com 82% de Acurácia",
        link="https://medium.com/@leonardoborges6947/como-construí-um-sistema-de-predição-de-tempo-de-entrega-que-atinge-82-de-acurácia-0ba00382b1f0"
    ),
    Article(
        title="Como Construí um Sistema de Recomendação Híbrido com 80% de Diversidade",
        link="https://medium.com/@leonardoborges6947/como-construí-um-sistema-de-recomendação-híbrido-que-descobre-livros-escondidos-combinando-eada76bc8d58"
    ),
    Article(
        title="Simplificando EDA com PyGWalker: Faça em 1 linha o que antes exigia 50",
        link="https://medium.com/@leonardoborges6947/cansado-de-escrever-50-linhas-de-matplotlib-faça-eda-com-1-linha-usando-pygwalker-4f8548813b2a"
    )
]

SKILLS = [
    {"name": "Python", "icon": "‣"},
    {"name": "SQL", "icon": "‣"},
    {"name": "C", "icon": "‣"},
    {"name": "IA Generativa", "icon": "‣"},
    {"name": "Machine Learning", "icon": "‣"},
    {"name": "PyTorch", "icon": "‣"},
    {"name": "Hugging Face", "icon": "‣"},
    {"name": "Power BI", "icon": "‣"},
    {"name": "Streamlit", "icon": "‣"},
    {"name": "Gradio", "icon": "‣"},
    {"name": "Plotly", "icon": "‣"},
    {"name": "Matplotlib", "icon": "‣"},
    {"name": "SAP Data Services", "icon": "‣"},
    {"name": "SAP Cockpit", "icon": "‣"},
    {"name": "SAS Viya", "icon": "‣"},
    {"name": "Pentaho", "icon": "‣"},
    {"name": "Banco de Dados", "icon": "‣"},
    {"name": "EDA", "icon": "‣"},
    {"name": "Estatística", "icon": "‣"}
]

# Header
header_col1, header_col2 = st.columns([3, 1])
with header_col1:
    st.markdown(f"# {PROFILE['name']}")
    st.markdown(f"<p style='color: #64748b; margin-top: -1rem;'>{PROFILE['role']}</p>", unsafe_allow_html=True)

with header_col2:
    social_html = f"""
    <div style='
        display: flex; 
        justify-content: flex-end; 
        gap: 1rem; 
        margin-top: 1rem; 
        font-family: Arial, sans-serif; 
        font-size: 0.9rem;
    '>
        <a href="{PROFILE['social']['linkedin']}" target="_blank" class="social-link" title="LinkedIn" style="text-decoration: none; color: inherit;">
            🔗 LinkedIn
        </a>
        <a href="{PROFILE['social']['github']}" target="_blank" class="social-link" title="GitHub" style="text-decoration: none; color: inherit;">
            🐙 GitHub
        </a>
        <a href="{PROFILE['social']['huggingface']}" target="_blank" class="social-link" title="Hugging Face" style="text-decoration: none; color: inherit;">
            🤗 HuggingFace
        </a>
        <a href="{PROFILE['social']['medium']}" target="_blank" class="social-link" title="Medium" style="text-decoration: none; color: inherit;">
            ✍️ Medium
        </a>
        <a href="mailto:{PROFILE['social']['email']}" class="social-link" title="Email" style="text-decoration: none; color: inherit;">
            📧 Email
        </a>
    </div>
    """

    st.markdown(social_html, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Seção de Introdução
st.markdown(f"<p style='color: #2563eb; font-weight: 500;'>▸ {PROFILE['location']}</p>", unsafe_allow_html=True)

st.markdown("""
<h1 style='font-size: 2.5rem; margin-top: 1rem;'>
    Ciência de Dados e<br>
    <span class='gradient-text'>Inteligência Artificial</span>
</h1>
""", unsafe_allow_html=True)

st.markdown(f"<p style='font-size: 1.125rem; color: #475569; line-height: 1.75; max-width: 48rem; margin-top: 1.5rem;'>{PROFILE['summary']}</p>", unsafe_allow_html=True)

# Skills
st.markdown("<h3 style='font-size: 0.75rem; font-weight: 600; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 2rem; margin-bottom: 1rem;'>COMPETÊNCIAS PRINCIPAIS</h3>", unsafe_allow_html=True)

skills_html = "<div>"
for skill in SKILLS:
    skills_html += f"<span class='skill-pill'>{skill['icon']} {skill['name']}</span>"
skills_html += "</div>"
st.markdown(skills_html, unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)

# Projetos em Destaque
st.markdown("## Projetos em Destaque")
st.markdown("<br>", unsafe_allow_html=True)

cols = st.columns(3)
for idx, project in enumerate(PROJECTS):
    with cols[idx % 3]:
        badge_class = "badge-hf" if project.type == "Hugging Face" else "badge-streamlit"
        
        card_html = f"""
        <div class='project-card'>
            <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;'>
                <h3 style='font-size: 1.25rem; font-weight: 600; flex: 1;'>{project.title}</h3>
                <span class='{badge_class}'>{project.type}</span>
            </div>
            <p style='color: #64748b; font-size: 0.875rem; margin-bottom: 1.5rem; line-height: 1.6; flex-grow: 1;'>
                {project.description}
            </p>
            <div style='margin-bottom: 1.5rem;'>
                {''.join([f"<span class='tag'>{tag}</span>" for tag in project.tags])}
            </div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
        st.link_button("▸ Acessar Projeto", project.link, use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Grid: Experiência e Educação
col1, col2 = st.columns(2)

with col1:
    st.markdown("## Experiência Profissional")
    st.markdown("<br>", unsafe_allow_html=True)
    
    timeline_html = "<div style='border-left: 2px solid #e2e8f0; padding-left: 0; margin-left: 0.75rem;'>"
    for exp in EXPERIENCE:
        timeline_html += f"""
        <div class='timeline-item'>
            <span class='timeline-dot'></span>
            <div style='display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 0.5rem;'>
                <h3 style='font-size: 1.125rem; font-weight: 700;'>{exp.company}</h3>
                <span style='font-size: 0.875rem; color: #64748b; font-weight: 500;'>{exp.period}</span>
            </div>
            <h4 style='color: #2563eb; font-weight: 500; margin-bottom: 0.75rem;'>{exp.role}</h4>
            <ul style='margin: 0; padding-left: 0; list-style: none;'>
        """
        for desc in exp.description:
            timeline_html += f"<li style='color: #475569; font-size: 0.875rem; line-height: 1.6; margin-bottom: 0.5rem;'>▸ {desc}</li>"
        timeline_html += "</ul></div>"
    timeline_html += "</div>"
    
    st.markdown(timeline_html, unsafe_allow_html=True)

with col2:
    # Educação
    st.markdown("## Formação Acadêmica")
    st.markdown("<br>", unsafe_allow_html=True)
    
    for edu in EDUCATION:
        edu_html = f"""
        <div class='edu-card'>
            <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem;'>
                <h3 style='font-weight: 700;'>{edu.institution}</h3>
                <span style='font-size: 0.875rem; color: #64748b; background: #f1f5f9; padding: 0.25rem 0.5rem; border-radius: 0.25rem;'>{edu.period}</span>
            </div>
            <p style='color: #2563eb; font-weight: 500; font-size: 0.875rem; margin-bottom: 0.5rem;'>{edu.degree}</p>
            <p style='color: #475569; font-size: 0.875rem;'>{edu.details}</p>
        </div>
        """
        st.markdown(edu_html, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Certificações
    st.markdown("## Certificações")
    st.markdown("<br>", unsafe_allow_html=True)
    
    for cert in CERTIFICATIONS:
        cert_html = f"""
        <div class='cert-card'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <div>
                    <h4 style='font-weight: 600; font-size: 0.875rem; margin-bottom: 0.25rem;'>{cert.name}</h4>
                    <p style='font-size: 0.75rem; color: #64748b; margin: 0;'>{cert.issuer}</p>
                </div>
                <span style='font-size: 0.75rem; font-family: monospace; color: #94a3b8;'>{cert.year}</span>
            </div>
        </div>
        """
        st.markdown(cert_html, unsafe_allow_html=True)
    
    # Certificações em andamento
    if CERTIFICATIONS_IN_PROGRESS:
 #       st.markdown("<div style='margin-top: 1rem; padding: 1rem; background: #f8fafc; border-left: 3px solid #2563eb; border-radius: 0.25rem;'>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 0.75rem; font-weight: 600; color: #64748b; margin-bottom: 0.5rem;'>EM ANDAMENTO:</p>", unsafe_allow_html=True)
        for cert_prog in CERTIFICATIONS_IN_PROGRESS:
            st.markdown(f"<p style='font-size: 0.875rem; color: #475569; margin: 0.25rem 0;'>▸ {cert_prog}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Artigos Técnicos
st.markdown("## Artigos Técnicos Publicados")
st.markdown("<br>", unsafe_allow_html=True)

for article in ARTICLES:
    article_html = f"""
    <a href="{article.link}" target="_blank" style="text-decoration: none;">
        <div class='article-card'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <p style='color: #334155; font-weight: 500; font-size: 0.875rem; margin: 0; flex: 1;'>▸ {article.title}</p>
                <span style='color: #94a3b8; font-size: 1rem; margin-left: 1rem;'>→</span>
            </div>
        </div>
    </a>
    """
    st.markdown(article_html, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    f"<p style='text-align: center; color: #64748b; font-size: 0.875rem;'>© 2025 Leonardo Braga. Construído para impacto em produção.</p>",
    unsafe_allow_html=True
)
