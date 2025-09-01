# streamlit_biological_age_app.py
# 설명: 사용자가 입력한 생활습관/환경 정보를 바탕으로 '생물학적 나이'를 추정하고,
# 실제(달력) 나이와 비교하여 개선점과 권장사항을 제시하는 교육용 시연용 앱입니다.
# 주의: 이 앱은 교육적・시연적 목적의 추정 모델을 제공합니다. 의료적 진단/치료를 대체하지 않습니다.

# streamlit_biological_age_app.py
# 설명: 사용자가 입력한 생활습관/환경 정보를 바탕으로 '생물학적 나이'를 추정하고,
# 실제(달력) 나이와 비교하여 개선점과 권장사항을 제시하는 교육용 시연용 앱입니다.
# 주의: 이 앱은 교육적·시연적 목적의 추정 모델을 제공합니다. 의료적 진단/치료를 대체하지 않습니다.

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="생물학적 나이 추정기", layout="centered")

st.title("🧬 생물학적 나이 추정기 (시연용)")
st.write(
    "이 앱은 생활습관과 환경 변수를 바탕으로 간단한 가중치 방식으로 '생물학적 나이'를 추정합니다.\n"
    "교육용·시연용으로 만든 예시 모델이므로 결과는 참고용으로만 활용하세요. 실제 임상 적용 전에는 전문의 상담이 필요합니다."
)
st.divider()

# ------------------ 사용자 입력 ------------------
with st.form(key='input_form'):
    st.subheader('기본정보')
    age = st.number_input('실제 연령(세)', min_value=10, max_value=120, value=30, step=1)
    sex = st.selectbox('성별', ['선택안함', '여성', '남성'])

    st.subheader('신체정보')
    height_cm = st.number_input('키(cm)', min_value=100, max_value=230, value=170)
    weight_kg = st.number_input('체중(kg)', min_value=30, max_value=250, value=65)

    st.subheader('생활습관 & 환경')
    smoking = st.selectbox('흡연 여부', ['비흡연', '과거 흡연자', '현재 흡연자'])
    alcohol = st.number_input('주당 음주(잔 단위)', min_value=0, max_value=200, value=2)
    exercise_min = st.number_input('주당 운동 시간(분)', min_value=0, max_value=3000, value=150)
    diet_score = st.slider('식습관 점수 (1=매우 불량 ~ 10=매우 우수)', min_value=1, max_value=10, value=6)
    sleep_hours = st.slider('평균 수면시간(시간)', min_value=0.0, max_value=12.0, value=7.0, step=0.5)
    stress = st.slider('주관적 스트레스 수준 (1=최저 ~ 10=최고)', min_value=1, max_value=10, value=5)
    chronic = st.checkbox('만성 질환(예: 고혈압/당뇨/심혈관계 질환) 보유')
    pollution = st.selectbox('생활 환경 - 대기오염 노출 정도', ['낮음', '보통', '높음'])
    ses = st.selectbox('사회경제적 지위(자기 판단)', ['높음', '보통', '낮음'])

    submitted = st.form_submit_button('생물학적 나이 계산하기')

if not submitted:
    st.info('위 항목을 입력한 뒤 "생물학적 나이 계산하기" 버튼을 눌러주세요.')
    st.stop()

# ------------------ 계산 함수 ------------------

def compute_biological_age(age, height_cm, weight_kg, smoking, alcohol, exercise_min,
                           diet_score, sleep_hours, stress, chronic, pollution, ses):
    contributions = {}

    # 기초값: 달력 나이를 기준으로 시작
    base = float(age)

    # 1) 흡연
    if smoking == '현재 흡연자':
        contributions['흡연'] = 6.0
    elif smoking == '과거 흡연자':
        contributions['흡연'] = 2.0
    else:
        contributions['흡연'] = 0.0

    # 2) 음주 (잔 수 기반, 단순화)
    if alcohol >= 21:
        contributions['음주'] = 2.5
    elif alcohol >= 7:
        contributions['음주'] = 1.0
    elif alcohol == 0:
        contributions['음주'] = -0.5
    else:
        contributions['음주'] = 0.0

    # 3) 운동
    if exercise_min >= 150:
        contributions['운동'] = -2.0
    elif exercise_min >= 75:
        contributions['운동'] = -1.0
    elif exercise_min >= 30:
        contributions['운동'] = 0.5
    else:
        contributions['운동'] = 2.0

    # 4) 식습관 (점수 중심)
    contributions['식습관'] = (5.5 - float(diet_score)) * 0.5

    # 5) 수면
    if 7 <= sleep_hours <= 9:
        contributions['수면'] = 0.0
    elif sleep_hours < 6:
        contributions['수면'] = 1.5
    elif 6 <= sleep_hours < 7:
        contributions['수면'] = 0.5
    else:  # > 9
        contributions['수면'] = 1.0

    # 6) BMI
    h_m = height_cm / 100.0
    bmi = weight_kg / (h_m * h_m)
    if bmi < 18.5:
        contributions['BMI'] = 1.0
    elif bmi < 25:
        contributions['BMI'] = 0.0
    elif bmi < 30:
        contributions['BMI'] = 1.5
    else:
        contributions['BMI'] = 3.0

    # 7) 스트레스
    contributions['스트레스'] = (float(stress) - 5.0) * 0.5

    # 8) 만성질환
    contributions['만성질환'] = 4.0 if chronic else 0.0

    # 9) 대기오염
    if pollution == '높음':
        contributions['대기오염'] = 1.5
    elif pollution == '보통':
        contributions['대기오염'] = 0.7
    else:
        contributions['대기오염'] = 0.0

    # 10) 사회경제적 지위
    if ses == '낮음':
        contributions['사회경제적지위'] = 1.5
    elif ses == '보통':
        contributions['사회경제적지위'] = 0.0
    else:
        contributions['사회경제적지위'] = -0.5

    # 총 기여 합산
    total_delta = sum(contributions.values())

    # 극단치 방지 (교육/시연 목적)
    total_delta = max(-10.0, min(total_delta, 15.0))

    biological_age = round(max(10.0, base + total_delta), 1)

    # 연관 추가 정보
    details = {
        'base': base,
        'biological_age': biological_age,
        'delta': round(biological_age - base, 1),
        'bmi': round(bmi, 1),
        'contributions': contributions
    }
    return details

# ------------------ 결과 계산 ------------------
result = compute_biological_age(age, height_cm, weight_kg, smoking, alcohol, exercise_min,
                                diet_score, sleep_hours, stress, chronic, pollution, ses)

# ------------------ 결과 출력 ------------------
st.subheader('결과 요약')
col1, col2, col3 = st.columns(3)
col1.metric('실제 나이', f"{result['base']} 세")
col2.metric('추정된 생물학적 나이', f"{result['biological_age']} 세", delta=f"{result['delta']}년")
col3.metric('BMI', f"{result['bmi']}")

st.markdown(f"**해석:** 입력하신 생활습관 정보를 바탕으로 계산한 결과, 생물학적 나이는 **{result['biological_age']}세**로, 실제 나이와 **{result['delta']}년**의 차이가 있습니다.\n\n"
            "(주의: 이 값은 교육용 추정치입니다. 실제 생물학적 나이는 유전자·혈액 바이오마커 등 직접측정에 의해 더 정확하게 평가됩니다.)")

# ------------------ 기여 요인 시각화 ------------------
st.subheader('생물학적 나이에 영향을 준 요인별 기여도 (년 단위)')
contrib_df = pd.DataFrame.from_dict(result['contributions'], orient='index', columns=['years'])
contrib_df = contrib_df.sort_values('years', ascending=False)
st.bar_chart(contrib_df)

st.markdown('요인별 기여도는 각 항목이 생물학적 나이(년 단위)에 더한(또는 뺀) 값을 단순 합산한 것입니다.\n이는 학술적 정밀모델이 아닌 시연용 가중치 모델임을 다시 한 번 알려드립니다.')

# ------------------ 사용자를 동일 연령대 시뮬레이션 집단과 비교 (통계적 시각화) ------------------
st.subheader('동일 연령대(시뮬레이션)와 비교')

@st.cache_data
def generate_simulated_cohort(base_age, n=500, seed=42):
    rng = np.random.default_rng(seed)
    # 평균은 base_age, 표준편차는 4~6세 사이로 가정
    sim = rng.normal(loc=base_age, scale=4.5, size=n)
    # 약간의 랜덤 포용 (교육용)
    return sim

sim_cohort = generate_simulated_cohort(age, n=500)

# Matplotlib 의존을 제거: 히스토그램을 numpy로 계산한 뒤 Streamlit의 bar_chart로 표시
hist, bin_edges = np.histogram(sim_cohort, bins=30)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
hist_df = pd.DataFrame({'bin_center': bin_centers, 'count': hist})
hist_df = hist_df.set_index('bin_center')

st.markdown('시뮬레이션된 동일 연령대 분포(히스토그램):')
st.bar_chart(hist_df['count'])

st.markdown(f"- 당신(생물학적 나이): **{result['biological_age']}세**\n- 당신(실제 나이): **{age}세**")

# 통계적 지표: 백분위수
percentile = float(np.mean(sim_cohort <= result['biological_age']) * 100)
st.write(f"같은 실제 연령({age}세) 기준의 시뮬레이션 집단에서 당신의 생물학적 나이는 상위 {percentile:.1f} 퍼센타일입니다.\n"
         "(값이 높을수록 상대적으로 더 '노화'되어 있음을 의미합니다.)")

# ------------------ 개선 권장사항 ------------------
st.subheader('우선 개선 권장사항 (우선순위)')

# 개선 항목 우선순위는 기여도가 큰 항목(양수) 위주로 정렬
sorted_contribs = sorted(result['contributions'].items(), key=lambda x: x[1], reverse=True)

recommendations = []
for k, v in sorted_contribs:
    if v <= 0:
        continue
    if k == '흡연':
        recommendations.append((k, v, '흡연은 생물학적 나이를 크게 높입니다. 금연 상담, 니코틴 보조요법(패치/껌), 전문의 상담을 권장합니다.'))
    elif k == '음주':
        recommendations.append((k, v, '과도한 음주는 노화에 악영향을 줄 수 있습니다. 주당 음주량을 줄이고 절주를 권장합니다.'))
    elif k == '운동':
        recommendations.append((k, v, '주당 최소 150분의 중등도 유산소 운동(예: 빠른 걷기)과 주 2회 근력운동을 목표로 하세요. 작은 목표부터 시작해 점차 증가시키면 좋습니다.'))
    elif k == '식습관':
        recommendations.append((k, v, '균형 잡힌 식사(채소·과일·통곡물·건강한 단백질)와 가공식품·설탕 섭취 제한을 권장합니다. 영양사 상담을 고려하세요.'))
    elif k == '수면':
        recommendations.append((k, v, '수면 시간이 부족하거나 과다하면 건강에 영향을 줍니다. 규칙적 수면시간과 수면 위생(취침 루틴, 전자기기 제한 등)을 개선하세요.'))
    elif k == 'BMI':
        recommendations.append((k, v, '현재 BMI가 정상 범위를 벗어나는 경우 체중 관리를 통해 정상 범위를 목표로 하세요. 영양·운동 전문가 상담 권장.'))
    elif k == '스트레스':
        recommendations.append((k, v, '만성 스트레스는 신체 전반에 영향을 줍니다. 명상, 심리상담, 규칙적 운동 등 스트레스 관리법을 도입하세요.'))
    elif k == '만성질환':
        recommendations.append((k, v, '기존 만성질환 관리는 생물학적 나이 개선에 중요합니다. 주치의와의 정기적 관리 및 약물 준수 필요.'))
    elif k == '대기오염':
        recommendations.append((k, v, '대기오염 노출시 실내 공기질 관리(공기청정기, 외출 시 마스크)와 통근 경로·시간 조정 등을 고려하세요.'))
    elif k == '사회경제적지위':
        recommendations.append((k, v, '사회경제적 요인은 건강에 영향을 미칩니다.지역사회 자원(보건소, 커뮤니티 서비스)을 활용하세요.'))

if len(recommendations) == 0:
    st.success('현재 입력값 기준으로 특별히 크게 문제되는 항목이 보이지 않습니다. 현재 생활습관을 계속 유지하고 정기 검진을 권장합니다.')
else:
    for name, val, text in recommendations:
        st.markdown(f"**{name}**: +{val}년 → {text}")

st.divider()

# ------------------ 추가 정보 및 다운로드 ------------------
st.subheader('결과 저장')
if st.button('결과 CSV로 저장 (다운로드 버튼 생성)'):
    out = {
        '실제나이': [result['base']],
        '생물학적나이': [result['biological_age']],
        '차이(년)': [result['delta']],
        'BMI': [result['bmi']],
        '생성일': [datetime.now().isoformat()]
    }
    out_df = pd.DataFrame(out)
    csv = out_df.to_csv(index=False).encode('utf-8-sig')
    st.download_button('다운로드', data=csv, file_name='biological_age_result.csv', mime='text/csv')

st.markdown('---')
st.caption('※ 다시 한 번 강조: 이 앱의 산출치는 교육/시연용 추정치입니다. 실제 건강 평가는 의료기관의 진료 및 바이오마커 검사로 확인하시기 바랍니다.')
