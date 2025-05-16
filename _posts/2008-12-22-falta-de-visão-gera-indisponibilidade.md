---
layout: post
title: "Falta de visão gera indisponibilidade"
date: 2008-12-22
tags: Falta,previsão
author: None
---
Por Rodrigo Ramos
Durante este ano de 2008 fiz muitas visitas &agrave; empresas que estavam (algumas continuam) com problemas de indisponibillidade de seus sistemas e consequentemente de suas informa&ccedil;&otilde;es.
Algumas dessas empresas precisaram gastar muito mais para colocar seus sistemas de volta no ar do que seria necess&aacute;rio investir para diminuir bastante os problemas de indisponibilidade.
Sempre termino estas visitas sem intender como &eacute; que uma empresa que fatura t&atilde;o bem pode ter este tipo de problema. Eu noto que os gerentes de T.I. at&eacute; tentam vender a id&eacute;ia de alta-disponibilidade, mas os diretores simplesmente n&atilde;o t&ecirc;m a vis&atilde;o necess&aacute;ria para comprar a id&eacute;ia.
J&aacute; existem solu&ccedil;&otilde;es para tudo o que se pode imaginar quando se fala em alta-diponibilidade. &Eacute; l&oacute;gico que a maioria delas n&atilde;o leva em considera&ccedil;&atilde;o fatores como a queda de um avi&atilde;o sobre o datacenter ou CPD, mas isto deve ser colocado em um mapa de riscos.
H&aacute; pouco tempo participei de um projeto que teoricamente deveria ser bem simples. A demanda era &ldquo;Inserir dois novos discos em um servidor e criar um RAID-1*&rdquo;. Como esta empresa n&atilde;o possui uma solu&ccedil;&atilde;o de alta-diponibilidade para o seu banco de dados (Oracle) e nossa janela de tempo para trabalhar era m&iacute;nima, tivemos que montra uma verdadeira opera&ccedil;&atilde;o de guerra para impedir que qualquer coisa desse errado e causasse a perda da disponibilidade do banco de dados. Bom, no final deu tudo certo, mas uma opera&ccedil;&atilde;o que deveria levar algumas poucas horas levou quase 02 dias e envolveu nada mais nada menos que 6 profissionais.
Na minha opini&atilde;o o problema est&aacute; na forma com que as coisas s&atilde;o vistas, s&atilde;o levantadas e apresentadas. Vou relatar um fato que ocorreu com um dos nossos clientes, mas que com toda certeza acontece diariamente em milhares de empresas.
O cliente estava buscando uma solu&ccedil;&atilde;o para trocar seu sistema de gest&atilde;o da empresa e finalmente achou uma que atendia seus requisitos funcioniais e financeiros. O vendedor da solu&ccedil;&atilde;o fez l&aacute; sua apresenta&ccedil;&atilde;o, disse quanto custava e completou dizendo que o sistema era muito leve e poderia rodar em qualquer m&aacute;quina, com qualquer sistema operacional Linux e que o mundo seria maravilhoso dal&iacute; em diante.
Bem, ap&oacute;s alguns dias o cliente estava certo que o seu investimento era de apenas R$ 80.000,00**. Ap&oacute;s algum tempo ele ficou sabendo que al&eacute;m dos R$ 80.000,00 para adquirir o sistema ele tamb&eacute;m precisaria:
- Da subscri&ccedil;&atilde;o do sistema operacional Linux escolhido, 
- Da licen&ccedil;a do banco de dados, 
- Contratar um DBA**** nem que seja para visitas semanais, quinzenais ou mensais;
- De um bom servidor de marca com um pacote de garantia de suporte com o melhor SLA*** poss&iacute;vel,
- Inserir o sistema operacional Linux dentro de um contrato de suporte tamb&eacute;m com SLA,
- Rever e corrigir qualquer problema em suas instala&ccedil;&otilde;es onde o servidor seria colocado,
- Contratar um profissional capaz de customizar ou gerenciar as customiza&ccedil;&otilde;es necess&aacute;rias no sistema de gest&atilde;o;
- Rever toda a sua infra-estrutura de backup;
- Montar e executar um projeto de alta-disponibilidade para garantir o investimento no sistema de gest&atilde;o.
Com tudo isto, no final das contas, o cliente descobriu que com R$ 80.000,00 ele completaria apenas a primeira volta de uma corrida com mais de 10 voltas.
Infelizmente a vis&atilde;o deste cliente impediu que ele montasse o projeto de alta-disponibilidade. A vis&atilde;o da maioria dos empres&aacute;rios e gestores s&oacute; vai at&eacute; os benef&iacute;cios dos sistemas. Eles n&atilde;o enxergam que o sistemas param e quando param o preju&iacute;zo &eacute; garantido.
*
Resumindo RAID-1....Tudo o que for feito em um disco deve ser feito no outro disco automaticamente. Um arquivo criado no disco 1 &eacute; automaticamente criado no disco 2.
**
O valores s&atilde;o fict&iacute;cios
***
SLA (Service Level Agreement). &Eacute; neste acordo com est&aacute; definido o tempo m&aacute;ximo que o fornecedor do hardware tem para substituir alguma pe&ccedil;a com defeito.
****
DBA (Database Administrator).
Bom, por hoje &eacute; s&oacute;. Na pr&oacute;xima semana tem mais.
N&atilde;o esquecam de mandar suas d&uacute;vidas e sugest&otilde;es para rodrigo.ramos@triforsec.com.br
Tenham todos uma &oacute;tima semana e um feliz Natal.
Rodrigo Ramos, diretor de Opera&ccedil;&otilde;es da TRIFORSEC - Tecnologia em Seguran&ccedil;a da Informa&ccedil;&atilde;o. 