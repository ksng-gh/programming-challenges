fn main()
{
    let mut fib_sum = 0;
    let mut count = 1;

    while count > 0
    {
        let i = nth_fib_seq(count);
        //println!("{i}");
        if i > 4000000
        {
            break
        }
        if i % 2 == 0 //Only even
        {
            fib_sum += i;
        }
        count += 1;
    }

    println!("fib sum: {fib_sum}");
}

fn nth_fib_seq(n : i32) -> i32
{
    if n <= 1
    {
        return n;
    }

    // (n - 1) + (n - 2)
    return nth_fib_seq(n - 1) + nth_fib_seq(n - 2);
}
