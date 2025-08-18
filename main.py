import streamlit as st
import datetime

# ===== 공휴일 데이터 =====
HOLIDAYS = {
    "01-01": ("신정", "🎉"),
    "03-01": ("삼일절", "🇰🇷"),
    "05-05": ("어린이날", "🧒"),
    "06-06": ("현충일", "🪖"),
    "08-15": ("광복절", "🇰🇷"),
    "10-03": ("개천절", "🌌"),
    "10-09": ("한글날", "🔤"),
    "12-25": ("크리스마스", "🎄"),
}

# 예시: 2025년 음력 공휴일
LUNAR_HOLIDAYS_2025 = {
    "01-28": ("설날 연휴", "🥟"),
    "01-29": ("설날", "🎊"),
    "01-30": ("설날 연휴", "🥟"),
    "10-05": ("추석 연휴", "🌕"),
    "10-06": ("추석", "🍂"),
    "10-07": ("추석 연휴", "🌕"),
}


def get_holidays(year, month):
    results = []
    for date_str, (name, emoji) in HOLIDAYS.items():
        m, d = map(int, date_str.split("-"))
        if m == month:
            results.append((datetime.date(year, m, d), name, emoji))

    # 2025년 음력 추가
    if year == 2025:
        for date_str, (name, emoji) in LUNAR_HOLIDAYS_2025.items():
            m, d = map(int, date_str.split("-"))
            if m == month:
                results.append((datetime.date(year, m, d), name, emoji))

    results.sort(key=lambda x: x[0])
    return results


# ===== Streamlit UI =====
st.set_page_config(page_title="한국 공휴일 조회기", page_icon="📅", layout="centered")

# 헤더
st.markdown(
    """
    <h1 style="text-align:center; color:#4B9CD3; font-size:50px;">📅 한국 공휴일 조회기</h1>
    <p style="text-align:center; font-size:18px; color:gray;">연도와 월을 선택하면 그 달의 휴일을 확인할 수 있어요 🎉</p>
    """,
    unsafe_allow_html=True,
)

# 사이드바 입력
st.sidebar.header("🔎 검색 조건")
year = st.sidebar.number_input("연도 입력", min_value=2000, max_value=2100, value=datetime.date.today().year)
month = st.sidebar.number_input("월 입력", min_value=1, max_value=12, value=datetime.date.today().month)

if st.sidebar.button("조회하기"):
    holidays = get_holidays(year, month)

    if holidays:
        st.subheader(f"✅ {year}년 {month}월의 공휴일")
        for date, name, emoji in holidays:
            st.markdown(
                f"""
                <div style="
                    background-color:#F0F8FF;
                    border-radius:15px;
                    padding:15px;
                    margin:10px 0;
                    box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
                ">
                    <h3 style="margin:0; color:#333;">{emoji} {name}</h3>
                    <p style="margin:0; color:#555;">📅 {date.strftime('%Y-%m-%d')}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        st.subheader("❌ 이 달에는 공휴일이 없어요.")
        st.markdown(
            """
            <div style="
                background-color:#FFF0F5;
                border-radius:15px;
                padding:20px;
                margin:15px 0;
                text-align:center;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            ">
                <h3 style="color:#D2691E;">💌 힘내세요!</h3>
                <p style="font-size:16px; color:#333;">
                    공휴일은 없지만,<br>
                    당신의 하루가 작은 휴일처럼 빛나길 바랍니다 ✨
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
