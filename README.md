# Molotovman - Game

Jogo baseado no Super Bomberman 3 de SNES desenvolvido por alunos da Universidade do Estado do Amazonas, do curso de Sistemas de Informação. Desenvolvedores: Arthur Uguen de Mendonça, Diana de Oliveira, Guilherme Tapajós, Johann Mayos e Júlio César Ferreira.
![Tela de referência do jogo](https://user-images.githubusercontent.com/90109601/161894357-73ca4d0f-95fc-4257-b51f-a53bef8c6b1f.jpg)


 # Tela do jogo
  De modo geral, há cinco telas no game:
  1. Tela de início: onde o jogo é introduzido e é possível escolher se este será em single ou em multiplayer.
  2. Tela principal: onde o jogo efetivamente acontece e os controles e comandos são executados.
  3. Tela de pause: exibida após um dos player apertar alguma tecla específica, esta denota, de algum modo, que a partida está pausada.
  4. Tela de vitória: exibe alguma mensagem que afirma a vitória do player contra o computador, do player 1 contra o player 2 e vice-versa.
  5. Tela de derrota: exibe alguma mensagem que afirma a derrota do player caso ele esteja jogando contra o computador.
 
 # Personagem e sua movimentação
  Os personagens são os bonecos. Estes terão designs diferentes.
  A movimentação destes ocorre para as direções dos pontos cardeais, ou seja, para frente, para trás e para os lados.
  
 # Controles e eventos
  De maneira específica, as teclas serão definidas: opções pressionadas na tela inicial para selecionar as especificações da partida e iniciá-la;
                                                    teclas para movimentar os jogadores para as direções especificadas(8 teclas no multiplayer);
                                                    uma tecla para pausar o jogo;
                                                    uma tecla para reiniciar partida após derrota ou vitória e uma para sair do jogo.
  Eventos: andar, soltar explosivo, explodir bloco da arena, ficar encurralado, explodir o adversário, explodir a si próprio, pontuar, ganhar, perder, pausar a partida, escolher o modo de partida e sair do jogo.
  
 # Mecânicas
  1. O boneco solta o explosivo e este explode.
  2. O explosivo destrói blocos específicos na arena.
  3. O boneco se move para as quatro direções fundamentais.
  4. Se o boneco estiver em um raio de alcance da explosão, morre.
  5. O score é incrementado após a morte do adversário.
  6. Os bonecos iniciam a partida em locais específicos da arena.
  7. Se o boneco estiver entre um bloco e um explosivo, está encurralado.
  
