package src;

import java.util.Scanner;

public class R2 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int r1 = input.nextInt();
        int answer = input.nextInt();

        System.out.println(answer*2 - r1);
    }
}
