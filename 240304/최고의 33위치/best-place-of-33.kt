fun main(){
    val N = readLine()!!.toInt()

    val arr = MutableList<List<Int>>(0){List(0){0}}

    for(i in 0 until N){
        arr.add(readLine()!!.trimEnd().split(" ").map{it.toInt()})
    }

    var max = 0
    for(r in 0 until N-2){
        for(c in 0 until N-2){
            var tempSum = 0
            for(y in r until r+3){
                for(x in c until c+3){
                    tempSum += arr[y][x]
                }
            }

            max = maxOf(tempSum, max)
        }
    }

    print(max)
}