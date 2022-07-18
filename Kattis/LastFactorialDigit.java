import java.util.Scanner;

public class LastFactorialDigit {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int sum = 1;
        int dig = 0;
        int times = input.nextInt();
        while (times > 0) {
            dig = input.nextInt();
            for (int i = dig; i > 1; i--) {
                sum *= dig--;
            }
            System.out.println(sum % 10);
            sum = 1;
            times--;
        }
        input.close();
    }
}
