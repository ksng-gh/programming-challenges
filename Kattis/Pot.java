package src;

import java.util.Scanner;

public class Pot {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int times = input.nextInt();
        int sum = 0;
        while(times > 0){
            int next = input.nextInt();
            sum += calc(next);
            times--;
        }
        System.out.println(sum);
    }

    public static double calc(int numb){
        int number = 0;
        int exponent = 0;

        String s = Integer.toString(numb);
        number = Integer.parseInt(s.substring(0,s.length() - 1));
        exponent = numb % 10;

        return Math.pow((double) number, (double) exponent);
    }
}
