# Log

Uma linha por operação: `## [YYYY-MM-DD] tipo | descrição`. Tipos: `create`, `ingest`, `query`, `lint`, `reorganize`, `review`, `compress`, `install`, `skill`.

## [2026-09-24] create | Setup inicial: estrutura criada por kb_agent/scripts/bootstrap-structure
## [2026-09-25] ingest | Survey PKB com agentes (n=25): CSV em 03 Resources/Data, JSON + nota leitura criados
## [2026-09-25] reorganize | Removido 03 Resources/Data/analyze_survey.py (script temporário)
## [2026-10-01] install | Modelo local ornith-1.5-9b via LM Studio (http://127.0.0.1:1234/v1) configurado em ~/.config/opencode/opencode.jsonc com tool_call+reasoning; perfil atualizado para lmstudio/ornith-1.5-9b
## [2026-10-01] install | obsidian-skills (local) adicionado como submodule em kb_agent/vendor + 6 symlinks em kb_agent/skills; perfil atualizado
## [2026-10-01] skill | daily-log: aberto (primeiro diário 2026-10-01)
## [2026-10-01] ingest | AMIE feasibility study (arXiv 2603.08448v3): nota de leitura em 03 Resources + PDF movido do inbox
