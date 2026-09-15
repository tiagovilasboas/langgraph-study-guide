# 02 — Agente de reflexão

**Fonte de estudo:** laboratório de criação de um agente de reflexão com LangGraph.

## Objetivo

Gerar uma resposta, avaliá-la e decidir se uma nova versão deve ser criada.

## Fluxo autoral

```text
gerar → criticar → (melhorar ou encerrar)
```

Uma implementação própria deve manter no estado a resposta atual, a crítica e um contador de iterações. A condição de parada precisa limitar o número de ciclos.

## O que observamos

O fluxo produziu várias gerações e críticas. Em um caso, o texto ultrapassou o limite de caracteres, embora o modelo afirmasse que a regra havia sido cumprida.

## Aprendizado

A reflexão ajuda a melhorar redação e cobertura. Ela não é um validador confiável para regras mensuráveis. Use uma função determinística para contar caracteres, verificar campos e validar formatos.
