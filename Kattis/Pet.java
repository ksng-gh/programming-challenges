import java.util.Scanner;

public class Pet {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int i = 1;
        int tr = 0;
        int tr2 = 0;
        while (i < 6) {
            int in1 = sc.nextInt();
            int in2 = sc.nextInt();
            int in3 = sc.nextInt();
            int in4 = sc.nextInt();

            int fin = vote(in1, in2, in3, in4);

            if (fin > tr) {
                tr = fin;
                tr2 = i;
            }

            i++;
        }
        System.out.println(tr2 + " " + tr);

        sc.close();

    }

    public static int vote(int i, int j, int k, int l) {
        return i + k + j + l;
    }

}
