import java.util.Scanner;
public class Hidden {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] s = sc.nextLine().split(" ");
        String a = s[0];
        String b = s[1];
        boolean t = true;
        boolean n = false;
        for(int i = 0; i < b.length(); i++){
            if (a.length() == 0){
                continue;
            }
            n = false;
            for(int j = 0; j < a.length(); j++){
                if(n){
                    continue;
                }
                char c = a.charAt(0);
                if(a.charAt(j) == b.charAt(i)){
                    if(a.charAt(j) != c){
                        t = false;
                        a = "";
                    } else {
                        if(a.length() > 0){
                            a = a.substring(1);
                            n = true;
                        }                        
                    }
                }
            }
        }
        if(t == false || a.length() > 0){
            System.out.println("FAIL");
        } else {
            System.out.println("PASS");
        }
    }
}
