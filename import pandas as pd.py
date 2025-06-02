import pandas as pd

# Load the dataset
df = pd.read_csv('netflix_titles.csv')
df.head()

# Understand the data
df.info()
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# Handle missing values
df = df.dropna(subset=['title'])  # Drop rows where 'title' is missing
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')
df['director'] = df['director'].fillna('No Director Info')
df['cast'] = df['cast'].fillna('No Cast Info')

# Remove duplicates
df = df.drop_duplicates()

# Clean and standardize text
df['type'] = df['type'].str.strip().str.title()
df['country'] = df['country'].str.strip().str.title()
df['rating'] = df['rating'].str.strip().str.title()

# Convert dates to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Optional: Format date as string (if you're not doing datetime ops)
# df['date_added'] = df['date_added'].dt.strftime('%d-%m-%Y')

# Rename columns: lowercase and replace spaces with underscores
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Ensure release_year is a nullable integer
df['release_year'] = df['release_year'].astype('Int64')

# Save cleaned dataset
df.to_csv('netflix_cleaned.csv', index=False)
