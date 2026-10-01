---
tipo: leitura
origem: assistente
tags: [paper]
titulo: MEDI-Q: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning
autores: Li, Balachandran, Feng et al. (UW, CMU, Cornell, Ai2)
ano:
venue:
doi:
url: https://github.com/stellalisy/mediQ
zotero:
status: a-ler
data: 2026-10-01
aliases: [MEDI-Q]
---
# MEDI-Q question-asking benchmark

## Em uma frase
Benchmarks estáticos superestimam confiabilidade; MEDI-Q testa se o LLM pergunta antes de decidir numa interação simulada paciente-especialista.

## Pergunta e contexto
Usuários usam LLMs de forma interativa, mas benchmarks avaliam em turno único. Obstáculo central: LLM responde mesmo sem contexto suficiente.

## Método
- Simulação de dois agentes: Patient System + Expert adaptativo.
- Expert deve conter o diagnóstico quando incerto e pedir detalhes via follow-ups.
- Métodos de abstention; modelos Llama-2/3 e GPT-3.5/4.

## Resultados
- LLMs tendem a responder mesmo com informação incompleta.
- Perguntar antes + abstention melhora confiabilidade (ver números no texto completo).

## Limitações e críticas
- Pacientes simulados, não reais.
- Abstrai multimodalidade e EHR.

## Relação com a minha base
- Referência do [[Mestrado]] p/ eixo interação/incerteza.
- Contrasta com [[2026-10-01 - AMIE prospective feasibility study]]: simulação vs mundo real.

## Citações-chave
> "LLMs are trained to answer any question, even with incomplete context or insufficient knowledge." (abstract)

## Ideias para notas permanentes
- Perguntar como capacidade mensurável, não como traço emergente.
- Abstention como pré-requisito de segurança, não como fallback.

## Fora do resumo
- Pipeline de construção do benchmark, prompts dos agentes, ablações por modelo.
