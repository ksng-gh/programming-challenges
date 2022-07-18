import java.util.Scanner;

public class Filip {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int first = input.nextInt();
        int second = input.nextInt();

        System.out.println(compare(first, second));
        input.close();

    }

    public static String compare(int a, int b) {
        String s1 = Integer.toString(a);
        String s2 = Integer.toString(b);

        int i = s1.length();

        while (i > 0) {
            int c1 = Integer.parseInt(s1.substring(i - 1, i));
            int c2 = Integer.parseInt(s2.substring(i - 1, i));

            if (c1 > c2) {
                return s1.substring(2) + s1.substring(1, 2) + s1.substring(0, 1);
            } else if (c1 < c2) {
                return s2.substring(2) + s2.substring(1, 2) + s2.substring(0, 1);
            }
            i--;
        }
        return "Not valid";
    }
}
