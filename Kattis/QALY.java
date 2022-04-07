package src;

import java.util.Locale;
import java.util.Scanner;

public class QALY {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in).useLocale(Locale.US);
        int counter = input.nextInt();

        double sum = 0;

        while (counter > 0){
            double a = input.nextDouble();
            double b = input.nextDouble();

            sum += a * b;
            counter--;
        }
        System.out.println(sum);
    }
}
