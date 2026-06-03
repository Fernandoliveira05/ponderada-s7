# Projeto Flask - Estrutura mínima (Clean Code)

Estrutura mínima para começar um projeto Flask seguindo princípios de organização e separação de responsabilidades.

## Arquitetura (Clean Code)

- **Handlers (Blueprints):** `app/blueprints/` — rotas HTTP, conversão request/response
- **Domain:** `app/domain/` — entidades e regras de negócio (SEM dependências externas)
- **Services:** `app/services/` — casos de uso e orquestração
- **Repositories:** `app/repositories/` — interfaces e implementações de persistência
  - Interface: `IFigurinhaRepository` (contrato abstrato)
  - Implementação: `FigurinhaSQLiteRepository` (detalhe de infra, ORM interno)

## Setup

1. Criar um ambiente virtual e ativar:

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# ou
.venv\Scripts\activate  # Windows
```

2. Instalar dependências:

```bash
pip install -r requirements.txt
```

3. Inicializar banco de dados SQLite:

```bash
python init_db.py
```

## Executar a aplicação

```bash
python run.py
```

A aplicação estará disponível em `http://localhost:5000`

## Rodar testes

```bash
pytest
```

## Estrutura do banco de dados

O projeto usa SQLite com a tabela `figurinhas`:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | Integer | Chave primária |
| numero | String(50) | Número da figurinha (único) |
| posicao | String(100) | Posição/localização da figurinha |
| created_at | DateTime | Data de criação |
| updated_at | DateTime | Data de última atualização |

## Princípios respeitados

- ✓ Domain puro (sem dependências de frameworks)
- ✓ Interfaces de repositório (inversão de dependência)
- ✓ ORM como detalhe de implementação (interno ao repositório)
- ✓ Separação clara de responsabilidades por camada


