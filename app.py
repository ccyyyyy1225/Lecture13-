# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------
# 頁面設定
# --------------------------
st.set_page_config(
    page_title="電影資料視覺化",
    page_icon="🎬",
    layout="wide"
)

# --------------------------
# 標題與介紹
# --------------------------
st.title("🎬 物聯網 HW3：電影資料視覺化")
st.markdown("""
這個 Streamlit App 展示從網站爬取的電影資訊（共10頁），
提供互動式資料檢視與簡易統計圖表分析。
""")

# --------------------------
# 讀取資料
# --------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("movie_info_from_10pages.csv")
    return df

try:
    df = load_data()
    st.success("✅ 成功載入電影資料！")
except Exception as e:
    st.error("❌ 無法載入資料，請確認 `movie_info_from_10pages.csv` 是否存在於同一目錄下。")
    st.stop()

# --------------------------
# 資料預覽
# --------------------------
st.subheader("📋 資料集預覽")
st.dataframe(df.head())

# --------------------------
# 篩選功能
# --------------------------
st.subheader("🔍 篩選條件")
col1, col2 = st.columns(2)

# 篩選條件示範（可依資料實際欄位修改）
if "類型" in df.columns:
    genre_list = df["類型"].dropna().unique().tolist()
    selected_genre = col1.multiselect("選擇電影類型", genre_list)
else:
    selected_genre = []

if "評分" in df.columns:
    min_rating, max_rating = float(df["評分"].min()), float(df["評分"].max())
    rating_range = col2.slider("選擇評分區間", min_rating, max_rating, (min_rating, max_rating))
else:
    rating_range = (0, 10)

# 篩選資料
filtered_df = df.copy()
if selected_genre:
    filtered_df = filtered_df[filtered_df["類型"].isin(selected_genre)]
if "評分" in df.columns:
    filtered_df = filtered_df[(filtered_df["評分"] >= rating_range[0]) & (filtered_df["評分"] <= rating_range[1])]

st.write(f"目前顯示 {len(filtered_df)} 筆資料。")
st.dataframe(filtered_df)

# --------------------------
# 視覺化分析
# --------------------------
st.subheader("📊 統計圖表")

if "評分" in df.columns:
    fig, ax = plt.subplots()
    ax.hist(filtered_df["評分"], bins=10, color="#ff7f50", edgecolor="black")
    ax.set_xlabel("評分")
    ax.set_ylabel("電影數量")
    ax.set_title("電影評分分佈")
    st.pyplot(fig)
else:
    st.info("未找到 '評分' 欄位，無法繪製統計圖。")

# --------------------------
# 結語
# --------------------------
st.markdown("---")
