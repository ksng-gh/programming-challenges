using System;

class Ratingproblems{
    static void Main(string[] args){
        string s = Console.ReadLine();
        int[] judge = Array.ConvertAll(s.Split(' '), int.Parse);

        int min = (judge[0] - judge[1]) * -3;
        int max = (judge[0] - judge[1]) * 3;
        int diff = 0;

        for(int i = 0; i < judge[1]; i++){
            diff += Convert.ToInt32(Console.ReadLine());
        }

        float minrate = (float) (min + diff) / (float) judge[0];
        float maxrate = (float) (max + diff) / (float) judge[0];

        Console.WriteLine("{0} {1}", minrate, maxrate);

    }
}