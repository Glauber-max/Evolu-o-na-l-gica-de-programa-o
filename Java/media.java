package Java; 
public class media { // criar uma função que calcula a media, tentar ser o mais reutilizavel possivel
    public static void main(String[] args) { // defini a lista e atribui a uma variavel o calculo e printei
        int[] media = {10, 8, 6, 8, 4, 3};
        float result = calcularMedia(media);
        System.out.println(result);
    }
    public static float calcularMedia(int[] media) { // fiz uma função que pega a lista de notas percorre ela e soma, e divide pela quantidade
        int notas = 0; // e me retorna o resultado
        for (int i = 0; i < media.length; i++) {
            notas += media[i];
        }
        float result = (float) notas / media.length;
        return result;
    }
}
