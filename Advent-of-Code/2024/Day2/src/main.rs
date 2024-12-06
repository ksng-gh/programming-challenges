use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::HashSet;

fn q1(vals: &Vec<i32>) -> bool
{
    let mut pos = HashSet::from([1, 2, 3]);
    let mut neg = HashSet::from([-1, -2, -3]); 

    for i in 0..vals.len() - 1
    {
        pos.insert(vals[i + 1] - vals[i]);
        neg.insert(vals[i + 1] - vals[i]);
    }

    if pos.len() == 3 || neg.len() == 3
    {
        return true;
    }
    return false;
}

fn q2(vals: &Vec<i32>) -> bool
{
    if q1(vals)
    {
        return true;
    }
    
    for i in 0..vals.len()
    {
        let mut copy = vals.clone();
        copy.remove(i);
        if q1(&copy)
        {
            return true;
        }
    }
    return false;
}

fn main() {
    if let Ok(lines) = read_lines("src/input.txt")
    {
        let mut is_safe = 0;
        let mut is_safe2: i32 = 0;
        for line in lines
        {
            if let Ok(inp) = line
            {
                let vals: Vec<i32> = inp.trim().split_whitespace().map(|i| i.parse::<i32>().unwrap()).collect();

                is_safe += q1(&vals) as i32;
                is_safe2 += q2(&vals) as i32;

                //Bad solution, part 1, comment of shame
                // if vals.is_sorted()
                // {
                //     let mut t = true;
                //     for nr in 0..vals.len() - 1
                //     {
                //         if !((vals[nr + 1] - vals[nr]) > 0 && (vals[nr + 1] - vals[nr]) < 4)
                //         {
                //             t = false;
                //             break;
                //         }
                //     }

                //     if t
                //     {
                //         is_safe += 1;
                //     }
                // }

                // vals.reverse(); //"Ascending"

                // if vals.is_sorted()
                // {
                //     let mut t = true;
                //     for nr in 0..vals.len() - 1
                //     {
                //         if !((vals[nr + 1] - vals[nr]) > 0 && (vals[nr + 1] - vals[nr]) < 4)
                //         {
                //             t = false;
                //             break;
                //         }
                //     }
                //     if t
                //     {
                //         is_safe += 1;
                //     }
                // }
            }
        }
        print!("{}", is_safe);
        print!("{}", is_safe2);
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
