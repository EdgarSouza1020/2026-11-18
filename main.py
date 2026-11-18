from app import transform
from app import extract
from app import config

def main():

    df = extract.load_data(config.INPUT_DIR / "2026.xlsx")
    
    df_agrupado = transform.agrupa_por_bandeira(df)
    print(df_agrupado)    
    
if __name__ == "__main__":
    main()
