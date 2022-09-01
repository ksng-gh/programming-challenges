using System;
using System.Collections.Generic;
using System.Linq;

//. .   . .

class Ultimatebinarywatch
{
    static void Main(string[] args)
    {
        int[] time = Array.ConvertAll(Console.ReadLine().ToCharArray(), c => (int)Char.GetNumericValue(c));
        char[] bin = new char[4];

        for (int i = 3; i >= 0; i--)
        {
            for (int j = 0; j < time.Length; j++)
            {
                int t = time[j];
                int diff = t - (int)(Math.Pow((double)2.0, i));
                int d = diff >= 0 ? diff : t;

                bin[j] = diff >= 0 ? '*' : '.';
                time[j] = d;
            }

            Console.WriteLine("{0} {1}   {2} {3}", bin[0], bin[1], bin[2], bin[3]);
        }
    }
}