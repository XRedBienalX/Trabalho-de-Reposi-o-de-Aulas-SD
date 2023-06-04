# Trabalho-de-Reposi-o-de-Aulas-SD
Tema: ZeroMQ  <br />Pesquise e desenvolva uma pequena aplicação usando ZeroMQ. Escolha um dos seguintes padrões para a aplicação:
request-reply (requisição-resposta)
publish-subscribe (publicação e subscrição)
Pipeline
 
 
<h1>Introdução</h1><br />  
  
  Nesse trabalho foi usado a arquitetura request-reply (requisição-resposta) e a linguaguem de programação foi python versão 3.9.10,além do uso da biblioteca ZeroMQ.A aplicação desenvolvida se basei na ideia de dois servidores que irão processar requisições de um cliente , por consequencia , as respostas das requisições será  em manter , vender ou compra um determinada ação.<br />
 
 <h2>Explicação tecnica da aplicação</h2><br />
 
 O servidor cria um soquete do tipo resposta , vincula-o a porta e, em seguida, aguarda mensagens.O cliente cria um soquete do tipo request, conecta e começa a enviar Mensagens.<br />
 
<h2>Passo a passo para o funcionamento da aplicação</h2><br />
0-pip install pyzmq <br />
1-Run servidor 1 <br />
2-Run servidor 2<br />
3-Run cliente<br />

<h2>Equipe : </h2> <br />
496157 - HERON RODRIGUES DE OLIVEIRA <br />
495374 - OTAVIO NORONHA NETO<br />
