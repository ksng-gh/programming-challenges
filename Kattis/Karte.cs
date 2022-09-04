using System;
using System.Collections.Generic;
using System.Linq;

class Karte
{
    static void Main(string[] args)
    {
        string s = Console.ReadLine();
        string[] newString = string.Join(string.Empty, s.Select((x, i) => i > 0 && i % 3 == 0 ? string.Format(" {0}", x) : x.ToString())).Split();
        string r = string.Empty;
        int[] counters = new int[4];

        for (int i = 0; i < newString.Length; i++)
        {
            switch (newString[i][0])
            {
                case 'P':
                    counters[0] += 1;
                    break;
                case 'K':
                    counters[1] += 1;
                    break;
                case 'H':
                    counters[2] += 1;
                    break;
                case 'T':
                    counters[3] += 1;
                    break;
            }
        }

        for (int i = 0; i < newString.Length - 1; i++)
        {
            for (int j = i + 1; j < newString.Length; j++)
            {
                if (newString[i] == newString[j])
                {
                    r = "GRESKA";
                }
            }
        }

        if (r.Length > 0)
        {
            Console.WriteLine(r);
        }
        else
        {
            Console.WriteLine("{0} {1} {2} {3}", 13 - counters[0], 13 - counters[1], 13 - counters[2], 13 - counters[3]);
        }
    }
}