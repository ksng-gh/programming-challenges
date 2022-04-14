import java.util.Scanner;

public class Zamka {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int lower = input.nextInt();
        int higher = input.nextInt();
        int target = input.nextInt();

        int retLow = 0;
        int retHi = 0;

        for(int i = lower; i <= higher; i++){
            if(giveIntAsSum(i) == target){
                retLow = i;
                break;
            }
        }

        for(int i = higher; i >= lower; i--){
            if(giveIntAsSum(i) == target){
                retHi = i;
                break;
            }
        }

        System.out.println(retLow);
        System.out.println(retHi);
    }

    public static int giveIntAsSum(int i){
        int added = 0;
        while(i > 0){
            added += i%10;
            i /= 10;
        }

        return added;
    }
}
