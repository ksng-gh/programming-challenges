import java.util.Scanner;

public class GrassSeed {
    public static void main(String[] args){
        Scanner inp = new Scanner(System.in);
        double cost = inp.nextDouble();
        int lawns = inp.nextInt();

        double one = 0;
        double two = 0;

        double sum = 0;
        while(lawns * 2 > 0){

            one = inp.nextDouble();
            two = inp.nextDouble();

            sum += one*two;

            lawns -= 1;
        }
        System.out.println(sum * cost);
    }
}
