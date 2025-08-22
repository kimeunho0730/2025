import streamlit as st

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

st.set_page_config(page_title="주기율표 경향", layout="centered")
st.title("📊 주기율표 주기적 성질 변화 (1주기 ~ 4주기, Z=1~20)")

# 원자 반지름 변화
data_radius = {"Z": [], "radius": []}
for elem in elements:
    data_radius["Z"].append(elem["Z"])
    data_radius["radius"].append(elem["radius"])

st.subheader("원자 반지름 (pm) 변화")
st.line_chart(data_radius, x="Z", y="radius")

# 전기음성도 변화
data_en = {"Z": [], "electronegativity": []}
for elem in elements:
    data_en["Z"].append(elem["Z"])
    data_en["electronegativity"].append(elem["electronegativity"] if elem["electronegativity"] is not None else None)

st.subheader("전기음성도 (Pauling) 변화")
st.line_chart(data_en, x="Z", y="electronegativity")

# 전자 배치 테이블 표시
table_data = [[elem["Z"], elem["symbol"], elem["period"], elem["config"]] for elem in elements]

st.subheader("전자 배치 변화")
st.table(table_data)
