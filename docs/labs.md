# O que fizemos nos laboratórios

Os laboratórios abaixo foram realizados como parte do curso [IA agêntica com LangChain e LangGraph, da IBM na Coursera](https://www.coursera.org/learn/agentic-ai-with-langchain-and-langgraph). Este documento relata o processo e os aprendizados; não redistribui os notebooks do curso.

## LangGraph 101: fluxo com estado

Começamos com um fluxo que carregava estado entre nós. O exercício mostrou como validar uma pergunta, fornecer contexto, gerar uma resposta e conectar os nós até `END`.

Também recuperamos o trabalho salvo do laboratório. A sessão chegou a `n == 13`, e identificamos uma correção necessária na assinatura de uma função: o estado deveria usar o tipo de estado do fluxo, em vez de um tipo genérico incorreto.

**O que ficou:** estado explícito torna o comportamento observável e facilita encontrar onde uma decisão saiu do esperado.

## Agente de reflexão

No laboratório de reflexão, montamos um ciclo com dois papéis:

1. um nó gera uma resposta;
2. outro nó critica a resposta;
3. uma condição decide se o fluxo gera uma nova versão ou encerra.

A execução produziu várias mensagens de geração e crítica. O caso mais instrutivo foi uma regra de tamanho: o texto passou do limite pedido, embora a crítica do modelo dissesse que estava dentro do limite.

**O que ficou:** reflexão é uma ferramenta de melhoria, não uma prova de conformidade. Contagem, formato e outras regras objetivas precisam de validação determinística.

## Reflexão com conhecimento externo

Na etapa seguinte, o agente recebeu a possibilidade de consultar conhecimento externo antes de revisar a resposta. O objetivo era perceber a diferença entre “o modelo acha que está certo” e “o fluxo trouxe evidência suficiente para continuar”.

A prática reforçou que a ferramenta deve ter um contrato claro: entrada, saída, erro e condição para seguir. Sem isso, o ciclo pode repetir chamadas sem melhorar o resultado.

## ReAct: raciocínio e ação

No laboratório ReAct, conectamos um modelo a ferramentas simuladas de busca e recomendação. O padrão separa o raciocínio da ação e do resultado da ação:

1. pensamento: o agente identifica o próximo passo;
2. ação: escolhe a ferramenta;
3. entrada da ação: envia os argumentos;
4. observação: recebe o resultado;
5. resposta final ou nova decisão.

No LangGraph, a função `should_continue` funciona como o roteador: verifica a mensagem mais recente e decide se há uma chamada de ferramenta pendente ou se o agente pode encerrar.

A busca externa retornou `401 Unauthorized` porque o notebook ainda tinha um marcador de chave. Nenhuma chave pessoal foi inserida. Registramos isso como parte do estudo: uma integração sem credencial deve falhar de forma visível e segura.

## Como reproduzir o aprendizado

## DocChat: RAG multiagente

No DocChat, combinamos preparação de documentos, busca híbrida e uma equipe de agentes coordenada por LangGraph. A busca lexical encontra termos exatos; a vetorial recupera significado. Agentes separados verificam evidências e podem pedir uma revisão quando há contradição. O registro detalhado e o estado da execução estão em [`labs/05-docchat.md`](../labs/05-docchat.md).

Para uma prática independente, recomendamos esta ordem:

1. simular o modelo e as ferramentas com funções determinísticas;
2. testar o estado e as transições;
3. adicionar validações objetivas;
4. só então conectar um provedor externo em ambiente seguro.

Isso reduz custo, facilita depuração e mantém o primeiro experimento livre de credenciais.
