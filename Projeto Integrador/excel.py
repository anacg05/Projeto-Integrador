
# EXCEL

import pandas as pd

def gerar_relatorio_excel(caminho_csv, caminho_excel):
    # para ler o arquivo csv
    df = pd.read_csv(caminho_csv, sep=',')

    # para salvar o arquivo excel usando os valoes da tabela
    df.to_excel(caminho_excel, index=False)

    # Mostra caso o arquivo foi gerado
    print(f"Relatório gerado:  {caminho_excel}")

# função principal do programa
def main():
    caminho_csv = "excelCSV.csv"  # arquivo CSV
    caminho_excel = "relatorio_est.xlsx"   # nome do arquivo excel que vai ser criado
    gerar_relatorio_excel(caminho_csv, caminho_excel)

if __name__ == "__main__":
    main()