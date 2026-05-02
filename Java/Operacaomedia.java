
public class Operacaomedia {  /* criar uma função que calcula a media, tentar ser o mais reutilizavel possivel */
    @SuppressWarnings("unused")
    static void main(String[] args) { // defini a lista e atribui a uma variavel o calculo e printei
        int[] media = {10, 8, 6, 8, 4, 3, 4, 9, 103, 3, 17, 188, 17};
        double result = calcularMedia(media);
        System.out.print(result);
    }
    public static double calcularMedia(int[] media) { // fiz uma função que pega a lista de notas percorre ela e soma, e divide pela quantidade
        int notas = 0; // e me retorna o resultado
        for (int item: media) {
            notas += item;
        }
        double  notasFinal = (double) notas / media.length;
        return (double) Math.round(notasFinal * 100)  / 100;
    }
}
