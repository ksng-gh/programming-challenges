import java.util.Scanner;

public class Trik {
    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);

        int ball = 1;

        String s = inp.nextLine();
        for (int i = 0; i < s.length(); i++) {
            ball = switchCup(s.charAt(i), ball);
        }
        System.out.println(ball);
        inp.close();
    }

    public static int switchCup(char c, int i) {
        if (c == 'C') {
            if (i == 1) {
                i = 3;
            } else if (i == 3) {
                i = 1;
            }
        } else if (c == 'B') {
            if (i == 2) {
                i = 3;
            } else if (i == 3) {
                i = 2;
            }
        } else if (c == 'A') {
            if (i == 1) {
                i = 2;
            } else if (i == 2) {
                i = 1;
            }
        }
        return i;
    }
}
