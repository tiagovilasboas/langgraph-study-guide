# LangChain e LangGraph: papéis diferentes no mesmo sistema

## LangChain organiza as peças

LangChain é uma camada para compor aplicações que usam modelos de linguagem. Ele ajuda a conectar prompts, modelos, mensagens, ferramentas, parsers e memória em uma sequência de chamadas.

Um uso típico é uma cadeia: receber uma pergunta, montar um prompt, chamar o modelo e converter o resultado para um formato que o código consiga usar. Essa abordagem funciona bem quando o caminho é linear e a decisão já está definida.

## LangGraph organiza o fluxo

LangGraph modela o processo como um grafo com estado. Cada nó faz uma parte do trabalho e cada aresta define para onde o fluxo segue. O grafo pode ter ramificações, ciclos, checkpoints e condições de parada explícitas.

Ele entra quando a aplicação precisa decidir entre caminhos, repetir uma etapa, chamar ferramentas ou manter um estado que muda ao longo da execução.

Uma forma simples de lembrar:

- **LangChain:** quais componentes vou conectar?
- **LangGraph:** como o estado passa por decisões e ciclos?

Eles podem ser usados juntos. LangChain fornece componentes; LangGraph coordena o comportamento.

## Um esqueleto autoral

O exemplo abaixo mostra a ideia sem depender de credenciais ou de um provedor específico:

```python
from typing import TypedDict

class State(TypedDict):
    question: str
    answer: str
    needs_tool: bool

def decide(state: State) -> State:
    state["needs_tool"] = "preço" in state["question"].lower()
    return state

def answer(state: State) -> State:
    state["answer"] = "Resposta baseada no estado disponível."
    return state
```

O ponto do exemplo é separar estado, decisão e resposta. O modelo pode entrar depois, dentro de um nó bem definido.
