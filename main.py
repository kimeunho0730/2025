import streamlit as st

# 페이지 설정 🌈
st.set_page_config(page_title="MBTI 진로 추천✨", page_icon="💫", layout="wide")

# 헤더 🎉
st.markdown("""
    <h1 style='text-align: center; color: #ff69b4;'>🌟 MBTI 기반 진로 추천 사이트 🌟</h1>
    <p style='text-align: center; font-size: 20px;'>당신의 성격 유형에 맞는 직업을 화려하게 추천해드려요 💼✨</p>
""", unsafe_allow_html=True)

# MBTI 선택 🎭
mbti = st.selectbox(
    "👉 당신의 MBTI를 선택하세요:",
    ["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP",
     "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"]
)

# 직업 추천 데이터 🌟
job_recommendations = {
    "INTJ": ["데이터 과학자 📊", "전략 컨설턴트 🧠", "연구원 🔬"],
    "INTP": ["철학자 📚", "프로그래머 💻", "AI 연구자 🤖"],
    "ENTJ": ["CEO 👑", "경영 컨설턴트 📈", "정치가 🏛️"],
    "ENTP": ["창업가 🚀", "마케터 📢", "기획자 🎬"],
    "INFJ": ["심리상담가 💖", "작가 ✍️", "교사 🍎"],
    "INFP": ["예술가 🎨", "시인 📝", "사회운동가 ✊"],
    "ENFJ": ["리더 🌟", "교육자 📘", "강연가 🎤"],
    "ENFP": ["탐험가 🧭", "배우 🎭", "디자이너 🎨"],
    "ISTJ": ["회계사 💼", "판사 ⚖️", "군인 🎖️"],
    "ISFJ": ["간호사 🏥", "사회복지사 🤝", "비서 📑"],
    "ESTJ": ["경영자 📊", "군 장교 🎖️", "프로젝트 매니저 📋"],
    "ESFJ": ["교사 🍎", "간호사 🏥", "HR 매니저 🧑‍💼"],
    "ISTP": ["엔지니어 🛠️", "파일럿 ✈️", "스포츠 선수 ⚽"],
    "ISFP": ["패션 디자이너 👗", "사진작가 📷", "음악가 🎶"],
    "ESTP": ["기업가 💼", "세일즈맨 💸", "스턴트 배우 🎬"],
    "ESFP": ["연예인 🎤", "여행가 🌍", "이벤트 플래너 🎉"]
}

# 선택한 MBTI 결과 출력 🌈
if mbti:
    st.markdown(f"""
        <div style='text-align: center; padding: 20px; border-radius: 20px; background-color: #ffe4f2;'>
            <h2>✨ 당신의 MBTI는 <span style='color:#ff1493'>{mbti}</span> ✨</h2>
            <h3>🌟 어울리는 직업 추천 리스트 🌟</h3>
        </div>
    """, unsafe_allow_html=True)

    for job in job_recommendations[mbti]:
        st.markdown(f"<h4 style='text-align: center;'>👉 {job}</h4>", unsafe_allow_html=True)

# Footer 🎆
st.markdown("""
    <hr>
    <p style='text-align: center;'>Made with ❤️ by Streamlit & MBTI World 🌍</p>
""", unsafe_allow_html=True)

