use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use regex::Regex;

fn decorrupt(line: &str) -> i32
{
    let regex = Regex::new(r"mul\(\d+,\d+\)").unwrap();

    let muls = regex.find_iter(line)
            .filter_map(|muls| muls.as_str().parse().ok())
            .collect::<Vec<String>>();
    
    let mulstrs: Vec<&str> = muls.iter().map(|s| &**s).collect();
    let mut c = 0;

    let vals = Regex::new(r"\d+,\d+").unwrap();

    for i in mulstrs //mul(int, int)
    {
        let m = vals.captures(i)
                .map(|captures|{
                    captures
                        .iter()
                        .flat_map(|c| c)
                        .map(|c| c.as_str())
                        .collect::<String>()
                });


        match m{
            None => {
                println!("Nope");
            }
            Some(m) => {
                //print!("{}", m);
                let parts = m.split(',').collect::<Vec<&str>>();
                
                c += parts[0].parse::<i32>().unwrap() * parts[1].parse::<i32>().unwrap();
                
            }
        }
    }
    return c;
}

//Can't make regex capture "do()" and "don't()". F this

fn main() {
    if let Ok(lines) = read_lines("src/input.txt")
    {
        let mut c = 0;
        let mut c2 = 0;
        for line in lines
        {
            if let Ok(inp) = line
            {
                c += decorrupt(&inp);
                //c2 += decorrupt2(&inp);
                
            }
        }
        println!("{}", c);
        println!("{}", c2);
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
