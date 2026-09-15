# LangGraph na prática: diário de estudo e guia de construção

Este repositório registra minha trajetória de estudo em **IA agêntica com LangChain e LangGraph**, acompanhando o curso da IBM na Coursera, e transforma os aprendizados em um guia independente para quem quer praticar com segurança.

> O curso foi a fonte de estudo e contexto. O texto, os exemplos e as conclusões deste repositório são autorais. O notebook e os materiais proprietários do curso não são redistribuídos aqui.

## O que você vai encontrar

- [Trajetória de estudo](docs/trajetoria.md): decisões, erros, correções e aprendizados por etapa.
- [Modelos mentais](docs/modelos-mentais.md): LangChain, LangGraph, reflexão e ReAct em linguagem direta.
- [Práticas autorais](examples/README.md): pequenos exemplos para reproduzir as ideias sem depender do notebook do curso.
- [Como estudar com responsabilidade](docs/estudo-responsavel.md): limites de credenciais, dados e publicação.

## Curso de referência

- [IA agêntica com LangChain e LangGraph — IBM, Coursera](https://www.coursera.org/learn/agentic-ai-with-langchain-and-langgraph)

Este repositório não substitui o curso. Use o material oficial para aulas, laboratórios, avaliações e instruções atualizadas.

## Por que este guia existe

A parte mais útil do estudo não foi decorar APIs. Foi observar o fluxo: um agente recebe estado, decide o próximo passo, usa uma ferramenta quando precisa e encerra quando tem informação suficiente. Quando um requisito é objetivo — por exemplo, limite de caracteres ou formato de saída — a validação precisa ser feita por código, não apenas pela reflexão do modelo.

## Status

Estudo em andamento. O Módulo 1 foi concluído; o Módulo 2 foi praticado com agentes de reflexão e ReAct. O Módulo 3 ainda será documentado conforme for estudado.

## Licença

Código e textos autorais deste repositório: MIT. A licença não se aplica ao conteúdo proprietário do curso, que permanece no ambiente da Coursera/IBM.
