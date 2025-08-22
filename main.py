import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1번 ~ 20번 원소 데이터 (간단 버전)
elements = [
    {"Z": 1, "symbol": "H", "period": 1, "radius": 53,  "electronegativity": 2.20, "config": "1s1"},
    {"Z": 2, "symbol": "He", "period": 1, "radius": 31,  "electronegativity": None, "config": "1s2"},
    {"Z": 3, "symbol": "Li", "period": 2, "radius": 167, "electronegativity": 0.98, "config": "[He] 2s1"},
    {"Z": 4, "symbol": "Be", "period": 2, "radius": 112, "electronegativity": 1.57, "config": "[He] 2s2"},
    {"Z": 5, "symbol": "B", "period": 2, "radius": 87,  "electronegativity": 2.04, "config": "[He] 2s2 2p1"},
    {"Z": 6, "symbol": "C", "period": 2, "radius": 67,  "electronegativity": 2.55, "config": "[He] 2s2 2p2"},
    {"Z": 7, "symbol": "N", "period": 2, "radius": 56,  "electronegativity": 3.04, "config": "[He] 2s2 2p3"},
    {"Z": 8, "symbol": "O", "period": 2, "radius": 48,  "electronegativity": 3.44, "config": "[He] 2s2 2p4"},
    {"Z": 9, "symbol": "F", "period": 2, "radius": 42,  "electronegativity": 3.98, "config": "[He] 2s2 2p5"},
    {"Z": 10, "symbol": "Ne", "period": 2, "radius": 38, "electronegativity": None, "config": "[He] 2s2 2p6"},
    {"Z": 11, "symbol": "Na", "period": 3, "radius": 190, "electronegativity": 0.93, "config": "[Ne] 3s1"},
    {"Z": 12, "symbol": "Mg", "period": 3, "radius": 145, "electronegativity": 1.31, "config": "[Ne] 3s2"},
    {"Z": 13, "symbol": "Al", "period": 3, "radius": 118, "electronegativity": 1.61, "config": "[Ne] 3s2 3p1"},
    {"Z": 14, "symbol": "Si", "period": 3, "radius": 111, "electronegativity": 1.90, "config": "[Ne] 3s2 3p2"},
    {"Z": 15, "symbol": "P", "period": 3, "radius": 98,  "electronegativity": 2.19, "config": "[Ne] 3s2 3p3"},
    {"Z": 16, "symbol": "S", "period": 3, "radius": 88,  "electronegativity": 2.58, "config": "[Ne] 3s2 3p4"},
    {"Z": 17, "symbol": "Cl", "period": 3, "radius": 79,  "electronegativity": 3.16, "config": "[Ne] 3s2 3p5"},
    {"Z": 18, "symbol": "Ar", "period": 3, "radius": 71,  "electronegativity": None, "config": "[Ne] 3s2 3p6"},
    {"Z": 19, "symbol": "K", "period": 4, "radius": 243, "electronegativity": 0.82, "config": "[Ar] 4s1"},
    {"Z": 20, "symbol": "Ca", "period": 4, "radius": 194, "electronegativity": 1.00, "config": "[Ar] 4s2"},
]

# DataFrame 변환
df = pd.DataFrame(elements)

st.set_page_config(page_title="주기율표 경향", layout="centered")
st.title("📊 주기율표 주기적 성질 변화 (1주기 ~ 4주기, Z=1~20)")

# 원자 반지름 변화
st.subheader("원자 반지름 (pm) 변화")
fig1, ax1 = plt.subplots()
for p in range(1, 5):
    sub = df[df["period"] == p]
    ax1.plot(sub["Z"], sub["radius"], marker="o", label=f"{p}주기")
ax1.set_xlabel("원자번호 (Z)")
ax1.set_ylabel("원자 반지름 (pm)")
ax1.legend()
st.pyplot(fig1)

# 전기음성도 변화
st.subheader("전기음성도 (Pauling) 변화")
fig2, ax2 = plt.subplots()
for p in range(1, 5):
    sub = df[df["period"] == p]
    ax2.plot(sub["Z"], sub["electronegativity"], marker="s", label=f"{p}주기")
ax2.set_xlabel("원자번호 (Z)")
ax2.set_ylabel("전기음성도 (Pauling)")
ax2.legend()
st.pyplot(fig2)

# 전자 배치 테이블
st.subheader("전자 배치 변화")
st.dataframe(df[["Z", "symbol", "period", "config"]])
