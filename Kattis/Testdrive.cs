using System;
using System.Collections.Generic;
using System.Linq;

class Testdrive
{
    static void Main(String[] args)
    {
        int[] pos = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
        int info = pos[1] - pos[0]; //first interval
        int decider = pos[2] - pos[1]; //2nd interval

        if (decider == info)
        {
            Console.WriteLine("cruised");
        }
        else if (info > 0 && decider < 0 || info < 0 && decider > 0)
        {
            Console.WriteLine("turned");
        }
        else if (Math.Abs(decider) > Math.Abs(info))
        {
            Console.WriteLine("accelerated");
        }
        else if (Math.Abs(decider) < Math.Abs(info))
        {
            Console.WriteLine("braked");
        }
    }
}