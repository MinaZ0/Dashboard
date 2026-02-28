import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")

# --- ต้องสร้างข้อมูลก่อนเอาไปใช้ใน Sidebar ---
data = {
    'Category': ['Electronics', 'Furniture', 'Clothing', 'Electronics', 'Furniture', 'Clothing'],
    'Sales': [450, 300, 200, 520, 280, 310],
    'Profit': [80, 40, 30, 95, 35, 55],
    'Month': ['Jan', 'Jan', 'Jan', 'Feb', 'Feb', 'Feb']
}
df = pd.DataFrame(data)

# --- ส่วน UI ---
st.title("ระบบวิเคราะห์ข้อมูลการขาย")
st.write("สรุปภาพรวมยอดขายและกำไรรายเดือน")

st.sidebar.header("ตัวเลือกข้อมูล")
selected_cat = st.sidebar.multiselect("เลือกหมวดหมู่:", df['Category'].unique(), default=df['Category'].unique())
filtered_df = df[df['Category'].isin(selected_cat)]

# --- ส่วนกราฟ ---
col1, col2 = st.columns(2)
with col1:
   fig1 = px.bar(filtered_df, x='Category', y='Sales', color='Month', barmode='group', 
             title="ยอดขายรายหมวดหมู่",
             labels={'Sales':'ยอดขาย (บาท)', 'Category':'หมวดหมู่สินค้า'})
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.pie(filtered_df, values='Profit', names='Category', title="สัดส่วนกำไร")
    st.plotly_chart(fig2, use_container_width=True)

fig3 = px.line(filtered_df, x='Month', y='Sales', color='Category', title="แนวโน้มยอดขาย")
st.plotly_chart(fig3)

if st.checkbox("แสดงตารางข้อมูลดิบ"):
    st.dataframe(filtered_df)