from datetime import datetime

# ===== DATA CONTOH KOMPETITOR =====
CONTOH_COMPETITOR_DATA = {
    'kipas_angin_competitor_price': 350000,
    'ac_portable_competitor_price': 2700000,
    'payung_competitor_price': 80000,
    'market_trend': 'cooling_products_up_15%',
    'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M")
}

# ===== DATA CONTOH INVENTORY =====
CONTOH_INVENTORY_DATA = {
    'ac_portable': {'stock': 12, 'price': 2800000, 'daily_sales': 3, 'profit_margin': 15},
    'kipas_angin': {'stock': 25, 'price': 380000, 'daily_sales': 5, 'profit_margin': 25},
    'payung_lipat': {'stock': 15, 'price': 75000, 'daily_sales': 2, 'profit_margin': 40},
    'minuman_dingin': {'stock': 50, 'price': 15000, 'daily_sales': 20, 'profit_margin': 30}
}