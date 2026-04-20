package Java; 
public class media { // criar uma função que calcula a media, tentar ser o mais reutilizavel possivel
    public static void main(String[] args) { 
        int[] media = {3, 4};
        float result = calcularMedia(media);
        System.out.println(result);
    
    }
    public static float calcularMedia(int[] media) {
        int notas = 0;
        for (int i = 0; i < media.length; i++) {
            notas += media[i];
        }
        float result = (float) notas / media.length;
        return result;
    }
}
