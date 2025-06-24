import streamlit as st

st.set_page_config(page_title="Thẻ căn cước công dân", page_icon="🪪")
st.title("🪪 TẠO THẺ CĂN CƯỚC CÔNG DÂN")

# Nhập dữ liệu
name = st.text_input("Họ và tên")
birth = st.text_input("Năm sinh")
hometown = st.text_input("Quê quán")
job = st.text_input("Nghề nghiệp")

# Hiển thị thẻ
if st.button("Tạo thẻ"):
    st.markdown("---")
    st.markdown("### 💳 THẺ CĂN CƯỚC")
    st.markdown(f"**Họ tên:** {name}")
    st.markdown(f"**Năm sinh:** {birth}")
    st.markdown(f"**Quê quán:** {hometown}")
    st.markdown(f"**Nghề nghiệp:** {job}")
    st.markdown("---")
