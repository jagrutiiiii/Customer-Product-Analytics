import pandas as pd

# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_csv("../Data/Ecommerce_Cleaned.csv")

print("Original dataset shape:", df.shape)


# # ==========================================
# # 2. CONVERT DATE
# # ==========================================

# df["visit_date"] = pd.to_datetime(
#     df["visit_date"],
#     format="%d-%m-%Y"
# )


# # ==========================================
# # 3. CHECK FOR MISSING VALUES
# # ==========================================

# print("\nMissing values:")
# print(df.isnull().sum().sum())


# # ==========================================
# # 4. CHECK FOR DUPLICATES
# # ==========================================

# print("\nDuplicate rows:")
# print(df.duplicated().sum())


# # ==========================================
# # 5. CREATE USEFUL DATE COLUMNS
# # ==========================================

# df["year"] = df["visit_date"].dt.year
# df["month"] = df["visit_date"].dt.month
# df["month_name"] = df["visit_date"].dt.strftime("%B")
# df["day"] = df["visit_date"].dt.day
# df["weekday"] = df["visit_date"].dt.day_name()


# # ==========================================
# # 6. CREATE PURCHASE STATUS
# # ==========================================

# df["purchase_status"] = df["purchased"].map({
#     0: "Not Purchased",
#     1: "Purchased"
# })


# # ==========================================
# # 7. CREATE CART STATUS
# # ==========================================

# df["cart_status"] = df["cart_abandoned"].map({
#     0: "Not Abandoned",
#     1: "Abandoned"
# })


# # ==========================================
# # 8. CREATE CART ADDITION STATUS
# # ==========================================

# df["cart_add_status"] = df["added_to_cart"].map({
#     0: "Not Added",
#     1: "Added"
# })


# # ==========================================
# # 9. CREATE CUSTOMER VALUE
# # ==========================================

# df["customer_value"] = pd.cut(
#     df["revenue"],
#     bins=[-1, 0, 500, 1500, float("inf")],
#     labels=["No Purchase", "Low Value", "Medium Value", "High Value"]
# )


# # ==========================================
# # 10. CREATE DISCOUNT CATEGORY
# # ==========================================

# df["discount_category"] = pd.cut(
#     df["discount_percent"],
#     bins=[-1, 0, 10, 20, 30],
#     labels=["No Discount", "Low Discount", "Medium Discount", "High Discount"]
# )


# # ==========================================
# # 11. CREATE TIME SPENT IN MINUTES
# # ==========================================

# df["time_on_site_min"] = df["time_on_site_sec"] / 60


# # ==========================================
# # 12. SAVE CLEANED DATA
# # ==========================================

# df.to_csv("../Data/Ecommerce_Cleaned.csv", index=False)


# # ==========================================
# # 13. FINAL CHECK
# # ==========================================

# print("\nCleaned dataset shape:")
# print(df.shape)

# print("\nNew columns:")
# print(df.columns.tolist())

# print("\nFirst 5 rows of cleaned data:")
# print(df.head())

# print("\nCleaned dataset saved successfully!")


# ==========================================
# EXPLORATORY DATA ANALYSIS
# ==========================================

print("\n" + "=" * 50)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 50)


# ==========================================
# 1. BUSINESS OVERVIEW
# ==========================================

total_sessions = df["session_id"].nunique()
total_customers = df["customer_id"].nunique()
total_products = df["product_id"].nunique()

total_revenue = df["revenue"].sum()
total_quantity = df["quantity"].sum()
total_purchases = df["purchased"].sum()

print("\n--- BUSINESS OVERVIEW ---")
print("Total Sessions:", total_sessions)
print("Unique Customers:", total_customers)
print("Unique Products:", total_products)
print("Total Revenue:", round(total_revenue, 2))
print("Total Quantity Sold:", total_quantity)
print("Total Purchases:", total_purchases)


# ==========================================
# 2. PURCHASE RATE
# ==========================================

purchase_rate = (total_purchases / total_sessions) * 100

print("\n--- PURCHASE PERFORMANCE ---")
print("Purchase Rate:", round(purchase_rate, 2), "%")


# ==========================================
# 3. CART BEHAVIOR
# ==========================================

total_cart_additions = df["added_to_cart"].sum()
total_cart_abandoned = df["cart_abandoned"].sum()

print("\n--- CART BEHAVIOR ---")
print("Cart Additions:", total_cart_additions)
print("Cart Abandoned:", total_cart_abandoned)


# ==========================================
# 4. AVERAGE ORDER VALUE
# ==========================================

purchased_orders = df[df["purchased"] == 1]

average_order_value = purchased_orders["revenue"].mean()

print("\n--- REVENUE METRICS ---")
print("Average Order Value:", round(average_order_value, 2))


# ==========================================
# 5. CUSTOMER SPENDING
# ==========================================

customer_spending = (
    df.groupby("customer_id")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- CUSTOMER SPENDING ---")
print("Average Customer Revenue:",
      round(customer_spending.mean(), 2))

print("Highest Customer Revenue:",
      round(customer_spending.max(), 2))

print("\nTop 10 Customers:")
print(customer_spending.head(10))


# ==========================================
# 6. REVENUE BY PRODUCT CATEGORY
# ==========================================

category_revenue = (
    df.groupby("product_category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- REVENUE BY PRODUCT CATEGORY ---")
print(category_revenue)


# ==========================================
# 7. QUANTITY BY PRODUCT CATEGORY
# ==========================================

category_quantity = (
    df.groupby("product_category")["quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- QUANTITY BY PRODUCT CATEGORY ---")
print(category_quantity)


# ==========================================
# 8. TOP PRODUCTS
# ==========================================

product_revenue = (
    df.groupby("product_id")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- TOP 10 PRODUCTS BY REVENUE ---")
print(product_revenue.head(10))


# ==========================================
# 9. MONTHLY REVENUE
# ==========================================

monthly_revenue = (
    df.groupby("month")["revenue"]
    .sum()
)

print("\n--- MONTHLY REVENUE ---")
print(monthly_revenue)


# ==========================================
# 10. DEVICE PERFORMANCE
# ==========================================

device_analysis = (
    df.groupby("device_type")
    .agg(
        sessions=("session_id", "count"),
        purchases=("purchased", "sum"),
        revenue=("revenue", "sum")
    )
)

print("\n--- DEVICE PERFORMANCE ---")
print(device_analysis)


# ==========================================
# 11. MARKETING CHANNEL PERFORMANCE
# ==========================================

channel_analysis = (
    df.groupby("marketing_channel")
    .agg(
        sessions=("session_id", "count"),
        purchases=("purchased", "sum"),
        revenue=("revenue", "sum")
    )
    .sort_values("revenue", ascending=False)
)

print("\n--- MARKETING CHANNEL PERFORMANCE ---")
print(channel_analysis)


# ==========================================
# 12. PAYMENT METHOD ANALYSIS
# ==========================================

payment_analysis = (
    df.groupby("payment_method")
    .agg(
        transactions=("purchased", "sum"),
        revenue=("revenue", "sum")
    )
    .sort_values("revenue", ascending=False)
)

print("\n--- PAYMENT METHOD ANALYSIS ---")
print(payment_analysis)


# ==========================================
# 13. DISCOUNT ANALYSIS
# ==========================================

discount_analysis = (
    df.groupby("discount_category")
    .agg(
        sessions=("session_id", "count"),
        purchases=("purchased", "sum"),
        revenue=("revenue", "sum")
    )
)

print("\n--- DISCOUNT ANALYSIS ---")
print(discount_analysis)


# ==========================================
# 14. CUSTOMER TYPE ANALYSIS
# ==========================================

user_analysis = (
    df.groupby("user_type")
    .agg(
        sessions=("session_id", "count"),
        purchases=("purchased", "sum"),
        revenue=("revenue", "sum")
    )
)

print("\n--- USER TYPE ANALYSIS ---")
print(user_analysis)


# ==================================================
# DEEPER BUSINESS ANALYSIS
# ==================================================

print("\n" + "=" * 50)
print("DEEPER BUSINESS ANALYSIS")
print("=" * 50)


# --------------------------------------------------
# 1. CONVERSION RATE BY DEVICE
# --------------------------------------------------

device_analysis = (
    df.groupby("device_type")
    .agg(
        sessions=("session_id", "count"),
        purchases=("purchased", "sum"),
        revenue=("revenue", "sum")
    )
)

device_analysis["conversion_rate"] = (
    device_analysis["purchases"] / device_analysis["sessions"] * 100
)

print("\n--- CONVERSION RATE BY DEVICE ---")
print(device_analysis.round(2))


# --------------------------------------------------
# 2. CONVERSION RATE BY MARKETING CHANNEL
# --------------------------------------------------

channel_analysis = (
    df.groupby("marketing_channel")
    .agg(
        sessions=("session_id", "count"),
        purchases=("purchased", "sum"),
        revenue=("revenue", "sum")
    )
)

channel_analysis["conversion_rate"] = (
    channel_analysis["purchases"] / channel_analysis["sessions"] * 100
)

print("\n--- CONVERSION RATE BY MARKETING CHANNEL ---")
print(channel_analysis.round(2).sort_values("conversion_rate", ascending=False))


# --------------------------------------------------
# 3. CART ABANDONMENT RATE
# --------------------------------------------------

cart_additions = df["added_to_cart"].sum()
cart_abandoned = df["cart_abandoned"].sum()

cart_abandonment_rate = (
    cart_abandoned / cart_additions * 100
)

print("\n--- CART ABANDONMENT ---")
print("Cart Additions:", cart_additions)
print("Cart Abandoned:", cart_abandoned)
print("Cart Abandonment Rate:", round(cart_abandonment_rate, 2), "%")


# --------------------------------------------------
# 4. REVENUE CONTRIBUTION BY PRODUCT CATEGORY
# --------------------------------------------------

category_revenue = (
    df.groupby("product_category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

category_contribution = (
    category_revenue / category_revenue.sum() * 100
)

category_analysis = pd.DataFrame({
    "revenue": category_revenue,
    "revenue_contribution_percent": category_contribution
})

print("\n--- REVENUE CONTRIBUTION BY CATEGORY ---")
print(category_analysis.round(2))


# --------------------------------------------------
# 5. REVENUE PER SESSION
# --------------------------------------------------

revenue_per_session = df["revenue"].sum() / len(df)

print("\n--- REVENUE PER SESSION ---")
print("Revenue per Session: ₹", round(revenue_per_session, 2))


# --------------------------------------------------
# 6. REPEAT VS ONE-TIME CUSTOMERS
# --------------------------------------------------

customer_sessions = (
    df.groupby("customer_id")
    .agg(
        sessions=("session_id", "count"),
        purchases=("purchased", "sum"),
        revenue=("revenue", "sum")
    )
)

customer_sessions["customer_type"] = customer_sessions["sessions"].apply(
    lambda x: "One-Time Customer" if x == 1 else "Repeat Customer"
)

customer_type_analysis = (
    customer_sessions.groupby("customer_type")
    .agg(
        customers=("sessions", "count"),
        total_revenue=("revenue", "sum"),
        total_purchases=("purchases", "sum")
    )
)

customer_type_analysis["average_revenue_per_customer"] = (
    customer_type_analysis["total_revenue"] /
    customer_type_analysis["customers"]
)

print("\n--- REPEAT VS ONE-TIME CUSTOMERS ---")
print(customer_type_analysis.round(2))


# --------------------------------------------------
# 7. CUSTOMER SEGMENTATION
# --------------------------------------------------

customer_revenue = (
    df.groupby("customer_id")["revenue"]
    .sum()
)

def segment_customer(revenue):
    if revenue == 0:
        return "No Purchase"
    elif revenue < 500:
        return "Low Value"
    elif revenue < 2000:
        return "Medium Value"
    else:
        return "High Value"


customer_segments = customer_revenue.apply(segment_customer)

segment_analysis = (
    pd.DataFrame({
        "revenue": customer_revenue,
        "segment": customer_segments
    })
    .groupby("segment")
    .agg(
        customers=("revenue", "count"),
        total_revenue=("revenue", "sum"),
        average_revenue=("revenue", "mean")
    )
)

segment_analysis["revenue_contribution_percent"] = (
    segment_analysis["total_revenue"] /
    segment_analysis["total_revenue"].sum() * 100
)

print("\n--- CUSTOMER SEGMENTATION ---")
print(segment_analysis.round(2))


# --------------------------------------------------
# 8. TOP 10 HIGH-VALUE CUSTOMERS
# --------------------------------------------------

top_customers = (
    customer_revenue
    .sort_values(ascending=False)
    .head(10)
)

print("\n--- TOP 10 HIGH-VALUE CUSTOMERS ---")
print(top_customers.round(2))


print("\n" + "=" * 50)
print("DEEPER ANALYSIS COMPLETED")
print("=" * 50)

# ==================================================
# CREATE ANALYSIS-READY DATASET
# ==================================================

print("\n" + "=" * 50)
print("CREATING ANALYSIS-READY DATASET")
print("=" * 50)


# --------------------------------------------------
# 1. REVENUE CONTRIBUTION
# --------------------------------------------------

total_revenue = df["revenue"].sum()

df["revenue_contribution_percent"] = (
    df["revenue"] / total_revenue * 100
)


# --------------------------------------------------
# 2. REVENUE PER SESSION
# --------------------------------------------------

df["revenue_per_session"] = df["revenue"]


# --------------------------------------------------
# 3. ORDER VALUE
# --------------------------------------------------

df["order_value"] = df["revenue"]


# --------------------------------------------------
# 4. CUSTOMER SESSION COUNT
# --------------------------------------------------

customer_session_count = (
    df.groupby("customer_id")["session_id"]
    .transform("count")
)

df["customer_session_count"] = customer_session_count


# --------------------------------------------------
# 5. CUSTOMER TYPE
# --------------------------------------------------

df["customer_type"] = df["customer_session_count"].apply(
    lambda x: "One-Time Customer"
    if x == 1
    else "Repeat Customer"
)


# --------------------------------------------------
# 6. CUSTOMER TOTAL REVENUE
# --------------------------------------------------

customer_total_revenue = (
    df.groupby("customer_id")["revenue"]
    .transform("sum")
)

df["customer_total_revenue"] = customer_total_revenue


# --------------------------------------------------
# 7. CUSTOMER VALUE SEGMENT
# --------------------------------------------------

def customer_segment(revenue):

    if revenue == 0:
        return "No Purchase"

    elif revenue < 500:
        return "Low Value"

    elif revenue < 2000:
        return "Medium Value"

    else:
        return "High Value"


df["customer_segment"] = (
    df["customer_total_revenue"]
    .apply(customer_segment)
)


# --------------------------------------------------
# 8. DISCOUNT CATEGORY
# --------------------------------------------------

def discount_category(percent):

    if percent == 0:
        return "No Discount"

    elif percent <= 10:
        return "Low Discount"

    elif percent <= 20:
        return "Medium Discount"

    else:
        return "High Discount"


df["discount_category"] = (
    df["discount_percent"]
    .apply(discount_category)
)


# --------------------------------------------------
# 9. SAVE FINAL DATASET
# --------------------------------------------------

output_path = "../Data/Ecommerce_Analysis_Ready.csv"

df.to_csv(
    output_path,
    index=False
)

print("\nAnalysis-ready dataset created successfully.")
print("Shape:", df.shape)
print("Saved to:", output_path)

print("\nFinal columns:")
print(df.columns.tolist())