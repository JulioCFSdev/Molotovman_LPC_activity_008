# Molotovman_LPC_activity_008
Jogo baseado no Super Bomberman 3 de SNES, desenvolvido por alunos da Universidade do Estado do Amazonas, do curso de Sistemas de Informação.
Desenvolvedores: Arthur Uguen de Mendonça, Diana de Oliveira, Guilherme Tapajós, Johann Mayos e Júlio César Ferreira.

![image](https://user-images.githubusercontent.com/90109601/162675559-7902d52e-5328-439d-9af1-de14081447db.png)


  # Tela do jogo
  De modo geral, há cinco telas no game:
  1. Tela de início: onde o jogo é introduzido e é iniciado.
  2. Tela principal: onde o jogo efetivamente acontece e os controles e comandos são executados.
  3. Tela de pause: exibida após um dos player apertar alguma tecla específica, esta denota, de algum modo, que a partida está pausada.
  4. Tela de vitória: exibe alguma mensagem que afirma a vitória de um player contra o outro.
  5. Tela de empate: caso haja empate, uma mensagem de empate será impressa.
 
   # Personagem e sua movimentação
  Os personagens são os dois players na arena. Estes apresentam diferentes uniformes.
  A movimentação destes ocorre em direção aos quatro pontos cardeais, ou seja, ao norte, ao sul, ao leste e ao oeste.
  
  # Controles e eventos
  De maneira específica, as teclas serão definidas: opções pressionadas pelo mouse na tela inicial ou pelo teclado para que se inicie a partida ou saia do jogo;
                                                    quatro teclas que movem às quatro direções fundamentais para cada player;
                                                    uma tecla para pausar o jogo;
                                                    uma tecla para sair da partida.
  Eventos: movimentar o player, soltar explosivo, quebrar bloco, colidir, pontuar, pausar o jogo, ganhar, mostrar imagem de vitória na tela.
  
  # Mecânicas
  1. O respectivo player anda para a direção concernente à tecla pressionada.
  2. O player recua levemente ao colidir com um bloco.
  3. Após apertar uma tecla específica, o explosivo é solto em uma determinada coordenada cuja referência é a posição do player.
  4. Um tipo específico de bloco some após entrar em contato com a explosão.
  5. Os players voltam às posições iniciais após um deles entrar em contato com a explosão.
  6. O player que fizer 3 pontos é o vencedor, e uma imagem é mostrada na tela.
  
