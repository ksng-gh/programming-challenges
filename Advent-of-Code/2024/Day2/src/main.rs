use std::fs::File;
use std::io::{self, BufRead};
use std::ops::Not;
use std::path::Path;

fn main() {
    if let Ok(lines) = read_lines("src/input.txt")
    {
        let mut is_safe = 0;
        for line in lines
        {
            if let Ok(inp) = line
            {
                let mut vals: Vec<i32> = inp.trim().split_whitespace().map(|i| i.parse::<i32>().unwrap()).collect();
                print!("{:?}\n", vals);

                //vals.reverse(); //"Descending"
                if vals.is_sorted()
                {
                    // print!("first sorted");
                    // continue;
                    let mut t = true;
                    for nr in 0..vals.len() - 1
                    {
                        if !((vals[nr + 1] - vals[nr]) > 0 && (vals[nr + 1] - vals[nr]) < 4)
                        {
                            t = false;
                            break;
                        }
                    }

                    if t
                    {
                        is_safe += 1;
                    }
                }

                vals.reverse(); //"Ascending"

                if vals.is_sorted()
                {
                    // print!("first sorted");
                    // continue;
                    let mut t = true;
                    for nr in 0..vals.len() - 1
                    {
                        if !((vals[nr + 1] - vals[nr]) > 0 && (vals[nr + 1] - vals[nr]) < 4)
                        {
                            t = false;
                            break;
                        }
                    }
                    if t
                    {
                        is_safe += 1;
                    }
                }
            }
            print!("{}", is_safe);
        }

    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
