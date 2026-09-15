"""Exemplos mínimos e autorais dos padrões estudados.

Roda apenas com a biblioteca padrão do Python. O objetivo é visualizar
estado, reflexão e ReAct antes de conectar um modelo ou uma API real.
"""
from dataclasses import dataclass, field


@dataclass
class FlowState:
    question: str
    answer: str = ""
    notes: list[str] = field(default_factory=list)


def stateful_flow(question: str) -> FlowState:
    """Fluxo linear: cada etapa atualiza o mesmo estado."""
    state = FlowState(question=question)
    state.notes.append("entrada validada")
    state.answer = f"Resposta de referência para: {question}"
    state.notes.append("resposta produzida")
    return state


def reflection_flow(draft: str, limit: int = 80) -> str:
    """Reflexão com uma validação objetiva de tamanho."""
    critique = "ok" if len(draft) <= limit else "reduzir texto"
    if critique == "reduzir texto":
        return draft[:limit].rstrip() + "…"
    return draft


def react_flow(question: str) -> str:
    """ReAct com uma ferramenta local simulada e condição de parada."""
    if "temperatura" in question.lower():
        observation = "22 °C (dado fictício)"
        return f"Observei {observation}; escolha roupas leves."
    return "Não é necessária uma ferramenta para esta pergunta."


if __name__ == "__main__":
    print(stateful_flow("O que é um grafo com estado?"))
    print(reflection_flow("Uma resposta curta para testar a validação."))
    print(react_flow("Qual é a temperatura?"))
