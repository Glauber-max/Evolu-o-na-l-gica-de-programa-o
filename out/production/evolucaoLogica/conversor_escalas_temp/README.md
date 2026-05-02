O programa é um Conversor de Escalas Termométricas desenvolvido em Java que utiliza uma arquitetura baseada em princípios SOLID para garantir que o código seja fácil de manter e expandir. A lógica central foi construída sobre uma classe abstrata chamada Escala, que serve como base para as implementações específicas de Celsius, Fahrenheit e Kelvin, podendo adicionar outras mexendo apenas no switch para funcionar corretamente e adicionar a forma de exibição. Para gerenciar a criação desses objetos sem espalhar instâncias pelo código, foi aplicado o padrão de projeto Factory Method através do método estático getinstance

Java jdk 17++
import Scanner
import Locale

digite qualquer escala entre as que o programa converte, escolha temperatura inicial e por fim a escala de destino