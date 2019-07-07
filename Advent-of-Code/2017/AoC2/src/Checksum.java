/*
Not finished due to nextLine fuckery
 */

import java.io.*;
import java.util.Scanner;


public class Checksum {

    public static void main(String[] args){
        int max = 0;
        int min = 0;
        int temp = 0;
        int sum = 0;

        File inputFile = new File("AoC2.txt");

        try{
            Scanner sc = new Scanner(inputFile);
            max = Integer.parseInt(sc.next());
            min = Integer.parseInt(sc.next());
            String newline = System.getProperty("line.separator");
            boolean hasNewline = sc.next().contains(newline);

            if(max < min){
                temp = min;
                min = max;
                max = temp;
            }
            while(!sc.next().equals('\n')) {
                temp = Integer.parseInt(sc.next());
                if (temp < min && temp < max) {
                    min = temp;
                } else if (temp > min && temp > max) {
                    max = temp;
                }
                System.out.println("T: " + temp);
            }

        } catch(IOException e) {
            e.printStackTrace();
        }
        System.out.println(sum);
    }

}
