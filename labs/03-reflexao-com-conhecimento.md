# 03 — Reflexão com conhecimento externo

**Fonte de estudo:** laboratório de agente de reflexão com integração de conhecimento externo.

## Objetivo

Dar ao agente uma etapa de consulta antes de criticar ou revisar uma resposta.

## Fluxo autoral

```text
pergunta → rascunho → consulta → crítica → revisão ou encerramento
```

A ferramenta deve ter um contrato explícito: recebe uma consulta, devolve evidências ou um erro e informa ao fluxo se há contexto suficiente.

## Aprendizado

“Consultar conhecimento externo” só melhora o agente quando a evidência recebida influencia uma decisão. Sem uma condição clara, o fluxo pode repetir chamadas sem melhorar a resposta.
