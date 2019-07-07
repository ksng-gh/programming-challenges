
import java.util.*;

public class Securedoors {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        boolean token = true;
        int size = in.nextInt();
        in.nextLine(); //Get rid of \n

        ArrayList<String> name = new ArrayList<>();
        String a  = "";
        String n = "";

        for(int i = 0; i < size; i++){
            String temp[] = in.nextLine().split(" ");
            a = temp[0];
            n = temp[1];

            if(a.equals("entry")){
                for(int j = 0; j < name.size(); j++){
                    if(n.equals(name.get(j))){
                        System.out.println(n + " entered (ANOMALY)");
                        token = false;
                    }
                }
                if(token){
                    name.add(n);
                    System.out.println(n + " entered");
                }
                token = true;
            } else {
                for(int k = 0; k < name.size(); k++){
                    if(n.equals(name.get(k))){
                        System.out.println(n + " exited");
                        name.remove(n);
                        token = false;
                    }
                }
                if(token){
                    System.out.println(n + " exited (ANOMALY)");
                }
                token = true;
            }
        }
    }
}
