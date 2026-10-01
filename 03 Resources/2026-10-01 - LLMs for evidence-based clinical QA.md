---
tipo: leitura
origem: assistente
tags: [paper]
titulo: Evaluating large language models for evidence-based clinical question answering
autores: Wang, Chen (JHU)
ano: 2026
venue: Patterns 7, 101519
doi: 10.1016/j.patter.2026.101519
url:
zotero:
status: a-ler
data: 2026-10-01
aliases: []
---
# LLMs for evidence-based clinical QA

## Em uma frase
LLMs acertam mais em guidelines clínicas do que em revisões sistemáticas e exibem overconfidence justamente quando a evidência é fraca; RAG melhora a precisão.

## Pergunta e contexto
Sistemas de IA navegam a incerteza da evidência médica real? Testam modelos de ponta em 20 mil questões sintetizadas de 8 mil+ revisões sistemáticas e guidelines.

## Método
- 20.000 questões sintetizadas de revisões sistemáticas + guidelines clínicas.
- Famílias proprietary e open-weight líderes.
- Erro cruzado com variância de effect-size e suporte de citações dos estudos-base.

## Resultados
- Guidelines > revisões sistemáticas em precisão.
- Overconfidence generalizado sob evidência fraca/ausente.
- RAG aumenta precisão.
- Padrão vale p/ todas as famílias testadas.

## Limitações e críticas
- Questões sintetizadas, não perguntas reais de clínicos.
- Só QA; nada de workflow ou interação.

## Relação com a minha base
- Referência do [[Mestrado]] p/ eixo incerteza/calibração.
- Dialoga com [[2026-10-01 - AMIE prospective feasibility study]]: benchmark estático vs mundo real.

## Citações-chave
> "LLMs are more accurate on clinical guidelines than on systematic reviews" (graphical abstract)

## Ideias para notas permanentes
- Overconfidence sob evidência fraca como eixo obrigatório de avaliação.
- RAG como baseline, não como diferencial.

## Fora do resumo
- Tabelas por modelo, detalhes do pipeline de síntese das questões.
