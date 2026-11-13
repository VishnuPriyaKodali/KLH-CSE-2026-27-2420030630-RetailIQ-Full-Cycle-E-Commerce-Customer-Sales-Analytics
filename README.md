# RetailIQ – Full-Cycle E-Commerce Customer & Sales Analytics

**RetailIQ** is a data science project that analyzes e-commerce customer behaviour, sales performance, and purchasing patterns. It uses Exploratory Data Analysis (EDA), RFM (Recency, Frequency, Monetary) analysis, and machine learning-based customer segmentation to generate meaningful business insights.

The project also includes an interactive dashboard developed using Streamlit to present analytical results and customer segments.

## Project Objectives

- Analyze e-commerce sales and customer behaviour.
- Identify purchasing patterns and cart abandonment trends.
- Perform data preprocessing and exploratory data analysis.
- Apply RFM analysis to understand customer purchasing behaviour.
- Segment customers using K-Means clustering.
- Compare different clustering models using evaluation metrics.
- Generate business recommendations based on customer segments.
- Present insights through an interactive dashboard.

## Dataset

**Dataset:** Indian E-Commerce Customer Behavior and Purchase Dataset

- Total records: 25,000
- Total features: 29
- Unique customers: 8,442
- Unique sessions: 25,000
- Missing values: 0
- Duplicate records: 0

Each row represents an individual customer session. A customer may have multiple sessions.

## Technologies Used

| Category | Tools |
|---|---|
| Programming Language | Python |
| Data Manipulation | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Dashboard | Streamlit |
| Development Environment | Jupyter Notebook, Anaconda, VS Code |

## Project Workflow

### 1. Data Preprocessing
- Loaded and inspected the dataset.
- Examined data types, missing values, and duplicate records.
- Validated discount and revenue calculations.
- Performed outlier analysis using the Interquartile Range (IQR) method.
- Applied outlier capping experiments to a separate RFM dataset copy.

### 2. Exploratory Data Analysis (EDA)
Analyzed:
- Purchase and non-purchase distribution.
- Sales and revenue patterns.
- Product category performance.
- Marketing channel performance.
- Shopping journey and cart abandonment.
- Customer purchasing behaviour.

### 3. RFM Analysis
Created three customer-level features:

- **Recency:** Number of days since the customer's most recent purchase.
- **Frequency:** Total number of purchases made by the customer.
- **Monetary:** Total amount spent by the customer.

A total of 4,176 purchasing customers were considered for RFM-based segmentation.

### 4. Customer Segmentation
Applied K-Means clustering to group customers based on their RFM characteristics.

- Number of clusters: 5
- Random state: 42
- Number of initializations: 10

Agglomerative clustering was also implemented for comparison.

### 5. Model Evaluation
Compared clustering models using:

- Silhouette Score
- Davies-Bouldin Index
- Calinski-Harabasz Index

PCA was used to reduce the three RFM dimensions into two components for visualization, retaining **85.32% of the explained variance**.

### 6. Interactive Dashboard
Developed a Streamlit dashboard to present the project's analytical findings, customer segmentation results, and business insights.

## Key Results

### Dataset Insights

| Metric | Result |
|---|---:|
| Total Sessions | 25,000 |
| Total Customers | 8,442 |
| Purchase Sessions | 5,616 |
| Purchase Rate | 22.46% |
| Cart Additions | 16,117 |
| Cart Abandonment Rate | 65.15% |
| Total Revenue | 10,116,169.06 |

### Customer Segments

The final K-Means model identified five customer segments:

| Customer Segment | Customers |
|---|---:|
| High-Value Frequent Customers | 324 |
| Recent One-Time Customers | 1,369 |
| Repeat Customers | 759 |
| Inactive / At-Risk Customers | 1,248 |
| High-Spending At-Risk Customers | 476 |
| **Total** | **4,176** |

### Clustering Model Comparison

| Evaluation Metric | K-Means (K=2) | K-Means (K=5) | Agglomerative (K=5) |
|---|---:|---:|---:|
| Silhouette Score | 0.4191 | 0.3992 | 0.3444 |
| Davies-Bouldin Index | 1.0859 | 0.9688 | 1.1261 |
| Calinski-Harabasz Index | 2540.67 | 2622.59 | 2220.34 |

K-Means with five clusters was selected to obtain more detailed and actionable customer segments. It achieved the lowest Davies-Bouldin Index and highest Calinski-Harabasz Index among the three compared models.

## Business Recommendations

| Customer Segment | Recommended Strategy |
|---|---|
| High-Value Frequent Customers | Loyalty rewards and
