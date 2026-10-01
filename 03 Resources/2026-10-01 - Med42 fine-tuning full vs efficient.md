---
tipo: leitura
origem: assistente
tags: [paper]
titulo: Med42 - Evaluating Fine-Tuning Strategies for Medical LLMs: Full-Parameter vs. Parameter-Efficient Approaches
autores: Christophe, Kanithi, Munjal et al. (G42 Healthcare, Core42, Cerebras)
ano: 2024
venue: arXiv 2404.14779
doi:
url: https://arxiv.org/abs/2404.14779
zotero:
status: a-ler
data: 2026-10-01
aliases: [Med42]
---
# Med42 fine-tuning full vs efficient

## Em uma frase
Full-parameter fine-tuning supera PEFT (LoRA) em tarefas médicas; Med42 chega a 72% no USMLE, recorde p/ modelo aberto na época.

## Pergunta e contexto
Qual estratégia de fine-tuning vale p/ LLM médico: ajustar tudo ou só adaptadores eficientes? Compara sistemático sobre base Llama-2.

## Método
- Série de modelos Llama-2 p/ conhecimento, raciocínio e QA médicos.
- Full-parameter vs parameter-efficient (LoRA).
- Benchmarks médicos padrão + análise de descontaminação.

## Resultados
- Full-parameter > PEFT em tarefas médicas (Figura 1 do paper).
- Med42: 72% USMLE.
- PEFT segue viável com custo menor, gap mensurável.

## Limitações e críticas
- Só benchmarks; nada de uso real.
- Base Llama-2 datada frente a modelos atuais.

## Relação com a minha base
- Referência do [[Mestrado]] p/ eixo técnico: como adaptar modelo médico.

## Citações-chave
> "Full-parameter fine-tuning achieved better performance than parameter-efficient fine-tuning in medical tasks." (discussion)

## Ideias para notas permanentes
- Custo vs performance de adaptação como decisão de projeto, não detalhe.
- Descontaminação como higiene metodológica obrigatória.

## Fora do resumo
- Curvas por benchmark, % de queda pós-descontaminação, hiperparâmetros.
