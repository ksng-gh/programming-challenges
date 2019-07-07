import java.util.*;

public class Sevenwonders {

    public static int getMin(int a, int b, int c){
        if(a >= c && b >= c){
            return c;
        } else if (a <= b){
            return a;
        } else {
            return b;
        }
    }

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        String s = in.nextLine();
        int t = 0;
        int c = 0;
        int g = 0;

        for(int i = 0; i < s.length(); i++){
            switch (s.charAt(i)){
                case 'T':
                    t++;
                    break;
                case 'C':
                    c++;
                    break;
                case 'G':
                    g++;
                    break;
            }
        }

        int min = getMin(t, c, g);

        t = t * t;
        c = c * c;
        g = g * g;
        System.out.println(7 * min + t + c + g);
    }
}