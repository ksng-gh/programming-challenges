use std::env;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut holder: Vec<char>;
    let mut count: i32 = 0;
    let mut n;
    //let contents = fs::read_to_string("src/input.txt").expect("Should be a file");
    if let Ok(lines) = read_lines("src/input.txt") {
        for line in lines {
            if let Ok(ip) = line {
                holder = ip.chars().filter(|char| char.is_digit(10)).collect();
                n = format!("{}{}", holder.clone().into_iter().nth(0).expect("Not an int"), holder.clone().into_iter().nth(holder.len() - 1).expect("Not an int"));
                let p: i32 = n.parse().expect("Not a digit");
                count = count + p;
                println!{"{}", count};
            }
        }
    }

    //println!("Contents {contents}");
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}