from typing import Dict, List

import streamlit as st
import pendulum as dt


class ConditionScore:
    """condition:score"""

    def __init__(self, data: Dict[str, float]) -> None:
        self._data = data

    @property
    def label(self) -> str:
        labels = []
        for condition, score in self._data.items():
            labels.append(f"{condition} {score}分")
        return ", ".join(labels)

    @property
    def conditions(self) -> List[str]:
        return self._data.keys()

    def score(self, condition: str) -> float:
        return self._data[condition]


st.title("上海新房积分计算器")
st.write(
    "上海买房实施积分摇号制度，购房人在认购后，"
    "将综合家庭、户籍、拥有的住房状况、五年内在沪购房记录以及在沪缴纳社保五大因素拥有一个积分，"
    "然后根据摇号人数比房源多30%的原则，按积分高低排序选取进入公证摇号选房的人员名单。"
)
score = 0

st.subheader("家庭情况")
cs = ConditionScore(dict(家庭=10, 单身=0))
family = st.radio(cs.label, cs.conditions, 1)
score += cs.score(family)

st.subheader("户籍情况")
cs = ConditionScore(dict(上海户口=10, 非上海户口=0))
house_hold = st.radio(cs.label, cs.conditions, 0)
score += cs.score(house_hold)

st.subheader("房产情况")
cs = ConditionScore(dict(上海无房=20, 上海有房=5))
house = st.radio(cs.label, cs.conditions, 0)
score += cs.score(house)

st.subheader("五年内购房情况")
cs = ConditionScore(
    {"无房-5年内无购房记录": 20, "有房-5年内无购房记录": 5, "无房-5年内有购房记录": 0, "有房-5年内有购房记录": 0}
)
house_record = st.radio(cs.label, cs.conditions, 0)
score += cs.score(house_record)

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
social_insurance_coefficient = st.slider("社保缴纳系数(0.1-0.24)", 0.10, 0.24, 0.13)

st.subheader("总分")
st.write(f"总计: {score+social_insurance_months*social_insurance_coefficient}")
