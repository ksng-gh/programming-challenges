using System;

class Grading
{
    static void Main(string[] args)
    {
        int[] grades = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
        int grade = int.Parse(Console.ReadLine());

        if (grade >= grades[0])
        {
            Console.WriteLine('A');
        }
        else if (grade >= grades[1])
        {
            Console.WriteLine('B');
        }
        else if (grade >= grades[2])
        {
            Console.WriteLine('C');
        }
        else if (grade >= grades[3])
        {
            Console.WriteLine('D');
        }
        else if (grade >= grades[4])
        {
            Console.WriteLine('E');
        }
        else
        {
            Console.WriteLine('F');
        }

    }

}
