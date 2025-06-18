# recom_system
# 🧠 Customer Segmentation & Product Recommendation System
> 📍 [Live App](https://recomsystem-xy2t4pw8aw2g76qsewvacz.streamlit.app/)  

 📌 Overview

This Streamlit app performs **unsupervised customer segmentation** on an e-commerce dataset using **KMeans clustering**, and provides **top product recommendations** per customer group. It also uses **PCA** for visualizing clusters in 2D.



## 🎯 Key Features

- ✅ E-commerce dataset preprocessing and cleaning  
- ✅ Feature engineering for customer behavior  
- ✅ KMeans clustering into meaningful segments  
- ✅ PCA-based 2D visualization of customer clusters  
- ✅ Top product recommendations for each customer segment  
- ✅ Cluster distribution via interactive pie chart  
- ✅ Clean and responsive UI with Streamlit  

---

## 📊 How It Works

1. **Loads and cleans** a sample e-commerce transactions dataset.
2. **Aggregates data per customer** (e.g., number of purchases, quantity, avg unit price).
3. **Scales features** using `StandardScaler`.
4. **Applies KMeans** to cluster customers into 4 segments.
5. **Reduces dimensionality** using PCA for 2D visualization.
6. Shows:
   - 📍 Cluster scatter plot  
   - 📦 Top 10 products per cluster  
   - 🔢 Customer count per cluster  


