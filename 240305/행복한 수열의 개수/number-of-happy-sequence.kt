fun main(){
    val (n, m) = readLine()!!.trimEnd().split(" ").map{it.toInt()}
    
    // 행복한 수열 : 연속해서 m개 이상의 동일한 원소가 나와야 함
    val array = MutableList<List<Int>>(0){List<Int>(0){0}}

    for(i in 1 .. n){
        array.add(readLine()!!.trimEnd().split(" ").map{it.toInt()})
    }

    var answer = 0
    // 1 x 1 처리
    if(n == 1){
        println(2)
        return
    }

    // 나머지 케이스
    // 가로 탐색
    for(r in 0 until n){
        var count = 1
        for(c in 1 until n){
            if(array[r][c] == array[r][c-1]){
                count++
            }else{
                count = 1
            }


            if(count >= m){
                answer++
                break
            }
        }
    }

    // 가로 탐색
    for(c in 0 until n){
        var count = 1
        for(r in 1 until n){
            if(array[r][c] == array[r-1][c]){
                count++
            }else{
                count = 1
            }


            if(count >= m){
                answer++
                break
            }
        }
    }

    println(answer)
}