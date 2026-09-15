# Decisões e trade-offs em nível Staff

Este documento transforma os aprendizados do curso em perguntas de arquitetura. A decisão não é “qual biblioteca é melhor”; é qual grau de controle o problema exige.

## 1. Cadeia, workflow ou agente?

| Opção | Quando usar | Ganho | Custo ou risco |
|---|---|---|---|
| Cadeia | O caminho é linear e conhecido. | Menos código e menor latência. | Pouca flexibilidade para exceções. |
| Workflow em grafo | Existem etapas, estados, ramificações e limites definidos. | Controle, teste e observabilidade do fluxo. | Mais modelagem e manutenção de estado. |
| Agente | O próximo passo depende do contexto e das ferramentas disponíveis. | Adaptação a problemas variados. | Mais variabilidade, custo e superfície de risco. |

A pergunta Staff é: **o que precisa ser decidido pelo modelo e o que pode continuar explícito no código?** Quanto mais importante for a previsibilidade, mais lógica deve permanecer determinística.

## 2. LangChain versus LangGraph

LangChain acelera integrações e agentes de alto nível. Isso reduz o tempo até o primeiro resultado e facilita trocar modelos ou ferramentas. O trade-off aparece quando a aplicação precisa expor transições, controlar ciclos, persistir estado ou inserir aprovação humana.

LangGraph oferece esse controle com nós, arestas, estado e checkpoints. O preço é assumir mais responsabilidade pelo desenho do fluxo, contratos entre nós e evolução do schema.

Uma decisão razoável é começar simples e migrar quando houver um sinal concreto: ramificações difíceis de testar, repetição sem limite, necessidade de retomada, auditoria ou intervenção humana.

## 3. Estado: memória útil versus acoplamento

Guardar tudo no estado parece conveniente, mas aumenta o acoplamento entre nós e pode expor dados desnecessários ao modelo. Guardar pouco demais força chamadas repetidas e dificulta retomada.

Critérios de revisão:

- manter no estado dados estruturados e necessários para a próxima decisão;
- formatar prompts sob demanda, em vez de guardar texto derivado sem necessidade;
- versionar mudanças no schema;
- definir o que pode ser persistido e por quanto tempo;
- remover ou mascarar dados sensíveis antes de registrar traces.

## 4. Reflexão: qualidade versus custo

Um ciclo de crítica pode melhorar uma resposta, mas cada iteração aumenta latência e custo. Também existe o risco de o modelo aprovar uma saída que viola uma regra objetiva.

A arquitetura deve combinar:

- limite máximo de iterações;
- condição de parada explícita;
- validações determinísticas para formato, tamanho e campos obrigatórios;
- fallback quando a crítica ou a ferramenta falhar;
- métricas para comparar qualidade antes e depois da reflexão.

## 5. ReAct: autonomia versus blast radius

Ferramentas tornam o agente útil, mas também ampliam o impacto de uma decisão errada. Uma ferramenta de leitura tem um risco; uma ferramenta que altera dados, envia mensagens ou movimenta dinheiro tem outro.

Antes de liberar uma ferramenta, revisar:

- escopo mínimo de permissão;
- allowlist de destinos e operações;
- timeout, retry e idempotência;
- validação dos argumentos;
- aprovação humana para efeitos irreversíveis;
- trilha de auditoria com correlação por execução.

## 6. Observabilidade e operação

Uma resposta final não explica por que o agente escolheu uma ferramenta. Para operar o sistema, precisamos reconstruir a execução: entrada, estado relevante, nó executado, ferramenta chamada, duração, erro e decisão de parada.

O mínimo operacional é um trace por execução, métricas de latência e custo, contagem de retries, taxa de fallback e identificação de versões de prompt e modelo. O [LangSmith](https://docs.langchain.com/langsmith/home) é uma opção do ecossistema para tracing e avaliação; a escolha final depende de requisitos de privacidade e operação.

## 7. Critério de pronto

Um agente está pronto para uma próxima fase quando, além de responder em um caso feliz, consegue:

- parar sob limite de iteração;
- falhar sem vazar segredo;
- retomar ou explicar por que não pode retomar;
- validar saídas objetivamente;
- operar dentro de orçamento de custo e latência;
- permitir investigação de uma execução ruim;
- manter o blast radius das ferramentas sob controle.

Esses critérios são mais importantes que a quantidade de frameworks no `requirements.txt`.
