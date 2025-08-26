import streamlit as st
import random

st.set_page_config(page_title="삶의 타임라인 시뮬레이터", layout="centered")

# --- 초기화 ---
if "stage" not in st.session_state:
    st.session_state.stage = "character_select"  # character_select → life_events → ending
    st.session_state.character = None
    st.session_state.age = 20
    st.session_state.history = []
    st.session_state.health = 50
    st.session_state.finance = 50
    st.session_state.social = 50

# --- 캐릭터 목록 ---
characters = {
    "민수": {"소득":"저소득","지역":"의료 취약지역","보험":"미가입","관계":"단절",
             "health":30,"finance":30,"social":25},
    "영희": {"소득":"중산층","지역":"중소도시","보험":"가입","관계":"보통",
             "health":50,"finance":50,"social":50},
    "철수": {"소득":"고소득","지역":"대도시","보험":"가입","관계":"친밀",
             "health":70,"finance":70,"social":75},
    "지영": {"소득":"저소득","지역":"대도시","보험":"불안정","관계":"보통",
             "health":40,"finance":35,"social":50},
}

# --- 이벤트 시나리오 ---
events = {
    20: {
        "대학 진학": {"health": -5, "finance": -10, "social": +10},
        "바로 취업": {"health": -10, "finance": +15, "social": +5},
        "아르바이트만 함": {"health": -8, "finance": +5, "social": -5}
    },
    30: {
        "직장 승진": {"health": -5, "finance": +20, "social": +5},
        "질병 발생": {"health": -20, "finance": -15, "social": -5},
        "결혼": {"health": +5, "finance": -10, "social": +20}
    },
    40: {
        "해외 이민": {"health": -10, "finance": -15, "social": +15},
        "운동 시작": {"health": +15, "finance": -2, "social": +5},
        "부모 간병": {"health": -10, "finance": -10, "social": +5}
    },
    50: {
        "퇴직 준비": {"health": -5, "finance": -5, "social": +5},
        "만성질환": {"health": -25, "finance": -15, "social": -10},
        "지역 모임 참여": {"health": +5, "finance": -5, "social": +20}
    },
    60: {
        "퇴직": {"health": -10, "finance": -20, "social": +5},
        "창업 도전": {"health": -15, "finance": -25, "social": +10},
        "봉사활동": {"health": +5, "finance": -5, "social": +20}
    },
    70: {
        "치매 초기": {"health": -20, "finance": -15, "social": -10},
        "손주 돌봄": {"health": -5, "finance": -5, "social": +15},
        "은둔 생활": {"health": -15, "finance": 0, "social": -20}
    }
}

# --- 화면 전환 ---
if st.session_state.stage == "character_select":
    st.title("삶의 타임라인 시뮬레이터")
    st.subheader("가상의 캐릭터를 선택하세요")

    for name, info in characters.items():
        with st.container():
            st.markdown(f"### {name}")
            st.write(f"소득: {info['소득']}, 지역: {info['지역']}, 보험: {info['보험']}, 사회적 관계: {info['관계']}")
            if st.button(f"{name} 선택하기"):
                st.session_state.character = name
                st.session_state.health = info["health"]
                st.session_state.finance = info["finance"]
                st.session_state.social = info["social"]
                st.session_state.stage = "life_events"
                st.experimental_rerun()

elif st.session_state.stage == "life_events":
    st.title(f"{st.session_state.character}의 인생 여정")
    st.subheader(f"현재 나이: {st.session_state.age}세")

    if st.session_state.age in events:
        st.write("선택지를 고르세요:")
        choice = st.radio("이벤트", list(events[st.session_state.age].keys()), key=f"choice_{st.session_state.age}")
        if st.button("선택 확정하기"):
            st.session_state.history.append((st.session_state.age, choice))
            effects = events[st.session_state.age][choice]
            st.session_state.health = max(0, min(100, st.session_state.health + effects["health"]))
            st.session_state.finance = max(0, min(100, st.session_state.finance + effects["finance"]))
            st.session_state.social = max(0, min(100, st.session_state.social + effects["social"]))
            st.session_state.age += 10
            st.experimental_rerun()
    else:
        # 모든 이벤트 끝남 → 엔딩
        st.session_state.stage = "ending"
        st.experimental_rerun()

elif st.session_state.stage == "ending":
    st.title("📜 당신의 선택의 결과입니다")
    st.subheader(f"{st.session_state.character}의 삶의 결말")

    # 엔딩 조건
    if st.session_state.health <= 20 and st.session_state.social <= 30:
        st.error("⚠️ 고독사 엔딩: 건강 악화와 사회적 단절로 홀로 생을 마감했습니다.")
    elif st.session_state.health <= 30:
        st.warning("💔 조기 사망: 의료 접근성 부족과 재정난으로 병을 이겨내지 못했습니다.")
    elif st.session_state.social >= 60 and st.session_state.health >= 50:
        st.success("🌈 건강한 노후: 가족·이웃과의 관계 속에서 행복한 삶을 마무리했습니다.")
    else:
        st.info("📖 평범한 삶: 특별히 길지 않았지만, 평범하게 생을 마쳤습니다.")

    st.write("### 📊 최종 지표")
    st.write(f"건강: {st.session_state.health}")
    st.write(f"재정: {st.session_state.finance}")
    st.write(f"사회적 관계: {st.session_state.social}")

    st.write("### 🛤️ 걸어온 길")
    for age, ev in st.session_state.history:
        st.write(f"- {age}세: {ev}")

    if st.button("다시 시작하기"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.experimental_rerun()
import streamlit as st
import random

st.set_page_config(page_title="삶의 타임라인 시뮬레이터", layout="centered")

# --- 초기화 ---
if "stage" not in st.session_state:
    st.session_state.stage = "character_select"  # character_select → life_events → ending
    st.session_state.character = None
    st.session_state.age = 20
    st.session_state.history = []
    st.session_state.health = 50
    st.session_state.finance = 50
    st.session_state.social = 50

# --- 캐릭터 목록 ---
characters = {
    "민수": {"소득":"저소득","지역":"의료 취약지역","보험":"미가입","관계":"단절",
             "health":30,"finance":30,"social":25},
    "영희": {"소득":"중산층","지역":"중소도시","보험":"가입","관계":"보통",
             "health":50,"finance":50,"social":50},
    "철수": {"소득":"고소득","지역":"대도시","보험":"가입","관계":"친밀",
             "health":70,"finance":70,"social":75},
    "지영": {"소득":"저소득","지역":"대도시","보험":"불안정","관계":"보통",
             "health":40,"finance":35,"social":50},
}

# --- 이벤트 시나리오 ---
events = {
    20: {
        "대학 진학": {"health": -5, "finance": -10, "social": +10},
        "바로 취업": {"health": -10, "finance": +15, "social": +5},
        "아르바이트만 함": {"health": -8, "finance": +5, "social": -5}
    },
    30: {
        "직장 승진": {"health": -5, "finance": +20, "social": +5},
        "질병 발생": {"health": -20, "finance": -15, "social": -5},
        "결혼": {"health": +5, "finance": -10, "social": +20}
    },
    40: {
        "해외 이민": {"health": -10, "finance": -15, "social": +15},
        "운동 시작": {"health": +15, "finance": -2, "social": +5},
        "부모 간병": {"health": -10, "finance": -10, "social": +5}
    },
    50: {
        "퇴직 준비": {"health": -5, "finance": -5, "social": +5},
        "만성질환": {"health": -25, "finance": -15, "social": -10},
        "지역 모임 참여": {"health": +5, "finance": -5, "social": +20}
    },
    60: {
        "퇴직": {"health": -10, "finance": -20, "social": +5},
        "창업 도전": {"health": -15, "finance": -25, "social": +10},
        "봉사활동": {"health": +5, "finance": -5, "social": +20}
    },
    70: {
        "치매 초기": {"health": -20, "finance": -15, "social": -10},
        "손주 돌봄": {"health": -5, "finance": -5, "social": +15},
        "은둔 생활": {"health": -15, "finance": 0, "social": -20}
    }
}

# --- 화면 전환 ---
if st.session_state.stage == "character_select":
    st.title("삶의 타임라인 시뮬레이터")
    st.subheader("가상의 캐릭터를 선택하세요")

    for name, info in characters.items():
        with st.container():
            st.markdown(f"### {name}")
            st.write(f"소득: {info['소득']}, 지역: {info['지역']}, 보험: {info['보험']}, 사회적 관계: {info['관계']}")
            if st.button(f"{name} 선택하기"):
                st.session_state.character = name
                st.session_state.health = info["health"]
                st.session_state.finance = info["finance"]
                st.session_state.social = info["social"]
                st.session_state.stage = "life_events"
                st.experimental_rerun()

elif st.session_state.stage == "life_events":
    st.title(f"{st.session_state.character}의 인생 여정")
    st.subheader(f"현재 나이: {st.session_state.age}세")

    if st.session_state.age in events:
        st.write("선택지를 고르세요:")
        choice = st.radio("이벤트", list(events[st.session_state.age].keys()), key=f"choice_{st.session_state.age}")
        if st.button("선택 확정하기"):
            st.session_state.history.append((st.session_state.age, choice))
            effects = events[st.session_state.age][choice]
            st.session_state.health = max(0, min(100, st.session_state.health + effects["health"]))
            st.session_state.finance = max(0, min(100, st.session_state.finance + effects["finance"]))
            st.session_state.social = max(0, min(100, st.session_state.social + effects["social"]))
            st.session_state.age += 10
            st.experimental_rerun()
    else:
        # 모든 이벤트 끝남 → 엔딩
        st.session_state.stage = "ending"
        st.experimental_rerun()

elif st.session_state.stage == "ending":
    st.title("📜 당신의 선택의 결과입니다")
    st.subheader(f"{st.session_state.character}의 삶의 결말")

    # 엔딩 조건
    if st.session_state.health <= 20 and st.session_state.social <= 30:
        st.error("⚠️ 고독사 엔딩: 건강 악화와 사회적 단절로 홀로 생을 마감했습니다.")
    elif st.session_state.health <= 30:
        st.warning("💔 조기 사망: 의료 접근성 부족과 재정난으로 병을 이겨내지 못했습니다.")
    elif st.session_state.social >= 60 and st.session_state.health >= 50:
        st.success("🌈 건강한 노후: 가족·이웃과의 관계 속에서 행복한 삶을 마무리했습니다.")
    else:
        st.info("📖 평범한 삶: 특별히 길지 않았지만, 평범하게 생을 마쳤습니다.")

    st.write("### 📊 최종 지표")
    st.write(f"건강: {st.session_state.health}")
    st.write(f"재정: {st.session_state.finance}")
    st.write(f"사회적 관계: {st.session_state.social}")

    st.write("### 🛤️ 걸어온 길")
    for age, ev in st.session_state.history:
        st.write(f"- {age}세: {ev}")

    if st.button("다시 시작하기"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.experimental_rerun()
