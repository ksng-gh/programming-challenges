import java.util.Scanner;

public class Luhnchecksum{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int tests = Integer.parseInt(in.nextLine());

        for(int t = 0; t < tests; t++){            
            StringBuilder s = new StringBuilder(in.nextLine()).reverse();
            int[] iarr = new int[s.length()];
            for(int i = 0; i < iarr.length; i++){
                iarr[i] = Character.getNumericValue(s.charAt(i));
            }
            int sum = 0;
            for (int c = 0; c < iarr.length; c++){
                int n = iarr[c];
                if(c % 2 == 1){
                    n *= 2;
                    if (n > 9){
                        String ns = Integer.toString(n) ;
                        n = Character.getNumericValue(ns.charAt(0)) + Character.getNumericValue(ns.charAt(1));
                    }
                }
                sum += n;
            }
            
            if(sum % 10 == 0){
                System.out.println("PASS");
            } else {
                System.out.println("FAIL");
            }
            
        }
    }
}