import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 데이터프레임 생성
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

# 데이터프레임을 화면에 표시
st.write("Our DataFrame:", df)

# 차트 그리기
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
