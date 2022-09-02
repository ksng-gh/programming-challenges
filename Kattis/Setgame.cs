using System;
using System.Collections.Generic;
using System.Linq;

/*
a = (1, 2, 3) - # of symbols
b = (D, S, O) - shape (diamond, squiggles, oval)
c = (S, T, O) - filling (solid, stripes, open)
d = (R, G, P) - color (red, green, purple)
*/

class Setgame
{
    static void Main(string[] args)
    {
        //Read info
        List<Tuple<int, int, int>> sets = new List<Tuple<int, int, int>>();
        List<Tuple<char, char, char, char>> table = new List<Tuple<char, char, char, char>>();
        for (int i = 0; i < 4; i++)
        {
            string[] row = Console.ReadLine().Split();
            for (int j = 0; j < 3; j++)
            {
                table.Add(Tuple.Create(row[j][0], row[j][1], row[j][2], row[j][3]));
            }
        }

        //Check all
        for (int first = 0; first < table.Count - 2; first++)
        {
            for (int second = first + 1; second < table.Count - 1; second++)
            {
                for (int third = second + 1; third < table.Count; third++)
                {
                    if (checker(table.ElementAt(first), table.ElementAt(second), table.ElementAt(third)))
                    {
                        sets.Add(Tuple.Create(first + 1, second + 1, third + 1));
                    }
                }
            }
        }

        //Print all
        if (sets.Count == 0)
        {
            Console.WriteLine("no sets");
        }
        else
        {
            for (int i = 0; i < sets.Count; i++)
            {
                Console.WriteLine("{0} {1} {2}", sets.ElementAt(i).Item1, sets.ElementAt(i).Item2, sets.ElementAt(i).Item3);
            }
        }
    }

    static bool checker(Tuple<char, char, char, char> a, Tuple<char, char, char, char> b, Tuple<char, char, char, char> c)
    {
        char a1 = a.Item1; //# of symbols
        char a2 = a.Item2; //shape
        char a3 = a.Item3; //filling
        char a4 = a.Item4; //color

        char b1 = b.Item1;
        char b2 = b.Item2;
        char b3 = b.Item3;
        char b4 = b.Item4;

        char c1 = c.Item1;
        char c2 = c.Item2;
        char c3 = c.Item3;
        char c4 = c.Item4;

        bool check1 = false;
        bool check2 = false;
        bool check3 = false;
        bool check4 = false;

        if ((a1 == b1 && b1 == c1) || (a1 != b1 && b1 != c1 && a1 != c1))
        {
            check1 = true;
        }

        if ((a2 == b2 && b2 == c2) || (a2 != b2 && b2 != c2 && a2 != c2))
        {
            check2 = true;
        }

        if ((a3 == b3 && b3 == c3) || (a3 != b3 && b3 != c3 && a3 != c3))
        {
            check3 = true;
        }

        if ((a4 == b4 && b4 == c4) || (a4 != b4 && b4 != c4 && a4 != c4))
        {
            check4 = true;
        }

        return (check1 && check2 && check3 && check4) ? true : false;
    }
}