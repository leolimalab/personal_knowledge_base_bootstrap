#!/usr/bin/env python3
import pandas as pd
import json
from collections import Counter

df = pd.read_csv('Survey da aula_ PKB com agentes(Sheet1).csv', sep=';')

print('## Análise Estatística do Survey PKB com Agentes')
print('='*60)
print()

print('### Resumo da Amostra')
print(f'- Total: {len(df)}')
faixa = df['Faixa etária'].value_counts().sort_index()
for f, c in faixa.items():
    print(f'  {f}: {c} ({100*c/len(df):.1f}%)')
gen = df['Gênero'].value_counts()
for g, c in gen.items():
    print(f'  {g}: {c} ({100*c/len(df):.1f}%)')
print()

print('### Cor Favorita')
cc = df['Entre estas, qual é a sua cor favorita?'].value_counts()
for cor, count in cc.items():
    print(f'- {cor}: {count} ({100*count/len(df):.1f}%)')
print()

print('## Sistema Operacional')
osc = df['Sistema operacional principal'].value_counts()
print(f'  Windows: {osc["Windows"]} ({100*osc["Windows"]/len(df):.1f}%)')
print(f'  Linux: {osc["Linux"]} ({100*osc["Linux"]/len(df):.1f}%)')
print(f'  macOS: {osc["macOS"]} ({100*osc["macOS"]/len(df):.1f}%)')
print()

print('## Memória RAM')
cpuc = df['Memória RAM da máquina que você vai usar'].value_counts()
for cpu, count in cpuc.items():
    print(f'- {cpu}: {count} ({100*count/len(df):.1f}%)')
print()

print('## GPU')
gpuc = df['GPU da máquina que você vai usar'].value_counts()
for gpu, count in gpuc.items():
    print(f'- {gpu}: {count} ({100*count/len(df):.1f}%)')
print()

print('## Familiaridade com Ferramentas')
ferramentas = [
    'GitHub / git', 'Obsidian', 'Modelos locais (Ollama, vLLM, LM Studio)',
    'Gerenciadores de pacotes', 'Jupyter Notebook',
    'Ambientes científicos com IA', 'Interface de chat',
    'MCP e skills', 'Workflows agênticos'
]

for ferr in ferramentas:
    col = f'Familiaridade com ferramentas.{ferr.replace(" ", "_").replace("/", "_")}'
    counts = df[col].value_counts()
    print(f'### {ferr}')
    total = counts.to_dict()
    for nivel, count in sorted(total.items(), key=lambda x: -x[1]):
        pct = 100*count/len(df)
        print(f'  - {nivel}: {count} ({pct:.1f}%)')
    print()

data = {
    'total': len(df),
    'os': os_counts.to_dict(),
    'cpu': cpu_counts.to_dict(),
    'gpu': gpu_counts.to_dict(),
    'faixa_etaria': df['Faixa etária'].value_counts().to_dict(),
    'genero': df['Gênero'].value_counts().to_dict(),
    'cor_favorita': cor_counts.to_dict(),
    'ferramentas': {}
}

for ferr in ferramentas:
    col = f'Familiaridade com ferramentas.{ferr.replace(" ", "_").replace("/", "_")}'
    data['ferramentas'][ferr] = df[col].value_counts().to_dict()

with open('survey_analysis.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)
    
print('\nData salva em survey_analysis.json')
