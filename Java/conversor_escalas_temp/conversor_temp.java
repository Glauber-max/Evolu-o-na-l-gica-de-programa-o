package Java.conversor_escalas_temp;
import java.util.Scanner;
import java.util.Locale;

public class conversor_temp { // criar um conversor de temperatura automatico que seja facil de manter e expandir, 
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in); 
        terminal mostrarInterface = new terminal(); 
        System.out.print("digite qual a escala de temperatura atual? (F = Farenheit, K = Kelvin, C = Celsios) "); 

        String tipoInicial = leitor.nextLine().toUpperCase(Locale.ROOT);
        System.out.print("digite a temperatura? ");

        Double valorI = leitor.nextDouble(); 
        System.out.print("pra qual escala de temperatura você quer ir? ");
        leitor.nextLine();
        String tipoFinal = leitor.nextLine().toUpperCase(Locale.ROOT);
        //peço todos os dados necessarios ao usuario e mando para o terminal exibir corretamente
        mostrarInterface.show(tipoInicial, valorI, tipoFinal); // a ordem de logica foi 
        leitor.close();                                        // class Terminal -> class Conversor -> class (Farenheit ou Celsius ou kelvin) 
    }                                                          // retorna o valor  para Conversor, passa para Terminal e exibe no terminal
}
abstract class Escala { // classe abstrata usada para dar uma função de conversao para todas as escalas de temperatura
    public static Escala getinstance(String tipo) { //feita seguindo o desin patter factory method, um metodo para criar objetos e usar suas funções
        return switch (tipo) {
                case "F" ->  new Fahrenheit(); 
                case "C" ->  new Celsius();
                case "K" ->  new Kelvin();
                default -> throw new IllegalArgumentException("Erro: " + tipo + " não existe.");
        };
    }
    public abstract double converterN(double valorI, String tipoFinal);
}
interface ConversorInter { // interface para usar um metodo abstrato
    public abstract double converter(String tipoinicial, double numeroInicial, String tipoFinal);
} 

class Conversor implements ConversorInter { //implementando interface no conversor e adicionando o metodo obrigatorio de conversao

    @Override
    public double converter(String tipoInicial, double numeroInicial, String tipoFinal) {
        Escala escala = Escala.getinstance(tipoInicial);
        double numFinal = escala.converterN(numeroInicial, tipoFinal);
        return numFinal;
    }
}// a baixo todas as classes que retornam os calculos de conversão
    class Fahrenheit extends Escala {

        @Override
        public double converterN(double valorI, String tipoFinal) {
            if (tipoFinal.equalsIgnoreCase("C")) {return 5.0 /9.0 * (valorI - 32);   
            } else if (tipoFinal.equalsIgnoreCase("K")){
                return  (5.0 /9.0 * (valorI - 32)) + 273.15;

            } else {
                System.out.println("error");
                return 0;}
        }
    }
    class Kelvin extends Escala{

        @Override
        public double converterN(double valorI, String tipoFinal) {
            if (tipoFinal.equalsIgnoreCase("F")) {return (9.0 /5.0 * (valorI - 273.15)) + 32; 
            } else if (tipoFinal.equalsIgnoreCase("C")){
                return valorI - 273.15;

            } else {
                System.out.println("error");
                return 0;}
        }
    }
    class Celsius extends Escala {
                @Override
        public double converterN(double valorI, String tipoFinal) {
            if (tipoFinal.equalsIgnoreCase("F")) {return (1.8 * valorI) + 32;
            } else if (tipoFinal.equalsIgnoreCase("K")){
                return valorI + 273.15;

            } else {
                System.out.println("error");
                return 0;}
        }
    } //classe abstrata implementada para caso no futuro precise de uma interface web ou outro tipo de interface
abstract class ControllerInterfaces {  
        public abstract void show(String tipoInicial, double numeroInicial, String tipoFinal);
}
class terminal extends ControllerInterfaces { //classe terminal que gerencia como o usuario irá ver os calculos, 
    @Override
    public void show(String tipoInicial, double numeroInicial, String tipoFinal){
        Conversor interfaceR = new Conversor();
        double numFinal = interfaceR.converter(tipoInicial, numeroInicial, tipoFinal); // ela chama o metodo converter que mandando os dados,
        if (tipoInicial.equalsIgnoreCase("F")) {                        //  que manda os dados para as class de escala que por sua vez retornam o calculo
            if (tipoFinal.equalsIgnoreCase("C")) {
                System.out.print("o valor em Farenheit " + numeroInicial + " ºF " + "em Celsios é " + (double) Math.round(numFinal * 100.0) / 100.0 + " ºC");
            } else {
                System.out.printf("o valor em Farenheit " + numeroInicial + " ºF " + "em Kelvin é " + (double) Math.round(numFinal * 100.0) / 100.0 + " ºK");
            }
        } else if (tipoInicial.equalsIgnoreCase("K")) {
            if (tipoFinal.equalsIgnoreCase("F")) {
                System.out.printf("o valor em Kelvin " + numeroInicial + " ºK" + " em Farenheit é " + (double) Math.round(numFinal * 100.0) / 100.0 + " ºF");
            } else {
                    System.out.printf("o valor em Kelvin " + numeroInicial + " ºK" + " em Celsius é " + (double) Math.round(numFinal * 100.0) / 100.0 + " ºC");
            }
        } else if (tipoInicial.equalsIgnoreCase("C")) {
            if (tipoFinal.equalsIgnoreCase("K")) {
                System.out.printf("o valor em Celsius " + numeroInicial + " ºC " + "em Kelvin é " + (double) Math.round(numFinal * 100.0) / 100.0 + " ºK");
            } else {
                    System.out.print("o valor em Celsius " + numeroInicial + " ºC " + "em Farenheit é "  + (double) Math.round(numFinal * 100.0) / 100.0 + " ºF");
            }
        }
    }
}