import streamlit as st
import datetime

# 한국 공휴일 데이터 (고정 공휴일 위주, 설날/추석 등 음력 기반은 예시로 일부 반영)
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

# 임시로 2025년 설날, 추석 등 추가 (예시)
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

    # 2025년 음력 공휴일
    if year == 2025:
        for date_str, (name, emoji) in LUNAR_HOLIDAYS_2025.items():
            m, d = map(int, date_str.split("-"))
            if m == month:
                results.append((datetime.date(year, m, d), name, emoji))

    results.sort(key=lambda x: x[0])
    return results

st.title("📅 한국 공휴일 조회기")
st.write("연도와 월을 선택하면 해당 달의 공휴일을 확인할 수 있어요!")

year = st.number_input("연도 입력", min_value=2000, max_value=2100, value=datetime.date.today().year)
month = st.number_input("월 입력", min_value=1, max_value=12, value=datetime.date.today().month)

if st.button("조회하기"):
    holidays = get_holidays(year, month)
    if holidays:
        st.subheader(f"✅ {year}년 {month}월의 공휴일")
        for date, name, emoji in holidays:
            st.write(f"{date.strftime('%Y-%m-%d')} - {name} {emoji}")
    else:
        st.subheader("❌ 이 달에는 공휴일이 없어요.")
        st.write("그래도 힘내세요! 당신의 하루가 작은 휴일처럼 빛나길 바랍니다 🌟")
