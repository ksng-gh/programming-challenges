fn main() {

    //let c = is_divisible(20);
    let c2 = is_divisible_cheat(20);
    //println!("c: {c}");
    println!("c2: {c2}");
}

fn is_divisible(div_val : i32) -> i32{
    let mut c = 1;
    while true{
        let mut id = true;
        for i in 1..=div_val{
            id = id & (c % i == 0);
        }
        //println!("{c}: {id}");
        if id {
            break;
        }
        c += 1;
    }
    return c;
}

fn is_divisible_cheat(div_val : i32) -> i32{
    let mut c = 2521;
    while true{
        let mut id = true;
        for i in 11..=div_val{
            id = id & (c % i == 0);
        }
        //println!("{c}: {id}");
        if id {
            break;
        }
        c += 1;
    }
    return c;
}

#[cfg(test)]
mod tests{
    #[test]
    fn test_is_divisible(){
        let c = super::is_divisible(10);
        assert_eq!(c, 2520)
    }
}