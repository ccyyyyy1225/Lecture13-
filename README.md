# Lecture13-爬蟲
# 電影網站爬蟲與資料視覺化

本專案為「物聯網應用與實作」課程的第 3 次作業（HW3），  
主要目標為：

1. 從目標電影網站爬取多頁電影資料  
2. 將電影資訊整理與儲存為 CSV 檔  
3. 使用 Streamlit 建立互動式網頁介面，呈現與分析電影資料  

---

## 📌 線上 Demo（Streamlit）

本專案已部署於 Streamlit Community Cloud：  

👉 [點此開啟 Demo](https://你的-app-名稱.streamlit.app/)  

> 若無法開啟，可能是伺服器尚未喚醒，請稍後再重新整理一次頁面。

---

## 📁 專案結構

.
├─ app.py                        # Streamlit 主程式（讀取並呈現電影資料）
├─ movie_info_from_10pages.csv   # 爬下來的電影資訊（10 頁）
├─ movie_info.ipynb                # 作業原始 Jupyter Notebook（爬蟲 & 前處理）
├─ requirements.txt              # 專案所需套件
└─ .streamlit/
   └─ config.toml                # （選配）Streamlit 主題設定
