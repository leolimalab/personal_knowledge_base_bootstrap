---
tipo: leitura
origem: assistente
tags: [paper]
titulo: Toward expert-level medical question answering with large language models
autores: Singhal et al. (Google)
ano: 2025
venue: Nature Medicine 31, 943-950
doi: 10.1038/s41591-024-03423-7
url: https://doi.org/10.1038/s41591-024-03423-7
zotero:
status: a-ler
data: 2026-10-01
aliases: [Med-PaLM 2]
---
# Med-PaLM 2 expert-level QA

## Em uma frase
86.5% no MedQA (+19pp sobre Med-PaLM), com respostas preferidas às de médicos em vários eixos — via ensemble refinement + chain of retrieval.

## Pergunta e contexto
Med-PaLM passou USMLE-style mas travou em long-form e workflow real. Fecha esses gaps com base melhor, fine-tuning médico e grounding.

## Método
- Base LLM melhorada + fine-tuning de domínio.
- Ensemble refinement e chain of retrieval p/ raciocínio e grounding.
- MultiMedQA múltipla escolha + long-form avaliado por médicos e leigos + adversariais + perguntas reais de especialistas.

## Resultados
- Até 86.5% MedQA; ganhos em MedMCQA, PubMedQA, MMLU clínico.
- Long-form: preferência sobre Med-PaLM e, em eixos, sobre médicos.
- SOTA ou perto em todo MultiMedQA múltipla escolha.

## Limitações e críticas
- Preferência em eval ≠ segurança em workflow.
- Benchmark, ainda não prospectivo (ver AMIE depois).

## Relação com a minha base
- Referência do [[Mestrado]]; elo entre [[2026-10-01 - LLMs encode clinical knowledge (Med-PaLM)]] e [[2026-10-01 - AMIE prospective feasibility study]].

## Citações-chave
> "Med-PaLM 2 scores up to 86.5% on the MedQA dataset, improving upon Med-PaLM by over 19%." (abstract)

## Ideias para notas permanentes
- Grounding/recuperação como alavanca maior que escala pura.
- Preferência humana como sinal fraco de segurança.

## Fora do resumo
- Extended Data tabelas de datasets, protocolo de eval humana, adversariais.
