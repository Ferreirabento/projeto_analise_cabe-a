import pandas as pd
from time import sleep

def organizacao_dados():
    # Tentativa de leitura do arquivo Excel
    try:
        df = pd.read_excel("geoMap.xlsx", header=None)
        df[["estados", "ocorrencias"]] = df[0].str.split(",", expand=True)
        df["estados"] = df["estados"].str.strip()
        df["ocorrencias"] = df["ocorrencias"].str.strip()
    except OSError:
        print("Erro ao abrir o arquivo. Verifique se o arquivo existe e está acessível.")
    except pd.errors.EmptyDataError:
        print("O arquivo está vazio. Verifique o conteúdo do arquivo.")
    except pd.errors.ParserError:
        print("Erro ao analisar o arquivo. Verifique se o formato do arquivo é compatível.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    else:
        print("Arquivo lido com sucesso.")
        print("continuando o processamento...")
        sleep(2)
        return df
    finally:
        print("organização de dados concluída.")
        


def tratamento_dados(df):
    # Tratamento de dados
    try:
        df["ocorrencias"] = pd.to_numeric(df["ocorrencias"], errors="coerce") # Convertendo para numérico, erros serão NaN
        df = df.dropna() # Remove linhas com qualquer valor NaN
        df = df.drop_duplicates()  # Remove duplicatas
    except KeyError:
        print("Coluna 'ocorrencias' não encontrada no DataFrame.")
    except ValueError:
        print("Erro ao converter valores para numérico. Verifique os dados na coluna 'ocorrencias'.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    else:
        print("Tratamento de dados concluído.")
        sleep(2)
        try:
            df.to_excel("geoMap.xlsx", index=False)  # Salva o DataFrame tratado
        except OSError:
            print("Erro ao salvar o arquivo. Verifique se você tem permissão para escrever no diretório.")
        else:
            print("Arquivo tratado salvo com sucesso.")
        finally:
            print("Exibindo DataFrame tratado:")
            print(df)
            return df
    finally:
        print("Processamento de tratamento de dados concluído.")
        
        
def exibir_dataframe():
    # Exibe o DataFrame tratado
    try:
        organizacao_dados()
    except Exception as e:
        print(f"Ocorreu um erro ao organizar os dados: {e}")
    except pd.errors.EmptyDataError:
        print("O arquivo está vazio. Verifique o conteúdo do arquivo.")
    except pd.errors.ParserError:
        print("Erro ao analisar o arquivo. Verifique se o formato do arquivo é compatível.")
    except OSError:
        print("Erro ao abrir o arquivo. Verifique se o arquivo existe e está acessível.")
    except KeyError:
        print("Coluna 'estados' não encontrada no DataFrame.")
    except ValueError:
        print("Erro ao converter valores para numérico. Verifique os dados na coluna 'ocorrencias'.")
    else:
        tratamento_dados(organizacao_dados())
    finally:
        print("Processamento finalizado.")


exibir_dataframe()

