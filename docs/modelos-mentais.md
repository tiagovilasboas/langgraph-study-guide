# Modelos mentais

## Estado

O estado é a memória explícita do fluxo. Cada nó recebe o estado atual e devolve uma atualização. Se uma informação importa para a próxima decisão, ela precisa estar no estado ou ser obtida por uma ferramenta.

## Nó

Um nó faz uma transformação pequena: gerar, criticar, consultar, validar ou formatar. Nós menores facilitam leitura, teste e observabilidade.

## Roteamento

Uma função de roteamento transforma o resultado do nó em uma decisão: seguir para a ferramenta, voltar para outro nó ou terminar.

## Reflexão

Reflexão é um ciclo de geração e crítica. Ela pode melhorar clareza e cobertura, mas não substitui verificadores objetivos.

## ReAct

O ciclo prático é:

1. o agente identifica o que precisa fazer;
2. escolhe uma ação;
3. prepara os dados da ação;
4. recebe uma observação;
5. responde ou decide continuar.

A função `should_continue` é o cruzamento desse fluxo: olha a mensagem mais recente e decide entre ferramenta e encerramento.
