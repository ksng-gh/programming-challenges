fn main() {
    
    let mut line: String = String::new();
    let b1 = std::io::stdin().read_line(&mut line).unwrap();
    let mut count: i32 = 0;
    for c in line.chars(){
        if c == 'u' {
            count += 1;
        }
    }
    println!("{}", count);
}
