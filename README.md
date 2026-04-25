Projeto Imobiliário: Automação de Regras de Locação e Orçamentos 🏠📊
Este projeto automatiza o fluxo de análise de regras para locação de imóveis, utilizando uma arquitetura robusta de dados para transformar informações brutas em planilhas prontas para análise orçamentária.

🚀 O Projeto
O sistema foi desenvolvido para resolver a complexidade das regras de negócio do setor imobiliário, seguindo as etapas abaixo:

Definição de Fluxograma: Mapeamento de todas as regras de locação (requisitos, garantias, taxas e condições) para garantir que o código siga estritamente a lógica de negócio.

ETL com Databricks: Utilização do ambiente Databricks para processar grandes volumes de dados imobiliários, realizando a Extração, Transformação e Limpeza (ETL) de forma escalável.

Processamento Python: Scripts em Python aplicam as regras de locação sobre os dados processados e gerenciam a lógica de cálculo de orçamentos.

Integração com Excel: Automação do output final que gera e abre diretamente um arquivo Excel, formatado para que a equipe financeira possa finalizar o orçamento.

🛠 Tecnologias Utilizadas
Ambiente de Dados: Databricks 🧱

Linguagem: Python 🐍

Manipulação de Dados: Pandas / PySpark

Output: Openpyxl / XlsxWriter (Integração com Excel)

Lógica de Negócio: Fluxograma de Regras de Locação

⚙️ Como Funciona
O script consome os dados tratados via Databricks.

A lógica Python valida cada imóvel e inquilino contra o Fluxograma de Regras.

O sistema consolida os valores e gera automaticamente o arquivo .xlsx.

Ao final da execução, o arquivo é aberto para conferência imediata.

📊 Benefícios
Agilidade: Redução do tempo manual na criação de orçamentos.

Precisão: Garantia de que todas as regras de locação sejam aplicadas sem erro humano.

Escalabilidade: O uso do Databricks permite que o projeto cresça para milhares de contratos.
