import numpy as np
import pandas as pd
import plotly.express as px

# Update file paths to local directory
metadata = pd.read_csv("gpu_metadata.csv")
df = pd.read_csv("gpu_price_history.csv")

# Convert Date column to datetime, auto-detect format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Clean Wattage and VRAM columns if they exist
if 'Wattage' in metadata.columns:
    metadata['Wattage'] = metadata['Wattage'].astype(str).str.replace('W', '', regex=False).astype(float)
if 'VRAM' in metadata.columns:
    metadata['VRAM'] = metadata['VRAM'].astype(str).str.replace('GB', '', regex=False).astype(float)

# Plot Retail vs Used Prices for all models
if 'Retail Price' in df.columns and 'Name' in df.columns:
    fig = px.box(df, x='Name', y='Retail Price', title='Retail Price Comparison Across Models',
                 labels={'Retail Price': 'Retail Price ($)', 'Name': 'Graphics Card Model'})
    fig.show()

if 'Used Price' in df.columns and 'Name' in df.columns:
    fig = px.box(df, x='Name', y='Used Price', title='Used Price Comparison Across Models',
                 labels={'Used Price': 'Used Price ($)', 'Name': 'Graphics Card Model'})
    fig.show()

# Scatter plot to show correlation between Retail and Used Price
if 'Retail Price' in df.columns and 'Used Price' in df.columns and 'Name' in df.columns:
    fig = px.scatter(df, x='Retail Price', y='Used Price', color='Name',
                     title='Retail vs Used Price Correlation',
                     labels={'Retail Price': 'Retail Price ($)', 'Used Price': 'Used Price ($)'})
    fig.show()

# Merge VRAM and plot
if 'VRAM' in metadata.columns:
    df = df.merge(metadata[['Name', 'VRAM']], on='Name', how='left')
    fig = px.scatter(df, x='VRAM', y='Retail Price', color='Name',
                     title='Retail Price vs VRAM',
                     labels={'Retail Price': 'Retail Price ($)', 'VRAM': 'VRAM (GB)'})
    fig.show()
    fig = px.scatter(df, x='VRAM', y='Used Price', color='Name',
                     title='Used Price vs VRAM',
                     labels={'Used Price': 'Used Price ($)', 'VRAM': 'VRAM (GB)'})
    fig.show()

# Merge Wattage and plot
if 'Wattage' in metadata.columns:
    df = df.merge(metadata[['Name', 'Wattage']], on='Name', how='left')
    fig = px.scatter(df, x='Wattage', y='Retail Price', color='Name',
                     title='Retail Price vs Wattage',
                     labels={'Retail Price': 'Retail Price ($)', 'Wattage': 'Wattage (W)'})
    fig.show()
    fig = px.scatter(df, x='Wattage', y='Used Price', color='Name',
                     title='Used Price vs Wattage',
                     labels={'Used Price': 'Used Price ($)', 'Wattage': 'Wattage (W)'})
    fig.show()

# Merge 3DMARK and plot
if '3DMARK' in metadata.columns:
    df = df.merge(metadata[['Name', '3DMARK']], on='Name', how='left')
    fig = px.scatter(df, x='3DMARK', y='Retail Price', color='Name',
                     title='Retail Price vs 3DMARK',
                     labels={'Retail Price': 'Retail Price ($)', '3DMARK': '3DMARK Score'})
    fig.show()
    fig = px.scatter(df, x='3DMARK', y='Used Price', color='Name',
                     title='Used Price vs 3DMARK',
                     labels={'Used Price': 'Used Price ($)', '3DMARK': '3DMARK Score'})
    fig.show()