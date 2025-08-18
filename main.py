import streamlit as st
import random

# 페이지 설정 🌈
st.set_page_config(page_title="MBTI 색깔 추천✨", page_icon="🎨", layout="wide")

# 헤더 🎉
st.markdown("""
    <h1 style='text-align: center; color: #ff69b4;'>🌟 MBTI 기반 색깔 추천 사이트 🌟</h1>
    <p style='text-align: center; font-size: 22px;'>💖 당신의 성격 유형에 딱 맞는 색깔과 그 이유를 알려드려요 🎨✨</p>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; font-size:30px;'>
🌈✨💫🌍🌟🔥🌸🍀🎶🎭🚀💼👑🎉🌻💎🎧🦄🌊
</div>
""", unsafe_allow_html=True)

# MBTI 선택 🎭
mbti = st.selectbox(
    "👉 당신의 MBTI를 선택하세요:",
    ["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP",
     "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"]
)

# MBTI별 색깔 추천 데이터 🎨
color_recommendations = {
    "INTJ": ("보라색 💜", "깊은 사고와 통찰력을 가진 INTJ에게는 신비롭고 창의적인 보라색이 어울립니다."),
    "INTP": ("청록색 🌀", "지적 호기심과 탐구심이 강한 INTP는 차분하면서도 독창적인 청록색이 잘 맞습니다."),
    "ENTJ": ("빨강 ❤️", "강한 리더십과 추진력을 가진 ENTJ는 열정과 힘을 상징하는 빨강이 어울립니다."),
    "ENTP": ("주황색 🧡", "도전적이고 에너지가 넘치는 ENTP는 활발하고 창의적인 주황색과 잘 맞습니다."),
    "INFJ": ("남색 💙", "깊은 공감 능력과 이상주의적인 INFJ는 차분하고 신뢰감을 주는 남색이 어울립니다."),
    "INFP": ("연두색 💚", "순수하고 따뜻한 감성을 가진 INFP는 자연과 희망을 상징하는 연두색과 잘 어울립니다."),
    "ENFJ": ("핑크색 🌸", "타인에게 따뜻하고 배려심이 깊은 ENFJ는 사랑과 조화를 상징하는 핑크색이 어울립니다."),
    "ENFP": ("노랑 💛", "긍정적이고 자유로운 영혼인 ENFP는 밝고 에너지 넘치는 노랑과 잘 맞습니다."),
    "ISTJ": ("회색 ⚪", "신뢰성과 책임감이 강한 ISTJ는 안정감과 질서를 상징하는 회색이 어울립니다."),
    "ISFJ": ("하늘색 🌤️", "배려심 많고 따뜻한 ISFJ는 평화롭고 편안한 하늘색이 잘 맞습니다."),
    "ESTJ": ("남색 💙", "체계적이고 리더십이 강한 ESTJ는 신뢰와 권위를 주는 남색이 어울립니다."),
    "ESFJ": ("연분홍 🌷", "친절하고 사교적인 ESFJ는 부드럽고 따뜻한 연분홍색이 잘 맞습니다."),
    "ISTP": ("검정 ⚫", "논리적이고 현실적인 ISTP는 차분하고 실용적인 검정색과 어울립니다."),
    "ISFP": ("민트색 🍃", "감성적이고 예술적인 ISFP는 신선하고 자유로운 민트색이 잘 맞습니다."),
    "ESTP": ("빨강 ❤️", "활발하고 모험심 강한 ESTP는 강렬하고 에너지 넘치는 빨강과 잘 어울립니다."),
    "ESFP": ("무지개색 🌈", "사교적이고 즐거움을 추구하는 ESFP는 다채롭고 화려한 무지개색이 어울립니다.")
}

# 선택한 MBTI 결과 출력 🌈
if mbti:
    color, reason = color_recommendations[mbti]

    st.markdown(f"""
        <div style='text-align: center; padding: 25px; border-radius: 25px; background-color: #fff0f5; box-shadow: 0 0 15px #ffb6c1;'>
            <h2>✨ 당신의 MBTI는 <span style='color:#ff1493'>{mbti}</span> ✨</h2>
            <h3>🌟 어울리는 색깔: <span style='color:#8a2be2'>{color}</span> 🌟</h3>
            <p style='font-size:20px;'>{reason}</p>
            <div style='font-size:35px;'>💎🌸🌈🔥🎶🦄🌍✨</div>
        </div>
    """, unsafe_allow_html=True)

# Footer 🎆
st.markdown("""
    <hr>
    <p style='text-align: center; font-size:18px;'>Made with ❤️ by Streamlit & MBTI Colors World 🌍✨🎉</p>
    <div style='text-align:center; font-size:26px;'>🌸💎🔥🌈🎶🌟💫💖🚀</div>
""", unsafe_allow_html=True)
