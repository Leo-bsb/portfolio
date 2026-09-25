# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Image
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import glob

# ---------- Fontes (tenta usar DejaVu para bom suporte a acentos) ----------
FONT_REG = "Helvetica"
FONT_BOLD = "Helvetica-Bold"
try:
    dejavu_reg = glob.glob("/usr/share/fonts/**/DejaVuSans.ttf", recursive=True)
    dejavu_bold = glob.glob("/usr/share/fonts/**/DejaVuSans-Bold.ttf", recursive=True)
    if dejavu_reg and dejavu_bold:
        pdfmetrics.registerFont(TTFont("DejaVu", dejavu_reg[0]))
        pdfmetrics.registerFont(TTFont("DejaVu-Bold", dejavu_bold[0]))
        pdfmetrics.registerFontFamily(
            "DejaVu", normal="DejaVu", bold="DejaVu-Bold", italic="DejaVu", boldItalic="DejaVu-Bold"
        )
        FONT_REG, FONT_BOLD = "DejaVu", "DejaVu-Bold"
except Exception:
    pass

# ---------- Paleta (mesma do site) ----------
INK = colors.HexColor("#101a17")
INK_DIM = colors.HexColor("#4b5b54")
INK_MUTE = colors.HexColor("#788a82")
ACCENT = colors.HexColor("#00996f")   # versão escurecida do mint p/ ficar legível em fundo claro
ACCENT_SOFT = colors.HexColor("#e8f8f2")
LINE = colors.HexColor("#d8e2dd")

PAGE_W, PAGE_H = A4
MARGIN = 16 * mm

doc = SimpleDocTemplate(
    "Leonardo_Borges_Braga_CV.pdf",
    pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=9 * mm, bottomMargin=8 * mm,
    title="Leonardo Borges Silva Braga — Currículo",
    author="Leonardo Borges Silva Braga",
)

styles = {
    "name": ParagraphStyle("name", fontName=FONT_BOLD, fontSize=20, textColor=INK, leading=23),
    "role": ParagraphStyle("role", fontName=FONT_REG, fontSize=10.5, textColor=ACCENT, leading=14, spaceAfter=2),
    "contact": ParagraphStyle("contact", fontName=FONT_REG, fontSize=8.4, textColor=INK_DIM, leading=11.5),
    "h2": ParagraphStyle("h2", fontName=FONT_BOLD, fontSize=10.4, textColor=INK, spaceBefore=3.5, spaceAfter=2.5,
                          leading=12),
    "body": ParagraphStyle("body", fontName=FONT_REG, fontSize=8.5, textColor=INK_DIM, leading=11.3),
    "job_title": ParagraphStyle("job_title", fontName=FONT_BOLD, fontSize=9.4, textColor=INK, leading=11.5),
    "job_meta": ParagraphStyle("job_meta", fontName=FONT_REG, fontSize=8, textColor=ACCENT, leading=10.5,
                                spaceAfter=1.5),
    "bullet": ParagraphStyle("bullet", fontName=FONT_REG, fontSize=8.3, textColor=INK_DIM, leading=10.8,
                              leftIndent=10, bulletIndent=0, spaceAfter=0.8),
    "skill_head": ParagraphStyle("skill_head", fontName=FONT_BOLD, fontSize=8.9, textColor=INK, leading=12),
    "skill_val": ParagraphStyle("skill_val", fontName=FONT_REG, fontSize=8.7, textColor=INK_DIM, leading=11,
                                 spaceAfter=2),
    "tag_line": ParagraphStyle("tag_line", fontName=FONT_REG, fontSize=9.6, textColor=INK, leading=13.5,
                                spaceAfter=2),
}

story = []

# ---------- Cabeçalho ----------
try:
    photo = Image("leonardo.jpg", width=22 * mm, height=22 * mm)
except Exception:
    photo = None

header_text = [
    Paragraph("Leonardo Borges Silva Braga", styles["name"]),
    Paragraph("Ciência de Dados · Engenharia de Dados · Governança &amp; Privacidade (LGPD)", styles["role"]),
    Spacer(1, 3),
    Paragraph(
        "leoborgesprofissional@gmail.com &nbsp;·&nbsp; (61) 9 9294-4998 &nbsp;·&nbsp; Brasília, DF<br/>"
        "linkedin.com/in/leonardo-borges1 &nbsp;·&nbsp; github.com/Leo-bsb &nbsp;·&nbsp; leonardo-braga.dev",
        styles["contact"],
    ),
]

if photo:
    header_tbl = Table([[photo, header_text]], colWidths=[24 * mm, None])
    header_tbl.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("LEFTPADDING", (1, 0), (1, 0), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(header_tbl)
else:
    story.extend(header_text)

story.append(Spacer(1, 3))
story.append(HRFlowable(width="100%", thickness=1.1, color=ACCENT))
story.append(Spacer(1, 3))

# ---------- Frase de posicionamento ----------
story.append(Paragraph(
    "Construo pontes entre engenharia, ciência e governança de dados: pipelines que entregam valor "
    "sem abrir mão de segurança, ética e conformidade com a LGPD.",
    styles["tag_line"],
))
story.append(Spacer(1, 1))

# ---------- Resumo ----------
story.append(Paragraph("RESUMO PROFISSIONAL", styles["h2"]))
story.append(Paragraph(
    "Cientista de Dados formado em Ciência de Dados e IA, com atuação prática em Engenharia de Dados e "
    "interesse central em Governança, Segurança e Ética no tratamento de dados, alinhado à LGPD. Domino "
    "SQL, Python e ferramentas de integração e analytics (SAP/Pentaho, SAS), com histórico de otimização "
    "de pipelines e melhoria de qualidade de dados em ambientes enterprise. Criei o Datalock Studio, uma "
    "biblioteca e plataforma de anonimização de dados com k-anonimato, pseudonimização e criptografia, "
    "publicada e em processo de submissão na Microsoft Store, além de projetos de Machine Learning como "
    "sistemas de recomendação híbridos. Busco uma oportunidade para aplicar essas competências no "
    "desenvolvimento de sistemas de dados robustos, seguros e eticamente responsáveis.",
    styles["body"],
))

# ---------- Experiência ----------
story.append(Paragraph("EXPERIÊNCIA", styles["h2"]))

def add_job(title, company, period, mode, bullets):
    story.append(Paragraph(f"{title} <font color='#4b5b54'>· {company}</font>", styles["job_title"]))
    story.append(Paragraph(f"{period} — {mode}", styles["job_meta"]))
    for b in bullets:
        story.append(Paragraph(f"–  {b}", styles["bullet"]))
    story.append(Spacer(1, 1.5))

add_job(
    "Estagiário em Ciência de Dados", "IZE Gestão Empresarial", "01/2026 — 05/2026", "Híbrido",
    [
        "Desenvolvi dashboards e KPIs em tempo real com Streamlit, Airflow e EvolutionAPI (integração com WhatsApp).",
        "Auditei a qualidade dos programas internos e corrigi bugs e más práticas de codebase.",
        "Automatizei fluxos de alimentação de banco de dados e planilhas com Apps Script.",
    ],
)
add_job(
    "Estagiário em Data Migration", "First Decision", "04/2025 — 01/2026", "Híbrido",
    [
        "Desenvolvimento e sustentação de pipelines de ETL complexos para clientes enterprise (Natura, Neugebauer).",
        "Otimizei fluxos de carga e transformação de dados — entrega 40% antecipada ao cronograma oficial.",
        "Implementei rotinas de validação e tratamento de erros (Data Quality), aumentando a confiabilidade dos relatórios.",
    ],
)
add_job(
    "Estagiário e Membro Consultor", "Empresa Júnior DatAí Tecnologia EJ", "07/2024 — 04/2025", "Remoto",
    [
        "Desenvolvi dashboards e análises interativas para clientes com SAS, Python, SQL e Power BI.",
        "Estruturei bancos de dados SQL para facilitar acesso e integração de dados.",
    ],
)

# ---------- Projeto em destaque ----------
story.append(Paragraph("PROJETO EM DESTAQUE — DATALOCK STUDIO", styles["h2"]))
story.append(Paragraph(
    "<b>Problema:</b> equipes de dados levam dias mascarando manualmente CPFs, e-mails e outras informações "
    "pessoais antes de compartilhar bases — processo lento, sujeito a erro humano e sem garantia formal de "
    "conformidade com a LGPD.",
    styles["body"],
))
story.append(Paragraph(
    "<b>Solução:</b> biblioteca Python (30+ funções) e plataforma no-code com detecção automática de PII, "
    "hash determinístico, pseudonimização reversível, cálculo de k-anonimato/risco de reidentificação e "
    "armazenamento em formato próprio (.dlk) com criptografia autenticada AES-256-GCM.",
    styles["body"],
))
story.append(Paragraph(
    "<b>Resultado:</b> processo de anonimização de horas/dias reduzido a minutos, com trilha de auditoria e "
    "métricas formais de privacidade. Publicada em produção (web e executável) e em submissão na Microsoft Store.",
    styles["body"],
))
story.append(Paragraph(
    "Python · Polars · FastAPI · SQLAlchemy · cryptography &nbsp;—&nbsp; datalock-studio.tech · github.com/py-datalock/datalock",
    styles["job_meta"],
))
story.append(Spacer(1, 1))

# ---------- Tecnologias / Skills em 2 colunas ----------
story.append(Paragraph("TECNOLOGIAS E CONHECIMENTOS", styles["h2"]))

skills = [
    ("Linguagens", "Python, SQL, SAS"),
    ("Engenharia de Dados & ETL", "Pentaho, SAP Data Services"),
    ("Pipeline & Deploy", "Docker, CI/CD, Airflow"),
    ("Banco de Dados", "MySQL, PostgreSQL"),
    ("Cloud & Infraestrutura", "Oracle Cloud Infrastructure (OCI)"),
    ("Governança & Privacidade", "LGPD, k-anonimato, pseudonimização, criptografia"),
    ("Analytics & Visualização", "Power BI, Streamlit, Plotly"),
    ("Machine Learning", "PyTorch, XGBoost, Scikit-learn"),
]

left_cells, right_cells = [], []
for i, (head, val) in enumerate(skills):
    cell = [Paragraph(head, styles["skill_head"]), Paragraph(val, styles["skill_val"])]
    if i % 2 == 0:
        left_cells.append(cell)
    else:
        right_cells.append(cell)

rows = []
for i in range(max(len(left_cells), len(right_cells))):
    l = left_cells[i] if i < len(left_cells) else [Paragraph("", styles["skill_val"])]
    r = right_cells[i] if i < len(right_cells) else [Paragraph("", styles["skill_val"])]
    rows.append([l, r])

skills_tbl = Table(rows, colWidths=[(PAGE_W - 2 * MARGIN) / 2] * 2)
skills_tbl.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
]))
story.append(skills_tbl)

# ---------- Certificações ----------
story.append(Paragraph("CERTIFICAÇÕES", styles["h2"]))
for c in [
    "Oracle Cloud Infrastructure (OCI) — 2025: Professional (Generative AI, Data Science); Foundations (OCI AI, Data Platform, Cloud Infrastructure) · Oracle Certified Generative AI &amp; Data Science Professional",
    "Databricks — 2025: Accreditations (Fundamentals, Generative AI Fundamentals)",
]:
    story.append(Paragraph(f"–  {c}", styles["bullet"]))

# ---------- Educação ----------
story.append(Paragraph("FORMAÇÃO", styles["h2"]))
story.append(Paragraph("Bacharelado em Ciência de Dados e Inteligência Artificial", styles["job_title"]))
story.append(Paragraph("IESB · 02/2023 — 10/2026", styles["job_meta"]))
story.append(Paragraph(
    "Disciplinas relevantes: Aprendizagem de Máquina, Mineração de Dados, Estatística Aplicada, Análise "
    "Exploratória e Visualização, Modelagem e Inferência Estatística, Processamento de Dados Massivos.",
    styles["body"],
))

doc.build(story)
print("PDF gerado com sucesso.")
