# 📅 Sistema de Gerenciamento de Eventos – Comunidade Tech

Este projeto é um sistema em Python desenvolvido para gerenciar eventos organizados pela Comunidade Tech — uma iniciativa acadêmica que promove workshops, hackathons, minicursos e outras atividades na área de tecnologia.

## 🎯 Objetivos

- Automatizar o controle de eventos, inscrições e participantes.
- Oferecer relatórios e estatísticas úteis para a organização.
- Consolidar conhecimentos de programação com foco em estruturas de dados, modularização e boas práticas em Python.

## ⚙️ Funcionalidades

### Funcionalidades principais:
-  Listagem de eventos com nome, data e tema.
-  Visualização dos participantes de cada evento.
-  Busca de participantes pelo código único.
-  Relatórios estatísticos:
  - Participantes mais ativos.
  - Temas mais frequentes.
  - Eventos com baixa participação (menos de 2 inscritos).
  - Taxa média de participação por tema.

### Funcionalidades avançadas:
-  Adição de novos eventos e participantes.
-  Remoção de eventos e participantes.
-  Atualização de dados (tema do evento, e-mail do participante).
-  Detecção e remoção automática de participantes duplicados.
-  Filtros por tema e faixa de data.
-  Agrupamento de eventos por tema.

## 🖥️ Interface

A navegação é feita por menu textual no terminal (linha de comando), facilitando a interação com o sistema mesmo sem interface gráfica.

## 🧠 Conceitos aplicados

- Estruturas de dados (listas, dicionários, conjuntos)
- Modularização e organização em múltiplos arquivos `.py`
- Compreensão de listas
- Boas práticas com Git e versionamento semântico

## 📂 Estrutura do projeto

📁 data/
└── event_data.py           # Dados simulados de eventos
└── participant_data.py     # Dados simulados de participantes

📁 src/
├── events.py               # Lógica relacionada aos eventos
├── main.py                 # Ponto de entrada do sistema
├── menu.py                 # Interface textual no terminal
└── participants.py         # Lógica relacionada aos participantes
└── report.py               # Geração de estatísticas e relatórios 
└── utils.py                # funções utilitárias auxiliares

README.md                   # Documentação do projeto

## 🚀 Como executar

1 - Clone este repositório

2 - Acesse a pasta do projeto

3 - Execute o arquivo main.py com Python 3:

## 📦 Dependências

- Este projeto utiliza a biblioteca InquirerPy para criar menus interativos no terminal, deixando a navegação mais amigável.

Para instalar as dependências, no repositório do projeto, rode:

```bash
pip install InquirerPy
```

## 🧠 Aprendizados e Propósito

Este projeto foi desenvolvido como parte do curso de Análise e Desenvolvimento de Sistemas, com foco em consolidar os conhecimentos sobre estruturas de dados, modularização, manipulação de arquivos, e boas práticas de programação em Python.

<<<<<<< HEAD
🎉
=======
💻
>>>>>>> 4afb296 (chore: versão final entregue)
