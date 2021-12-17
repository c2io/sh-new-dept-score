from typing import Tuple
from dataclasses import dataclass

import streamlit as st
import pendulum as dt


@dataclass
class ConditionScore:
    conditions: Tuple
    scores: Tuple


def ratio_label(cs: ConditionScore) -> str:
    labels = []
    for condition, score in zip(cs.conditions, cs.scores):
        labels.append(f"{condition} {score}分")

    return ", ".join(labels)


st.title("上海新房积分计算器")

score = 0

st.subheader("家庭情况")
cs = ConditionScore(["家庭", "单身"], [10, 0])
family = st.radio(ratio_label(cs), cs.conditions, 1)
score += cs.scores[0] if family == cs.conditions[0] else cs.scores[1]

st.subheader("户籍情况")
cs = ConditionScore(["上海户口", "非上海户口"], [10, 0])
house_hold = st.radio(ratio_label(cs), cs.conditions)
score += cs.scores[0] if house_hold == cs.conditions[0] else cs.scores[1]

st.subheader("房产情况")
cs = ConditionScore(["上海无房", "上海有房"], [20, 5])
house = st.radio(ratio_label(cs), cs.conditions)
score += cs.scores[0] if house == cs.conditions[0] else cs.scores[1]

st.subheader("五年内购房情况")
cs = ConditionScore(
    ["无房-5年内无购房记录", "有房-5年内无购房记录", "无房-5年内有购房记录", "有房-5年内有购房记录"], [20, 5, 0, 0]
)
house_record = st.radio(ratio_label(cs), cs.conditions)
score += cs.scores[cs.conditions.index(house_record)]

st.subheader("基础分")
st.write(f"总计: {score}")

st.subheader("2003年1月起到现在的累计社保月数")
social_insurance_start_date = st.date_input("社保起交日期", dt.date(2015, 8, 6))

st.subheader("社保月数")
social_insurance_months = (
    dt.now() - dt.parse(str(social_insurance_start_date))
).in_months()
st.write(f"总计: {social_insurance_months}")

st.subheader("社保系数")
social_insurance_coefficient = st.slider("社保缴纳系数(0.1-0.24)", 0.1, 0.24, 0.13)

st.subheader("总分")
st.write(f"总计: {score+social_insurance_months*social_insurance_coefficient}")
