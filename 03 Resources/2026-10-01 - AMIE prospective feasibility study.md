---
tipo: leitura
origem: assistente
tags: [paper]
titulo: A prospective clinical feasibility study of a conversational diagnostic AI in an ambulatory primary care clinic
autores: Brodeur, Koshy, Palepu et al. (Google Research, DeepMind, Beth Israel Deaconess)
ano: 2026
venue: arXiv 2603.08448v3
doi:
url: https://arxiv.org/abs/2603.08448
zotero:
status: a-ler
data: 2026-10-01
aliases: [AMIE feasibility study]
---
# AMIE prospective feasibility study

## Em uma frase
Um chatbot clínico (AMIE) fazendo anamnese e sugerindo diagnósticos antes da consulta de urgent care se mostrou seguro e viável no mundo real, com raciocínio diagnóstico comparável ao de clínicos — mas perdendo em praticidade e custo-efetividade do plano.

## Pergunta e contexto
LLMs já funcionam bem em conversas diagnósticas simuladas; faltava testar em fluxo clínico real, com supervisão de segurança rigorosa. O estudo leva o AMIE (Articulate Medical Intelligence Explorer) para um pronto-atendimento acadêmico (Beth Israel Deaconess, Boston).

## Método
- Prospectivo, braço único: 100 pacientes completaram chat em texto com AMIE até 5 dias antes da consulta; 98 completaram consulta com o clínico (PCP).
- Supervisores médicos humanos monitoraram todas as conversas em tempo real, com 4 critérios pré-definidos de interrupção.
- Diagnóstico final por revisão de prontuário 8 semanas após; comparação cega AMIE vs PCP (DDx e plano de manejo).
- Modelo: Gemini 2.5 Pro, trocado por Flash no meio do estudo por latência na infra de pesquisa.
- Ingerido em [[2026-10-01]] a partir de `2603.08448v3.pdf` (63 p.).

## Resultados
- Segurança: zero interrupções pelos supervisores; 3 intervenções pontuais menores (esclarecer sintoma, critério de emergência, correção de data).
- Pacientes: alta satisfação; atitude frente à IA melhorou (p < 0.001). Clínicos acharam o output útil para preparo.
- DDx do AMIE incluiu o diagnóstico final em 90% dos casos; 75% de acurácia top-3.
- Avaliação cega: qualidade geral de DDx e plano semelhantes (DDx p = 0.6; adequação p = 0.1; segurança p = 1.0). PCPs superaram AMIE em praticidade (p = 0.003) e custo-efetividade (p = 0.004) do manejo.

## Limitações e críticas
- As admitidas: piloto, braço único, n = 100, centro único; sem gestantes nem queixas de saúde mental; possível efeito Hawthorne; chat só-texto sem acesso ao prontuário (EHR); barreira de acesso (precisava laptop/desktop).
- Minha leitura: a troca Pro → Flash no meio enfraquece a atribuição dos resultados a uma versão do modelo; amostra enviesada para alta literacia digital (45.9% score máximo).

## Relação com a minha base
- Primeira nota de leitura da base; candidata a referência metodológica quando o projeto do Mestrado envolver avaliação de IA.
- Ingestão registrada em [[2026-10-01]].

> [!gap] Projeto do Mestrado ainda não definido — sem destino para esta referência além de `03 Resources/`.

## Citações-chave
> "AMIE's differential diagnosis (DDx) included the final diagnosis [...] in 90% of cases, with 75% top-3 accuracy." (p. 1)
>
> "Human safety supervisors monitored all patient-AMIE interactions in real time and did not need to intervene to stop any consultations based on pre-defined criteria." (p. 1)

## Ideias para notas permanentes
- Supervisão humana em tempo real como "gold standard" de segurança para LLM falando com paciente.
- Texto puro sem EHR limita diagnóstico — multimodalidade como próximo passo.
- IA empata no diagnóstico mas perde no manejo prático: saber o quê ≠ saber como conduzir com custo e contexto.

## Fora do resumo
- Demografia completa, surveys pré/pós (paciente, clínico, supervisor), checklist TRIPOD-LLM, detalhes de infra e latência, fluxograma de recrutamento (140 consentiram → 98 completaram ambos).
