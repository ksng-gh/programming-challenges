

import java.util.*;

import java.io.File;

import java.io.FileNotFoundException;
import java.io.IOException;

public class Passphrases {

    public static void main(String[] args){

        ArrayList<String> listOfPassphrase = new ArrayList<String>();
        File inputFile = new File("AoC4.txt");

        int pos = 0;

        try{
            Scanner sc = new Scanner(inputFile);
            listOfPassphrase.add(sc.next());

            while(sc.hasNext()){
                String current = sc.next();
                if(!current.equals(listOfPassphrase.get(pos))){
                    listOfPassphrase.add(current);
                }
            }
        System.out.println(listOfPassphrase.size());
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
