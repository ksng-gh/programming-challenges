import java.util.Scanner;

public class Tarifa {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int megabyte = input.nextInt();
        int month = input.nextInt();

        int i = megabyte;

        while (month > 0){
            i -= input.nextInt();
            i += megabyte;

            month--;
        }

        System.out.println(i);

    }

}
