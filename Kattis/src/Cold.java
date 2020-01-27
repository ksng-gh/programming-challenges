package src;

import java.util.Scanner;

public class Cold {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        int totInp = in.nextInt();
        int negCount = 0;

        while(totInp > 0){
            if(in.nextInt() < 0){
                negCount++;
            }
            totInp--;
        }
        System.out.println(negCount);
    }
}
