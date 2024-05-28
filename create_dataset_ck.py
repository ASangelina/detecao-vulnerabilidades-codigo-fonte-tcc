import os
import pandas as pd
import subprocess
import tempfile

# Caminho para o JAR do CK
ck_jar_path = "C:/Users/angel/ck/target/ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar"

# Função para criar uma classe temporária
def create_temp_class(java_code):
    return f"""
    public class TempClass {{
        {java_code}
    }}
    """

# Função para executar o CK e capturar as métricas
def run_ck(java_code):
    # Cria um diretório temporário para armazenar o arquivo Java temporário
    with tempfile.TemporaryDirectory() as temp_dir:
        # Caminho para o arquivo temporário Java
        java_file_path = os.path.join(temp_dir, "TempClass.java")
        
        # Cria a classe temporária com o código Java
        full_code = create_temp_class(java_code)
        
        # Escreve o código Java no arquivo temporário
        with open(java_file_path, "w",encoding='utf-8') as java_file:
            java_file.write(full_code)
        
        # Executa o CK no arquivo Java temporário
        result = subprocess.run(
            ["java", "-jar", ck_jar_path, java_file_path],
            capture_output=True,
            text=True
        )
        
        # Verifica a saída do CK
        if result.returncode != 0:
            print(f"Erro ao executar CK: {result.stderr}")
            return None
        
        # Caminho para o arquivo de métricas no diretório principal
        metrics_file_path = os.path.join(os.getcwd(), "class.csv")
        
        # Lê os resultados do CK
        if os.path.exists(metrics_file_path):
            metrics_df = pd.read_csv(metrics_file_path)
            metrics_df = metrics_df.drop(columns=['file', 'class', 'type'], errors='ignore')
            return metrics_df
        else:
            print("Arquivo de métricas não encontrado.")
            return None

# Função principal para processar o dataset
# Função principal para processar o dataset
def process_dataset(input_csv_path, output_csv_path):
    # Lê o dataset original
    df = pd.read_csv(input_csv_path)
    
    # Lista para armazenar resultados
    results = []
    
    # Processa cada linha do dataset
    for index, row in df.iterrows():
        label = row['label']
        code = row['code']
        
        # Executa o CK e obtém as métricas
        metrics_df = run_ck(code)
        
        if metrics_df is not None and not metrics_df.empty:
            # Adiciona o label, code e as métricas ao resultado
            metrics_row = metrics_df.iloc[0].to_dict()
            metrics_row['label'] = label
            metrics_row['code'] = code
            results.append(metrics_row)
        else:
            print(f"Falha ao processar o código na linha {index}, métricas não foram geradas ou o arquivo está vazio.")
    
    # Cria um DataFrame com os resultados
    if results:
        results_df = pd.DataFrame(results)
        # Reorganiza as colunas para garantir que 'label' e 'code' estejam no início
        columns = ['label', 'code'] + [col for col in results_df.columns if col not in ['label', 'code']]
        results_df = results_df[columns]
        results_df.insert(0, '', range(len(results_df)))
        # Salva o novo dataset
        results_df.to_csv(output_csv_path, index=False)
    else:
        print("Nenhuma métrica foi gerada para o dataset fornecido.")


# Caminhos para os arquivos de entrada e saída
input_csv_path = "train.csv"
output_csv_path = "new_train.csv"

# Processa o dataset
process_dataset(input_csv_path, output_csv_path)
