import streamlit as st

# -------------------------------
# 메인 제목
# -------------------------------
st.set_page_config(page_title="신경·호르몬 조절 시뮬레이터", page_icon="🧠", layout="centered")

st.title("🧠 신경·호르몬 조절 시뮬레이터")
st.write("생명과학Ⅰ - 항상성과 조절 단원 학습용 웹사이트")
st.divider()

# -------------------------------
# 상황 선택
# -------------------------------
st.subheader("1️⃣ 상황을 선택하세요")
scenario = st.selectbox(
    "다음 중 한 가지 상황을 선택해보세요:",
    ["🍰 단 음식 섭취 후", "🏃 운동 직후", "❄️ 추운 환경", "💧 물을 많이 마신 후"]
)

# -------------------------------
# 반응 시뮬레이션
# -------------------------------
st.subheader("2️⃣ 우리 몸의 반응")

if scenario == "🍰 단 음식 섭취 후":
    st.write("**혈당이 상승했습니다.**")
    st.progress(90, text="혈당 수치 ↑")
    st.markdown("- 췌장 **β세포** → 인슐린 분비 증가 🟢")
    st.markdown("- 간 → 글리코젠 합성 ⬆️")
    st.markdown("- 결과: 혈당이 정상으로 조절 ✅")

elif scenario == "🏃 운동 직후":
    st.write("**혈당이 낮아지고, 체온은 올라갔습니다.**")
    st.progress(20, text="혈당 수치 ↓")
    st.markdown("- 췌장 **α세포** → 글루카곤 분비 증가 🟠")
    st.markdown("- 간 → 글리코젠 분해 → 포도당 방출 ⬆️")
    st.markdown("- 체온 조절 → 땀 분비 증가, 혈관 확장")
    st.markdown("- 결과: 혈당과 체온이 정상으로 회복 ✅")

elif scenario == "❄️ 추운 환경":
    st.write("**체온이 낮아졌습니다.**")
    st.progress(30, text="체온 ↓")
    st.markdown("- 시상하부 감지 → 체온 유지 신호 발동 🔵")
    st.markdown("- 혈관 수축, 근육 떨림, 대사량 증가")
    st.markdown("- 결과: 체온이 정상으로 회복 ✅")

elif scenario == "💧 물을 많이 마신 후":
    st.write("**혈액의 삼투압이 낮아졌습니다.**")
    st.progress(40, text="삼투압 ↓")
    st.markdown("- 뇌하수체 후엽 → ADH(항이뇨호르몬) 분비 감소 🧊")
    st.markdown("- 콩팥에서 물 재흡수 감소 → 소변량 증가")
    st.markdown("- 결과: 삼투압이 정상으로 회복 ✅")

st.divider()

# -------------------------------
# 퀴즈
# -------------------------------
st.subheader("3️⃣ 개념 확인 퀴즈")

quiz_q = st.radio(
    "혈당이 낮아졌을 때 분비되는 호르몬은 무엇일까요?",
    ["인슐린", "글루카곤", "ADH", "에피네프린"]
)

if quiz_q:
    if quiz_q == "글루카곤":
        st.success("✅ 정답! 혈당이 낮을 때 글루카곤이 분비됩니다.")
    else:
        st.error("❌ 다시 생각해보세요. 혈당이 낮을 때는 글루카곤이 필요합니다.")
