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
| High-Value Frequent Customers | Loyalty rewards and personalized recommendations |
| Recent One-Time Customers | Second-purchase incentives |
| Repeat Customers | Retention campaigns and personalized offers |
| Inactive / At-Risk Customers | Re-engagement campaigns |
| High-Spending At-Risk Customers | Personalized win-back offers |

## Project Structure

```text
RetailIQ/
│
├── Ecommerce.csv
├── RetailIQ_Implementation.ipynb
├── app.py
│
├── RetailIQ_Graphs/
│
├── RetailIQ_Model_Comparison.csv
├── RetailIQ_Feature_Set_Comparison.csv
├── RetailIQ_Customer_Segments.csv
├── RetailIQ_Segment_Summary.csv
├── RetailIQ_Business_Recommendations.csv
│
└── README.md
```

*Note: Update this structure to match the actual files and folders in your GitHub repository.*

## How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/VishnuPriyaKodali/KLH-CSE-2026-27-2420030630-RetailIQ-Full-Cycle-E-Commerce-Customer-Sales-Analytics
```

### Step 2: Navigate to the Project Folder

```bash
cd RetailIQ
```

### Step 3: Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit jupyter
```

### Step 4: Run the Jupyter Notebook

```bash
jupyter notebook RetailIQ_Implementation.ipynb
```

Run the notebook cells to explore the data analysis and machine learning workflow.

### Step 5: Launch the Streamlit Dashboard

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

**Dataset Note:** Place `Ecommerce.csv` in the expected project location before running the notebook or dashboard. Check the file paths in the code if your folder structure differs.

## Future Scope

- Integrating real-time e-commerce data.
- Exploring additional customer segmentation techniques.
- Improving prediction and recommendation capabilities.
- Extending the dashboard with more interactive analytical features.

## Conclusion

RetailIQ demonstrates a complete data analytics and machine learning workflow for understanding e-commerce customer behaviour and sales performance. By combining exploratory analysis, RFM-based customer segmentation, clustering model evaluation, and an interactive dashboard, the project provides useful insights that can support data-driven business decisions.

## Project Team

- Vishnu Priya Kodali
- Ivaturi Vennela
- Lakshman Angara

**Institution:** Koneru Lakshmaiah Education Foundation

**Academic Year:** 2026–2027
