fn main()
{
    // let sum_of_square = 
    // let square_of_sum: = 
    //square_of_sum();
    let i = 100;

    println!("{}: {}", i, square_of_sum(i) - sum_of_square(i));
}

fn square_of_sum(max_val : i32) -> i32
{
    let s = (1..=max_val).fold(0, |a, b| {
        // println!("a: {a}");
        // println!("b: {b}");
        a + b

    });
    println!("s: {s}");
    return s * s;
}

fn sum_of_square(max_val : i32) -> i32
{
    let t = (1..=max_val).fold(0, |a, b| a + b * b);
    println!("{t}");
    return t;
}

#[cfg(test)]
mod tests{
    #[test]
    fn test_sum_of_square(){
        let sum_of_square = super::sum_of_square(10);
        assert_eq!(sum_of_square, 385)
    }

    #[test]
    fn test_square_of_sum(){
        let square_of_sum = super::square_of_sum(10);
        assert_eq!(square_of_sum, 3025)
    }

    #[test]
    fn test_base(){
        let diff = super::square_of_sum(10) - super::sum_of_square(10);
        assert_eq!(diff, 2640)
    }
}