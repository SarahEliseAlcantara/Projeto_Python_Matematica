import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def render():
    st.header("Rendimento Mensal do Trabalho e Rigor Estatístico")
    st.write("Cálculos analíticos contendo medidas de tendência central e de dispersão exigidos pelos critérios de avaliação do projeto matemático.")
    
    # amostra de rendimentos de trabalho 
    rendimentos = np.array([
        1320, 1400, 1500, 1550, 1600, 1750, 1800, 1900, 2100, 2200, 
        2500, 2800, 3100, 3500, 4200, 5000, 6200, 7500, 18000, 25000
    ])
    
    # Calculo usando NumPy/Pandas
    media = np.mean(rendimentos)
    mediana = np.median(rendimentos)
    q1 = np.percentile(rendimentos, 25)
    q3 = np.percentile(rendimentos, 75)
    iqr = q3 - q1
    amplitude = np.max(rendimentos) - np.min(rendimentos)
    desvio_padrao = np.std(rendimentos)
    
    
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    outliers = rendimentos[(rendimentos < limite_inferior) | (rendimentos > limite_superior)]
    
    # layout de metricas
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Média Aritmética", f"R$ {media:.2f}")
    col2.metric("Mediana (Robustez)", f"R$ {mediana:.2f}")
    col3.metric("IQR (Intervalo Quartil)", f"R$ {iqr:.2f}")
    col4.metric("Desvio Padrão (σ)", f"R$ {desvio_padrao:.2f}")
    
    st.markdown(f"Amplitude Total: R$ {amplitude:.2f} | **Q1 (25%):** R$ {q1:.2f} | **Q3 (75%):** R$ {q3:.2f}")
    
    
    st.info(f"Análise Crítica de Outliers (Regra 1.5 × IQR):** Foram identificados os seguintes valores anômalos (Outliers) de alta renda: **{outliers}**. A presença destes salários elevados distorce a Média (R$ {media:.2f}) para cima, tornando a Mediana (R$ {mediana:.2f}) a medida de tendência central mais confiável para representar o trabalhador típico.")
    
    # graficos: Boxplot e histograma
    st.subheader("Gráficos de Distribuição de Renda")
    fig_box = px.box(y=rendimentos, title="Boxplot Interativo de Rendimentos (Detecção Visual de Outliers)", labels={'y': 'Rendimento Mensal (R$)'})
    st.plotly_chart(fig_box, use_container_width=True)
    
    fig_hist = px.histogram(x=rendimentos, nbins=15, title="Histograma de Distribuição Salarial (Análise de Assimetria à Direita)", labels={'x': 'Rendimento Mensal (R$)', 'y': 'Frequência'})
    st.plotly_chart(fig_hist, use_container_width=True)
    
    # Bloco de noticias
    st.divider()
    st.header("Conteúdo Informativo e Economia do Trabalho")
    st.markdown("Mercado de trabalho fecha 2026 com taxa estável de informalidade")
    st.caption("Fonte: Adaptado da cobertura analítica da PNAD Contínua - IBGE")
    st.write("Estudos recentes apontam que a busca por empregos de carteira assinada mantém forte correlação com o nível de escolaridade do candidato. As regiões Sul e Sudeste lideram os índices de contratação formal nas frentes tecnológicas (STEM), enquanto setores tradicionais buscam reestruturação tributária.")
