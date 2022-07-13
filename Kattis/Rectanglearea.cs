using System;

class Rectanglearea
{
    static void Main(string[] args)
    {
        string s = Console.ReadLine();
        double[] v = Array.ConvertAll(s.Split(' '), double.Parse);

        double[] c1 = maxFirst(v[0], v[2]);
        double[] c2 = maxFirst(v[1], v[3]);

        Console.WriteLine(Math.Abs((c1[0] - c1[1]) * (c2[0] - c2[1])));
    }

    static double[] maxFirst(double a, double b)
    {
        return a > b ? new double[] { a, b } : new double[] { b, a };
    }
}