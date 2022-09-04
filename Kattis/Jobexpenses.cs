using System;
using System.Linq;

class Jobexpenses
{
    static void Main(string[] args)
    {
        int l = int.Parse(Console.ReadLine());
        int[] finance = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

        int sum = 0;
        for (int i = 0; i < finance.Length; i++)
        {
            if (finance[i] < 0)
            {
                sum += Math.Abs(finance[i]);
            }
        }

        Console.WriteLine(sum);
    }
}