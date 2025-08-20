import pandas as pd
import os
import glob
from utils_log import log_decorator


# =========================
# Função de Extract
# =========================


@log_decorator
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    """
    Lê todos os arquivos JSON da pasta e consolida em um único DataFrame.
    """
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))  

    if not arquivos_json:
        print(f"⚠️ Nenhum arquivo JSON encontrado na pasta: {pasta}")
        return pd.DataFrame()  # retorna vazio

    df_list = []
    for arquivo in arquivos_json:
        try:
            df = pd.read_json(arquivo)
            df_list.append(df)
        except ValueError as e:
            print(f"❌ Erro ao ler {arquivo}: {e}")

    if df_list:
        df_total = pd.concat(df_list, ignore_index=True)
        return df_total
    else:
        print("⚠️ Nenhum JSON válido para consolidar.")
        return pd.DataFrame()


# =========================
# Função de Transform
# =========================

@log_decorator
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adiciona a coluna 'Total' calculando Quantidade * Venda.
    Verifica se as colunas existem antes de calcular.
    """
    df_novo = df.copy()
    if "Quantidade" not in df_novo.columns or "Venda" not in df_novo.columns:
        print("⚠️ Colunas 'Quantidade' ou 'Venda' não existem no DataFrame.")
        return df_novo

    df_novo["Total"] = df_novo["Quantidade"] * df_novo["Venda"]
    return df_novo


# =========================
# Função de Load
# =========================
@log_decorator
def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    Salva o DataFrame em CSV e/ou Parquet.
    format_saida: lista com 'csv', 'parquet' ou ambos
    """
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv("dados.csv", index=False)
            print("✅ Arquivo CSV salvo: dados.csv")
        elif formato == 'parquet':
            df.to_parquet("dados.parquet", index=False)
            print("✅ Arquivo Parquet salvo: dados.parquet")
        else:
            print(f"❌ Formato '{formato}' não suportado.")


# =========================
# Execução principal
# =========================
if __name__ == "__main__":
    pasta_argumento = 'data'
     
    # Extract
    dataframe = extrair_dados_e_consolidar(pasta_argumento)
    
    if dataframe.empty:
        print("⚠️ Nenhum dado para processar.")
    else:
        # Transform
        dataframe_calculado = calcular_kpi_de_total_de_vendas(dataframe)
        
        # Load
        formatos = ['csv', 'parquet']  # escolha os formatos desejados
        carregar_dados(dataframe_calculado, format_saida=formatos)
        
        print("✅ ETL concluído com sucesso!")



def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formatos: list):
    """
    Pipeline completo de ETL: Extrai, transforma e carrega os dados.
    """
    # Extract
    df_extraido = extrair_dados_e_consolidar(pasta)
    
    if df_extraido.empty:
        print("⚠️ Nenhum dado para processar no pipeline.")
        return
    
    # Transform
    df_transformado = calcular_kpi_de_total_de_vendas(df_extraido)
    
    # Load
    carregar_dados(df_transformado, format_saida=formatos)
    
    print("✅ Pipeline ETL concluído com sucesso!")