---
layout: post
title: "Transportando informações com segurança"
date: 2008-09-29
tags: Segurança
author: None
---
Por Rodrigo Buarque Ramos
Os dois &uacute;ltimos textos renderam alguns e-mails enviados a minha conta rodrigo.ramos@triforsec.com.br, onde coincidentemente leitores aqui do Blog de Jamildo perguntam sobre uma forma segura de transportar suas informa&ccedil;&otilde;es fora de seus lares e organiza&ccedil;&otilde;es onde trabalham.
A &uacute;nica forma de transportar dados de forma segura &eacute; tornando-os inacess&iacute;veis a terceiros, ou seja, utilizando algum meio que impe&ccedil;a o acesso direto aos mesmos.
Seguindo este racioc&iacute;nio, mesmo que seja poss&iacute;vel acessar o dispositivo, n&atilde;o ser&aacute; poss&iacute;vel ler o conte&uacute;do. Para tal, &eacute; necess&aacute;rio utilizar uma ferramenta de criptografia que ir&aacute; intermediar o acesso aos dados mediante uma senha, por exemplo.
Existe uma ferramenta dispon&iacute;vel na Internet chamada Truecrypt, que tem entre suas funcionalidades a possibilidade de criptografar dispositivos, como por exemplo, pendrives.
Essa ferramenta deve ser instalada em todos os computadores onde se deseja utilizar o dispositivo criptografado. &Eacute; poss&iacute;vel tamb&eacute;m carregar o instalador do Truecrypt junto ao pendrive em uma &aacute;rea n&atilde;o criptografada para o caso de precisar utilizar os dados que est&atilde;o criptografados em uma m&aacute;quina que n&atilde;o possua o Truecrypt instalado.
Com o Truecrypt tamb&eacute;m &eacute; poss&iacute;vel criar arquivos criptografados que ser&atilde;o reconhecidos pelo sistema operacional como 'unidades de disco' remov&iacute;veis. Por exemplo, um arquivo de 100MB, criptografado pelo Truecrypt se transforma na unidade G: (a letra pode ser alterada), e tudo o que for utilizado na unidade G: estar&aacute; criptografado.
Ap&oacute;s a utiliza&ccedil;&atilde;o, &eacute; poss&iacute;vel copiar o arquivo criptografado e transport&aacute;-lo para onde quiser, CD/DVD/Pendrive. Para utiliz&aacute;-lo novamente, basta apontar o Truecrypt para o arquivo criptografado. Uma outra pr&aacute;tica, por&eacute;m n&atilde;o t&atilde;o comum do Truecrypt, se chama 'Whole Disk Encryption', que criptografa o disco inteiro, assim como o sistema operacional, que s&oacute; se inicia mediante senha de criptografia.
O acesso n&atilde;o autorizado aos dados do HD se torna praticamente imposs&iacute;vel por um bom tempo.
Outra fun&ccedil;&atilde;o interessante desta maravilhosa ferramenta est&aacute; na capacidade de criar mais de um volume criptografado dentro de uma &aacute;rea j&aacute; criptografada no HD.
Hoje existem vers&otilde;es do Truecrypt para Windows e para Linux.
Al&eacute;m do Truecrypt, outras ferramentas possuem o mesmo objetivo e podem ser concatenadas com algumas fun&ccedil;&otilde;es do sistema operacional, passando alguns par&acirc;metros ao sistema operacional, quando certos eventos forem identificados.
Ao inv&eacute;s de permitir que um &quot;atacante&quot; tente quebrar a senha da criptografia, o sistema pode ser configurado para apagar toda e qualquer informa&ccedil;&atilde;o do sistema, ap&oacute;s um n&uacute;mero pr&eacute;-estabelecido de tentativas sem sucesso.
Na pr&oacute;xima semana vamos falar sobre criptografia nas comunica&ccedil;&otilde;es via email. At&eacute; l&aacute;.
PS: Rodrigo Ramos &eacute; Diretor da Triforsec
&nbsp;
&nbsp; 