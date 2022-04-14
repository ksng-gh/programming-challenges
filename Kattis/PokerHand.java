import java.util.Arrays;
import java.util.Scanner;

public class PokerHand {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        String line = input.nextLine();
        String[] hand = line.split(" ");
        int strength = 0;
        int cStrength = 1;

        for(int i = 0; i < hand.length; i++){
            int val = returnCorrectValue(hand[i]);
            for(int j = i + 1; j < hand.length; j++){
                if(val == returnCorrectValue(hand[j])){
                    cStrength++;
                }
            }
            if(cStrength > strength){
                strength = cStrength;
                cStrength = 1;
            }
        }
        System.out.println(strength);

    }

    public static int returnCorrectValue(String card){

        char c = card.charAt(0);

        if(c == 'A'){
            return 1;
        } else if(c == 'T') {
            return 10;
        } else if(c == 'J') {
            return 11;
        } else if(c == 'Q'){
            return 12;
        } else if (c == 'K'){
            return 13;
        } else {
            return c;
        }
    }
}
