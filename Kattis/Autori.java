import java.util.Scanner;

public class Autori {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        String s = input.nextLine();
        String res = "";

        int i = 0;
        while(i < s.length()){
            if(Character.isUpperCase(s.charAt(i))){
                res = res+s.charAt(i);
            }
            i++;
        }
        System.out.println(res);
    }
}
