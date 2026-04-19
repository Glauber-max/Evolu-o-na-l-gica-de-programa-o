
package Java;
import java.util.Scanner;
public class soma {
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);
        System.out.print("digite o numero 1 da soma ");
        int n1 = leitor.nextInt();
        System.out.print("diga o segundo numero ");
        int n2 = leitor.nextInt();
        int soma = CalcularSoma(n1, n2);
        System.out.println("a soma é " + soma);
        leitor.close();
    }
           public static int CalcularSoma(int numero1, int numero2) {
        return numero1 + numero2;
    }
}
