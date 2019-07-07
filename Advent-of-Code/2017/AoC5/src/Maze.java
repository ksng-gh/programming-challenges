/*import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class Maze {

    public static void main(String[] args){
        ArrayList<Integer> listOfSteps = new ArrayList<Integer>();
        File inputFile = new File("AoC5.txt");
        int posInList = 0;
        int posMemory = 0;
        int jump = 0;

        try{
            Scanner sc = new Scanner(inputFile);

            while (sc.hasNext()){
                listOfSteps.add(Integer.parseInt(sc.next()));
            }

            while(listOfSteps.size() > posInList){
                posMemory = posInList;
                posInList = posInList + listOfSteps.get(posInList);
                listOfSteps.set(posMemory, listOfSteps.get(posMemory) + 1);
                jump++;
            }
            System.out.println("J: " + jump);


        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
*/