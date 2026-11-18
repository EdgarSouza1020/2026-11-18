from pathlib import Path
import pandas as pd

def load_data(path: Path) -> pd.DataFrame:
    """Carrega um arquivo Excel e transforma em Dataframe"""
    return pd.read_excel(path)
