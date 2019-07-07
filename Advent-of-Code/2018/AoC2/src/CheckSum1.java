import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class CheckSum1 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner inputFile = new Scanner(new File("-"));

        String s = "";
        int hasTwo = 0;
        int hasThree = 0;

        boolean hasTwoAlready = false;
        boolean hasThreeAlready = false;
        boolean letterUsedAlready = false;

        int letterCount = 0;

        ArrayList<Character> letterUsed = new ArrayList<>();

        while(inputFile.hasNextLine()){
            s = inputFile.nextLine();

            for(int i = 0; i < s.length(); i++){
                letterCount++;
                letterUsed.add(s.charAt(i));

                for(int z = 0; z < letterUsed.size() - 1; z++){
                    if(s.charAt(i) == letterUsed.get(z)){
                        letterUsedAlready = true;
                    }
                }

                if(!letterUsedAlready) {
                    for (int j = i + 1; j < s.length(); j++) {
                        if (s.charAt(i) == s.charAt(j)) {
                            letterCount++;
                        }

                    }
                    if (letterCount == 3 && !hasThreeAlready) {
                        hasThree++;
                        hasThreeAlready = true;
                    }
                    if (letterCount == 2 && !hasTwoAlready) {
                        hasTwo++;
                        hasTwoAlready = true;
                    }
                }
                letterUsedAlready = false;
                letterCount = 0;
            }

            hasThreeAlready = false;
            hasTwoAlready = false;
            letterUsed.clear();

        }

        System.out.println(hasThree * hasTwo);
    }

}
