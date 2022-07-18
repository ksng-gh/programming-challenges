import java.util.*;

public class Statistics {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = 1;
        int max = -10000001;
        int min = 10000001;
        while (sc.hasNext()) {
            int cases = sc.nextInt();
            for (int i = 0; i < cases; i++) {
                int t = sc.nextInt();
                if (max < t) {
                    max = t;
                }
                if (min > t) {
                    min = t;
                }
            }
            System.out.println("Case " + n++ + ": " + min + " " + max + " " + (max - min));
        }
        sc.close();
    }
}
