# Fix the Bug — English Tenses Debugger

Projeto de seminário para a disciplina **Inglês Técnico** (Ciência da Computação).
Uma página web com visual de editor de código (estilo VS Code) onde os "bugs" são
erros de **tempo verbal em inglês** (Simple Present, Present Continuous e
concordância verbal) escondidos em comentários de código de 10 arquivos
diferentes (JavaScript, Python, C, YAML).

## Como executar

Não precisa instalar nada. Basta dar duplo clique no arquivo:

```
fix_the_bug.html
```

Ele abre direto no navegador (Chrome, Edge, Firefox...) e funciona 100%
offline — ideal para apresentar em qualquer computador da faculdade.

## Como funciona

1. No **Explorer** (barra lateral esquerda), cada "arquivo" é uma pergunta.
2. Dentro do código, uma parte do comentário aparece **sublinhada em vermelho
   (ondulado)** — exatamente como um erro apontado por um linter/IDE.
3. Ao clicar na palavra sublinhada, aparece um menu "💡 Quick Fix" com 3-4
   opções de correção (como no VS Code de verdade).
4. Ao escolher a opção certa: o texto fica verde com um ✓, aparece uma
   notificação explicando a regra gramatical, e o log some no painel
   **Terminal**.
5. Ao escolher errado: a palavra "treme" (shake) e o log mostra o erro,
   permitindo tentar de novo.
6. Depois de corrigir os 10 arquivos, aparece uma tela final estilo
   `npm run build`, com animação de digitação, **confete** e uma nota final
   (A+, A, B ou C) baseada em quantos erros vocês cometeram no caminho.

## Os 10 bugs (conteúdo gramatical)

| Arquivo | Regra testada |
|---|---|
| `server.js` | Simple Present, 3ª pessoa (+s) |
| `algorithm.py` | Present Continuous ("right now") |
| `backup.py` | Present Continuous ("currently") |
| `network.c` | Present Continuous ("at this moment") |
| `api.js` | Concordância com substantivo coletivo ("team") |
| `cache.py` | Simple Present, 3ª pessoa (+s) |
| `auth.js` | Concordância com sujeito plural (sem +s) |
| `loop.py` | Present Continuous negativo ("isn't") |
| `deploy.yml` | Simple Present, 3ª pessoa (+s) |
| `monitor.py` | "Everything" é sempre singular (+is) |

## Dicas para a apresentação (15–20 min)

- **Introdução (2–3 min):** expliquem a regra do Simple Present (hábito,
  rotina, 3ª pessoa + `s`) e do Present Continuous (`to be + verbo-ing`,
  ação em andamento) em 1 slide de apoio.
- **Contexto (1–2 min):** liguem a ideia com código real — comentários e
  documentação costumam usar Simple Present (o que a função faz), enquanto
  logs/mensagens de status usam Present Continuous (o que está acontecendo
  agora).
- **Demonstração ao vivo (8–10 min):** projetem a tela e chamem colegas para
  "debugar" cada arquivo, um por vez, explicando a regra que aparece na
  notificação depois de cada acerto.
- **Fechamento (2–3 min):** deixem o "build" final rodar com confete e
  comentem a nota da turma.

## Estrutura do projeto

```
fix_the_bug.html          # aplicação completa (HTML + CSS + JS em um arquivo só)
quiz_ingles_tecnico.py     # versão anterior (quiz simples em Python/Tkinter)
README.md                  # este arquivo
```

## Possíveis melhorias (caso queiram ir além)

- Adicionar mais arquivos/bugs (Simple Past, Present Perfect, verbos modais).
- Colocar um cronômetro geral da "sprint" (ex: 5 minutos para corrigir tudo).
- Salvar a pontuação de cada grupo/aluno que testar, comparando no final.
