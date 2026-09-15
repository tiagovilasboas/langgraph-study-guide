# 04 — ReAct com ferramentas

**Fonte de estudo:** laboratório ReAct do curso IBM na Coursera.

## Objetivo

Combinar raciocínio, ação e observação para responder perguntas que exigem uma ferramenta.

## Ciclo

```text
pensamento → ação → entrada da ação → observação → resposta final
```

## Componentes praticados

- modelo de conversa;
- prompt com um rascunho intermediário;
- ferramentas de busca e recomendação;
- estado que acumula mensagens;
- roteamento entre agente, ferramenta e encerramento;
- função `should_continue` para decidir o próximo passo.

## O que observamos

A chamada do modelo para o exercício de clima terminou sem erro. A busca externa retornou `401 Unauthorized` porque o ambiente ainda usava um marcador de chave. Nenhuma chave pessoal foi inserida.

## Aprendizado

Falha de credencial precisa aparecer como estado do fluxo. O comportamento seguro é simular a ferramenta ou configurar o segredo em ambiente próprio, sem colocá-lo no notebook ou no repositório.
