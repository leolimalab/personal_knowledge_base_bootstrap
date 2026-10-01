---
tipo: leitura
origem: assistente
tags: [paper]
titulo: Large Language Models Encode Clinical Knowledge
autores: Singhal, Azizi, Tu et al. (Google Research, DeepMind)
ano: 2022
venue: arXiv 2212.13138
doi:
url: https://arxiv.org/abs/2212.13138
zotero:
status: a-ler
data: 2026-10-01
aliases: [Med-PaLM]
---
# LLMs encode clinical knowledge (Med-PaLM)

## Em uma frase
Flan-PaLM com instruction prompt tuning passa a barra USMLE-style e funda o MultiMedQA, mas a avaliação humana expõe gaps de alinhamento e segurança.

## Pergunta e contexto
Faltava padrão p/ avaliar conhecimento clínico amplo dos LLMs além de benchmarks fragmentados. Primeiro modelo a passar em questões estilo USMLE.

## Método
- MultiMedQA: MedQA, MedMCQA, PubMedQA, HealthSearchQA, LiveQA, MedicationQA.
- Flan-PaLM + instruction prompt tuning médico.
- Avaliação humana por médicos e leigos (alinhamento, segurança, viés).

## Resultados
- SOTA em múltipla escolha médica na época.
- Long-form e raciocínio seguem fracos.
- Eval humana: omissões e respostas inseguras persistem.

## Limitações e críticas
- Benchmark múltipla escolha superestima prontidão clínica.
- Modelo fechado; reprodução limitada.

## Relação com a minha base
- Referência do [[Mestrado]]; precursor de [[2026-10-01 - Med-PaLM 2 expert-level QA]] e [[2026-10-01 - AMIE prospective feasibility study]].

## Citações-chave
> "There is no standard to evaluate model predictions and reasoning across a breadth of tasks." (intro)

## Ideias para notas permanentes
- Múltipla escolha ≠ prontidão clínica; tese reforçada pelo comentário Schaekermann 2026.

## Fora do resumo
- Detalhes de prompt tuning, tabelas por dataset, protocolo de eval humana.
