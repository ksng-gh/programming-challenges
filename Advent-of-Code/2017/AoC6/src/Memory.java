import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Memory {
    public static int getBiggest(int[] a){
        int t = 0;
        int v = a[0];
        while(t < a.length){
            if(a[t] > v){
                v = a[t];
            }
            t++;
        }
        return v;
    }

    public static int part1(int[] array){
        ArrayList<int[]> outerList = new ArrayList<>();
        int biggest = array[0];
        int pos = 0;
        int addToArrayListPos = 0;
        int done = 0;

        while(true) {
            //Getting the position of the biggest value
            //and getting the biggest value
            for (int i = 0; i < array.length; i++) {
                if (biggest < array[i]) {
                    biggest = array[i];
                    if (i < (array.length - 1)) {
                        pos = i + 1;
                    } else if(i == (array.length - 1)){
                        pos = 0;
                    }

                    if(biggest == getBiggest(array)){
                        array[pos - 1] = 0;
                    }
                }
            }

            //Adds the biggest to others in the list
            while (biggest != 0) {

                array[pos]++;
                System.out.println("Test: " + biggest);
                System.out.println("Met: " + Arrays.toString(array));


                if (pos < array.length - 1) {
                    pos++;
                } else if (pos == array.length - 1){
                    pos = 0;
                }
                biggest--;
            }
            System.out.println("Yo sup: ");

            // Adds the arrays to arraylist
            int[] addArray = array;
            outerList.add(addToArrayListPos, addArray);
            addToArrayListPos++;

            //compares the arrays to each other
            if(outerList.size() >= 2) {
                System.out.println(Arrays.equals(outerList.get(0), outerList.get(1)));
                System.out.println("T: " + Arrays.toString(outerList.get(0)));
                System.out.println("Y: " + Arrays.toString(outerList.get(1)));
                for (int a = 0; a < outerList.size(); a++) {
                    for (int b = a + 1; b < outerList.size(); b++) {
                        if (Arrays.equals(outerList.get(a), outerList.get(b))) {
                            return done;
                        }
                    }
                }
            }
            done++;
        }
    }

    public static void main(String[] args){
        File inputFile = new File("AoC6.txt");
        ArrayList<Integer> templist = new ArrayList<>();



        try{
            Scanner sc = new Scanner(inputFile);
            while(sc.hasNext()){
                templist.add(Integer.parseInt(sc.next()));
            }

            int[] inputArray = new int[templist.size()];
            for(int i = 0; i < templist.size(); i++){
                inputArray[i] = templist.get(i);
            }
            System.out.println(Arrays.toString(inputArray));

            System.out.println("Test: " + part1(inputArray));


        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
