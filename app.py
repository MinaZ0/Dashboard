import plotly.express as px
st.title("ระบบวิเคราะห์ข้อมูลการขาย")
st.write("สรุปภาพรวมยอดขายและกำไรรายเดือน")
st.sidebar.header("ตัวเลือกข้อมูล")

data = {
    'Category': ['Electronics', 'Furniture', 'Clothing', 'Electronics', 'Furniture', 'Clothing'],
    'Sales': [450, 300, 200, 520, 280, 310],
    'Profit': [80, 40, 30, 95, 35, 55],
    'Month': ['Jan', 'Jan', 'Jan', 'Feb', 'Feb', 'Feb']
}
df = pd.DataFrame(data)
fig1 = px.bar(df, x='Category', y='Sales', color='Month', barmode='group', title="ยอดขายรายหมวดหมู่")
st.plotly_chart(fig1)
fig2 = px.pie(df, values='Profit', names='Category', title="สัดส่วนกำไร")
st.plotly_chart(fig2)
fig3 = px.line(df, x='Month', y='Sales', color='Category', title="แนวโน้มยอดขาย")
st.plotly_chart(fig3)

