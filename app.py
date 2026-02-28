import streamlit as st
import pandas as pd
import plotly.express as px

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
fig1 = px.bar(filtered_df, x='Category', y='Sales', color='Month', barmode='group', title="ยอดขายรายหมวดหมู่")
st.plotly_chart(fig1)

fig2 = px.pie(filtered_df, values='Profit', names='Category', title="สัดส่วนกำไร")
st.plotly_chart(fig2)

fig3 = px.line(filtered_df, x='Month', y='Sales', color='Category', title="แนวโน้มยอดขาย")
st.plotly_chart(fig3)