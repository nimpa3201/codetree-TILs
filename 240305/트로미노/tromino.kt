fun main(){
    val (n, m) = readLine()!!.trimEnd().split(" ").map{it.toInt()}
    val arr = MutableList<List<Int>>(0){List<Int>(0){0}}

    for(i in 1 .. n){
        arr.add(readLine()!!.trimEnd().split(" ").map{it.toInt()})
    }

    // 블럭들
    val block1 = listOf(listOf(0, 0), listOf(0, 1), listOf(0, -1))
    val block2 = listOf(listOf(0, 0), listOf(1, 0), listOf(-1, 0))
    val block3 = listOf(listOf(0, 0), listOf(1, 0), listOf(0, 1))
    val block4 = listOf(listOf(0, 0), listOf(-1, 0), listOf(0, 1))
    val block5 = listOf(listOf(0, 0), listOf(1, 0), listOf(0, -1))
    val block6 = listOf(listOf(0, 0), listOf(-1, 0), listOf(0, -1))

    val blocks = listOf(block1, block2, block3, block4, block5, block6)

    // 탐색
    var max = 0;
    for(r in 0 until n){
        for(c in 0 until m){
            // 블럭 확인
            for(block in blocks){
                var temp = 0;
                var flag = true
                for(b in block){
                    val nr = r + b[0]
                    val nc = c + b[1]

                    if(nr >= 0 && nc >= 0 && nr < n && nc < m){
                        temp += arr[nr][nc]
                    }else{
                        flag = false
                        break
                    }
                }

                if(flag){
                    //println("$r $c $block : $temp")
                    max = maxOf(max, temp)
                }
            }
        
        }
    }

    println(max)
}