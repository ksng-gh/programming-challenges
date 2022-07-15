using System;
using System.Linq;

class Unlockpattern
{
    static void Main(string[] args)
    {
        Tuple<double, double>[] arrayOfPos = new Tuple<double, double>[9];

        for (int i = 0; i < 3; i++)
        {
            string[] inp = Console.ReadLine().Split();

            for (int j = 0; j < inp.Length; j++)
            {
                arrayOfPos[int.Parse(inp[j]) - 1] = new Tuple<double, double>((double)i, (double)j);
            }
        }

        double totallength = 0.0;
        for (int i = 0; i < arrayOfPos.Length - 1; i++)
        {
            totallength += calcDiagDist(arrayOfPos[i], arrayOfPos[i + 1]);
        }

        Console.WriteLine(totallength);
    }

    static double calcDiagDist(Tuple<double, double> pos1, Tuple<double, double> pos2)
    {
        return Math.Sqrt(Math.Pow(pos1.Item1 - pos2.Item1, 2) + Math.Pow(pos1.Item2 - pos2.Item2, 2));
    }
}