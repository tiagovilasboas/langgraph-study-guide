# LangGraph na prática: diário de estudo e guia de construção

Este repositório registra minha trajetória de estudo em **IA agêntica com LangChain e LangGraph**, acompanhando o curso da IBM na Coursera, e transforma os aprendizados em um guia independente para quem quer praticar com segurança.

> O curso foi a fonte de estudo e contexto. O texto, os exemplos e as conclusões deste repositório são autorais. O notebook e os materiais proprietários do curso não são redistribuídos aqui.

## O que você vai encontrar

- [Auditoria do curso](docs/auditoria-do-curso.md): estrutura, objetivos e estado observado de cada módulo.
- [Trajetória de estudo](docs/trajetoria.md): decisões, erros, correções e aprendizados por etapa.
- [LangChain e LangGraph](docs/langchain-e-langgraph.md): o propósito de cada biblioteca e como elas se complementam.
- [Laboratórios](docs/labs.md): o que foi feito no curso, com erros e aprendizados.
- [Modelos mentais](docs/modelos-mentais.md): estado, reflexão e ReAct em linguagem direta.
- [Práticas autorais](examples/README.md): pequenos exemplos para reproduzir as ideias sem depender do notebook do curso.
- [Como estudar com responsabilidade](docs/estudo-responsavel.md): limites de credenciais, dados e publicação.

## Curso de referência

- [IA agêntica com LangChain e LangGraph — IBM, Coursera](https://www.coursera.org/learn/agentic-ai-with-langchain-and-langgraph)

Este repositório não substitui o curso. Use o material oficial para aulas, laboratórios, avaliações e instruções atualizadas.

## Por que este guia existe

A parte mais útil do estudo não foi decorar APIs. Foi observar o fluxo: um agente recebe estado, decide o próximo passo, usa uma ferramenta quando precisa e encerra quando tem informação suficiente. Quando um requisito é objetivo — por exemplo, limite de caracteres ou formato de saída — a validação precisa ser feita por código, não apenas pela reflexão do modelo.

## Status

Estudo em andamento. Os Módulos 1 e 2 aparecem concluídos na plataforma. O Módulo 3 está incompleto e será documentado conforme for estudado.

## Licença

Código e textos autorais deste repositório: MIT. A licença não se aplica ao conteúdo proprietário do curso, que permanece no ambiente da Coursera/IBM.
