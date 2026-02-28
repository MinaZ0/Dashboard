st.title("ระบบวิเคราะห์ข้อมูลการขาย")
data = {
    'Category': ['Electronics', 'Furniture', 'Clothing', 'Electronics', 'Furniture', 'Clothing'],
    'Sales': [450, 300, 200, 520, 280, 310],
    'Profit': [80, 40, 30, 95, 35, 55],
    'Month': ['Jan', 'Jan', 'Jan', 'Feb', 'Feb', 'Feb']
}
df = pd.DataFrame(data)