using System;
using System.Collections.Generic;
using System.Linq;

//C# so strong that this same code be used for Shoppinglist.cs
class Shoppinglisteasy
{
    static void Main(string[] args)
    {
        string[] values = Console.ReadLine().Split(' ');
        int n = int.Parse(values[0]);
        int m = int.Parse(values[1]);

        List<string> groceries = new List<string>(Console.ReadLine().Split(' '));

        if (n != 1)
        {
            for (int i = 0; i < n - 1; i++)
            {
                List<string> newgroceries = new List<string>(Console.ReadLine().Split(' '));
                var intersect = groceries.Intersect(newgroceries);
                groceries = intersect.ToList();
            }
        }

        groceries.Sort();
        Console.WriteLine(groceries.Count);
        foreach (string g in groceries)
        {
            Console.WriteLine(g);
        }
    }
}