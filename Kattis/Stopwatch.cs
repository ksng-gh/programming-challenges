using System;

class Stopwatch{
    static void Main(string[] args){
        int presses = Convert.ToInt32(Console.ReadLine());
        int seconds = 0;

        if (presses % 2 == 1){
            Console.WriteLine("still running");
            
        } else {
            for(int i = 0; i < presses; i+=2){
                int timer = Convert.ToInt32(Console.ReadLine());
                int timer2 = Convert.ToInt32(Console.ReadLine());
                seconds += timer2 - timer;
            }
            Console.WriteLine(seconds);
        }
    }
}