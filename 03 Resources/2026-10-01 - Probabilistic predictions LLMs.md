---
tipo: leitura
origem: assistente
tags: [paper]
titulo: Probabilistic medical predictions of large language models
autores: Gu, Desai, Lin, Yang
ano: 2024
venue: npj Digital Medicine
doi: 10.1038/s41746-024-01366-4
url: https://doi.org/10.1038/s41746-024-01366-4
zotero:
status: a-ler
data: 2026-10-01
aliases: []
---
# Probabilistic predictions LLMs

## Em uma frase
Probabilidades explícitas geradas em texto são piores que as implícitas (likelihood do token correto) em 6 LLMs abertos x 5 datasets médicos.

## Pergunta e contexto
Predição clínica exige probabilidade confiável p/ transparência e decisão. Prompt explícito pede número, mas raciocínio numérico do LLM é fraco.

## Método
- 6 LLMs open-source avançados, 5 datasets médicos.
- Explícita (número no texto) vs implícita (likelihood do token do label correto).
- Sem CoT; só open-source (implícita exige acesso a logits).

## Resultados
- Implícita > explícita consistentemente.
- Limites numéricos do texto gerado confirmados.

## Limitações e críticas
- Sem chain-of-thought; binário pode não generalizar p/ múltipla escolha.
- Só open-source; generalização de domínio pendente.

## Relação com a minha base
- Referência do [[Mestrado]] p/ eixo calibração/incerteza; relevante p/ segurança estilo AMIE.
- Ecoa [[2026-10-01 - LLMs for evidence-based clinical QA]] (overconfidence).

## Citações-chave
> "Explicit probabilities consistently underperformed implicit probabilities." (abstract)

## Ideias para notas permanentes
- Calibrar via probabilidade implícita quando houver acesso a logits.
- Número falado pelo modelo ≠ confiança real.

## Fora do resumo
- Curvas por modelo/dataset, detalhes de extração de logits.
