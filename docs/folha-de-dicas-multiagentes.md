# Folha de dicas autoral: sistemas multiagentes e RAG

Este documento é um resumo autoral da leitura **Folha de dicas: Sistemas Multi-Agentes e RAG Agêntico com LangGraph**, do curso [IA agêntica com LangChain e LangGraph, da IBM na Coursera](https://www.coursera.org/learn/agentic-ai-with-langchain-and-langgraph). Ele organiza as ideias para revisão e não reproduz o material original.

## Por que dividir o trabalho?

Um único agente pode receber contexto demais, misturar papéis e ficar difícil de depurar. Um sistema multiagente divide o problema em subtarefas com contratos claros. Pense em uma equipe: uma pessoa pesquisa, outra analisa, outra escreve e outra revisa.

Dividir não é automaticamente melhor. Cada agente acrescenta latência, custo de comunicação e uma nova possibilidade de falha. A pergunta de Staff é: a separação reduz um erro relevante o suficiente para justificar essa complexidade?

## Três formas de comunicação

- **Pipeline:** cada agente passa seu resultado ao próximo, como pesquisa → análise → redação → revisão.
- **Paralelo com agregação:** especialistas trabalham ao mesmo tempo e um agregador combina os resultados.
- **Diálogo:** agentes trocam mensagens para esclarecer requisitos ou refinar uma decisão.

## RAG agêntico

No RAG agêntico, a recuperação deixa de ser uma etapa fixa. Um agente escolhe a fonte, recupera evidências, outro raciocina sobre elas e um verificador procura inconsistências antes da resposta.

Um fluxo robusto precisa de uma saída clara quando não existe evidência suficiente. O sistema deve admitir a lacuna, encaminhar para uma alternativa ou pedir esclarecimento, em vez de preencher o vazio com invenção.

## Como o LangGraph organiza o fluxo

- **Nó:** um agente ou tarefa.
- **Aresta:** a transição possível entre etapas.
- **Estado compartilhado:** dados que passam pelo fluxo, como pedido, evidências, resultado, erros e próxima ação.
- **Roteamento condicional:** decisão que escolhe o próximo nó com base no estado.

Uma forma prática de modelar o estado é registrar também `errors` e `next_action`. Isso torna o caminho percorrido observável e permite tratar falhas sem esconder o motivo.

## Padrões para escolher a arquitetura

Use agentes especializados quando há papéis realmente diferentes, fontes distintas ou necessidade de verificação independente. Mantenha o fluxo simples quando uma cadeia linear já atende ao caso. Evite criar agentes apenas para aumentar a quantidade de componentes.

Na revisão de uma implementação, confira:

1. se cada agente tem uma responsabilidade testável;
2. se o estado contém apenas o contexto necessário;
3. se há limite para retries e ciclos;
4. se erros, fontes e decisões ficam registrados;
5. se latência, custo e qualidade são medidos separadamente.

## Referências do ecossistema

- [LangGraph: visão geral](https://docs.langchain.com/oss/python/langgraph/overview)
- [LangGraph: workflows e agentes](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
- [LangChain: visão geral](https://docs.langchain.com/oss/python/langchain/overview)
- [Curso da IBM na Coursera](https://www.coursera.org/learn/agentic-ai-with-langchain-and-langgraph)

