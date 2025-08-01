# Enriquecendo Dados do Ministério da Saúde (CNES) via API

## Este projeto foi criado com o objetivo de aprimorar a qualidade dos dados do CNES (Cadastro Nacional de Estabelecimentos de Saúde), cruzando os CEPs fornecidos nos registros com a API ViaCEP para obter informações de endereço atualizadas, padronizadas e completas.
## Eu sempre estou usando dados reais, mas antes de começar qualquer coisa, analiso os dados para entender como vou trabalhar. E nessa análise percebi que os dados do CNES não apresentam os endereços de forma clara, dificultando identificar a localização exata dos estabelecimentos. Achei isso uma falha importante e decidi resolver enriquecendo os dados com as informações corretas de endereço.


### 💡 Motivação
#### Sempre trabalho com dados reais e gosto de entender a estrutura antes de aplicar qualquer transformação. Ao analisar os dados do CNES, percebi que muitos registros tinham informações de endereço incompletas ou confusas. Isso me motivou a buscar uma forma de complementar esses dados de forma
automática, garantindo maior clareza e usabilidade.

### 🎯 Objetivo:

#### Melhorar a qualidade dos dados do CNES (Cadastro Nacional de Estabelecimentos de Saúde) enriquecendo os registros com informações de endereço obtidas pela API ViaCEP, garantindo maior padronização e completude dos dados.


### 📊 Resultados esperados

* Arquivo CNES com campos de endereço completos e padronizados.

* Dados mais confiáveis para análises em saúde pública, planejamento e logística.

* Facilidade na identificação de registros com CEPs inválidos ou desatualizados.

* Redução de erros em sistemas que utilizam esses dados para tomada de decisão.
  
##### 5. Complemento

### ⚙️ Tecnologias utilizadas
##### 1. Python (pandas, requests). Uso Poetry para gerenciar dependências, com todas as bibliotecas e versões listadas no arquivo pyproject.toml.

##### 2. API ViaCEP para validação e enriquecimento de endereços. Link da API https://viacep.com.br/ 

##### 3. Git para controle de versão do projeto, garantindo organização e histórico das alterações.

 

## 🚀 Etapas do projeto
### 1. Coleta dos dados CNES (formato CSV). 

#### Os dados utilizados nesse projeto foram obtidos:  https://opendatasus.saude.gov.br/dataset/cnes-cadastro-nacional-de-estabelecimentos-de-saude

#### Como a base contém muitos registros, e a API usada (ViaCEP) é gratuita e possui limites de requisição, utilizei apenas uma parte dos dados.

#### Em projetos reais que exigem o endereço completo de todos os registros (por exemplo, uma tabela de clientes com CEP, mas sem endereço completo), o ideal seria usar uma API paga.


### 2. Tratamento inicial e limpeza dos dados.

#### Antes de iniciar as consultas à API, verifiquei se o CSV tinha linhas duplicadas. Não havia. Porém, havia CEPs repetidos com dados diferentes, o que é normal em bases reais (ex: diferentes estabelecimentos no mesmo CEP).

### 3. Consulta à API ViaCEP para buscar endereço completo usando CEP

#### Foi criada a função cep_api_viacep que percorre cada CEP do DataFrame e faz requisições à API pública do ViaCEP. Para cada CEP encontrado com sucesso, os dados retornados (logradouro, bairro, localidade, UF) são adicionados em um novo DataFrame. A função também trata possíveis erros de requisição e continua mesmo que algum CEP falhe.

### 4. Enriquecimento dos dados com endereço completo

#### Após consultar a API, os dados de endereço foram unidos aos dados originais. Algumas linhas ficaram duplicadas por causa da repetição de CEPs com dados diferentes.

5. Padronização dos campos.

#### Essa etapa é opcional, mas padronizei os dados de endereço para ficar com a mesma cara que os dados originais do CNES.


## Obs: Todo o código e desenvolvimento está documentado na pasta notebooks.





* Base mais consistente para futuras integrações e análises.


