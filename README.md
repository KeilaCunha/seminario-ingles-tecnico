# Fix the Bug — English Tenses Debugger

Projeto de seminário para a disciplina **Inglês Técnico** (Ciência da Computação).
Uma página web com visual de editor de código (estilo VS Code) onde os "bugs" são
erros de **tempo verbal em inglês** escondidos em comentários de código. Cobre
toda a ementa da disciplina: Simple Present, Present Continuous, Simple Past,
Past Continuous, Simple Future e Present Perfect — vários arquivos são baseados
diretamente nas atividades corrigidas em sala (Aulas 03 e 04).

## Como executar

Não precisa instalar nada. Basta dar duplo clique no arquivo:

```
fix_the_bug.html
```

Ele abre direto no navegador (Chrome, Edge, Firefox...) e funciona 100%
offline — ideal para apresentar em qualquer computador da faculdade.

## Como funciona

1. Na **tela inicial**, cada grupo/aluno pode ativar (ou não) um **cronômetro
   de sprint** opcional, escolhendo quantos minutos terá para corrigir tudo.
2. Ao clicar em "Iniciar sessão", o sistema sorteia **5 arquivos aleatórios**
   dentre um banco de 20 — a cada nova sessão (ou reinício) a combinação e a
   ordem mudam, então duas pessoas abrindo o app não recebem as mesmas
   perguntas.
3. No **Explorer** (barra lateral esquerda), cada "arquivo" é uma pergunta.
4. Dentro do código, uma parte do comentário aparece **sublinhada em vermelho
   (ondulado)** — exatamente como um erro apontado por um linter/IDE.
5. Ao clicar na palavra sublinhada, aparece um menu "Quick Fix" com 3-4
   opções de correção (como no VS Code de verdade).
6. Ao escolher a opção certa: o texto fica verde com um "OK", aparece uma
   notificação explicando a regra gramatical, e o log aparece no painel
   **Terminal**.
7. Ao escolher errado: a palavra "treme" (shake) e o log mostra o erro,
   permitindo tentar de novo.
8. Se o cronômetro estiver ativado e o tempo acabar antes de terminar, a
   sessão encerra automaticamente com uma tela "TIME'S UP" mostrando quantos
   bugs foram corrigidos até aquele momento.
9. Se todos os 5 bugs forem corrigidos a tempo, aparece a tela final estilo
   `npm run build`, com animação de digitação, **confete** e uma nota final
   (A+, A, B ou C) baseada em quantos erros vocês cometeram no caminho.
10. O botão "Reiniciar (novas perguntas)" sorteia uma nova combinação de 5
    arquivos, para outro grupo tentar em seguida.

## Banco de bugs (conteúdo gramatical)

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
| `release_notes.py` | Simple Past, verbo to be (was/were) |
| `bugfix_log.js` | Simple Past, verbo irregular (send -> sent) |
| `sprint_summary.py` | Simple Past, verbo irregular (write -> wrote) |
| `incident_report.js` | Past Continuous (ação interrompida) |
| `standup_question.py` | Past Continuous, forma interrogativa |
| `roadmap.py` | Simple Future (will be + particípio) |
| `migration_plan.js` | Simple Future, forma negativa (won't) |
| `changelog.py` | Present Perfect (yet / already) |
| `project_history.js` | Present Perfect (since / for) |
| `onboarding.py` | Present Perfect (never / ever) |

A cada sessão, apenas **5 desses 20** são sorteados aleatoriamente.

## Dicas para a apresentação (15–20 min)

- **Introdução (2–3 min):** expliquem rapidamente as regras dos tempos
  verbais que aparecem no jogo (Simple Present, Present Continuous, Simple
  Past, Past Continuous, Simple Future e Present Perfect) em 1 slide de
  apoio.
- **Contexto (1–2 min):** liguem a ideia com código real — comentários e
  documentação costumam usar Simple Present (o que a função faz), enquanto
  logs/mensagens de status usam Present Continuous (o que está acontecendo
  agora), e changelogs/relatórios usam Simple Past, Past Continuous, Simple
  Future e Present Perfect.
- **Demonstração ao vivo (8–10 min):** projetem a tela, ativem o cronômetro
  de sprint (opcional) e chamem colegas para "debugar" cada arquivo, um por
  vez, explicando a regra que aparece na notificação depois de cada acerto.
  Cliquem em "Reiniciar" para sortear novas perguntas para o próximo grupo.
- **Fechamento (2–3 min):** deixem o "build" final rodar com confete e
  comentem a nota da turma.

## Estrutura do projeto

```
fix_the_bug.html          # aplicação completa (HTML + CSS + JS em um arquivo só)
quiz_ingles_tecnico.py     # versão anterior (quiz simples em Python/Tkinter)
README.md                  # este arquivo
```

## Possíveis melhorias (caso queiram ir além)

- Adicionar mais arquivos/bugs (verbos modais, imperativo, ordem direta/indireta).
- Permitir escolher quantas perguntas sortear (hoje é fixo em 5).
