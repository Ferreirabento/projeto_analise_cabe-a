# Projeto de Análise de Dados - Ocorrências por Estado

Este projeto tem como objetivo realizar a limpeza, organização e análise de dados de ocorrências por estado, utilizando Python (Pandas), com possibilidade de integração futura com SQL e Power BI para visualização e exploração avançada dos dados.

## Estrutura do Projeto

```
etapa-1/
    geoMap.xlsx
    limpeza_e_organizacao.py
```

- **geoMap.xlsx**: Arquivo de dados brutos contendo informações de ocorrências por estado.
- **limpeza_e_organizacao.py**: Script Python responsável pela limpeza e organização dos dados.

## Como executar

1. Certifique-se de ter o Python 3.x instalado.
2. Instale as dependências necessárias:
    ```sh
    pip install pandas openpyxl
    ```
3. Coloque o arquivo `geoMap.xlsx` na pasta `etapa-1/`.
4. Execute o script:
    ```sh
    python etapa-1/limpeza_e_organizacao.py
    ```

O script irá:
- Ler o arquivo Excel.
- Separar os dados em colunas (`estados` e `ocorrencias`).
- Limpar e tratar os dados (remover espaços, converter para numérico, remover duplicatas e valores ausentes).
- Salvar o arquivo tratado sobrescrevendo o original.

## Próximas Etapas

- **Integração com SQL**: Importar os dados tratados para um banco de dados relacional para consultas avançadas.
- **Visualização com Power BI**: Conectar o Power BI ao banco de dados ou ao arquivo Excel tratado para criar dashboards e relatórios interativos.

## Requisitos

- Python 3.x
- pandas
- openpyxl (para manipulação de arquivos Excel)

## Autor

Seu Nome

---

Este projeto faz parte de um estudo de análise de dados, com foco em boas práticas de limpeza, organização e visualização

