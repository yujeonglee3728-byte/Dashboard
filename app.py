import streamlit as st
import pandas as pd
import json
from pathlib import Path

st.set_page_config(page_title="팀 업무 대시보드", layout="wide")

# 상대 경로 사용
TASKS_PATH = Path(__file__).parent / "tasks.json"

@st.cache_data
def load_tasks():
    with open(TASKS_PATH, encoding="utf-8") as f:
        return json.load(f)

data = load_tasks()

CATEGORIES = ["MDR", "FDA", "CyberSecurity", "GMP", "MFDS"]

STATUS_COLORS = {
    "완료": "background-color: #d4edda; color: #155724;",
    "대기중": "background-color: #fff3cd; color: #856404;",
    "진행중": "",
    "검토중": "",
}

def style_row(row):
    color = STATUS_COLORS.get(row["상태"], "")
    return [color] * len(row)

# 사이드바
st.sidebar.title("카테고리 필터")
selected = {cat: st.sidebar.checkbox(cat, value=True) for cat in CATEGORIES}
active_cats = [cat for cat, checked in selected.items() if checked]

# 메인
st.title("팀 업무 대시보드")

# 최근 일정
st.subheader("📅 최근 일정")
schedule = data.get("Schedule", [])
if schedule:
    df_schedule = pd.DataFrame(schedule).rename(columns={"date": "날짜", "client": "고객사", "manager": "담당자"})
    df_schedule = df_schedule.sort_values("날짜")
    st.table(df_schedule.reset_index(drop=True))
else:
    st.info("등록된 일정이 없습니다.")

st.divider()

# 카테고리별 업무 리스트
st.subheader("📋 카테고리별 업무 현황")

if not active_cats:
    st.warning("사이드바에서 카테고리를 하나 이상 선택해주세요.")
else:
    for cat in active_cats:
        tasks = data.get(cat, [])
        st.markdown(f"### {cat}")
        if tasks:
            df = pd.DataFrame(tasks).rename(columns={
                "project": "프로젝트명",
                "status": "상태",
                "update": "최근 업데이트",
                "note": "비고",
            })
            styled = df.style.apply(style_row, axis=1)
            st.dataframe(styled, use_container_width=True, hide_index=True)
        else:
            st.info("항목 없음")
        st.markdown("")
