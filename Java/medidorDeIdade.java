package Java;

import java.util.Scanner;

public class medidorDeIdade {
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);
        System.out.print("digite seu nome ");
        String nome = leitor.next();
        System.out.print("digite a sua idade ");
        int idade = leitor.nextInt();
        if (idade >= 18) {
            System.out.println("vc pode dirigir" + ", pois tem " + idade + " anos");
        } else {
            System.out.println("vc nao pode dirigir " + nome);
        }
        leitor.close();
    }
}
