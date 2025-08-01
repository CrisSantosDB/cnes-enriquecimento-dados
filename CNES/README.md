### Projeto voltado para tratamento, enriquecimento e padronização dos dados públicos do Cadastro Nacional de Estabelecimentos de Saúde (CNES), com o objetivo de corrigir informações incompletas, como ausência de cidade, estado e dados desatualizados de logradouro.


### 🎯 Objetivo:

Melhorar a qualidade dos dados do CNES disponibilizados pelo Ministério da Saúde, identificando falhas nos registros e utilizando APIs externas para complementar e validar informações como:

Cidade

Estado

Região

Logradouro atualizado

Complemento

### ⚙️ Tecnologias utilizadas
Python (pandas, requests)

API ViaCEP para validação e enriquecimento de endereços

Jupyter Notebook para testes e visualização intermediária dos dados

Link da API https://viacep.com.br/ 




## 🚀 Etapas do projeto
### 1. Coleta dos dados CNES (formato CSV). 

#### Os dados utilizados nesse projeto foram obtidos:  https://opendatasus.saude.gov.br/dataset/cnes-cadastro-nacional-de-estabelecimentos-de-saude

#### Como a base contém muitos registros, e a API usada (ViaCEP) é gratuita e possui limites de requisição, utilizei apenas uma parte dos dados.

#### Em projetos reais que exigem o endereço completo de todos os registros (por exemplo, uma tabela de clientes com CEP, mas sem endereço completo), o ideal seria usar uma API paga.


### 2. Tratamento inicial e limpeza dos dados.

#### Antes de iniciar as consultas à API, verifiquei se o CSV tinha linhas duplicadas. Não havia. Porém, havia CEPs repetidos com dados diferentes, o que é normal em bases reais (ex: diferentes estabelecimentos no mesmo CEP).

### 3. Consulta à API ViaCEP para buscar endereço completo usando CEP

Foi criada uma função chamada cep_api_viacep que percorre todos os CEPs do DataFrame original e faz requisições à API pública do ViaCEP. A cada CEP consultado com sucesso, os dados retornados (como logradouro, bairro, localidade e UF) são adicionados a um novo DataFrame.

Essa função trata erros de conexão e continua o processo mesmo se algum CEP falhar. No final, ela retorna um DataFrame com os dados atualizados, prontos para serem combinados com os dados originais.

4. Enriquecimento dos dados com endereço completo

Após o enriquecimento com a API ViaCEP, algumas linhas foram duplicadas devido a múltiplas ocorrências do mesmo CEP com dados diferentes no DataFrame original. Para garantir um conjunto final mais limpo, foi aplicada uma deduplicação com drop_duplicates, mantendo apenas a primeira ocorrência de cada linha idêntica.

5. Padronização dos campos.

Aqui é opcional, mas para uma melhor visialização eu deixei tudo padronizado de acordo com o arquivo do CNES


Obs: Todos os detalhes do codigo do desenvolvimento do projeto está na pasta notebooks.




### 📊 Resultados esperados
Arquivo CNES com campos de localização completos

Melhoria na confiabilidade dos dados para uso em análises de saúde pública, alocação de recursos e planejamento logístico

Detecção de registros com CEPs inválidos ou desatualizados


### 💡 Motivação
Durante a análise dos dados brutos do CNES, identifiquei que muitos registros estavam incompletos, dificultando análises por região, estado ou cidade. Esse projeto foi criado para resolver esses problemas e garantir dados mais precisos para quem precisa trabalhar com informações de estabelecimentos de saúde no Brasil.