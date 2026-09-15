# Trajetória de estudo

Este registro acompanha o estudo feito com o curso da IBM na Coursera. As datas são um diário pessoal; o estado oficial deve sempre ser conferido na página do curso.

## 1. Começo: separar generativo de agêntico

A primeira virada foi entender que gerar texto e executar um fluxo com decisões são problemas diferentes. Um sistema agêntico pode observar o estado, escolher uma ação, chamar uma ferramenta e repetir o ciclo até alcançar uma condição de parada.

**Aprendizado:** antes de escolher uma biblioteca, desenhar o fluxo e as condições de parada.

## 2. LangChain versus LangGraph

LangChain ajuda a montar componentes e chamadas de modelo. LangGraph organiza um fluxo com estado, nós e transições, inclusive quando há ciclos e decisões condicionais.

**Aprendizado:** quando o processo tem etapas previsíveis, uma cadeia simples pode bastar; quando há estado, ramificações ou repetição, um grafo torna o comportamento mais explícito.

## 3. Primeiro fluxo com estado

A prática de LangGraph ajudou a tornar o conceito concreto: o estado entra no grafo, um nó transforma esse estado e uma aresta decide o próximo nó. O valor está na visibilidade do fluxo, não em esconder a lógica dentro de uma única chamada ao modelo.

## 4. Agente de reflexão

No laboratório de reflexão, o fluxo alternava entre gerar uma resposta e criticá-la. A execução mostrou um limite importante: a crítica do próprio modelo pode dizer que um texto cumpre uma regra objetiva quando a contagem real prova o contrário.

**Regra que ficou:** reflexão melhora a qualidade, mas validações determinísticas devem ficar em funções e testes.

## 5. ReAct: raciocínio e ação

O padrão ReAct conecta pensamento, ação, entrada da ação e observação. No LangGraph, uma função de roteamento analisa a mensagem mais recente e decide se o agente deve seguir para uma ferramenta ou encerrar.

Durante a prática, a busca externa falhou porque o exemplo usava um marcador de chave. Nenhuma chave pessoal foi inserida. Isso virou parte do aprendizado: credencial ausente é um estado explícito do sistema, não algo para contornar copiando segredo para o notebook.

## 6. O que ainda está aberto

- avançar pelo Módulo 3, sobre sistemas multiagentes e RAG agêntico;
- transformar os exemplos em testes pequenos e reproduzíveis;
- comparar ferramentas simuladas com integrações reais em um ambiente seguro;
- revisar este guia à medida que novas práticas forem concluídas.
