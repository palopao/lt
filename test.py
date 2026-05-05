# python3 -m venv venv
# source venv/bin/activate
# streamlit run test.py

import streamlit as st
from unidecode import unidecode

# 1. Tabela Pitagórica Oficial
# A=1, B=2, C=3, D=4, E=5, F=6, G=7, H=8, I=9
# J=1, K=2, L=3, M=4, N=5, O=6, P=7, Q=8, R=9
# S=1, T=2, U=3, V=4, W=5, X=6, Y=7, Z=8
def calcular_expressao(nome):
    if not nome: return 0
    nome = unidecode(nome.strip().upper().replace(" ", ""))
    tabela = {
        'A':1,'J':1,'S':1, 'B':2,'K':2,'T':2, 'C':3,'L':3,'U':3,
        'D':4,'M':4,'V':4, 'E':5,'N':5,'W':5, 'F':6,'O':6,'X':6,
        'G':7,'P':7,'Y':7, 'H':8,'Q':8,'Z':8, 'I':9,'R':9
    }
    soma = sum(tabela.get(letra, 0) for letra in nome)
    
    # Redução numerológica (mantendo mestres 11 e 22)
    while soma > 9 and soma not in [11, 22]:
        soma = sum(int(d) for d in str(soma))
    return soma

# 2. Matriz de Afinidade Numerológica (em %)
# Baseado nas relações de amizade/concordância entre os números
afinidade_numeros = {
    1: {1:70, 2:50, 3:90, 4:60, 5:90, 6:50, 7:90, 8:70, 9:80, 11:60, 22:50},
    2: {1:50, 2:70, 3:80, 4:80, 5:60, 6:99, 7:50, 8:90, 9:99, 11:90, 22:80},
    3: {1:90, 2:80, 3:70, 4:50, 5:99, 6:80, 7:60, 8:50, 9:99, 11:70, 22:50},
    4: {1:60, 2:80, 3:50, 4:70, 5:60, 6:90, 7:50, 8:99, 9:70, 11:60, 22:99},
    5: {1:90, 2:60, 3:99, 4:60, 5:70, 6:60, 7:99, 8:50, 9:70, 11:50, 22:50},
    6: {1:50, 2:99, 3:80, 4:90, 5:60, 6:70, 7:60, 8:90, 9:99, 11:99, 22:90},
    7: {1:90, 2:50, 3:60, 4:50, 5:99, 6:60, 7:70, 8:60, 9:90, 11:90, 22:60},
    8: {1:70, 2:90, 3:50, 4:99, 5:50, 6:90, 7:60, 8:70, 9:60, 11:50, 22:99},
    9: {1:80, 2:99, 3:99, 4:70, 5:70, 6:99, 7:90, 8:60, 9:70, 11:80, 22:70},
    11:{1:60, 2:90, 3:70, 4:60, 5:50, 6:99, 7:90, 8:50, 9:80, 11:70, 22:60},
    22:{1:50, 2:80, 3:50, 4:99, 5:50, 6:90, 7:60, 8:99, 9:70, 11:60, 22:70}
}

# 3. Tabela de Signos (imagem_dbcf5a.png)
signos = ["Áries", "Touro", "Gémeos", "Câncer", "Leão", "Virgem", "Libra", "Escorpião", "Sagitário", "Capricórnio", "Aquário", "Peixes"]
compat_signos = {
    "Áries":      [75, 75, 99, 85, 99, 75, 99, 75, 99, 85, 99, 99],
    "Touro":      [75, 99, 85, 99, 75, 99, 85, 99, 75, 99, 75, 99],
    "Gémeos":     [99, 85, 99, 85, 85, 99, 99, 75, 85, 75, 99, 85],
    "Câncer":     [85, 99, 85, 99, 85, 99, 85, 99, 75, 99, 75, 99],
    "Leão":       [99, 75, 85, 85, 75, 85, 99, 85, 75, 75, 99, 75],
    "Virgem":     [75, 99, 99, 99, 85, 99, 85, 75, 85, 99, 75, 99],
    "Libra":      [99, 85, 99, 85, 99, 85, 99, 85, 85, 85, 99, 75],
    "Escorpião":  [75, 99, 75, 99, 85, 75, 85, 99, 85, 99, 75, 85],
    "Sagitário":  [99, 75, 85, 75, 75, 85, 85, 85, 75, 75, 85, 85],
    "Capricórnio":[85, 99, 75, 99, 75, 99, 85, 99, 75, 99, 75, 85],
    "Aquário":    [99, 75, 99, 75, 99, 75, 99, 75, 85, 75, 75, 85],
    "Peixes":     [99, 99, 85, 99, 75, 99, 75, 85, 85, 85, 85, 99]
}

# Interface Streamlit
st.title("💖 Calculadora de Afinidade")

c1, c2 = st.columns(2)
with c1:
    st.subheader("Alma 1")
    nome1 = st.text_input("Nome 1")
    signo1 = st.selectbox("Signo 1", signos)
with c2:
    st.subheader("Alma 2")
    nome2 = st.text_input("Nome 2")
    signo2 = st.selectbox("Signo 2", signos)

if st.button("Calcular Compatibilidade"):
    if nome1 and nome2:
        # Resultado Nomes
        n1 = calcular_expressao(nome1)
        n2 = calcular_expressao(nome2)
        res_nomes = afinidade_numeros[n1][n2]
        
        # Resultado Signos
        idx2 = signos.index(signo2)
        res_signos = compat_signos[signo1][idx2]
        
        # Média Final
        total = (res_nomes + res_signos) / 2
        
        st.divider()
        st.metric("Afinidade Final", f"{total}%")
        if total > 90:
            st.balloons()
            st.success("Conexão de Almas Gémeas! ✨")
        elif total > 80:
            st.info("Grande potencial de harmonia! 🤝")
        else:
            st.warning("Existem desafios, mas o amor supera tudo! 💪")
    else:
        st.warning("Preencha os nomes para calcular!")