---
tipo: leitura
origem: assistente
tags: [survey, pkb, ia-pesquisa]
data: 2026-09-24
fonte: Data/Survey da aula_ PKB com agentes(Sheet1).csv
---

# 2026-09-24 - Survey PKB com agentes

## Em uma frase
Turma de 25, maioria Windows com maquina forte, pronta para rodar PKB local.

## Método
- Survey via Google Sheets, 25 respostas em 2026-09-24.
- Parse manual via `csv` (pandas quebrou no `;` dentro de campo).
- Estatística descritiva. Resultado em `Data/survey_analysis.json`.

## Resultados
Total: 25.

### Demografia
- 21 a 25: 8 (32.0%)
- 26 a 30: 8 (32.0%)
- 31 a 40: 3 (12.0%)
- 41 a 50: 5 (20.0%)
- 51 ou mais: 1 (4.0%)
- Masculino: 21 (84.0%)
- Feminino: 3 (12.0%)
- Não binário: 1 (4.0%)

### Sistema operacional
- Windows: 16 (64.0%)
- macOS: 7 (28.0%)
- Linux: 2 (8.0%)

### Hardware
RAM:
- 16 GB: 10 (40.0%)
- 32 GB: 6 (24.0%)
- 64 GB ou mais: 4 (16.0%)
- 8 GB ou menos: 4 (16.0%)
- Não sei: 1 (4.0%)
- >=16 GB: 20 (80.0%)

GPU:
- Nenhuma ou não sei: 9 (36.0%)
- NVIDIA: 8 (32.0%)
- Apple Silicon (M1 a M4): 7 (28.0%)
- AMD: 1 (4.0%)

### Cor favorita
- Azul: 10 (40.0%)
- Preto: 5 (20.0%)
- Verde: 4 (16.0%)
- Roxo: 3 (12.0%)
- Vermelho / Rosa / Laranja: 1 cada (4.0%)

## Limitações e críticas
- n=25, amostra de sala, sem inferência.
- Familiaridade com ferramentas não analisada — colunas `Familiaridade com ferramentas.*` com parse quebrado.

> [!gap] Falta analisar familiaridade (Git, Obsidian, Ollama, terminal, Python, Markdown, Zotero, opencode). Corrigir parser e atualizar `Data/survey_analysis.json`.

## Relação com a minha base
- Alimenta [[Objetivos]] de mestrado / pesquisa acadêmica.
- Base para decidir setup local (Ollama + opencode) por OS/GPU.
- Ver metodologia em [[GTD]] · [[PARA]] · [[Zettelkasten]].

## Fora do resumo
- Colunas de familiaridade deixadas de fora (ver gap acima).
- Emails/nomes anonimizados, não analisados.
