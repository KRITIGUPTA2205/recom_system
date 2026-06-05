# 🧠 Customer Segmentation & Product Recommendation System

**An intelligent e-commerce platform that segments customers and delivers personalized product recommendations using ML clustering and analysis.**

[![Live App](https://img.shields.io/badge/Live-App-streamlit?logo=streamlit&color=FF4B4B)](https://recomsystem-xy2t4pw8aw2g76qsewvacz.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/ML-Clustering-brightgreen)](https://scikit-learn.org/)

---

## 🎯 Overview

This advanced machine learning application performs unsupervised customer segmentation on real-world e-commerce data using KMeans clustering and provides data-driven product recommendations for each customer segment. The system identifies distinct customer groups based on purchasing behavior and recommends the top products for each segment.

---

## ✨ Key Features

🎯 **Smart Segmentation**
- KMeans clustering to identify 4 distinct customer segments
- Unsupervised learning approach (no labels required)
- Behavior-based grouping

📦 **Product Recommendations**
- Top 10 products recommended per customer segment
- Recommendation based on purchase frequency and quantity
- Cross-selling opportunities identification

📊 **Advanced Analytics**
- PCA dimensionality reduction for 2D visualization
- Interactive cluster scatter plots
- Cluster distribution pie charts
- Detailed segment insights

💾 **Data Processing**
- Automatic data cleaning and preprocessing
- Feature engineering for customer behavior patterns
- StandardScaler for normalized comparisons
- Aggregated metrics per customer

🎨 **Interactive Dashboard**
- Clean, responsive Streamlit interface
- Real-time visualization updates
- Easy navigation and user experience

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|----------|
| Language | Python 3.8+ |
| Frontend | Streamlit |
| ML Framework | Scikit-Learn |
| Data Processing | Pandas, NumPy |
| Dimensionality Reduction | PCA |
| Clustering | KMeans |
| Visualization | Matplotlib, Plotly |
| Deployment | Streamlit Cloud |

---

## 📂 Project Structure

```
Customer-Segmentation-Product-Recommendation-System/
├── README.md
├── requirements.txt
├── app.py                          # Main Streamlit application
├── data/
│   ├── ecommerce_data.csv         # Sample e-commerce dataset
│   └── processed/
├── models/
│   └── kmeans_model.pkl           # Trained KMeans model
├── utils/
│   ├── preprocessing.py           # Data cleaning & feature engineering
│   ├── clustering.py              # KMeans implementation
│   └── recommendations.py         # Recommendation engine
└── notebooks/
    └── eda_analysis.ipynb         # Exploratory Data Analysis
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip or conda package manager
- Git

### Installation

```bash
# Clone repository
git clone https://github.com/KRITIGUPTA2205/Customer-Segmentation-Product-Recommendation-System.git
cd Customer-Segmentation-Product-Recommendation-System

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run Locally

```bash
streamlit run app.py
```

Navigate to `http://localhost:8501`

### Live Demo
🌐 **[View Live Application](https://recomsystem-xy2t4pw8aw2g76qsewvacz.streamlit.app/)**

---

## 💡 How It Works

### Step 1: Data Loading & Cleaning
```
Raw e-commerce data → Handle missing values → Remove duplicates
```

### Step 2: Feature Engineering
```
Transaction data → Customer aggregation → Behavior metrics
(Purchases, Quantity, Avg Price, Total Spending, etc.)
```

### Step 3: Feature Scaling
```
Raw features → StandardScaler normalization → Normalized features
(Ensures fair comparison across different scales)
```

### Step 4: Clustering
```
Scaled features → KMeans (k=4) → Customer segments
(Identifies 4 distinct customer groups)
```

### Step 5: Dimensionality Reduction
```
4D features → PCA → 2D visualization
(Enables easy visualization and interpretation)
```

### Step 6: Recommendations
```
Customer segments → Product analysis → Top 10 products per segment
(Business actionable insights)
```

---

## 📊 Customer Segments

The system identifies **4 customer segments**:

| Segment | Characteristics | Strategy |
|---------|-----------------|----------|
| **High-Value** | High spending, frequent purchases | Premium offers, loyalty programs |
| **Regular** | Moderate spending, consistent purchases | Cross-sell, bundle deals |
| **Casual** | Low frequency, lower spend | Incentive campaigns, first-time deals |
| **At-Risk** | Declining purchases | Re-engagement, special promotions |

---

## 📈 Business Applications

✅ **Targeted Marketing**: Segment-specific campaigns
✅ **Product Strategy**: Stock products for each segment
✅ **Revenue Optimization**: Personalized pricing & offers
✅ **Customer Retention**: Segment-based loyalty programs
✅ **Inventory Management**: Demand forecasting by segment
✅ **A/B Testing**: Segment-based experimentation

---

## 🎓 Technical Skills Demonstrated

- ✅ **Unsupervised Learning**: KMeans clustering
- ✅ **Dimensionality Reduction**: PCA analysis
- ✅ **Feature Engineering**: Customer behavior metrics
- ✅ **Data Preprocessing**: Cleaning, scaling, normalization
- ✅ **Data Visualization**: Interactive charts and plots
- ✅ **Web Development**: Streamlit dashboard
- ✅ **Statistical Analysis**: Cluster validation
- ✅ **Business Intelligence**: Actionable insights

---

## 📊 Key Metrics

- **Silhouette Score**: Measures cluster quality (0-1 range)
- **Inertia**: Within-cluster sum of squares
- **Davies-Bouldin Index**: Cluster separation metric
- **Recommendation Accuracy**: Based on product popularity

---

## 🔮 Future Enhancements

- [ ] Hierarchical clustering option
- [ ] Elbow method for optimal k selection
- [ ] Time-series segmentation
- [ ] RFM (Recency, Frequency, Monetary) analysis
- [ ] DBSCAN for density-based clustering
- [ ] Deep learning embeddings
- [ ] Real-time data streaming
- [ ] API for batch predictions
- [ ] Export segmentation results
- [ ] A/B testing dashboard

---

## 📁 Data Format

Expected CSV format:

```
CustomerID, Product, Quantity, Price, Date
1001, Widget A, 2, 25.00, 2024-01-15
1002, Widget B, 1, 45.00, 2024-01-16
...
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Open Pull Request

---

## 📚 References

- [KMeans Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- [PCA Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

## 📄 License

MIT License - Open source and free to use

---

## 📧 Support

Questions or suggestions? Open an issue on GitHub!

---

**⭐ Like this project? Show your support by starring it!**