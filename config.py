import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    HF_TOKEN = os.getenv('HF_TOKEN')
    BMKG_BASE_URL = "https://api.bmkg.go.id/publik/prakiraan-cuaca"
    BMKG_ATTRIBUTION = os.getenv('BMKG_ATTRIBUTION', "Data cuaca dari BMKG")
    LLAMA_MODEL = "meta-llama/Llama-4-Scout-17B-16E-Instruct"
    
    # Jakarta Administrative Codes (Correct Structure)
    JAKARTA_CODES = {
        'kepulauan_seribu': '31.01',  # Kab. Administrasi Kepulauan Seribu
        'jakarta_pusat': '31.71',     # Kota Administrasi Jakarta Pusat
        'jakarta_utara': '31.72',     # Kota Administrasi Jakarta Utara
        'jakarta_barat': '31.73',     # Kota Administrasi Jakarta Barat
        'jakarta_selatan': '31.74',   # Kota Administrasi Jakarta Selatan
        'jakarta_timur': '31.75'      # Kota Administrasi Jakarta Timur
    }
    
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

def validate_config():
    if not Config.HF_TOKEN:
        print("❌ HF_TOKEN not found!")
        return False
    
    print("✅ Configuration OK!")
    print(f"🤖 HF Token: {Config.HF_TOKEN[:10]}...")
    print(f"🏙️ Jakarta codes: {len(Config.JAKARTA_CODES)} areas")
    return True

if __name__ == "__main__":
    validate_config()