fn main() {
    
    let mut inp1: String = String::new();
    let _ = std::io::stdin().read_line(&mut inp1).unwrap();
    let i: i32 = inp1.trim().parse().unwrap();

    let mut inp2: String = String::new();
    let _ = std::io::stdin().read_line(&mut inp2).unwrap();
    let j: i32 = inp2.trim().parse().unwrap();

    let t: i32 = i + j;
    println!("{}", t);
}