using System;
class Wannabe
{
    static void Main(string[] args)
    {
        string s = Console.ReadLine();
        int[] info = Array.ConvertAll(s.Split(), int.Parse);

        var pokenoms = new List<(int, int, int)>();

        for (int i = 0; i < info[0]; i++)
        {
            int[] d = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            pokenoms.Add(Tuple.Create(d[0], d[1], d[2]));
        }

        for (int p = 0; p < info[1]; p++)
        {
            int diff = 0;
            int a, d, h, ai, di, hi = 0;


        }
    }
}


