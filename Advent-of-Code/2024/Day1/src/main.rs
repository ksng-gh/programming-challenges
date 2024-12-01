use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

//Improvements: Group similar numbers or something.
fn main() {
    if let Ok(lines) = read_lines("src/input.txt")
    {
        let mut left: Vec<i32> = Vec::new();
        let mut right: Vec<i32> = Vec::new();

        let mut dist = 0;
        let mut score: i32 = 0;
        for line in lines
        {
            if let Ok(inp) = line
            {
                let vals: Vec<&str> = inp.split_whitespace().collect();
                
                left.push(vals[0].parse().expect("Couldnt parse"));
                right.push(vals[1].parse().expect("Couldnt parse"));
            }
        }
//PART 1
        // left.sort();
        // right.sort();

        // for n in 0..left.len()
        // {
        //     dist += i32::abs(left[n] - right[n]);
        // }
        // print!("{}", dist);

//PART 2                
        let mut occ = 0;
        for n in 0..left.len()
        {
            for j in 0..right.len()
            {
                if right[j] == left[n]
                {
                    occ += 1
                }
            }
            score += (left[n] * occ);
            occ = 0;
        }
        print!("{}", score);
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
