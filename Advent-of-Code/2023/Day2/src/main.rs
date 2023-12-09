use std::env;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

//max: 12 red, 13 green, 14 blue

fn main() {
    let mut count: i32 = 0;
    let part = 2;
    let mut mincol: Vec<i32> = vec![0; 3]; //red, green, blue

    //if let Ok(lines) = read_lines("src/test.txt") {
    if let Ok(lines) = read_lines("src/input.txt") {
        for line in lines {
            if let Ok(ip) = line {
                //print!("{}", ip);
                
                if(part == 1)
                {
                    let p: Vec<String> = ip.split(":").map(|s| s.to_string()).collect();
                    let gamenr: i32 = p.clone().into_iter().nth(0).unwrap().split(' ').map(|s| s.to_string()).into_iter().nth(1).unwrap().parse().unwrap();
    
                    let mut game: Vec<String> = p.into_iter().nth(1).unwrap().split(";").map(|s| s.to_string()).collect();
                    let mut ok = true;
                    for round in game.iter_mut(){
                        let mut case: Vec<String> = round.split(',').map(|x| x.to_string()).collect();
                        for i in case.iter_mut(){ //j = (x blue)
                            let a: Vec<String> = i.split_whitespace().map(|t| t.to_string()).collect();
                            let n: i32 = a.clone().into_iter().nth(0).unwrap().parse().unwrap();
                            let c = a.into_iter().nth(1).unwrap();
                            match c.as_str(){
                                "red" if n > 12 => ok = false,
                                "blue" if n > 14 => ok = false,
                                "green" if n > 13 => ok = false,
                                _ => (),
                            }
                        }
                    }
                    if ok == true {
                        count += gamenr
                    }
                    println!("count: {}", count)
                }
                else{
                    let p: Vec<String> = ip.split(":").map(|s| s.to_string()).collect();
                    let gamenr: i32 = p.clone().into_iter().nth(0).unwrap().split(' ').map(|s| s.to_string()).into_iter().nth(1).unwrap().parse().unwrap();
    
                    let mut game: Vec<String> = p.into_iter().nth(1).unwrap().split(";").map(|s| s.to_string()).collect();
                    let mut ok = true;
                    for round in game.iter_mut(){
                        let mut case: Vec<String> = round.split(',').map(|x| x.to_string()).collect();
                        for i in case.iter_mut(){ //j = (x blue)
                            let a: Vec<String> = i.split_whitespace().map(|t| t.to_string()).collect();
                            let n: i32 = a.clone().into_iter().nth(0).unwrap().parse().unwrap();
                            let c = a.into_iter().nth(1).unwrap();
                            println!("n: {}", n);
                            println!("c: {}", c);
                            match c.as_str(){
                                "red" if n > mincol.clone().into_iter().nth(0).unwrap() => mincol[0] = n,
                                "blue" if n > mincol.clone().into_iter().nth(2).unwrap() => mincol[2] = n,
                                "green" if n > mincol.clone().into_iter().nth(1).unwrap() => mincol[1] = n,
                                _ => (),
                            }
                            println!("{:?}", mincol);
                        }
                    }
                    
                    let mut t: i32 = 1;
                    for i in mincol.iter_mut(){
                        println!("i: {}", i);
                        t *= *i;
                    }
                    mincol = vec![0; 3];

                    println!("t: {}", t);

                    count += t;
                    println!("count: {}", count);
                }
            }
        }
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
