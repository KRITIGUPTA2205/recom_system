import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
@st.cache_data
def load_data():
    df = pd.read_excel("data_sample.xlsx", engine="openpyxl")
    df.columns = df.columns.str.strip()  # 🔧 Fix column name issues
    st.write("Column names:", df.columns.tolist())  # 🐛 Debug: print column names
    df.dropna(inplace=True)
    df = df[df['Quantity'] > 0]
    df = df[df['UnitPrice'] > 0]
    return df



df = load_data()

# App title
st.title("🧠 Customer Segmentation & Product Recommendation System")
st.markdown("This app clusters customers based on purchasing behavior and recommends products accordingly.")

# Show raw data
st.subheader("📦 Sample E-commerce Dataset")
st.dataframe(df.head())

# Feature engineering
customer_df = df.groupby('CustomerID').agg({
    'InvoiceNo': 'nunique',
    'Quantity': 'sum',
    'UnitPrice': 'mean',
    'StockCode': 'nunique'
}).reset_index()

customer_df.columns = ['CustomerID', 'NumPurchases', 'TotalQuantity', 'AvgUnitPrice', 'UniqueItems']
X = customer_df[['NumPurchases', 'TotalQuantity', 'AvgUnitPrice', 'UniqueItems']]

# Normalize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# KMeans clustering
kmeans = KMeans(n_clusters=4, random_state=42)
customer_df['Cluster'] = kmeans.fit_predict(X_scaled)

# PCA for visualization
pca = PCA(n_components=2)
pca_result = pca.fit_transform(X_scaled)
customer_df['PCA1'] = pca_result[:, 0]
customer_df['PCA2'] = pca_result[:, 1]

# 📍 PCA Scatter Plot
st.subheader("📍 Customer Clusters (Visualized in 2D with PCA)")
fig1, ax1 = plt.subplots()
sns.scatterplot(data=customer_df, x='PCA1', y='PCA2', hue='Cluster', palette='Set2', s=60, ax=ax1)
st.pyplot(fig1)

# 🧮 Clustered customer segments
st.subheader("🧮 Clustered Customer Segments")
st.dataframe(customer_df.head())

# 🎯 Product Recommendations by Cluster
st.subheader("🎯 Product Recommendations by Cluster")
selected_cluster = st.selectbox("Select a Cluster", sorted(customer_df['Cluster'].unique()))

# Get top products for selected cluster
cluster_customers = customer_df[customer_df['Cluster'] == selected_cluster]['CustomerID']
top_products = df[df['CustomerID'].isin(cluster_customers)] \
    .groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)

st.write("📌 **Top Products Purchased in this Cluster:**")
st.dataframe(top_products)

# 📦 Bar Chart: Top Products in Cluster
st.subheader("📦 Bar Chart: Top Products in Cluster")
fig2, ax2 = plt.subplots()
top_products.plot(kind='bar', color='skyblue', ax=ax2)
plt.ylabel("Total Quantity Sold")
plt.title(f"Top 10 Products in Cluster {selected_cluster}")
st.pyplot(fig2)

# 🔢 Pie Chart: Cluster Distribution
st.subheader("🔢 Cluster Distribution (Customer Count per Cluster)")
cluster_counts = customer_df['Cluster'].value_counts()
fig3, ax3 = plt.subplots()
ax3.pie(cluster_counts, labels=cluster_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title("Customer Distribution by Cluster")
st.pyplot(fig3)
