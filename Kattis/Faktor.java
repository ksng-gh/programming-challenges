import java.util.Scanner;

public class Faktor {
    // output/first input = second input.
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int first = input.nextInt();
        int second = input.nextInt();

        int sum = first * second - first + 1;

        System.out.println(sum);
        input.close();
    }
}
