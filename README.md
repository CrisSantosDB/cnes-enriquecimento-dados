# cnes-enriquecimento-dados

### Projeto voltado para tratamento, enriquecimento e padronização dos dados públicos do Cadastro Nacional de Estabelecimentos de Saúde (CNES), com o objetivo de corrigir informações incompletas, como ausência de cidade, estado e dados desatualizados de logradouro.


### 🎯 Objetivo:

#### Melhorar a qualidade dos dados do CNES disponibilizados pelo Ministério da Saúde, identificando falhas nos registros e utilizando APIs externas para complementar e validar informações como:

##### 1. Cidade

##### 2. Estado

##### 3. Região

##### 4. Logradouro atualizado

##### 5. Complemento

### ⚙️ Tecnologias utilizadas
##### 1. Python (pandas, requests). Esse projeto estou usando o Poetry, podemos ver todas as bibliotecas e versões que eu usei o projeto no arquivo pyproject.tom

##### 2. API ViaCEP para validação e enriquecimento de endereços. Link da API https://viacep.com.br/ 

##### 3. Jupyter Notebook para testes e visualização intermediária dos dados

 

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




### 📊 Resultados esperados
#### 1 . Arquivo CNES com campos de localização completos

#### 2. Melhoria na confiabilidade dos dados para uso em análises de saúde pública, alocação de recursos e planejamento logístico

#### 3. Detecção de registros com CEPs inválidos ou desatualizados


### 💡 Motivação
#### Durante a análise dos dados brutos do CNES, identifiquei que muitos registros estavam incompletos, dificultando análises por região, estado ou cidade. Esse projeto foi criado para resolver esses problemas e garantir dados mais precisos para quem precisa trabalhar com informações de estabelecimentos de saúde no Brasil.
