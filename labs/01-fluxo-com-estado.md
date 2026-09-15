# 01 — Fluxo com estado

**Fonte de estudo:** laboratório LangGraph 101 do curso IBM na Coursera.

## Objetivo

Passar uma pergunta por um fluxo que valida a entrada, obtém contexto e produz uma resposta. O estado compartilhado permite que cada nó receba o resultado do anterior.

## Versão autoral reduzida

```python
from typing import TypedDict

class QAState(TypedDict):
    question: str
    context: str
    answer: str

def validate(state: QAState) -> QAState:
    if not state["question"].strip():
        state["answer"] = "Faça uma pergunta para continuar."
    return state

def provide_context(state: QAState) -> QAState:
    state["context"] = "Contexto de demonstração sobre grafos com estado."
    return state

def answer(state: QAState) -> QAState:
    if not state["context"]:
        state["answer"] = "Não encontrei contexto suficiente."
    else:
        state["answer"] = f"Resposta baseada em: {state['context']}"
    return state
```

## O que observamos

- uma pergunta irrelevante pode terminar com fallback quando não há contexto;
- uma pergunta sobre LangGraph pode seguir até o nó de resposta;
- nós pequenos tornam as transições fáceis de inspecionar.

## Aprendizado

O estado é o contrato entre os nós. Se a próxima decisão depende de uma informação, ela precisa estar representada nesse contrato.
