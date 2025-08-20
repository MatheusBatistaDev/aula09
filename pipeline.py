from etl import pipeline_calcular_kpi_de_vendas_consolidado

if __name__ == "__main__":
    pasta_argumento = "data"
    formatos = ['csv', 'parquet']
    df = pipeline_calcular_kpi_de_vendas_consolidado(pasta_argumento, formatos)
    
    
        
       