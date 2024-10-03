#!/usr/bin/env python
# coding: utf-8

# # Proyek Analisis Data: [E-commerce-public-dataset]
# - **Nama:** [Dudi Nurdiyansah]
# - **Email:** [m271b4ky1187@bangkit.academy]
# - **ID Dicoding:** [dudi_nurdiyansah_usFA]

# ## Menentukan Pertanyaan Bisnis

# - Pertanyaan 1: Kategori produk mana yang mendorong penjualan terbanyak?
# - Pertanyaan 2: Bagaimana tren penjualan untuk kategori produk dengan penjualan terbanyak?
# - Pertanyaan 3: Kategori produk mana yang mendapatkan penjualan terendah?
# - Pertanyaan 4: Bagaimana rata-rata tren penjualan produk secara keseluruhan?
# - Pertanyaan 5: Jenis pembayaran mana yang paling dominan digunakan oleh customers?
# - Pertanyaan 6: Apa status pesanan yang paling umum dan bagaimana distribusi status pesanan tersebut?
# - Pertanyaan 7: Kota mana yang memiliki kontribusi terbesar terhadap jumlah pelanggan, dan bagaimana strategi pemasaran dapat disesuaikan untuk meningkatkan pangsa pasar di kota-kota lainnya?
# - Pertanyaan 8: Apa kategori produk dengan rating ulasan tertinggi dan terendah?
# - Pertanyaan 9: Apakah ada korelasi antara nilai review ulasan dan biaya pengiriman?
# - Pertanyaan 10 : Di kota mana konsentrasi seller paling tinggi?

# ## Import Semua Packages/Library yang Digunakan

# In[289]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import streamlit as st


# In[290]:


st.title("Proyek Analisis Data")


# ## Data Wrangling

# ### Gathering Data

# #### Data Customers

# In[219]:


data_customers = pd.read_csv('customers_dataset.csv')
data_customers.head()


# #### Data Geolocations

# In[220]:


data_geolocations = pd.read_csv('geolocation_dataset.csv')
data_geolocations.head()


# #### Data Order Items

# In[221]:


data_order_items = pd.read_csv('order_items_dataset.csv')
data_order_items.head()


# #### Data Order Payments

# In[222]:


data_order_payments = pd.read_csv('order_payments_dataset.csv')
data_order_payments.head()


# #### Data Order Reviews

# In[223]:


data_order_reviews = pd.read_csv('order_reviews_dataset.csv')
data_order_reviews.head()


# #### Data Orders

# In[224]:


data_orders = pd.read_csv('orders_dataset.csv')
data_orders.head()


# #### Data Product Category

# In[225]:


data_product_category_name_translation = pd.read_csv('product_category_name_translation.csv')
data_product_category_name_translation.head()


# #### Data Products

# In[226]:


data_products = pd.read_csv('products_dataset.csv')
data_products.head()


# #### Data Sellers

# In[227]:


data_sellers = pd.read_csv('sellers_dataset.csv')
data_sellers.head()


# **Insight:**
# - Terdapat 9 dataset yaitu : Data Customers, Data Geolocations, Data Order Items, Data Payments, Data Order Reviews, Data Orders, Data Product Category Name Translation, Data Products, dan Data Sellers
# - Pada data-data tersebut terdapat atribut yang memiliki hubungan satu sama lain yang nanti akan dilakukan join pada saat EDA.
# 
# **English:**
# 
# - There are 9 datasets: Data Customers, Data Geolocations, Data Order Items, Data Payments, Data Order Reviews, Data Orders, Data Product Category Name Translation, Data Products, and Data Sellers.
# - In these datasets, there are attributes that are related to each other, which will later be joined during the EDA (Exploratory Data Analysis).

# ### Assessing Data

# In[228]:


data_customers.info()


# In[229]:


data_customers.describe()


# In[230]:


data_customers.isnull().sum()


# In[231]:


data_geolocations.info()


# In[232]:


data_geolocations.describe()


# In[233]:


data_geolocations.isnull().sum()


# In[234]:


data_order_items.info()


# In[235]:


data_order_items.describe()


# In[236]:


data_order_items.isnull().sum()


# In[237]:


data_order_payments.info()


# In[238]:


data_order_payments.describe()


# In[239]:


data_order_payments.isnull().sum()


# In[240]:


data_order_reviews.info()


# In[241]:


data_order_reviews.describe()


# In[242]:


data_order_reviews.isnull().sum()


# In[243]:


data_orders.info()


# In[244]:


data_orders.isnull().sum()


# In[245]:


data_orders.describe()


# In[246]:


data_products.info()


# In[247]:


data_products.describe()


# In[248]:


data_products.isnull().sum()


# In[249]:


data_product_category_name_translation.info()


# In[250]:


data_product_category_name_translation.describe()


# In[251]:


data_product_category_name_translation.isnull().sum()


# In[252]:


data_sellers.info()


# In[253]:


data_sellers.describe()


# In[254]:


data_sellers.isnull().sum()


# **Insight:**
# - Pada Data Order Reviews, terdapat atribut review_comment_title sebanyak 87656 memiliki value null dan review_comment_message sebanyak 58247 value null sehingga diperlukan penyesuaian pada saat Cleaning Data.
# - Pada Data Orders, terdapat atribut order_approved_at sebanyak 160 memiliki value null, order_delivered_carrier_date sebanyak 1783, dan order_delivered_customer_date sebanyak 2965.
# - Data product pada atribut product_category_name sebanyak 610 memiliki value null, product_name_lenght sebanyak 610, product_description_lenght sebanyak 610, dan product_photos_qty   sebanyak 610 value.
# 
# **English:**
# - In the Data Order Reviews, there are attributes: review_comment_title with 87,656 null values and review_comment_message with 58,247 null values, requiring adjustments during the data cleaning process.
# - In the Data Orders, there are attributes: order_approved_at with 160 null values, order_delivered_carrier_date with 1,783 null values, and order_delivered_customer_date with 2,965 null values.
# - In the Data Products, the attributes have null values as follows: product_category_name with 610 null values, product_name_length with 610 null values, product_description_length with 610 null values, and product_photos_qty with 610 null values.

# ### Cleaning Data

# In[255]:


# Mengganti nilai null dengan "tidak mencantumkan"
data_order_reviews['review_comment_title'] = data_order_reviews['review_comment_title'].fillna('tidak mencantumkan')
data_order_reviews['review_comment_message'] = data_order_reviews['review_comment_message'].fillna('tidak mencantumkan')

# Memeriksa kembali jumlah nilai null setelah penggantian
print(data_order_reviews.isnull().sum())


# In[256]:


# Mengganti nilai null dengan "data tidak tersedia"
data_orders['order_approved_at'] = data_orders['order_approved_at'].fillna('data tidak tersedia')
data_orders['order_delivered_carrier_date'] = data_orders['order_delivered_carrier_date'].fillna('data tidak tersedia')
data_orders['order_delivered_customer_date'] = data_orders['order_delivered_customer_date'].fillna('data tidak tersedia')

# Memeriksa kembali jumlah nilai null setelah penggantian
print(data_orders.isnull().sum())


# In[257]:


# Mengganti nilai null dengan "tidak ada data"
data_products['product_category_name'] = data_products['product_category_name'].fillna('tidak ada data')
data_products['product_name_lenght'] = data_products['product_name_lenght'].fillna('tidak ada data')
data_products['product_description_lenght'] = data_products['product_description_lenght'].fillna('tidak ada data')
data_products['product_photos_qty'] = data_products['product_photos_qty'].fillna('tidak ada data')
data_products['product_weight_g'] = data_products['product_weight_g'].fillna('tidak ada data')
data_products['product_length_cm'] = data_products['product_length_cm'].fillna('tidak ada data')
data_products['product_height_cm'] = data_products['product_height_cm'].fillna('tidak ada data')
data_products['product_width_cm'] = data_products['product_width_cm'].fillna('tidak ada data')

# Memeriksa kembali jumlah nilai null setelah penggantian
print(data_products.isnull().sum())


# **Insight:**
# - Kolom review_comment_title dan review_comment_message pada Data Order Reviews diisi dengan nilai "tidak mencantumkan" pada value yang null.
# - Kolom order_approved_at, order_delivered_carrier_date, dan order_delivered_customer_date pada Data Orders diisi dengan nilai "data tidak tersedia" pada value yang null.
# - Kolom pada Data Products, yaitu product_category_name, product_name_lenght, product_description_lenght, product_photos_qty, product_weight_g, product_length_cm, product_height_cm, dan product_width_cm diisi dengan nilai "tidak ada data" pada value yang null.
# 
# **English:**
# 
# - The columns review_comment_title and review_comment_message in the Data Order Reviews are filled with the value "tidak mencantumkan" for null values.
# - The columns order_approved_at, order_delivered_carrier_date, and order_delivered_customer_date in the Data Orders are filled with the value "data tidak tersedia" for null values.
# - In the Data Products, the columns product_category_name, product_name_length, product_description_length, product_photos_qty, product_weight_g, product_length_cm, product_height_cm, and product_width_cm are filled with the value "tidak ada data" for null values.

# ## Exploratory Data Analysis (EDA)

# ### Langkah EDA dibawah ini dilakukan untuk mengetahui apakah untuk setiap dataset memiliki hubungan satu dengan yang lainnya.

# ### Following EDA steps are conducted to determine whether each dataset has relationships with one another.

# #### Join Data Customers to Oders

# In[258]:


customers_orders = pd.merge(data_customers, data_orders, on="customer_id")
customers_orders.head()


# - Key: customer_id
# 
# - Tujuan: Menyambungkan informasi customer dengan order yang dilakukan.

# #### Join Data Order to Oders Item

# In[259]:


orders_items = pd.merge(data_orders, data_order_items, on="order_id")
orders_items.head()


# - Key: order_id
# 
# - Tujuan: Menyambungkan detail order dengan item yang dibeli dalam order tersebut.

# #### Join Data Order Payment to Order Dataset

# In[260]:


orders_payments = pd.merge(data_order_payments, data_orders, on="order_id")
orders_payments.head()


# - Key: order_id
# 
# - Tujuan: Menghubungkan order dengan detail pembayaran yang dilakukan untuk order tersebut.

# #### Join Data Customers to Order Geolocation

# In[261]:


customers_geolocations = pd.merge(data_customers, data_geolocations, left_on="customer_zip_code_prefix", right_on="geolocation_zip_code_prefix")
customers_geolocations.head()


# - Key: customer_zip_code_prefix = geolocation_zip_code_prefix
# 
# - Tujuan: Menghubungkan customer dengan informasi geolokasi (latitude dan longitude).

# #### Join Data Sellers to Order Geolocation

# In[262]:


sellers_geolocations = pd.merge(data_sellers, data_geolocations, left_on="seller_zip_code_prefix", right_on="geolocation_zip_code_prefix")
sellers_geolocations.head()


# - Key: seller_zip_code_prefix = geolocation_zip_code_prefix
# 
# - Tujuan: Menghubungkan seller dengan informasi geolokasi.

# #### Mengetahui Waktu pengiriman

# In[264]:


print(data_orders['order_delivered_customer_date'].unique())
print(data_orders['order_delivered_carrier_date'].unique())


# In[265]:


data_orders['order_delivered_customer_date'] = data_orders['order_delivered_customer_date'].replace("data tidak tersedia", pd.NaT)
data_orders['order_delivered_carrier_date'] = data_orders['order_delivered_carrier_date'].replace("data tidak tersedia", pd.NaT)


# In[266]:


data_orders['order_delivered_customer_date'] = pd.to_datetime(data_orders['order_delivered_customer_date'], errors='coerce')
data_orders['order_delivered_carrier_date'] = pd.to_datetime(data_orders['order_delivered_carrier_date'], errors='coerce')


# In[268]:


delivery_time = data_orders['order_delivered_customer_date'] - data_orders['order_delivered_carrier_date']
delivery_time_days = delivery_time.dt.total_seconds() 
data_orders['delivery_time'] = round(delivery_time_days / 86400)


# In[269]:


# Mengganti nilai yang tidak valid dengan NaT
data_orders['order_delivered_customer_date'] = data_orders['order_delivered_customer_date'].replace("data tidak tersedia", pd.NaT)
data_orders['order_delivered_carrier_date'] = data_orders['order_delivered_carrier_date'].replace("data tidak tersedia", pd.NaT)

# Mengubah kolom menjadi format datetime
data_orders['order_delivered_customer_date'] = pd.to_datetime(data_orders['order_delivered_customer_date'], errors='coerce')
data_orders['order_delivered_carrier_date'] = pd.to_datetime(data_orders['order_delivered_carrier_date'], errors='coerce')

# Menghitung waktu pengiriman
delivery_time = data_orders['order_delivered_customer_date'] - data_orders['order_delivered_carrier_date']
delivery_time_days = delivery_time.dt.total_seconds() 

# Menambahkan kolom baru 'delivery_time' dalam satuan hari ke dalam dataset
data_orders['delivery_time'] = round(delivery_time_days / 86400)

# Menampilkan hasil
print(data_orders['delivery_time'].head())


# #### Jumlah order berdasarkan kota

# In[188]:


customers_orders.groupby(by="customer_city").order_id.nunique().sort_values(ascending=False).reset_index().head(10)


# #### Join Data Orders to Order Items and Data Products

# In[189]:


orders_items = pd.merge(data_orders, data_order_items, on="order_id")
orders_items_products = pd.merge(orders_items, data_products, on="product_id")
orders_items_products_payments = pd.merge(orders_items_products, data_order_payments, on="order_id")

orders_items_products_payments.head()


# **Insight:**
# - Dilakukan join pada beberapa dataset untuk digunakan pada section visualization.
# - Memproses data tanggal pengiriman dengan mengganti entri yang tidak valid dengan NaT, mengonversi kolom tanggal ke format datetime, menghitung waktu pengiriman dalam satuan hari, dan menambahkannya sebagai kolom baru ke dalam dataset.
# - Memproses informasi tentang kota-kota yang paling aktif dalam melakukan pembelian, yang dapat membantu dalam analisis lebih lanjut dalam visualisai.
# - Menggabungkan beberapa Data terkait order, item, product, dan payment untuk menghasilkan DataFrame mengenai informasi lengkap tentang setiap pesanan, termasuk detail item, produk, dan metode pembayaran yang digunakan, memungkinkan analisis yang lebih dalam bentuk visualisasi.
# 
# **English:**
# - Joined several datasets for use in the visualization section.
# - Processed delivery date data by replacing invalid entries with NaT, converting date columns to datetime format, calculating delivery time in days, and adding it as a new column to the dataset.
# - Processed information about the most active cities in making purchases, which can aid in further analysis in visualizations.
# - Merged several data related to orders, items, products, and payments to produce a DataFrame with comprehensive information about each order, including item details, products, and payment methods used, enabling deeper analysis in the form of visualizations.

# ## Visualization & Explanatory Analysis

# ### Pertanyaan 1: Kategori produk mana yang mendorong penjualan terbanyak?

# In[270]:


# Menggabungkan data items dan produk dengan kategori
items_products = pd.merge(data_order_items, data_products, on="product_id")
items_products_category = pd.merge(items_products, data_product_category_name_translation, on="product_category_name")

# Menghitung penjualan per kategori untuk semua kategori
all_category_sales = items_products_category['product_category_name_english'].value_counts()

# Mengambil 5 kategori dengan jumlah penjualan tertinggi
top_category_sales = all_category_sales.nlargest(5)

# Menampilkan 5 kategori tertinggi
print("5 Kategori dengan Penjualan Tertinggi:")
print(top_category_sales)

# Plot bar chart untuk 5 kategori tertinggi
plt.figure(figsize=(10, 6))
sns.barplot(x=top_category_sales.values, y=top_category_sales.index, palette="viridis")
plt.title("5 Kategori Produk dengan Penjualan Tertinggi")
plt.xlabel("Jumlah Penjualan")
plt.ylabel("Kategori Produk")
plt.show()



# ### Pertanyaan 2: Bagaimana tren penjualan untuk kategori produk dengan penjualan terbanyak?

# In[271]:


# Menggabungkan data order items dengan orders untuk mendapatkan data timestamp
orders_items = pd.merge(data_order_items, data_orders, on="order_id")

# Pastikan kolom 'order_purchase_timestamp' ada dan ubah ke format datetime
orders_items['order_purchase_timestamp'] = pd.to_datetime(orders_items['order_purchase_timestamp'])

# Tambahkan kolom bulan setelah kolom dikonversi ke datetime
orders_items['purchase_month'] = orders_items['order_purchase_timestamp'].dt.to_period('M')

# Menggabungkan dengan produk dan kategori
items_products_category = pd.merge(orders_items, data_products, on="product_id")
items_products_category = pd.merge(items_products_category, data_product_category_name_translation, on="product_category_name")

# Menghitung total penjualan per kategori
total_sales_per_category = items_products_category.groupby('product_category_name_english')['price'].sum()

# Mendapatkan 5 kategori produk teratas berdasarkan total penjualan
top_5_categories = total_sales_per_category.nlargest(5).index

# Memfilter hanya untuk 5 kategori teratas
filtered_items = items_products_category[items_products_category['product_category_name_english'].isin(top_5_categories)]

# Menghitung tren penjualan per kategori per bulan untuk 5 kategori teratas
monthly_sales_top_5 = filtered_items.groupby(['purchase_month', 'product_category_name_english'])['price'].sum().unstack()

# Plot line chart untuk tren penjualan 5 kategori teratas
plt.figure(figsize=(12,8))
monthly_sales_top_5.plot(marker='o')
plt.title("Tren Penjualan 5 Kategori Produk Teratas Per Bulan")
plt.xlabel("Bulan")
plt.ylabel("Total Penjualan")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# ### Pertanyaan 3:  Kategori produk mana yang mendapatkan penjualan terendah?

# In[272]:


# Menghitung penjualan per kategori untuk semua kategori
all_category_sales = items_products_category['product_category_name_english'].value_counts()

# Mengambil 5 kategori dengan jumlah penjualan terendah dan mengurutkannya secara descending
lowest_category_sales = all_category_sales.nsmallest(5).sort_values(ascending=False)

# Menampilkan 5 kategori terendah
print("5 Kategori dengan Penjualan Terendah:")
print(lowest_category_sales)

# Plot bar chart untuk 5 kategori terendah
plt.figure(figsize=(10, 6))
sns.barplot(x=lowest_category_sales.values, y=lowest_category_sales.index, palette="viridis")
plt.title("5 Kategori Produk dengan Penjualan Terendah (Descending)")
plt.xlabel("Jumlah Penjualan")
plt.ylabel("Kategori Produk")
plt.show()



# ### Pertanyaan 4:  Bagaimana rata-rata tren penjualan produk secara keseluruhan?

# In[273]:


# Analisis Tren Penjualan 
data_orders['order_purchase_timestamp'] = pd.to_datetime(data_orders['order_purchase_timestamp'])
sales_trend = data_orders.resample('M', on='order_purchase_timestamp').size()

plt.figure(figsize=(12, 6))
sns.lineplot(data=sales_trend)
plt.title('Tren Penjualan Seiring Waktu')
plt.xlabel('Waktu')
plt.ylabel('Jumlah Penjualan')
plt.xticks(rotation=45)
plt.show()


# ### Pertanyaan 5:  Jenis pembayaran mana yang paling dominan digunakan oleh customers?

# In[274]:


# Menghitung jumlah setiap jenis pembayaran
payment_counts = orders_payments['payment_type'].value_counts()

# Menampilkan persentase setiap jenis pembayaran
payment_percentage = (payment_counts / payment_counts.sum()) * 100
print("Persentase setiap jenis pembayaran:")
print(payment_percentage)

# Membuat pie chart 
plt.figure(figsize=(10, 6))
plt.pie(payment_counts, labels=None, startangle=140, colors=sns.color_palette("Set2"))

# Menambahkan legenda 
plt.legend(
    labels=[f'{count} ({percentage:.1f}%)' for count, percentage in zip(payment_counts, payment_percentage)],
    title="Jenis Pembayaran",
    loc="best"
)

plt.title("Perbandingan Jenis Pembayaran")
plt.axis('equal')  
plt.show()


# ### Pertanyaan 6 : Apa status pesanan yang paling umum dan bagaimana distribusi status pesanan tersebut?

# In[275]:


# Menghitung jumlah setiap status pesanan
order_status_counts = orders_items['order_status'].value_counts()

# Menampilkan persentase setiap status pesanan
order_status_percentage = (order_status_counts / order_status_counts.sum()) * 100
print("Persentase setiap status pesanan:")
print(order_status_percentage)

# Membuat pie chart
plt.figure(figsize=(10, 6))
plt.pie(order_status_counts, labels=None, startangle=140, colors=sns.color_palette("Set2"))

# Menambahkan legenda 
plt.legend(
    labels=[f'{count} ({percentage:.1f}%)' for count, percentage in zip(order_status_counts, order_status_percentage)],
    title="Status Pesanan",
    loc="best"
)

plt.title("Perbandingan Status Pesanan")
plt.axis('equal')  # Menjaga pie chart tetap bulat
plt.show()


# ### Pertanyaan 7 : Kota mana yang memiliki kontribusi terbesar terhadap jumlah pelanggan, dan bagaimana strategi pemasaran dapat disesuaikan untuk meningkatkan pangsa pasar di kota-kota lainnya?

# In[276]:


# Menghitung jumlah pelanggan per kota
customer_city_counts = data_customers['customer_city'].value_counts()

# Membuat pie chart
plt.figure(figsize=(10, 6))
plt.pie(customer_city_counts, startangle=140, colors=sns.color_palette("Set2"))

# Menambahkan legenda dengan persentase
plt.legend(
    labels=[f'{label}: {count} ({count / customer_city_counts.sum() * 100:.1f}%)' for label, count in zip(customer_city_counts.index, customer_city_counts)],
    title="Kota Pelanggan",
    loc="best"
)

plt.title("Distribusi Pelanggan Berdasarkan Kota")
plt.axis('equal')  
plt.show()


# In[277]:


# Menghitung jumlah pelanggan per kota
customer_city_counts = data_customers['customer_city'].value_counts()

# Mengambil 5 kota teratas 
top_5_cities = customer_city_counts.head(5)
other_cities_count = customer_city_counts[5:].sum()  # Jumlah kota lainnya
top_5_cities['lain-lain'] = other_cities_count  # Menambahkan kategori 'kota lain'

# Menampilkan jumlah pelanggan per kota
print("Jumlah pelanggan per kota:")
print(top_5_cities)

# Membuat pie chart
plt.figure(figsize=(10, 6))
plt.pie(top_5_cities, startangle=140, colors=sns.color_palette("Set2"), autopct='%1.1f%%')

# Menambahkan legenda
plt.legend(
    labels=[f'{label}: {count}' for label, count in zip(top_5_cities.index, top_5_cities)],
    title="Kota Pelanggan",
    loc="best"
)

plt.title("Distribusi Customers Berdasarkan 5 Kota Teratas")
plt.axis('equal')  
plt.show()


# ### Pertanyaan 8 : Apa kategori produk dengan rating ulasan tertinggi dan terendah?

# In[278]:


# Menggabungkan data Order Reviews dengan Order Items berdasarkan order_id
merged_reviews_items = pd.merge(data_order_reviews, data_order_items, on='order_id')

# Menggabungkan hasil dengan Data Products berdasarkan product_id
merged_all = pd.merge(merged_reviews_items, data_products, on='product_id')

# Menghitung rata-rata skor ulasan untuk setiap produk
average_review_scores = merged_all.groupby('product_id')['review_score'].mean().reset_index()

# Mengambil 5 produk dengan rata-rata skor ulasan tertinggi
top_5_average_scores = average_review_scores.nlargest(5, 'review_score')

# Menggabungkan dengan Data Products untuk mendapatkan nama kategori produk
top_5_average_scores = pd.merge(top_5_average_scores, data_products[['product_id', 'product_category_name']], on='product_id')

# Menampilkan hasil rata-rata skor
print("5 Produk dengan Rata-rata Skor Ulasan Tertinggi:")
print(top_5_average_scores[['product_id', 'review_score', 'product_category_name']])

# Mengatur ukuran plot
plt.figure(figsize=(10, 6))

# Membuat bar plot menggunakan product_category_name sebagai y-label
sns.barplot(data=top_5_average_scores, x='review_score', y='product_category_name', palette="viridis")

# Menambahkan judul dan label
plt.title("5 Produk dengan Rata-rata Skor Ulasan Tertinggi")
plt.xlabel("Rata-rata Skor Ulasan")
plt.ylabel("Kategori Produk")
plt.grid(axis='x')

# Menampilkan plot
plt.show()



# In[280]:


# Menggabungkan data Order Reviews dengan Order Items berdasarkan order_id
merged_reviews_items = pd.merge(data_order_reviews, data_order_items, on='order_id')

# Menggabungkan hasil dengan Data Products berdasarkan product_id
merged_all = pd.merge(merged_reviews_items, data_products, on='product_id')

# Menghitung rata-rata skor ulasan untuk setiap produk
average_review_scores = merged_all.groupby('product_id')['review_score'].mean().reset_index()

# Mengambil 5 produk dengan rata-rata skor ulasan terendah
bottom_5_average_scores = average_review_scores.nsmallest(5, 'review_score')

# Menggabungkan dengan Data Products untuk mendapatkan nama kategori produk
bottom_5_average_scores = pd.merge(bottom_5_average_scores, data_products[['product_id', 'product_category_name']], on='product_id')

# Menampilkan hasil rata-rata skor
print("5 Produk dengan Rata-rata Skor Ulasan Terendah:")
print(bottom_5_average_scores[['product_id', 'review_score', 'product_category_name']])

# Mengatur ukuran plot
plt.figure(figsize=(10, 6))

# Membuat bar plot menggunakan product_category_name sebagai y-label
sns.barplot(data=bottom_5_average_scores, x='review_score', y='product_category_name', palette="viridis")

# Menambahkan judul dan label
plt.title("5 Produk dengan Rata-rata Skor Ulasan Terendah")
plt.xlabel("Rata-rata Skor Ulasan")
plt.ylabel("Kategori Produk")
plt.grid(axis='x')

# Menampilkan plot
plt.show()


# ### Pertanyaan 9 : Apakah ada korelasi antara nilai review ulasan dan biaya pengiriman?

# In[281]:


# Menggabungkan data order items dengan orders dan customers
orders_items_customers = pd.merge(data_order_items, data_orders, on="order_id")
orders_items_customers_geo = pd.merge(orders_items_customers, data_customers, on="customer_id")

# Menggabungkan data ulasan (reviews) untuk mendapatkan review score
orders_items_customers_reviews = pd.merge(orders_items_customers_geo, data_order_reviews, on="order_id")

# Menghitung rata-rata biaya pengiriman per state
shipping_cost_by_state = orders_items_customers_reviews.groupby('customer_state')['freight_value'].mean().reset_index()

# Menghitung rata-rata skor ulasan per state
average_review_by_state = orders_items_customers_reviews.groupby('customer_state')['review_score'].mean().reset_index()

# Menggabungkan data biaya pengiriman dan rata-rata skor ulasan
state_analysis = pd.merge(shipping_cost_by_state, average_review_by_state, on="customer_state")
state_analysis.columns = ['customer_state', 'freight_value_shipping', 'review_score']

# Plot scatter plot untuk menunjukkan hubungan antara biaya pengiriman dan skor ulasan
# Plot scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=state_analysis, x='freight_value_shipping', y='review_score', hue='customer_state', palette="Set2", s=100)

plt.title("Hubungan antara Biaya Pengiriman dan Skor Ulasan per State")
plt.xlabel("Rata-rata Biaya Pengiriman (Rupiah)")
plt.ylabel("Rata-rata Skor Ulasan")

# Menambahkan garis rata-rata skor ulasan
plt.axhline(y=state_analysis['review_score'].mean(), color='r', linestyle='--', label='Rata-rata Skor Ulasan')

# Menempatkan legend
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='State')  # Mengubah posisi legend
plt.grid(True)
plt.show()




# In[282]:


# Menggabungkan data order items dengan orders dan customers
orders_items_customers = pd.merge(data_order_items, data_orders, on="order_id")
orders_items_customers_geo = pd.merge(orders_items_customers, data_customers, on="customer_id")

# Menggabungkan data ulasan (reviews) untuk mendapatkan review score
orders_items_customers_reviews = pd.merge(orders_items_customers_geo, data_order_reviews, on="order_id")

# Menghitung rata-rata biaya pengiriman per state
shipping_cost_by_state = orders_items_customers_reviews.groupby('customer_state')['freight_value'].mean().reset_index()

# Menghitung rata-rata skor review per state
average_review_by_state = orders_items_customers_reviews.groupby('customer_state')['review_score'].mean().reset_index()

# Menggabungkan data biaya pengiriman dan rata-rata skor review
state_analysis = pd.merge(shipping_cost_by_state, average_review_by_state, on="customer_state")

# Pastikan nama kolom sesuai setelah penggabungan
state_analysis.columns = ['customer_state', 'freight_value_shipping', 'review_score']

# Membuat matriks untuk heatmap
heatmap_data = state_analysis.pivot("customer_state", "freight_value_shipping", "review_score")

# Plot heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", fmt=".2f", cbar_kws={'label': 'Rata-rata Skor Ulasan'})
plt.title("Heatmap Hubungan antara Biaya Pengiriman dan Rata-rata Skor Ulasan per State")
plt.xlabel("Rata-rata Biaya Pengiriman ")
plt.ylabel("State Pelanggan")
plt.show()


# In[283]:


# Menghitung nilai korelasi antara 'freight_value_shipping' dan 'review_score'
correlation = state_analysis['freight_value_shipping'].corr(state_analysis['review_score'])

# Mencetak nilai korelasi
print(f"Nilai Korelasi antara Biaya Pengiriman dan Skor Ulasan: {correlation:.2f}")


# **Insight:**
# - Pertanyaan 1: Kategori produk mana yang mendorong penjualan terbanyak? Kategori bed_bath_table memimpin penjualan, diikuti health_beauty, sports_leisure, furniture_decor, dan computers_accessories, mencerminkan tren konsumen yang berfokus pada kenyamanan rumah, kesehatan, hiburan, dan teknologi.
# - Pertanyaan 2: Bagaimana tren penjualan untuk kategori produk dengan penjualan terbanyak? Semua produk mengalami peningkatan penjualan selama Janiari 2017 - 2018 namun fluktuatif dari Januari 2018 - Juli 2018
# - Pertanyaan 3:  Kategori produk mana yang mendapatkan penjualan terendah? Kategori dengan penjualan terendah adalah security_and_services (2 penjualan), diikuti oleh fashion_childrens_clothes (8 penjualan), la_cuisine dan cds_dvds_musicals (masing-masing 14 penjualan), serta arts_and_craftmanship (24 penjualan), menunjukkan bahwa produk terkait keamanan, pakaian anak, dan media fisik memiliki permintaan yang sangat rendah.
# - Pertanyaan 4:  Bagaimana rata-rata tren penjualan produk keseluruhan? tren penjualan secara keseluruhan juga mengalami peningkatan antara selama Januari 2017 - 2018 namun fluktuatif dimulai pada tahun 2018.
# - Pertanyaan 5:  Jenis pembayaran mana yang paling dominan digunakan oleh customers?Jenis pembayaran yang paling dominan digunakan oleh pelanggan adalah credit card dengan persentase 73,92%, menunjukkan bahwa sebagian besar customer lebih memilih kartu kredit sebagai metode pembayaran utama mereka.
# - Pertanyaan 6 : Apa status pesanan yang paling umum dan bagaimana distribusi status pesanan tersebut?Status pesanan yang paling umum adalah delivered dengan persentase 97,82%, menunjukkan bahwa hampir semua pesanan berhasil dikirim, sementara status lainnya seperti shipped (1,05%) dan canceled (0,48%) memiliki distribusi yang jauh lebih rendah.
# - Pertanyaan 7 : Kota mana yang memiliki kontribusi terbesar terhadap jumlah pelanggan, dan bagaimana strategi pemasaran dapat disesuaikan untuk meningkatkan pangsa pasar di kota-kota lainnya? Kota Sao Paulo memiliki kontribusi terbesar terhadap jumlah pelanggan dengan 15.540 pelanggan, diikuti oleh Rio de Janeiro (6.882) dan Belo Horizonte (2.773). Strategi pemasaran dapat difokuskan pada kota-kota dengan kontribusi lebih kecil, seperti Curitiba dan Brasilia, melalui kampanye misalnnya penawaran khusus yang dapat menaring customer.
# - Pertanyaan 8 : Apa kategori produk dengan rating ulasan tertinggi dan terendah?Kategori produk dengan rating ulasan tertinggi adalah perfumaria, utilidades_domesticas, relogios_presentes, cool_stuff, dan cama_mesa_banho, semuanya dengan skor ulasan sempurna 5.0. sSementara Kategori produk dengan rating ulasan terendah adalah cama_mesa_banho, automotivo, pet_shop, esporte_lazer, dan construcao_ferramentas_construcao, semuanya dengan skor ulasan 1.0.
# - Pertanyaan 9 : Apakah ada korelasi antara nilai review ulasan dan biaya pengiriman? Nilai korelasi -0.34 antara biaya pengiriman dan skor review menunjukkan hubungan negatif yang lemah, artinya semakin tinggi biaya pengiriman, cenderung ada sedikit penurunan dalam skor review, meskipun hubungan ini tidak terlalu kuat.
# 
# **English:**
# - Question 1: Which product category drives the most sales? The bed_bath_table category leads sales, followed by health_beauty, sports_leisure, furniture_decor, and computers_accessories, reflecting consumer trends focused on home comfort, health, entertainment, and technology.
# - Question 2: What are the sales trends for the top-selling product categories? All products experienced an increase in sales from January 2017 to 2018, but sales fluctuated from January 2018 to July 2018.
# - Question 3: Which product category has the lowest sales? The category with the lowest sales is security_and_services (2 sales), followed by fashion_childrens_clothes (8 sales), la_cuisine and cds_dvds_musicals (14 sales each), and arts_and_craftmanship (24 sales), indicating that products related to security, children's clothing, and physical media have very low demand.
# - Question 4: What is the overall product sales trend? Overall, product sales showed an increase from January 2017 to 2018, but sales became more volatile starting in 2018.
# - Question 5: What is the most dominant payment method used by customers? The most dominant payment method used by customers is credit card, with a percentage of 73.92%, indicating that most customers prefer credit cards as their primary payment method.
# - Question 6: What is the most common order status, and what is the distribution of order statuses? The most common order status is delivered, accounting for 97.82% of orders, indicating that almost all orders were successfully delivered, while other statuses such as shipped (1.05%) and canceled (0.48%) have much lower distributions.
# - Question 7: Which city contributes the most to the customer base, and how can marketing strategies be adjusted to increase market share in other cities? The city of Sao Paulo contributes the most to the customer base with 15,540 customers, followed by Rio de Janeiro (6,882) and Belo Horizonte (2,773). Marketing strategies could focus on smaller contributing cities, such as Curitiba and Brasilia, through targeted promotions or special offers to attract more customers.
# - Question 8: Which product category has the highest and lowest review ratings? The product categories with the highest review ratings are perfumaria, utilidades_domesticas, relogios_presentes, cool_stuff, and cama_mesa_banho, all with a perfect 5.0 score. Meanwhile, the categories with the lowest review ratings are cama_mesa_banho, automotivo, pet_shop, esporte_lazer, and construcao_ferramentas_construcao, all with a review score of 1.0.
# - Question 9: Is there a correlation between review scores and shipping costs? The correlation value of -0.34 between shipping costs and review scores indicates a weak negative relationship, meaning that as shipping costs increase, there is a slight tendency for review scores to decrease, though the relationship is not particularly strong.
# 

# ## Analisis Lanjutan (Opsional)

# ### Pertanyaan 10 : Di kota mana konsentrasi seller paling tinggi?

# In[284]:


# Membaca data geolokasi
data_geolocations = pd.read_csv('geolocation_dataset.csv')

# Menghitung jumlah seller per kota
seller_city_counts = data_sellers['seller_city'].value_counts().reset_index()
seller_city_counts.columns = ['seller_city', 'count']

# Menggabungkan data geolokasi dengan jumlah seller
merged_data = pd.merge(data_geolocations, seller_city_counts, left_on='geolocation_city', right_on='seller_city', how='left')

# Mengubah DataFrame menjadi GeoDataFrame
gdf = gpd.GeoDataFrame(merged_data, geometry=gpd.points_from_xy(merged_data['geolocation_lng'], merged_data['geolocation_lat']))

# Mengatur ukuran plot 
plt.figure(figsize=(16, 12))  

# Mengambil data peta dunia dari file shapefile 
world = gpd.read_file('C:/Users/hp/ne_110m_admin_0_countries.shp')

# Membuat plot
ax = world.plot(color='white', edgecolor='black')

# Menambahkan titik lokasi seller ke peta
gdf.plot(ax=ax, marker='o', color='red', markersize=gdf['count'].fillna(0) * 2, label='Jumlah Seller')  # Ukuran titik diperkecil lebih lanjut

# Menambahkan label
plt.title('Peta Penyebaran Seller Berdasarkan Kota')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.show()


# - Pertanyaan 10 : Di kota mana konsentrasi seller paling tinggi? Berdasarkan pada peta yang ditunjukkan, konsentrasi seller tertinggi ada pada Negara Brazil, Russia dan Spanyol.

# ## Conclusion

# - Kategori produk yang mendorong penjualan terbanyak: Kategori bed_bath_table memimpin penjualan, menunjukkan konsumen lebih memilih produk untuk kenyamanan rumah.
# 
# - Tren penjualan kategori produk terlaris: Penjualan meningkat secara umum dari Januari 2017 hingga 2018, tetapi mengalami fluktuasi yang signifikan di tahun 2018.
# 
# - Kategori produk dengan penjualan terendah: Security_and_services memiliki penjualan sangat rendah (2 penjualan), menunjukkan rendahnya permintaan untuk kategori tersebut.
# 
# - Rata-rata tren penjualan keseluruhan: Tren penjualan keseluruhan menunjukkan peningkatan antara Januari 2017 dan 2018, tetapi juga fluktuatif di tahun 2018.
# 
# - Jenis pembayaran dominan: Metode pembayaran paling umum adalah kartu kredit (73,92%), menunjukkan preferensi pelanggan terhadap pembayaran yang cepat dan aman.
# 
# - Status pesanan yang umum: Status delivered mendominasi (97,82%), menunjukkan efektivitas pengiriman pesanan, sementara status lain seperti shipped dan canceled relatif rendah.
# 
# - Kota dengan kontribusi pelanggan terbanyak: Sao Paulo adalah kota dengan jumlah pelanggan terbanyak; strategi pemasaran perlu difokuskan pada kota-kota lain dengan kontribusi lebih rendah untuk meningkatkan pangsa pasar.
# 
# - Kategori produk dengan rating ulasan tertinggi dan terendah: Kategori dengan rating tertinggi adalah perfumaria dan sejenisnya (skor 5.0), sementara kategori dengan rating terendah termasuk automotivo (skor 1.0), menandakan perbedaan besar dalam kepuasan pelanggan.
# 
# - Korelasi antara skor ulasan dan biaya pengiriman: Terdapat korelasi negatif yang lemah (-0.34) antara biaya pengiriman dan skor ulasan, menunjukkan bahwa biaya pengiriman yang lebih tinggi cenderung dikaitkan dengan skor ulasan yang lebih rendah, meskipun tidak signifikan.
# 
# - Berdasarkan pada peta yang ditunjukkan, konsentrasi seller tertinggi ada pada Negara Brazil, Russia dan Spanyol.

# In[288]:


jupyter nbconvert --to script Proyek_Analisis_Data_Dudi_Nurdiyansah.ipynb


# In[ ]:




