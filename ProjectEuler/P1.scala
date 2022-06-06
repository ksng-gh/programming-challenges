object P1{
    def main(args: Array[String]) = {
        var a = 0
        var sum = 0
        for (a <- 1 until 1000){
            if(a % 3 == 0 || a % 5 == 0){
                sum += a
            }
        }
        println(sum)
    }

}