package src;

import java.util.Scanner;

public class StuckInATimeLoop {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int times = input.nextInt();
        int counter = 1;

        while(counter <= times){
            System.out.println(counter + " Abracadabra");
            counter++;
        }
    }
}
