import java.util.Scanner;

public class Spavanac {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int hour = input.nextInt();
        int min = input.nextInt();

        min -= 45;
        if(min < 0) {
            min = 60 - Math.abs(min);
            hour--;
        }
        if(hour < 0){
            hour = 23;
        }
        System.out.println(hour + " " + min);
    }
}
