from dotenv import load_dotenv
import os

from app import extract
from app import transform
from app import load
from app import config

load_dotenv()

def main():
    
    df = extract.load_data(config.INPUT_DIR / "2026.xlsx")
    
    load.save_data(df, config.OUTPUT_DIR / "arq-final.xlsx")
    print(f"O arquivo foi gerado na pasta: {config.OUTPUT_DIR}")
        
    
    
if __name__ == "__main__":
    main()
