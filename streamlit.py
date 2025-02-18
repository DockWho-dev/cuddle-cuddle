import streamlit as st
import requests
import pandas as pd

# Lambda API Gateway URL
API_BASE_URL = "https://t47nht6fk5.execute-api.us-east-1.amazonaws.com/dev"

st.title("🎭 공연 일정 검색 봇")

# 🔍 배우 검색
st.header("🔍 배우 검색")
actor_name = st.text_input("배우 이름을 입력하세요:", "")
if st.button("검색"):
    if actor_name:
        response = requests.get(f"{API_BASE_URL}/search/actor", params={"name": actor_name})
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame([
                {
                    "날짜": item["date"],
                    "시간": item["time"],
                    "제목": item["title"],
                    "장소": item["location"],
                    "배우1": item["cast"]["배우1"],
                    "배우2": item["cast"]["배우2"],
                    "배우3": item["cast"]["배우3"],
                    "배우4": item["cast"]["배우4"],
                    "배우5": item["cast"]["배우5"],
                    "이벤트": item["event"]
                }
                for item in data
            ])
            st.markdown("""
                <style>
                    table {
                        width: 100%;
                        border-collapse: collapse;
                    }
                    th, td {
                        border: 1px solid #ddd;
                        padding: 8px;
                        text-align: left;
                    }
                    th {
                        background-color: #f4f4f4;
                    }
                </style>
                """, unsafe_allow_html=True)

            st.table(df)
        else:
            st.error("배우 정보를 가져오지 못했습니다.")

# 📅 날짜 검색
st.header("📅 날짜별 공연 검색")
selected_date = st.date_input("날짜를 선택하세요")
if st.button("공연 검색"):
    response = requests.get(f"{API_BASE_URL}/search/date", params={"date": selected_date})
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame([
            {
                "날짜": item["date"],
                "시간": item["time"],
                "제목": item["title"],
                "장소": item["location"],
                "배우1": item["cast"]["배우1"],
                "배우2": item["cast"]["배우2"],
                "배우3": item["cast"]["배우3"],
                "배우4": item["cast"]["배우4"],
                "배우5": item["cast"]["배우5"],
                "이벤트": item["event"]
            }
            for item in data
        ])
        st.markdown("""
            <style>
                table {
                    width: 100%;
                    border-collapse: collapse;
                }
                th, td {
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }
                th {
                    background-color: #f4f4f4;
                }
            </style>
            """, unsafe_allow_html=True)

        st.table(df)
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
