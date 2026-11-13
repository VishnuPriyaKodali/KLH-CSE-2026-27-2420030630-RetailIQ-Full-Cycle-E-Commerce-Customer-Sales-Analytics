import os
import streamlit as st
import pandas as pd

# --------------------------------------------------
# 1. PAGE SETTINGS
# --------------------------------------------------
st.set_page_config(
    page_title="RetailIQ | Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# 2. THEME AND STYLING
# --------------------------------------------------
st.markdown("""
<style>
.stApp {
    background: #EDE9FE;
    color: #292653;
}

.block-container {
    padding-top: 1.8rem;
    padding-bottom: 2rem;
    max-width: 1500px;
}

[data-testid="stSidebar"] {
    background: #292653 !important;
    border-right: 1px solid #45416F;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

[data-testid="stSidebar"] hr {
    border-color: #625C91 !important;
}

h1 {
    color: #292653 !important;
    font-size: 2rem !important;
    line-height: 1.25 !important;
}

h2 {
    color: #292653 !important;
    font-size: 1.35rem !important;
    line-height: 1.3 !important;
}

h3,
.stMarkdown h3 {
    color: #292653 !important;
    font-size: 1.05rem !important;
    line-height: 1.35 !important;
    font-weight: 650 !important;
    margin-top: 0.35rem !important;
    margin-bottom: 0.55rem !important;
    overflow-wrap: normal !important;
    word-break: normal !important;
}

p, li {
    color: #514A79;
}

[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid #D8CCFF;
    border-radius: 14px;
    padding: 20px 24px;
    min-height: 120px;
    box-shadow: 0 4px 14px rgba(41, 38, 83, 0.07);
    overflow-wrap: anywhere;
}

[data-testid="stMetricLabel"] {
    color: #6D6595 !important;
    font-size: 15px !important;
}

[data-testid="stMetricValue"] {
    color: #6554C0 !important;
    font-size: clamp(22px, 2.4vw, 32px) !important;
    font-weight: 700;
    white-space: normal !important;
    overflow-wrap: anywhere;
}

[data-testid="stDataFrame"] {
    background: #FFFFFF;
    border: 1px solid #D8CCFF;
    border-radius: 10px;
}

.stButton button {
    background: #6554C0;
    color: #FFFFFF;
    border: none;
    border-radius: 8px;
}

.stButton button:hover {
    background: #51429E;
    color: #FFFFFF;
}

[data-testid="stExpander"] {
    background: #FFFFFF;
    border: 1px solid #D8CCFF;
    border-radius: 10px;
}

hr {
    border-color: #D8CCFF;
}

.workflow-container {
    display: grid;
    grid-template-columns: repeat(5, minmax(0, 1fr));
    gap: 12px;
    width: 100%;
}

.workflow-step {
    background: #FFFFFF;
    border: 1px solid #D8CCFF;
    border-radius: 14px;
    padding: 18px 6px;
    text-align: center;
    min-width: 0;
    box-sizing: border-box;
    box-shadow: 0 4px 12px rgba(41, 38, 83, 0.05);
}

.workflow-number {
    color: #6554C0;
    font-size: 23px;
    font-weight: 700;
    margin-bottom: 10px;
}

.workflow-label {
    color: #292653;
    font-size: 13px;
    font-weight: 600;
    line-height: 1.4;
    white-space: nowrap;
}

.chart-heading {
    color: #292653;
    font-size: 1.05rem;
    font-weight: 650;
    line-height: 1.35;
    margin-top: 0.35rem;
    margin-bottom: 0.65rem;
    overflow-wrap: normal;
    word-break: normal;
}

@media (max-width: 900px) {
    .workflow-container {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .workflow-label {
        white-space: normal;
    }

    h3, .stMarkdown h3 {
        font-size: 1rem !important;
    }

    .chart-heading {
        font-size: 0.98rem;
    }
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# 3. FILE LOCATIONS
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(BASE_DIR, "Ecommerce.csv")
SEGMENTS_FILE = os.path.join(
    BASE_DIR, "RetailIQ_Customer_Segments.csv"
)
SUMMARY_FILE = os.path.join(
    BASE_DIR, "RetailIQ_Segment_Summary.csv"
)
RECOMMENDATIONS_FILE = os.path.join(
    BASE_DIR, "RetailIQ_Business_Recommendations.csv"
)
MODEL_FILE = os.path.join(
    BASE_DIR, "RetailIQ_Model_Comparison.csv"
)
FEATURE_FILE = os.path.join(
    BASE_DIR, "RetailIQ_Feature_Set_Comparison.csv"
)
GRAPH_DIR = os.path.join(BASE_DIR, "RetailIQ_Graphs")


# --------------------------------------------------
# 4. LOAD DATA
# --------------------------------------------------
@st.cache_data
def load_csv(path):
    if os.path.exists(path):
        try:
            return pd.read_csv(path)
        except Exception:
            return pd.DataFrame()
    return pd.DataFrame()


df = load_csv(DATA_FILE)
segments = load_csv(SEGMENTS_FILE)
segment_summary = load_csv(SUMMARY_FILE)
recommendations = load_csv(RECOMMENDATIONS_FILE)
model_comparison = load_csv(MODEL_FILE)
feature_comparison = load_csv(FEATURE_FILE)


# --------------------------------------------------
# 5. HELPER FUNCTIONS
# --------------------------------------------------
def find_column(data, possible_names):
    if data.empty:
        return None

    lookup = {
        str(col).strip().lower(): col
        for col in data.columns
    }

    for name in possible_names:
        key = name.strip().lower()
        if key in lookup:
            return lookup[key]

    return None


def money(value):
    # Display monetary values with the dollar symbol.
    try:
        if pd.isna(value):
            return "N/A"
        return f"₹{float(value):,.2f}"
    except (ValueError, TypeError):
        return "N/A"


def percent(value):
    try:
        if pd.isna(value):
            return "N/A"
        return f"{float(value):.2f}%"
    except (ValueError, TypeError):
        return "N/A"


def show_table(data):
    if data.empty:
        st.info("This file is unavailable or contains no data.")
    else:
        st.dataframe(
            data,
            width="stretch",
            hide_index=True
        )


def show_graph(path, caption=None):
    if os.path.exists(path):
        st.image(path, width="stretch")
        if caption:
            st.caption(caption)
    else:
        st.warning(
            f"Graph not found: {os.path.basename(path)}"
        )


def show_chart_title(title, description=None):
    st.markdown(
        f'<div class="chart-heading">{title}</div>',
        unsafe_allow_html=True
    )

    if description:
        st.caption(description)


# --------------------------------------------------
# 6. BUSINESS METRICS
# --------------------------------------------------
total_sessions = len(df)

customer_col = find_column(
    df, ["customer_id", "customerid", "customer"]
)
purchase_col = find_column(
    df, ["purchased", "purchase", "purchase_status"]
)
revenue_col = find_column(
    df, ["revenue", "purchase_amount", "amount"]
)
cart_col = find_column(
    df, ["added_to_cart", "cart_added", "add_to_cart"]
)

unique_customers = (
    df[customer_col].nunique()
    if customer_col is not None else 0
)

purchases = 0
purchase_rate = 0.0
total_revenue = 0.0
average_purchase_revenue = 0.0
cart_additions = 0
abandoned_carts = 0
abandonment_rate = 0.0
purchased_mask = pd.Series(False, index=df.index)

if purchase_col is not None:
    raw_purchase = df[purchase_col]

    if pd.api.types.is_numeric_dtype(raw_purchase):
        purchase_values = pd.to_numeric(
            raw_purchase, errors="coerce"
        ).fillna(0)
        purchased_mask = purchase_values == 1
    else:
        purchased_mask = raw_purchase.astype(str).str.strip().str.lower().isin(
            ["1", "true", "yes", "purchased", "purchase"]
        )

    purchases = int(purchased_mask.sum())

    if total_sessions > 0:
        purchase_rate = purchases / total_sessions * 100

if revenue_col is not None:
    revenue_values = pd.to_numeric(
        df[revenue_col], errors="coerce"
    ).fillna(0)

    total_revenue = revenue_values.sum()

    purchased_revenues = revenue_values[purchased_mask]

    if len(purchased_revenues) > 0:
        average_purchase_revenue = purchased_revenues.mean()

if cart_col is not None:
    raw_cart = df[cart_col]

    if pd.api.types.is_numeric_dtype(raw_cart):
        cart_values = pd.to_numeric(
            raw_cart, errors="coerce"
        ).fillna(0)
        cart_mask = cart_values == 1
    else:
        cart_mask = raw_cart.astype(str).str.strip().str.lower().isin(
            ["1", "true", "yes", "added", "added to cart"]
        )

    cart_additions = int(cart_mask.sum())

    if purchase_col is not None:
        abandoned_carts = int(
            (cart_mask & ~purchased_mask).sum()
        )

        if cart_additions > 0:
            abandonment_rate = (
                abandoned_carts / cart_additions * 100
            )


# --------------------------------------------------
# 7. SIDEBAR
# --------------------------------------------------
with st.sidebar:

    st.markdown("# RetailIQ")
    st.markdown("E-Commerce Intelligence")

    st.divider()

    page = st.radio(
        "PROJECT MODULES",
        [
            "Project Overview",
            "Data Preprocessing",
            "Exploratory Data Analysis",
            "RFM Analysis",
            "Customer Segmentation",
            "Model Evaluation",
            "Feature Comparison",
            "Business Recommendations"
        ]
    )

    st.divider()
    st.caption("DATA SCIENCE PROJECT")
    st.caption("Customer & Sales Analytics")


# --------------------------------------------------
# 8. PROJECT OVERVIEW
# --------------------------------------------------
if page == "Project Overview":

    st.title("RetailIQ Dashboard")
    st.write("Full-Cycle E-Commerce Customer & Sales Analytics")

    st.markdown(
        "Monitor business performance, explore customer "
        "behaviour, evaluate customer segments, and identify "
        "actionable insights."
    )

    st.divider()

    k1, k2 = st.columns(2)
    k1.metric("Total Revenue", money(total_revenue))
    k2.metric("Total Sessions", f"{total_sessions:,}")

    k3, k4 = st.columns(2)
    k3.metric("Unique Customers", f"{unique_customers:,}")
    k4.metric("Purchases", f"{purchases:,}")

    k5, k6 = st.columns(2)
    k5.metric("Purchase Rate", percent(purchase_rate))
    k6.metric(
        "Average Revenue per Purchase",
        money(average_purchase_revenue)
    )

    k7, k8 = st.columns(2)
    k7.metric("Cart Additions", f"{cart_additions:,}")
    k8.metric(
        "Cart Abandonment Rate",
        percent(abandonment_rate)
    )

    st.divider()

    left, right = st.columns(2, gap="large")

    with left:
        show_chart_title("Monthly Revenue")
        show_graph(
            os.path.join(
                GRAPH_DIR, "02_monthly_revenue_trend.png"
            )
        )

    with right:
        show_chart_title("Monthly Purchases")
        show_graph(
            os.path.join(
                GRAPH_DIR, "03_monthly_purchase_trend.png"
            )
        )

    left, right = st.columns(2, gap="large")

    with left:
        show_chart_title("Shopping Funnel")
        show_graph(
            os.path.join(
                GRAPH_DIR, "08_shopping_journey_funnel.png"
            )
        )

    with right:
        show_chart_title("Channel Performance")
        show_graph(
            os.path.join(
                GRAPH_DIR, "05_marketing_channel_performance.png"
            )
        )

    st.divider()
    show_chart_title("Project Workflow")

    st.markdown("""
    <div class="workflow-container">
        <div class="workflow-step">
            <div class="workflow-number">01</div>
            <div class="workflow-label">Data Collection</div>
        </div>
        <div class="workflow-step">
            <div class="workflow-number">02</div>
            <div class="workflow-label">Preprocessing</div>
        </div>
        <div class="workflow-step">
            <div class="workflow-number">03</div>
            <div class="workflow-label">EDA</div>
        </div>
        <div class="workflow-step">
            <div class="workflow-number">04</div>
            <div class="workflow-label">RFM &amp; Clustering</div>
        </div>
        <div class="workflow-step">
            <div class="workflow-number">05</div>
            <div class="workflow-label">Business Insights</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# 9. DATA PREPROCESSING
# --------------------------------------------------
elif page == "Data Preprocessing":

    st.title("Data Preprocessing")
    st.write(
        "Review the dataset and the preparation steps used "
        "before exploratory and customer-level analysis."
    )

    if df.empty:
        st.error("Ecommerce.csv could not be loaded.")
    else:
        duplicate_count = int(df.duplicated().sum())
        missing_count = int(df.isnull().sum().sum())

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Rows", f"{df.shape[0]:,}")
        c2.metric("Columns", f"{df.shape[1]:,}")
        c3.metric("Missing Values", f"{missing_count:,}")
        c4.metric("Duplicate Rows", f"{duplicate_count:,}")

        st.divider()
        show_chart_title("Dataset Preview")
        st.dataframe(df.head(10), width="stretch")

        left, right = st.columns(2, gap="large")

        with left:
            show_chart_title("Column Data Types")
            type_data = pd.DataFrame({
                "Column": df.columns,
                "Data Type": df.dtypes.astype(str).values
            })
            show_table(type_data)

        with right:
            show_chart_title("Missing Values")

            missing_data = df.isnull().sum().reset_index()
            missing_data.columns = [
                "Column", "Missing Values"
            ]
            missing_data = missing_data[
                missing_data["Missing Values"] > 0
            ]

            if missing_data.empty:
                st.success(
                    "No missing values found in the source dataset."
                )
            else:
                show_table(missing_data)

        st.divider()
        show_chart_title("Preprocessing Summary")

        st.markdown("""
        - Checked dataset structure and column data types.
        - Checked missing values and duplicate records.
        - Converted the visit date into a date format for time-based analysis.
        - Created additional features for exploratory analysis.
        - Prepared customer-level RFM features for segmentation.
        """)

        st.caption(
            "The source CSV is not modified by this dashboard."
        )


# --------------------------------------------------
# 10. EXPLORATORY DATA ANALYSIS
# --------------------------------------------------
elif page == "Exploratory Data Analysis":

    st.title("Exploratory Data Analysis")
    st.write(
        "Explore business performance, purchase behaviour, "
        "customer patterns, and clustering visualisations."
    )

    graph_files = [
        ("Overall Business Metrics", "01_overall_business_metrics.png"),
        ("Monthly Revenue", "02_monthly_revenue_trend.png"),
        ("Monthly Purchases", "03_monthly_purchase_trend.png"),
        ("Category Revenue", "04_category_revenue.png"),
        ("Channel Performance", "05_marketing_channel_performance.png"),
        ("Device Purchase Behaviour", "06_device_purchase_behavior.png"),
        ("Customer Type Purchase Rate", "07_customer_type_purchase_rate.png"),
        ("Shopping Funnel", "08_shopping_journey_funnel.png"),
        ("Correlation Heatmap", "09_numerical_correlation_heatmap.png"),
        ("Discount vs Revenue", "10_discount_vs_revenue.png"),
        ("Session Duration", "11_session_duration_distribution.png"),
        ("Duration by Purchase", "12_session_duration_by_purchase.png"),
        ("Category Purchase Counts", "13_category_purchase_counts.png"),
        ("Channel Conversion Rate", "14_marketing_channel_conversion_rate.png"),
        ("Purchase Revenue Boxplot", "15_purchase_revenue_boxplot.png"),
        ("Pages by Purchase Outcome", "16_pages_viewed_by_purchase_outcome.png"),
        ("Seasonal Purchase Rate", "17_seasonal_purchase_rate.png"),
        ("Numerical Distributions", "18_univariate_numerical_distributions.png"),
        ("Categorical Distributions", "19_categorical_variable_distributions.png"),
        ("Shopping Behaviour", "20_shopping_behavior_distributions.png"),
        ("Pages vs Time by Purchase", "21_pages_vs_time_by_purchase.png"),
        ("Discount vs Purchase Rate", "22_discount_vs_purchase_rate.png"),
        ("Device Purchase Heatmap", "23_customer_device_purchase_heatmap.png"),
        ("Channel Purchase Heatmap", "24_channel_customer_purchase_heatmap.png"),
        ("RFM Distributions", "25_rfm_distributions.png"),
        ("Cluster Selection", "26_optimal_cluster_selection.png"),
        ("Segment Profiles", "27_customer_segment_profiles.png"),
        ("Revenue by Segment", "28_cluster_revenue_contribution.png"),
        ("RFM Clusters", "29_rfm_clusters_pca.png")
    ]

    available_graphs = [
        item for item in graph_files
        if os.path.exists(os.path.join(GRAPH_DIR, item[1]))
    ]

    if not available_graphs:
        st.warning(
            "No EDA graph files were found in RetailIQ_Graphs."
        )
    else:
        selected_graph = st.selectbox(
            "Choose a graph to explore",
            available_graphs,
            format_func=lambda item: item[0]
        )

        show_graph(
            os.path.join(GRAPH_DIR, selected_graph[1]),
            selected_graph[0]
        )

        st.divider()
        show_chart_title("More Visualisations")

        remaining_graphs = [
            item for item in available_graphs
            if item != selected_graph
        ]

        for i in range(0, len(remaining_graphs), 2):
            left, right = st.columns(2, gap="large")

            with left:
                title, filename = remaining_graphs[i]
                with st.expander(title):
                    show_graph(
                        os.path.join(GRAPH_DIR, filename)
                    )

            if i + 1 < len(remaining_graphs):
                with right:
                    title, filename = remaining_graphs[i + 1]
                    with st.expander(title):
                        show_graph(
                            os.path.join(GRAPH_DIR, filename)
                        )


# --------------------------------------------------
# 11. RFM ANALYSIS
# --------------------------------------------------
elif page == "RFM Analysis":

    st.title("RFM Analysis")
    st.write(
        "RFM analysis evaluates customers using Recency, "
        "Frequency, and Monetary value."
    )

    c1, c2, c3 = st.columns(3, gap="large")

    with c1:
        show_chart_title("Recency")
        st.write("How recently did the customer purchase?")

    with c2:
        show_chart_title("Frequency")
        st.write("How often did the customer purchase?")

    with c3:
        show_chart_title("Monetary")
        st.write("How much revenue did the customer generate?")

    st.divider()
    show_chart_title("RFM Distributions")
    show_graph(
        os.path.join(GRAPH_DIR, "25_rfm_distributions.png")
    )

    st.divider()
    show_chart_title("Customer Records")

    if not segments.empty:
        st.dataframe(
            segments.head(100),
            width="stretch"
        )
        st.caption(
            "Showing up to 100 rows for readability. "
            "The full dataset remains in the CSV file."
        )
    else:
        st.warning(
            "RetailIQ_Customer_Segments.csv was not found."
        )


# --------------------------------------------------
# 12. CUSTOMER SEGMENTATION
# --------------------------------------------------
elif page == "Customer Segmentation":

    st.title("Customer Segmentation")
    st.write(
        "Group customers using RFM features to identify "
        "purchasing patterns and business opportunities."
    )

    st.divider()
    show_chart_title("Segment Profiles")
    show_graph(
        os.path.join(
            GRAPH_DIR, "27_customer_segment_profiles.png"
        )
    )

    left, right = st.columns(2, gap="large")

    with left:
        show_chart_title("Revenue by Segment")
        show_graph(
            os.path.join(
                GRAPH_DIR, "28_cluster_revenue_contribution.png"
            )
        )

    with right:
        show_chart_title("RFM Clusters")
        show_graph(
            os.path.join(GRAPH_DIR, "29_rfm_clusters_pca.png")
        )

    # Segment Summary: display as a table like other dashboard tables.
    st.divider()
    show_chart_title("Segment Summary")

    
    if not segment_summary.empty:

        display_summary = segment_summary.reset_index(drop=True).copy()

        for col in display_summary.columns:
            col_name = str(col).lower().replace("_", " ").strip()

            if "monetary" in col_name or "revenue" in col_name:
                display_summary[col] = display_summary[col].apply(
                    lambda value: (
                        f"₹{float(value):,.2f}"
                        if pd.notna(value)
                        else "N/A"
                    )
                )

        st.dataframe(
            display_summary,
            width="stretch",
            hide_index=True
        )

        summary_segment_col = find_column(
            segment_summary,
            [
                "segment",
                "segment_name",
                "customer_segment",
                "customer_type",
                "cluster",
                "cluster_label"
            ]
        )

        summary_count_col = find_column(
            segment_summary,
            [
                "customer_count",
                "customers",
                "count",
                "number_of_customers",
                "total_customers",
                "customer_total",
                "size"
            ]
        )

        # Prepare customer distribution data for the chart.
        chart_data = pd.DataFrame()

        if (
            summary_segment_col is not None
            and summary_count_col is not None
        ):
            chart_data = segment_summary[
                [summary_segment_col, summary_count_col]
            ].copy()

        elif not segments.empty:
            records_segment_col = find_column(
                segments,
                [
                    "segment",
                    "segment_name",
                    "customer_segment",
                    "customer_type",
                    "cluster",
                    "cluster_label"
                ]
            )

            if records_segment_col is not None:
                chart_data = (
                    segments[records_segment_col]
                    .fillna("Unknown")
                    .astype(str)
                    .value_counts()
                    .rename_axis("Customer Segment")
                    .reset_index(name="Customer Count")
                )

                summary_segment_col = "Customer Segment"
                summary_count_col = "Customer Count"

        if not chart_data.empty:

            chart_data[summary_count_col] = pd.to_numeric(
                chart_data[summary_count_col],
                errors="coerce"
            )

            chart_data = chart_data.dropna(
                subset=[summary_count_col]
            )

            if not chart_data.empty:
                chart_data = chart_data.set_index(
                    summary_segment_col
                )

                st.markdown("**Customer Distribution by Segment**")

                # Fixed-height vertical chart.
                st.bar_chart(
                    chart_data[summary_count_col],
                    horizontal=False,
                    width="stretch",
                    height=400
                )
            else:
                st.info(
                    "Customer counts are not available "
                    "for the segment distribution chart."
                )
        else:
            st.info(
                "A segment column and customer counts "
                "could not be identified for the chart."
            )

    else:
        st.warning(
            "RetailIQ_Segment_Summary.csv was not found."
        )

    # Customer Records: filter records by customer segment.
    st.divider()
    show_chart_title("Customer Records")

    if not segments.empty:

        records_segment_col = find_column(
            segments,
            [
                "segment",
                "segment_name",
                "customer_segment",
                "customer_type",
                "cluster",
                "cluster_label"
            ]
        )

        filtered_segments = segments.copy()

        if records_segment_col is not None:

            segment_options = (
                filtered_segments[records_segment_col]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

            segment_options = sorted(segment_options)

            selected_segment = st.selectbox(
                "Filter customers by segment",
                ["All Segments"] + segment_options,
                key="customer_segment_filter"
            )

            if selected_segment != "All Segments":
                filtered_segments = filtered_segments[
                    filtered_segments[records_segment_col]
                    .astype(str) == selected_segment
                ]

        else:
            st.info(
                "A segment column was not identified. "
                "Showing all customer records."
            )

        st.caption(
            f"Matching customer records: "
            f"{len(filtered_segments):,}"
        )

        # Display up to 100 matching records in a table.
        display_records = filtered_segments.head(100)

        if not display_records.empty:
            st.table(display_records.reset_index(drop=True))

            if len(filtered_segments) > 100:
                st.caption(
                    "Showing the first 100 matching records. "
                    "The original CSV contains the complete dataset."
                )
        else:
            st.info(
                "No customer records were found for this segment."
            )

    else:
        st.warning(
            "Customer segment records are not available."
        )


# --------------------------------------------------
# 13. MODEL EVALUATION
# --------------------------------------------------
elif page == "Model Evaluation":

    st.title("Model Evaluation")
    st.write(
        "Review clustering performance and the saved "
        "model-comparison results."
    )

    st.markdown("""
    - **Silhouette Score:** Higher values generally indicate better-separated clusters.
    - **Davies–Bouldin Index:** Lower values generally indicate better cluster separation.
    - **Calinski–Harabasz Score:** Higher values generally indicate denser, better-separated clusters.
    """)

    st.divider()
    show_chart_title("Cluster Selection")
    show_graph(
        os.path.join(
            GRAPH_DIR, "26_optimal_cluster_selection.png"
        )
    )

    st.divider()
    show_chart_title("Model Comparison")

    if not model_comparison.empty:
        show_table(model_comparison)
    else:
        st.warning(
            "RetailIQ_Model_Comparison.csv was not found."
        )
    st.divider()
    show_chart_title("Cluster Selection")
    show_graph(
        os.path.join(
            GRAPH_DIR, "26_optimal_cluster_selection.png"
        )
    )

    st.divider()
    show_chart_title("Model Comparison")

    if not model_comparison.empty:
        show_table(model_comparison)
    else:
        st.warning(
            "RetailIQ_Model_Comparison.csv was not found."
        )
    st.divider()
    show_chart_title("Evaluation Metrics Comparison")

    col1, col2 = st.columns(2)

    with col1:
        show_chart_title("Silhouette Score")
        show_graph(
            os.path.join(GRAPH_DIR, "30_model_comparison_silhouette.png")
        )

    with col2:
        show_chart_title("Davies-Bouldin Index")
        show_graph(
            os.path.join(GRAPH_DIR, "31_model_comparison_davies_bouldin.png")
        )

    show_chart_title("Calinski-Harabasz Score")
    show_graph(
        os.path.join(GRAPH_DIR, "32_model_comparison_calinski_harabasz.png")
    )


    st.info(
    "The final customer segmentation uses K-Means with five clusters "
    "on the original, uncapped RFM features. A separate experiment "
    "tested capped Frequency and Monetary values to assess sensitivity "
    "to extreme values. The results showed modest, mixed changes in "
    "evaluation metrics, so the original model was retained."
    )

    st.caption(
    "Five clusters were selected for more detailed, actionable "
    "customer groups. This is a business-oriented choice and does "
    "not mean K=5 performs best under every evaluation metric."
    )


# --------------------------------------------------
# 14. FEATURE COMPARISON
# --------------------------------------------------
elif page == "Feature Comparison":

    st.title("Feature Set Comparison")
    st.write(
        "Compare clustering performance using RFM features "
        "and shopping-behaviour features."
    )

    st.divider()

    if not feature_comparison.empty:
        show_table(feature_comparison)
    else:
        st.warning(
            "RetailIQ_Feature_Set_Comparison.csv was not found."
        )

    st.divider()
    left, right = st.columns(2, gap="large")

    with left:
        show_chart_title("RFM Features")
        st.write(
            "Recency, Frequency, and Monetary value describe "
            "the customer's purchasing history."
        )

    with right:
        show_chart_title("Shopping Behaviour")
        st.write(
            "Average pages viewed, average time on site, "
            "and cart addition rate describe session behaviour."
        )

    st.divider()
    show_chart_title("Segment Profiles")
    show_graph(
        os.path.join(
            GRAPH_DIR, "27_customer_segment_profiles.png"
        )
    )

    st.info(
        "The recorded experiment reported stronger clustering "
        "results for the RFM feature set across the three evaluated "
        "metrics. This describes the tested feature sets only."
    )


# --------------------------------------------------
# 15. BUSINESS RECOMMENDATIONS
# --------------------------------------------------
elif page == "Business Recommendations":

    st.title("Business Recommendations")
    st.write(
        "Suggested actions based on purchasing patterns "
        "identified by customer segmentation."
    )

    st.divider()

    if not recommendations.empty:
        show_table(recommendations)

        st.divider()
        show_chart_title("Recommendation Details")

        for _, row in recommendations.iterrows():
            with st.expander(str(row.iloc[0])):
                for column in recommendations.columns[1:]:
                    st.markdown(
                        f"**{column.replace('_', ' ').title()}**"
                    )
                    st.write(str(row[column]))

    else:
        actions = [
            (
                "High-Value Frequent Customers",
                "Offer loyalty rewards and personalised product recommendations."
            ),
            (
                "High-Spending At-Risk Customers",
                "Use targeted win-back offers and relevant product reminders."
            ),
            (
                "Inactive / At-Risk Customers",
                "Try re-engagement campaigns and carefully targeted incentives."
            ),
            (
                "Repeat Customers",
                "Encourage bundles, complementary products, and cross-selling."
            ),
            (
                "Recent One-Time Customers",
                "Send relevant follow-up recommendations and second-purchase offers."
            )
        ]

        for title, description in actions:
            with st.container(border=True):
                show_chart_title(title)
                st.write(description)

    st.divider()
    st.caption(
        "These are proposed business actions based on historical data. "
        "Their actual effectiveness would need to be tested."
    )


# --------------------------------------------------
# 16. FOOTER
# --------------------------------------------------
st.divider()

st.caption(
    "RetailIQ | E-Commerce Customer & Sales Analytics | "
    "Data Science Project"
)