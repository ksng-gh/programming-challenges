using System;
using System.Linq;
using System.Collections.Generic;

class Simone
{
    static void Main(string[] args)
    {
        string[] nk = Console.ReadLine().Split();
        int n = int.Parse(nk[0]);
        int k = int.Parse(nk[1]);

        string colors = Console.ReadLine();
        int[] colorsarray = Array.ConvertAll(colors.Split(), int.Parse);
        int[] colortracker = new int[k];

        for (int i = 0; i < colorsarray.Length; i++)
        {
            colortracker[colorsarray[i] - 1] += 1;
        }

        int min = colortracker.Min();
        List<int> rettracker = new List<int>();

        for (int i = 0; i < colortracker.Length; i++)
        {
            if (colortracker[i] == min)
            {
                rettracker.Add(i + 1);
            }
        }

        Console.WriteLine(rettracker.Count());
        for (int i = 0; i < rettracker.Count(); i++)
        {
            Console.Write(rettracker[i] + " ");
        }
    }
}