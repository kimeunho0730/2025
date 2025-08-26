import streamlit as st
import random

st.set_page_config(page_title="삶의 타임라인 시뮬레이터", layout="wide")

# --- 초기화 ---
if "age" not in st.session_state:
    st.session_state.age = 20
    st.session_state.health = 50
    st.session_state.finance = 50
    st.session_state.social = 50
    st.session_state.events = []

st.title("🕰️ 삶의 타임라인 시뮬레이터")
st.write("당신의 선택이 인생의 건강, 재정, 사회적 관계에 어떤 영향을 미칠까요?")

# --- 초기 조건 입력 ---
with st.sidebar:
    st.header("초기 조건 설정")
    income = st.radio("소득 수준", ["저소득", "중산층", "고소득"])
    region = st.radio("거주 지역", ["의료 취약지역", "중소도시", "대도시"])
    insurance = st.radio("의료 보험", ["미가입", "불안정", "가입"])
    social = st.radio("사회적 관계", ["단절", "보통", "친밀"])

    if st.button("조건 반영하기"):
        st.session_state.health = {"저소득":30,"중산층":50,"고소득":70}[income]
        st.session_state.finance = {"저소득":30,"중산층":50,"고소득":70}[income]
        st.session_state.social = {"단절":30,"보통":50,"친밀":70}[social]
        st.session_state.age = 20
        st.session_state.events = []
        st.success("초기 조건이 반영되었습니다!")

# --- 현재 상태 표시 ---
st.subheader(f"현재 나이: {st.session_state.age}세")
st.progress(st.session_state.health / 100)
st.caption(f"건강: {st.session_state.health}")
st.progress(st.session_state.finance / 100)
st.caption(f"재정: {st.session_state.finance}")
st.progress(st.session_state.social / 100)
st.caption(f"사회적 관계: {st.session_state.social}")

# --- 이벤트 시뮬레이션 ---
st.divider()
st.subheader("📌 인생 이벤트")

events = {
    "대학 진학": {"health": -5, "finance": -10, "social": +10},
    "취업 성공": {"health": -5, "finance": +20, "social": +5},
    "운동 시작": {"health": +15, "finance": -2, "social": +3},
    "해외 이민": {"health": -10, "finance": -15, "social": +20},
    "질병 발생": {"health": -25, "finance": -20, "social": -10},
    "결혼": {"health": +5, "finance": -10, "social": +20},
}

choice = st.radio("다음 이벤트를 선택하세요:", list(events.keys()))

if st.button("이벤트 적용"):
    effect = events[choice]
    st.session_state.health = min(max(st.session_state.health + effect["health"], 0), 100)
    st.session_state.finance = min(max(st.session_state.finance + effect["finance"], 0), 100)
    st.session_state.social = min(max(st.session_state.social + effect["social"], 0), 100)
    st.session_state.age += 5
    st.session_state.events.append((st.session_state.age, choice))
    st.success(f"{choice} 이벤트가 적용되었습니다! 현재 나이: {st.session_state.age}세")

# --- 결과 요약 ---
if st.session_state.age >= 80:
    st.divider()
    st.header("📊 인생 요약 결과")
    st.write(f"최종 건강 점수: {st.session_state.health}")
    st.write(f"최종 재정 점수: {st.session_state.finance}")
    st.write(f"최종 사회적 관계 점수: {st.session_state.social}")
    st.write("거쳐온 이벤트:")
    for age, ev in st.session_state.events:
        st.write(f"- {age}세: {ev}")

