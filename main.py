import streamlit as st

# 원소 데이터 (간단 버전: 원자번호, 기호, 이름, 원자량, 전자배치, 전기음성도)
elements = {
    1: {"symbol": "H", "name": "Hydrogen", "weight": 1.008, "config": "1s1", "electronegativity": 2.20},
    2: {"symbol": "He", "name": "Helium", "weight": 4.0026, "config": "1s2", "electronegativity": None},
    6: {"symbol": "C", "name": "Carbon", "weight": 12.011, "config": "[He] 2s2 2p2", "electronegativity": 2.55},
    7: {"symbol": "N", "name": "Nitrogen", "weight": 14.007, "config": "[He] 2s2 2p3", "electronegativity": 3.04},
    8: {"symbol": "O", "name": "Oxygen", "weight": 15.999, "config": "[He] 2s2 2p4", "electronegativity": 3.44},
    11: {"symbol": "Na", "name": "Sodium", "weight": 22.990, "config": "[Ne] 3s1", "electronegativity": 0.93},
    17: {"symbol": "Cl", "name": "Chlorine", "weight": 35.45, "config": "[Ne] 3s2 3p5", "electronegativity": 3.16},
    26: {"symbol": "Fe", "name": "Iron", "weight": 55.845, "config": "[Ar] 3d6 4s2", "electronegativity": 1.83},
    29: {"symbol": "Cu", "name": "Copper", "weight": 63.546, "config": "[Ar] 3d10 4s1", "electronegativity": 1.90},
    47: {"symbol": "Ag", "name": "Silver", "weight": 107.87, "config": "[Kr] 4d10 5s1", "electronegativity": 1.93},
    79: {"symbol": "Au", "name": "Gold", "weight": 196.97, "config": "[Xe] 4f14 5d10 6s1", "electronegativity": 2.54},
}

st.set_page_config(page_title="주기율표 탐색기", layout="wide")
st.title("🔬 주기율표 인터랙티브 탐색기")
st.write("원소를 클릭하면 상세 정보를 볼 수 있습니다.")

# 버튼으로 원소 표시 (간단 예시)
cols = st.columns(5)

selected = None
for i, (num, data) in enumerate(elements.items()):
    col = cols[i % 5]
    if col.button(f"{data['symbol']} ({num})"):
        selected = num

# 선택된 원소 정보 출력
if selected:
    elem = elements[selected]
    st.subheader(f"원소 정보: {elem['name']} ({elem['symbol']})")
    st.write(f"**원자번호:** {selected}")
    st.write(f"**원자량:** {elem['weight']}")
    st.write(f"**전자 배치:** {elem['config']}")
    st.write(f"**전기음성도:** {elem['electronegativity'] if elem['electronegativity'] else 'N/A'}")
