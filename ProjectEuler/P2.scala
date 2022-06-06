object P2{
    def main(args: Array[String]) = {
        var a = 1
        var b = 2
        var sum = 0
        while(b < 40){
            var temp = a
            a = b
            b = temp + b
            
            if(b % 2 == 0){
                sum += b
            }
        }
        println(sum)
    }

}