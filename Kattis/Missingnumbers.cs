using System;
using System.Collections.Generic;
using System.Linq;

class Missingnumbers
{
    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        List<int> numbers = new List<int>();
        for (int i = 0; i < n; i++)
        {
            numbers.Add(int.Parse(Console.ReadLine()));
        }
        if (numbers.Last() == numbers.Count())
        {
            Console.WriteLine("good job");
        }
        else
        {
            int current = 1;
            for (int i = 0; i < numbers.Count; i++)
            {
                int c = numbers.ElementAt(i);
                while (current < c)
                {
                    Console.WriteLine(current);
                    current += 1;
                }
                current = c + 1;
            }
        }


    }
}