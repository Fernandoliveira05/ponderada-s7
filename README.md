# Atividade Ponderada 3 - Semana 07
 
Durante a semana 07 do décimo módulo de Engenharia da Computação recebemos o nosso terceiro desafio: construir uma API para gerenciar as figurinhas da Copa do Mundo 2026. O diferencial aqui não era só fazer funcionar. Tínhamos que fazer funcionar direito, aplicando os conceitos de Clean Code. Separação de camadas, injeção de dependência, erros de domínio bem nomeados, banco SQLite local. 
 
# Responsáveis por essa atividade
 
<div align="center">
<table>
  <tr>
    <td align="center" width="260">
      <img src="./assets/Fernando.jpg" width="120" alt="Foto de Fernando Soares de Oliveira" /><br><br>
      <strong>Fernando Soares de Oliveira</strong><br>
      <sub>Código, ideias de resolução e perguntas constantemente</sub><br><br>
      <a href="https://www.linkedin.com/in/fernando-soares-de-oliveira/">LinkedIn</a>
    </td>
    <td align="center" width="260">
      <img src="./assets/pietra.jpg" width="120" alt="Foto de Pietra Batista" /><br><br>
      <strong>Pietra Batista</strong><br>
      <sub>Código, ideias de resolução e perguntas constantemente</sub><br><br>
      <a href="https://www.linkedin.com/in/pietrabatista/">LinkedIn</a>
    </td>
  </tr>
</table>
</div>

# Qual o racional da equipe?
 
A gente costuma anotar tudo durante o desenvolvimento, cada decisão, cada dúvida, cada erro. É um hábito que já salvou a gente mais de uma vez na hora de documentar e para organizar nosso processo de desenvolvimento. Então aqui vai o registro de como a atividade se desenrolou, do começo ao fim.
 
Antes de escrever qualquer linha de código, quebramos o problema em tarefas menores:
 
TASK:
 
1. decidir a linguagem e o framework
2. preparar o ambiente com a estrutura de pastas do Clean Code
3. definir a entidade `figurinha` na camada Domain
4. implementar o Repository com as consultas ao banco
5. implementar o Service com as regras de negócio
6. implementar os Handlers (rotas) com o Blueprint do Flask
7. configurar o Swagger para documentação e testes
8. conectar tudo e testar os endpoints
---
 
CONCLUSÃO:
 
- a API responde corretamente para todos os métodos (POST, GET, PUT, DELETE)
- as regras de negócio estão na camada Service, não no Handler
- os erros de domínio são mapeados para os status HTTP corretos
- o banco SQLite é inicializado e conectado localmente
- enums implementados e validados nas camadas corretas
---
 
## DIÁRIO DE DESENVOLVIMENTO (versão crua, exatamente como anotamos):
 
- Primeiro decidimos a linguagem que iríamos utilizar, o Flask. Ele é um microframework de python e tomamos essa decisão pela familiaridade que temos com a linguagem. Por conta do tempo limitado, essa é uma linguagem que permite maior modularização e facilidade.
- Preparamos o ambiente ideal para o desenvolvimento da atividade usando os conceitos de *clean code*.
- O que entendemos da estrutura: na pasta `blueprint` vamos fazer os nossos *handlers* (uma exigência do Flask para criação de rotas). Na pasta `services` definimos as regras de negócio da aplicação, ou seja, como que deve funcionar o fluxo e comunicação do sistema.
- Optamos por começar o desenvolvimento definindo as entidades na pasta `domain`. As entidades é a tabela das próprias figurinhas. O exemplo já foi passado pelo professor na atividade e vamos construir com base nisso e em uma pesquisa na internet para saber como se cria uma entidade em Flask.
- Criamos a entidade 'figurinha' no domain. definimos uma classe que contém a estrutura da tabela (id, numero, tipo, posicao, created_at, updated_at) e duas funções com as exigências de 2 regras de negócio.
- Agora partimos para a implementação do 'repository', onde terá toda a lógica de consulta e conexão com o banco de dados.
- Tivemos dificuldades com a compreensão das estruturas corretas de clean code utilizando Flask. Por conta de vícios, imaginamos que precisava ter uma pasta só de models, mas entendemos depois com o auxílio do professor de que poderíamos declarar isso em domain e passar as regras de negócio para service. no domain definimos a nossa entidade e apagamos o models.
- No repository, mantivemos como estava, pois criamos as consultas exigidas, como criar nova figurinha, deletar, atualizar e pegar geral (haha) ou por id.
- Agora definimos o `service`. Aqui vai todas as regras de negócios. Usamos IA generativa para auxiliar na estrutura, pedimos um trecho de código mínimo e com base nele criamos o nosso. Conseguimos definir classes com funções que criam figurinhas, listam elas, deletam e tratamos o erro caso não exista.
- No `handler` definimos as rotas e métodos necessários para criar nova figurinha, buscar figurinha por ID, listar todas, deletar e atualizar. Todas com tratamento de erros adequadas.
- Quando fomos testar as rotas descobrimos que o Swagger do Flask era diferente do FastAPI e precisava ser configurado manualmente.
- Usamos IA para criar as rotas e suas especificações no Swagger, porque era uma tarefa bem chata de fazer na mão.
- Testamos, percebemos que as respostas e alguns detalhes não estavam iguais ao do professor (Exemplo: caso não exista uma figurinha a resposta padrão deve ser 404, mas o nosso código devolvia 505). Isso porque a função falhava e não sabia lidar com isso.
- Percebemos a implementação errada do UUID, que tava colocando um ID enorme. Optamos pelo auto increment do próprio banco de dados.
- Percebemos também que o domain do jeito que tava, mesmo que fosse a sugestão do professor, tava ruim para relacionarmos com as camadas acima.
- Nosso banco de dados tava dando um errinho chato porque não tínhamos percebido que tudo estava dentro de /app.
- Implementamos os enums também. Com o Swagger ficou bem mais fácil de testar as rotas também.
  
Essa é a versão crua, exatamente como anotamos. Abaixo, a mesma história com um pouco mais de organização (com auxílio de IA):
 
## Processo de Desenvolvimento
 
A primeira decisão foi sobre linguagem e framework. Escolhemos Flask, um microframework Python, pela familiaridade que já tínhamos com a linguagem. Com o tempo de aula sendo o que é, Python nos dava mais agilidade e deixava o projeto mais fácil de modularizar.
 
Com isso definido, preparamos o ambiente já pensando na estrutura de pastas do Clean Code. O entendimento que chegamos foi: na pasta `blueprint` ficam os handlers, que é como o Flask organiza a criação de rotas; na pasta `services` ficam as regras de negócio, ou seja, como o fluxo e a comunicação do sistema devem funcionar de verdade.
 
Decidimos começar pela camada `domain`, onde definimos a entidade `figurinha`. O professor já havia passado um exemplo base na atividade, então usamos como referência e complementamos com uma pesquisa sobre como criar entidades corretamente em Flask. A classe que criamos contém a estrutura da tabela — `id`, `numero`, `tipo`, `posicao`, `created_at`, `updated_at` e duas funções para atender as regras de negócio exigidas.
 
Em seguida, fomos para o `repository`, responsável por toda a lógica de consulta e conexão com o banco. Criamos as operações necessárias: criar figurinha, deletar, atualizar, listar todas e buscar por id.
 
Foi nessa etapa que também batemos de frente com a nossa maior dificuldade conceitual. Por vícios de projetos anteriores, a primeira intuição foi criar uma pasta de `models` separada. Após uma conversa com o professor, entendemos que no contexto que estávamos aplicando, fazia mais sentido declarar a entidade no `domain` e deixar as regras de negócio para o `service`. Com isso, apagamos o `models` e reorganizamos a estrutura.
 
Depois implementamos o `service`. Usamos IA generativa como apoio: pedimos um trecho de código mínimo como referência e, a partir dele, construímos o nosso. Conseguimos definir classes com funções para criar, listar e deletar figurinhas, além de tratar corretamente o erro caso uma figurinha inexistente seja buscada.
 
Com o `service` pronto, partimos para o `handler`, onde definimos todas as rotas e métodos da API: criar, buscar por ID, listar, deletar e atualizar, todas com tratamento de erro adequado.
 
Aí veio uma surpresa: o Swagger do Flask funciona de forma diferente do FastAPI e precisava ser configurado manualmente. Usamos IA para montar as rotas e suas especificações, porque era uma tarefa bem chata de fazer na mão. Mas valeu a pena, com o Swagger funcionando, testar as rotas ficou muito mais simples.
 
Os testes trouxeram alguns bugs interessantes. O primeiro: ao buscar uma figurinha inexistente, o esperado era um 404, mas o nosso código devolvia 505, a função falhava e não sabia lidar com o erro. O segundo: a implementação do UUID estava gerando IDs enormes, quando o que queríamos era algo simples. Resolvemos trocando pelo auto increment do próprio banco de dados. O terceiro: o domain, mesmo seguindo a sugestão do professor como ponto de partida, estava ruim para se relacionar com as camadas acima, então ajustamos. E o quarto: o banco de dados dava um erro chato porque não tínhamos percebido que tudo estava dentro de `/app`.
 
Por último, implementamos os enums para os campos `tipo` e `posicao`, garantindo que só valores válidos fossem aceitos.
 
# Quais foram as dificuldades do trabalho?
 
A maior dificuldade foi conceitual: por vícios de projetos anteriores, a primeira intuição foi criar uma pasta de `models` separada. Mas no contexto do Clean Code que estávamos aplicando, o certo era declarar a entidade no `domain` e delegar as regras de negócio ao `service`. O professor ajudou a destrinchar isso durante a aula e, no final, foi um dos aprendizados mais sólidos da atividade.
 
A fase de testes também trouxe surpresas: configurar o Swagger manualmente no Flask, o UUID gerando IDs inesperados, o 505 no lugar do 404 e o banco quebrando por causa do caminho `/app`. Nenhum desses bugs era difícil isoladamente, mas apareceram todos juntos, o que tornou essa etapa a mais demorada.
 
# Contribuições de cada membro
 
| Integrante | Foto | Contribuições |
|---|---|---|
| **Fernando Soares de Oliveira** | <img src="./assets/Fernando.jpg" width="90" /> | Código, ideias de resolução e perguntas constantemente |
| **Pietra Batista** | <img src="./assets/pietra.jpg" width="90" /> | Código, ideias de resolução e perguntas constantemente |
 
# Como rodar o projeto localmente
 
### Pré-requisitos
 
- Python 3.10+
- pip
### Instalação
 
```bash
# Clone o repositório
git clone <url-do-repositorio>
cd <nome-da-pasta>
 
# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
 
# Instale as dependências
pip install -r requirements.txt
 
# Rode o servidor
flask run
```
  
### Endpoints disponíveis
 
| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/figurinha` | Cria uma nova figurinha |
| `GET` | `/figurinha` | Lista todas (aceita filtros `?posicao=` e `?tipo=`) |
| `GET` | `/figurinha/:id` | Busca por ID |
| `PUT` | `/figurinha/:id` | Atualiza por ID |
| `DELETE` | `/figurinha/:id` | Deleta por ID |
