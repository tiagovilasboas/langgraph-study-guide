# LangChain e LangGraph na prática

Um guia autoral para entender e experimentar aplicações agênticas com Python, LangChain e LangGraph.

Este repositório nasceu durante o estudo do curso [IA agêntica com LangChain e LangGraph](https://www.coursera.org/learn/agentic-ai-with-langchain-and-langgraph), da IBM na Coursera. A proposta é transformar a experiência de laboratório em um caminho útil para outras pessoas: começar pelo modelo mental, observar o fluxo e só depois conectar serviços reais.

> O curso é a referência de estudo. Os textos, exemplos e conclusões aqui são autorais. Os notebooks, vídeos, leituras e respostas de avaliação do curso não são redistribuídos.

## O que você vai aprender

Ao seguir este guia, você vai conseguir explicar:

- o papel do LangChain na composição de prompts, modelos e ferramentas;
- quando um fluxo linear deixa de ser suficiente;
- como o LangGraph representa estado, nós, arestas e decisões;
- como Reflection, Reflexion e ReAct organizam ciclos de melhoria e ação;
- por que validações objetivas devem ser feitas por código;
- como experimentar sem colocar credenciais ou dados reais no notebook.

## Links oficiais para continuar

- [LangChain — visão geral](https://docs.langchain.com/oss/python/langchain/overview): framework, agentes e integrações.
- [LangChain — agentes](https://docs.langchain.com/oss/python/langchain/agents): ferramentas, loop de execução e condições de parada.
- [LangGraph — visão geral](https://docs.langchain.com/oss/python/langgraph/overview): runtime para workflows e agentes com estado.
- [LangGraph — Graph API](https://docs.langchain.com/oss/python/langgraph/use-graph-api): estado, nós, arestas, sequências, ramificações e loops.
- [Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph): como decompor um processo antes de escrever o grafo.
- [Workflows e agentes](https://docs.langchain.com/oss/python/langgraph/workflows-agents): quando usar caminhos determinísticos ou decisões do agente.
- [LangSmith](https://docs.langchain.com/langsmith/home): rastreamento, depuração e avaliação de aplicações LLM.

Os links apontam para a documentação oficial atual da equipe LangChain.

## LangChain e LangGraph em uma frase

**LangChain conecta as peças; LangGraph coordena o fluxo quando existe estado, decisão ou repetição.**

Uma cadeia simples pode ser suficiente para receber uma pergunta, montar um prompt e gerar uma resposta. Um grafo ajuda quando o sistema precisa consultar uma ferramenta, avaliar o resultado, escolher outro caminho ou repetir uma etapa até uma condição de parada.

```mermaid
flowchart LR
    A[Entrada] --> B[Estado]
    B --> C[Nó: decidir]
    C -->|precisa de ferramenta| D[Nó: ferramenta]
    D --> E[Observação]
    E --> C
    C -->|pronto| F[Resposta]
```

## Comece pelo exemplo executável

O exemplo usa apenas a biblioteca padrão do Python. Ele simula os padrões estudados com dados fictícios, sem API key e sem custo:

```bash
python3 examples/padroes_autorais.py
```

O arquivo mostra três ideias pequenas:

1. **Estado:** etapas diferentes atualizam o mesmo objeto.
2. **Reflexão:** uma resposta é revisada com uma regra objetiva de tamanho.
3. **ReAct:** o agente decide se precisa de uma ferramenta local simulada, observa o resultado e encerra.

Depois de entender esse fluxo, você pode substituir cada função por componentes reais de LangChain e LangGraph, seguindo a documentação oficial.

## Mapa do repositório

| Caminho | Para que serve |
|---|---|
| [`docs/auditoria-do-curso.md`](docs/auditoria-do-curso.md) | Estrutura atual dos módulos, lições e avaliações observadas na Coursera. |
| [`docs/langchain-e-langgraph.md`](docs/langchain-e-langgraph.md) | Diferença entre as bibliotecas e um esqueleto de fluxo com estado. |
| [`docs/labs.md`](docs/labs.md) | Relato do que foi feito nos laboratórios e dos aprendizados. |
| [`docs/trajetoria.md`](docs/trajetoria.md) | Decisões, erros, correções e evolução do estudo. |
| [`docs/modelos-mentais.md`](docs/modelos-mentais.md) | Estado, nós, roteamento, reflexão e ReAct em linguagem direta. |
| [`docs/estudo-responsavel.md`](docs/estudo-responsavel.md) | Regras para experimentar e publicar sem expor segredos ou material proprietário. |
| [`docs/decisoes-staff.md`](docs/decisoes-staff.md) | Trade-offs de arquitetura e critérios de prontidão operacional. |
| [`labs/`](labs/) | Versões autorais resumidas dos quatro exercícios práticos realizados. |
| [`examples/`](examples/) | Código mínimo executável para visualizar os padrões. |

## O que muda quando pensamos como Staff

A discussão completa está em [Decisões e trade-offs em nível Staff](docs/decisoes-staff.md).

Um protótipo que “responde bem” é só o começo. Antes de colocar um agente em um produto, vale responder perguntas de arquitetura:

| Decisão | Pergunta de revisão | Evidência esperada |
|---|---|---|
| Escopo | O que o agente pode decidir e o que continua determinístico? | Diagrama com fronteiras claras. |
| Estado | Qual é o mínimo de estado necessário para retomar uma execução? | Schema versionado e exemplos de transição. |
| Ferramentas | Quais ações têm efeito externo e quais são somente leitura? | Contrato de entrada, saída, timeout e erro. |
| Parada | Quando o fluxo termina, repete ou pede intervenção humana? | Condição de parada testada e limite de iterações. |
| Observabilidade | Como investigar uma resposta ruim ou uma chamada cara? | Trace por execução, métricas e correlação. |
| Segurança | Que dados podem entrar no prompt e quais segredos ficam fora dele? | Allowlist, redaction e gestão de segredos. |
| Custo e latência | Qual é o orçamento por execução e o pior caso? | Cenários medidos, timeout e fallback. |

A escolha entre LangChain e LangGraph deve sair dessas restrições. Um fluxo simples pode começar com abstrações de alto nível; um processo com ciclos, aprovação humana, persistência ou múltiplos agentes precisa tornar o controle explícito.

## O que fizemos nos laboratórios

A sequência prática foi:

1. **LangGraph 101:** fluxo com estado, validação, contexto, resposta e encerramento.
2. **Reflection:** geração, crítica e decisão entre melhorar ou terminar.
3. **Reflexion com conhecimento externo:** consulta, evidência e revisão condicionada.
4. **ReAct:** pensamento, ação, entrada da ação, observação e resposta final.

Um detalhe importante apareceu durante a prática: o modelo afirmou que uma resposta respeitava um limite de caracteres quando a contagem real mostrava o contrário. A conclusão vale para qualquer agente: reflexão pode ajudar a melhorar uma saída, mas não substitui um verificador determinístico.

No laboratório ReAct, a busca externa retornou `401 Unauthorized` porque o ambiente ainda tinha um marcador de chave. Nenhuma chave pessoal foi inserida. O erro ficou registrado como aprendizado de segurança e integração.

## Trilha recomendada

Se você está começando, siga esta ordem:

1. leia [LangChain e LangGraph](docs/langchain-e-langgraph.md);
2. execute o exemplo autoral;
3. leia [01 — Fluxo com estado](labs/01-fluxo-com-estado.md);
4. compare Reflection, Reflexion e ReAct nos outros arquivos de [`labs/`](labs/);
5. só então conecte um modelo ou uma ferramenta em um ambiente seguro;
6. registre entradas, saídas, erros e condições de parada.

## Relação com o curso

O curso da IBM na Coursera apresenta conceitos, leituras, vídeos, práticas e laboratórios que serviram como base para este estudo. Este repositório ajuda a organizar o aprendizado e oferece referências independentes; ele não substitui a plataforma, as instruções oficiais nem as avaliações.

Para ver a estrutura que foi conferida na conta, consulte a [auditoria do curso](docs/auditoria-do-curso.md).

## Status do estudo

Os Módulos 1 e 2 aparecem concluídos na plataforma. O Módulo 3 está incompleto e será documentado conforme for estudado.

## Como contribuir

Encontrou uma explicação confusa, um exemplo que pode ser mais simples ou uma fonte oficial útil? Abra uma issue descrevendo o ponto e, se possível, proponha uma alteração pequena. A ideia é manter o guia verificável, acessível e útil para quem está praticando.

## Licença

Código e textos autorais deste repositório: MIT. A licença não se aplica ao conteúdo proprietário do curso, que permanece no ambiente da Coursera/IBM.
