import java.util.Scanner;

public class TakeTwoStones {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();

        if(num % 2 == 1){
            System.out.println("Alice");
        } else {
            System.out.println("Bob");
        }
    }
}
