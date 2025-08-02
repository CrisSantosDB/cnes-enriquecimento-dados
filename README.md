# Enriquecimento de Dados do CNES (Ministério da Saúde) via API
![Logo do Ministério da Saúde](MinisteriodaSaude.jpg)

### Este projeto nasceu da análise dos dados reais do CNES (Cadastro Nacional de Estabelecimentos de Saúde), onde percebi que muitos registros tinham informações de endereço incompletas ou confusas, dificultando a localização exata dos estabelecimentos. Para resolver essa falha, desenvolvi uma solução que cruza os CEPs dos registros com a API ViaCEP, enriquecendo os dados com informações de endereço atualizadas, padronizadas e completas.

---
## 💡 Motivação
### Sempre trabalho com dados reais e gosto de entender a estrutura antes de aplicar qualquer transformação. Ao analisar os dados do CNES, percebi que muitos registros tinham informações de endereço incompletas ou confusas. Isso me motivou a buscar uma forma de complementar esses dados de forma automática, garantindo maior clareza e usabilidade.

---

## 🎯 Objetivo:

### Melhorar a qualidade dos dados do CNES (Cadastro Nacional de Estabelecimentos de Saúde) enriquecendo os registros com informações de endereço obtidas pela API ViaCEP, garantindo maior padronização e completude dos dados.

---
## 📊 Resultados esperados

* ###  Arquivo CNES com campos de endereço completos e padronizados.

* ### Dados mais confiáveis para análises em saúde pública, planejamento e logística.

* ### Facilidade na identificação de registros com CEPs inválidos ou desatualizados.

* ### Redução de erros em sistemas que utilizam esses dados para tomada de decisão.

---


## ⚙️ Tecnologias utilizadas
### 1. Python (pandas, requests). Uso Poetry para gerenciar dependências, com todas as bibliotecas e versões listadas no arquivo pyproject.toml.

### 2. API ViaCEP para validação e enriquecimento de endereços. Link da API https://viacep.com.br/ 

### 3. Git para controle de versão do projeto, garantindo organização e histórico das alterações.

 
---

## 📂 Estrutura do Projeto

### - notebooks/ — Contém os notebooks Jupyter usados para desenvolvimento, testes e análise exploratória dos dados. Aqui você encontra o passo a passo detalhado do projeto com comentários explicativos.
### - src/cnes/ — Contém o código principal do projeto em formato .py. Esse arquivo é a versão “limpa” do código, pronta para execução e integração.
### - data/ — Pasta com os dados utilizados no projeto, incluindo os arquivos CSV originais e os arquivos com dados enriquecidos gerados.
### - pyproject.toml — Arquivo de configuração do Poetry com as dependências e versões utilizadas.
### - .gitignore — Arquivo que define os arquivos e pastas que não devem ser versionados no Git.

---

## 🚀 Etapas do projeto
## 1. Coleta dos dados CNES (formato CSV). 

### Os dados utilizados nesse projeto foram obtidos:  https://opendatasus.saude.gov.br/dataset/cnes-cadastro-nacional-de-estabelecimentos-de-saude

### Como a base contém muitos registros, e a API usada (ViaCEP) é gratuita e possui limites de requisição, utilizei apenas uma parte dos dados.

### Em projetos reais que exigem o endereço completo de todos os registros (por exemplo, uma tabela de clientes com CEP, mas sem endereço completo), o ideal seria usar uma API paga.


## 2. Tratamento inicial e limpeza dos dados.

### Antes de iniciar as consultas à API, verifiquei se o CSV tinha linhas duplicadas. Não havia. Porém, havia CEPs repetidos com dados diferentes, o que é normal em bases reais (ex: diferentes estabelecimentos no mesmo CEP).

## 3. Consulta à API ViaCEP para buscar endereço completo usando CEP

### Foi criada a função cep_api_viacep que percorre cada CEP do DataFrame e faz requisições à API pública do ViaCEP. Para cada CEP encontrado com sucesso, os dados retornados (logradouro, bairro, localidade, UF) são adicionados em um novo DataFrame. A função também trata possíveis erros de requisição e continua mesmo que algum CEP falhe.

## 4. Enriquecimento dos dados com endereço completo

### Após o enriquecimento com a API ViaCEP, algumas linhas foram duplicadas devido a múltiplas ocorrências do mesmo CEP com dados diferentes no DataFrame original. Para garantir um conjunto final mais limpo, foi aplicada uma deduplicação com drop_duplicates, mantendo apenas a primeira ocorrência de cada linha idêntica.

## 5. Padronização dos campos.

### Essa etapa é opcional, mas padronizei os dados de endereço para ficar com a mesma cara que os dados originais do CNES.


## 📁 **Observação:** Todo o código-fonte, bem como o desenvolvimento completo do projeto, está documentado na pasta notebooks/. Cada etapa do processo está explicada e comentada.
