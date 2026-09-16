# Lab 05 — DocChat: RAG multiagente

Este registro resume o laboratório **DocChat: Build a Multi-Agent RAG System**, oferecido no curso [IA agêntica com LangChain e LangGraph, da IBM na Coursera](https://www.coursera.org/learn/agentic-ai-with-langchain-and-langgraph). É uma explicação autoral para estudo; o notebook do curso continua sendo a fonte da atividade prática.

## A ideia em uma analogia

Imagine uma biblioteca com uma equipe de pesquisa. Uma pessoa localiza trechos relevantes, outra confere se a resposta está apoiada nesses trechos e uma terceira revisa quando encontra contradições. O DocChat organiza esse trabalho para responder perguntas sobre documentos longos.

O ganho não vem de “ter vários modelos por moda”. Cada agente tem uma responsabilidade menor e verificável, e o grafo decide qual etapa vem depois.

## O que observamos no laboratório

- **Docling** prepara documentos, inclusive texto, tabelas e estrutura, antes da busca.
- **ChromaDB** funciona como um índice semântico para recuperar trechos parecidos em significado.
- **BM25** complementa a busca vetorial com correspondência de palavras exatas. É como usar dois catálogos da biblioteca: um encontra o termo preciso; o outro entende a intenção.
- **LangChain** conecta recuperação, prompts, modelos e ferramentas que compõem o RAG.
- **LangGraph** coordena os agentes, o estado e as decisões de transição.
- **Gradio** apresenta a interface para carregar documentos e consultar o resultado.
- **ibm_watsonx_ai** integra o modelo usado pelo ambiente do curso.

O laboratório também informa que a análise de um documento pode levar cerca de um a dois minutos, porque o fluxo precisa recuperar contexto e passar pelas etapas de verificação.

## O pensamento de Staff

O desenho melhora rastreabilidade, mas adiciona custo e pontos de falha. Antes de adotar o padrão, vale perguntar:

1. Qual agente é responsável por cada decisão e qual evidência ele precisa produzir?
2. O que acontece quando busca lexical e vetorial retornam trechos diferentes?
3. Existe limite de tentativas para a autocorreção, ou o grafo pode entrar em loop?
4. Como medir qualidade: precisão da fonte, latência, custo por consulta e taxa de respostas sem evidência?
5. O sistema consegue mostrar ao usuário de onde veio a resposta?

Uma arquitetura simples costuma ser suficiente no começo. Multiagentes fazem sentido quando a separação de responsabilidades reduz erros que uma única cadeia não consegue controlar.

## Estado desta execução

Abrimos o laboratório pela Coursera, clonamos o repositório inicial do Skills Network e selecionamos a versão final (`2-final`) no Cloud IDE. A instalação das dependências foi iniciada no ambiente remoto; a execução da interface depende da conclusão desse download e da inicialização do `app.py` na porta 5000.

## Referências

- [Documentação do LangChain](https://docs.langchain.com/oss/python/langchain/overview)
- [Documentação do LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)
- [Curso da IBM na Coursera](https://www.coursera.org/learn/agentic-ai-with-langchain-and-langgraph)

