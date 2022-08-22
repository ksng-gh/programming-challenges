using System;
using System.Collections.Generic;

class Piglatin
{
    static void Main(string[] args)
    {
        string word;
        HashSet<char> vowels = new HashSet<char> { 'a', 'e', 'i', 'o', 'u', 'y' };

        while (!string.IsNullOrEmpty(word = Console.ReadLine()))
        {
            string[] words = word.Split();
            for (int i = 0; i < words.Length; i++)
            {
                Console.Write(pigify(words[i], vowels) + " ");
            }
            Console.WriteLine();

        }
    }

    static string pigify(string s, HashSet<char> vowels)
    {
        if (vowels.Contains(s[0]))
        {
            s += "yay";
        }
        else
        {
            string temp = "";
            int i = 0;
            while (!vowels.Contains(s[i]))
            {
                temp += s[i];
                i++;
            }
            s = s.Remove(0, i);
            s += temp;
            s += "ay";

        }
        return s;
    }
}