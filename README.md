## 1. Problema de negócio

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

O CEO foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards, a partir dessas análises, para responder às seguintes perguntas:

### Geral
1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

### País
1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?

### Cidade
1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

### Restaurantes
1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

### Tipos de Culinária
1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?

O CEO também pediu que fosse gerado um dashboard que permitisse que ele visualizasse as principais informações das perguntas que ele fez. O CEO precisa dessas informações o mais rápido possível, uma vez que ele também é novo na empresa e irá utilizá-las para entender melhor a empresa Fome Zero para conseguir tomar decisões mais assertivas.

Seu trabalho é utilizar os dados que a empresa Fome Zero possui e responder as perguntas feitas pelo CEO e criar o dashboard solicitado.


## 2. Premissas assumidas para a análise 

1-O modelo de negócio assumido foi o marketplace.

2-As principais visões do negócio foram: Visão Geral, Visão Países, Visão Cidades, Visão Restaurantes (incluindo tipos culinários).


## 3. Estratégia da solução

O painel foi desenvolvido utilizando as métricas que refletem as principais visões do modelo de negócio da empresa. Cada visão é representada pelos conjuntos de métricas a seguir:

1-Visão Geral

    a. Países cadastrados
    b. Cidades cadastradas
    c. Restaurantes cadastrados
    d. Tipos culinários
    e. Número de avaliações
    f. Localização geográfica (visual)

2-Visão Países

    a. Número de cidades registradas por país
    b. Número de restaurantes registrados por país
    c. Nota média das avaliações por país
    d. Preço médio do prato para duas pessoas por país
    e. Tipos culinários por país

3-Visão Cidades

    a. Número de restaurantes registrados por cidade
    b. Nota média das avaliações por cidade
    c. Preço médio do prato para duas pessoas por cidade
    d. Tipos culinários por cidade

4-Visão Restaurantes

    a. Preço médio do prato para duas pessoas por tipo culinário
    b. Nota média das avaliações por tipo culinário
    c. Relação entre restaurantes que aceitam pedido online e avaliação média
    d. Relação entre restaurantes que aceitam reserva e avaliação média
    e. Relação entre classificação de preço e avaliação média


## 4. Top insights de dados

1- Restaurantes que não aceitam pedido online tem avaliação média 4.14 enquanto restaurantes que aceitam pedido online tem avaliação média 4.10. Esse resultado equivale a uma diferença de aproxidamente 1%.

2- Restaurantes que não fazem reserva tem avaliação média 4.11 e restaurantes que fazem reserva tem avaliação média 4.37. A diferença é de aproxidamente 6%. Analisando os resultados, vemos que a condição 'fazer reserva' influencia positivamente mais que 'aceitar pedido online'.

3- Com relação à classificação de preço dos pratos, a avaliação média dos pratos classificados como 'cheap' foi de 3.92 e dos pratos classificados como gourmet, 4.20. Em geral, pratos com classificações de preço mais altas tiveram melhor resultado que aqueles com classificações mais baixas.


## 5. Produto final do projeto

O produto final é um painel online, hospedado em uma cloud e disponível para acesso em qualquer dispositivo conectado à internet.

O painel pode ser acessado através do link: https://lresende-ftc-fomezero-marketplace.streamlit.app/visao_geral


## 6. Conclusão

O objetivo desse projeto é criar um dashboard que permitisse ao CEO da empresa Fome Zero visualizar as principais informações sobre a empresa de forma que ele consiga melhor entendê-las e usá-las de maneira mais assertiva para a tomada de decisões.

O painel criado engloba quatro diferentes visões que permitem ao CEO ter um entendimento mais completo e, ao mesmo tempo, mais detalhado sobre as métricas da empresa. Possibilita também analisar como diferentes aspectos dos restaurantes influenciam nas características do negócio da Fome Zero. Como exemplo, fazer reserva influencia mais nas avaliações dos usuários do que poder fazer o pedido de forma online.


## 7. Próximos passos

1-Analisar como os tipos culinários se relacionam com as avaliações feitas pelos usuários.

2-Analisar como a localização geográfica pode estar relacionada às classificações de preço dos pratos e às avaliações médias feitas pelos usuários.
