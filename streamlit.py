import streamlit as st
import requests

# Lambda API Gateway URL
API_BASE_URL = "https://your-lambda-api-url/dev"

st.title("🎭 공연 일정 검색 봇")

# 🔍 배우 검색
st.header("🔍 배우 검색")
actor_name = st.text_input("배우 이름을 입력하세요:", "")
if st.button("검색"):
    if actor_name:
        response = requests.get(f"{API_BASE_URL}/search_actor", params={"name": actor_name})
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("배우 정보를 가져오지 못했습니다.")

# 📅 날짜 검색
st.header("📅 날짜별 공연 검색")
selected_date = st.date_input("날짜를 선택하세요")
if st.button("공연 검색"):
    response = requests.get(f"{API_BASE_URL}/search_date", params={"date": selected_date})
    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error("해당 날짜의 공연 정보를 가져오지 못했습니다.")

# ⭐ 내 일정 확인
st.header("⭐ 내 일정 확인")
user_id = st.text_input("유저 ID 입력")
if st.button("내 일정 보기"):
    response = requests.get(f"{API_BASE_URL}/save_my_schedule", params={"user_id": user_id})
    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error("일정 정보를 가져오지 못했습니다.")
