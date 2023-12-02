use std::env;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut holder: Vec<char>;
    let mut count: i32 = 0;
    let mut n;

    //if let Ok(lines) = read_lines("src/test.txt") {
    if let Ok(lines) = read_lines("src/input.txt") {
        for line in lines {
            if let Ok(ip) = line {

                //part 2
                let s: String = replace_text_to_numbers(ip);

                print!("{}", s);
                print!("{}", " ");

                holder = s.chars().filter(|char| char.is_digit(10)).collect(); //p2 filter numbers
                //holder = ip.chars().filter(|char| char.is_digit(10)).collect(); //p1 filter numbers
                n = format!("{}{}", holder.clone().into_iter().nth(0).expect("Not an int"), holder.clone().into_iter().nth(holder.len() - 1).expect("Not an int")); //"append" chars
                let p: i32 = n.parse().expect("Not a digit"); //parse
                count = count + p;
                
                println!{"{}", count};
            }
        }
    }
}

fn replace_text_to_numbers(mut s: String) -> String {
    s = s.replace("one", "o1e");
    s = s.replace("two", "t2o");
    s = s.replace("three", "t3e");
    s = s.replace("four", "f4r");
    s = s.replace("five", "f5e");
    s = s.replace("six", "s6x");
    s = s.replace("seven", "s7n");
    s = s.replace("eight", "e8t");
    s = s.replace("nine", "n9e");
    s
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

