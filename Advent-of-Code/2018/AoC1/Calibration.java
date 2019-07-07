import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Calibration {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner input = new Scanner(new File("-"));

        String line = "";
        int sum = 0;

        while(input.hasNext()){
            line = input.nextLine();

            System.err.println(line);

            if(line.charAt(0) == '+'){

                sum += Integer.parseInt(line.substring(1));
            } else {
                sum -= Integer.parseInt(line.substring(1));
            }
        }


        System.err.println("Result: " + sum);
    }
}
