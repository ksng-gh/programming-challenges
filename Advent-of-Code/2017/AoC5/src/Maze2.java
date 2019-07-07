import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Maze2 {

    public static int part2(int[] e){
        int current = 0;
        int steps = 0;
        while(e.length > current){
            int temp = e[current];
            if(temp >= 3){
                e[current]--;
            } else {
                e[current]++;
            }
            current += temp;
            steps++;
        }
        return steps;
    }

    public static void main(String[] args){
        ArrayList<Integer> listOfSteps = new ArrayList<Integer>();
        File inputFile = new File("AoC5.txt");


        try{
            Scanner sc = new Scanner(inputFile);

            while (sc.hasNext()){
                listOfSteps.add(Integer.parseInt(sc.next()));
            }
            int[] a = new int[listOfSteps.size()];

            for(int i = 0; i < a.length; i++){
                a[i] = listOfSteps.get(i);
            }

            System.out.println("J: " + part2(a));


        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

