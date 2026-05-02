package Java;
import java.util.Scanner;
import java.util.Map; 
import java.util.HashMap;
import java.math.*;
public class calculadora {
    public static void main(String[] args) {
    Show calculadora = new Show();
    Scanner leitor = new Scanner(System.in);
    System.out.print("escolha sua operação (media(m), soma(+), subtração(-), multiplicação(x), porcentagem(%)) ");
    String numero = leitor.nextLine();
    System.out.print("escolha tambem quantos numeros participarão dessa operação ");
    int tamanho = leitor.nextInt();
    double[] lista = new double[tamanho];
    if (numero.equalsIgnoreCase("%")) {
        System.out.println("porcentagem só permite dois numeros, coloque o total e após isso a porcentagem que quer, ex: (100 X 10% = 10) ");
    }
    for (int i = 0; i < lista.length; i++) {
        System.out.print("escolha os numeros que quer fazer essa operação ");
        double num = leitor.nextDouble();
        lista[i] = num;
    }
    calculadora.mostrar(numero, lista);
    leitor.close();
    }
}
interface Calculate {
    public abstract double calcular(double[] lista);
}
class Media implements Calculate {
    @Override
    public double calcular(double[] lista) {
        double acumulater = 0;
        int qtd = lista.length;
        for (int i = 0; i < qtd; i++) {
            acumulater = acumulater + lista[i];
        }
        return (double) Math.round((acumulater / qtd) * 100) / 100;
    }
}
class Soma implements Calculate {
    @Override
    public double calcular(double[] lista) {
        double acumulater = 0;
        for (int i = 0; i < lista.length; i++) {
            acumulater += lista[i];
        }
        return (double) Math.round(acumulater * 100) / 100;
    }
}
class Subtração implements Calculate {
    @Override
    public double calcular(double[] lista) {
        double acumulater = lista[0];
        for (int i = 1; i < lista.length; i++) {
            acumulater -= lista[i];

        }
        return (double) Math.round(acumulater * 100) / 100;
    }
}
class Multiplicação implements Calculate {
    @Override
    public double calcular(double[] lista) {
        double acumulater = 1;
        for (int i = 0; i < lista.length; i++) {
            acumulater *= lista[i];
        }
        return (double) Math.round(acumulater * 100) / 100;
    }
}
class Porcentagem implements Calculate {
    @Override
    public double calcular(double[] lista) {
        if (lista.length > 2) {System.out.println("digite apenas o numero e a porcentagem em seguida (dois termos)");}
        double resultado = lista[0] * (lista[1] / 100);
        return (double) Math.round(resultado * 100) / 100;
    }
}
class interfaces {
    public static final Map<String, Calculate> operacoes = new HashMap<>();
    static {
        operacoes.put("+", new Soma());
        operacoes.put("m", new Media());
        operacoes.put("-", new Subtração());
        operacoes.put("x", new Multiplicação());
        operacoes.put("%", new Porcentagem());
    } 
    public static Calculate getOperacao(String escolha) {
        return operacoes.get(escolha.toLowerCase());
    }
}
class Show {
    public void mostrar(String escolha, double[] lista) {
        Calculate calculadora = interfaces.getOperacao(escolha);
        if (escolha.equalsIgnoreCase("+")) { double numero = calculadora.calcular(lista);  System.out.println("o resultado da soma é " + numero);
        } else if (escolha.equalsIgnoreCase("m")) {double numero = calculadora.calcular(lista);  System.out.println("o resultado da media é " + numero);
        } else if (escolha.equalsIgnoreCase("-")) {double numero = calculadora.calcular(lista);  System.out.println("o resultado da subtração é " + numero);
        } else if (escolha.equalsIgnoreCase("x")) {double numero = calculadora.calcular(lista);  System.out.println("o resultado da multiplicação é " + numero);
        } else if (escolha.equalsIgnoreCase("%")) {double numero = calculadora.calcular(lista);  System.out.println("o resultado da porcentagem é " + numero);
        }
    }
}
