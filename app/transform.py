import pandas as pd

def agrupa_por_bandeira(
    df: pd.DataFrame,
    coluna_agrupar: str = "Bandeira"
) -> pd.DataFrame:
    """Agrupa o dataframe pela bandeira"""
    colunas_metricas = [
        "Venda R$",
        "Qtde. Venda"
    ]
    return (
        df.groupby(coluna_agrupar)[colunas_metricas]
        .sum()
        .reset_index()
    )
