import kagglehub

# Download latest version
path = kagglehub.dataset_download("mkechinov/ecommerce-events-history-in-cosmetics-shop")

print("Path to dataset files:", path)