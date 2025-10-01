import streamlit as st
import pandas as pd
import random
# โหลดข้อมูลจาก CSV
df = pd.read_csv("data.csv")
# ส่วนหัวแอป
st.title("AI ผู้ช่วยเลือกเมนูอาหารเพื่อสุขภาพ " )
st.write ( "เลือกเงื่อนไขที่คุณต้องการ แล้วระบบจะแนะนำเมนูให้")
# ให้ผู้ใช้เลือก
goal = st.selectbox (" เป้าหมายสุขภาพ", df["เหมาะกับ"]. unique())
meal_type = st. selectbox(" ประเภทอาหาร", df["ประเภท"]. unique())
# กรองข้อมูล
filtered = df[ (df["เหมาะกับ"] == goal) & (df["ประเภท"] == meal_type) ]
# แสดงผล
if not filtered. empty:
    menu = random.choice(filtered["เมนู"].tolist())
    st. success (f"เมนที่แนะนำคือ : **{menu}**")
else:
    st.warning ("ไม่พบเมนูที่ตรงเงื่อนไข ลองเปลี่ยนตัวเลือกดูนะครับ")
