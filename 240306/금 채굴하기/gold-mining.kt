import java.util.*

class Main{
    val dir = listOf(listOf(1, 0), listOf(-1, 0), listOf(0, 1), listOf(0, -1))

    fun solution(){
        val (n, m) = readLine()!!.trimEnd().split(" ").map{it.toInt()}

        val arr = MutableList<List<Int>>(0){List<Int>(0){0}}

        for(i in 1..n){
            arr.add(readLine()!!.trimEnd().split(" ").map{it.toInt()})
        }

        fun diamond(s : Point, k : Int) : List<Int>{
            val q : Queue<Point> = LinkedList()
            q.offer(s)
            val v = Array<BooleanArray>(n){BooleanArray(n)}
            v[s.r][s.c] = true

            var price = 0
            var count = 0

            while(q.isNotEmpty()){
                val cur = q.poll()
                if(cur.level > k){
                    continue;
                }

                if(arr[cur.r][cur.c] == 1){
                    price += m
                    count++
                }

                // 상하좌우 자기자신 포함
                for(d in dir){
                    val nr = cur.r + d[0]
                    val nc = cur.c + d[1]

                    if(nr >= 0 && nr < n && nc >= 0 && nc < n && !v[nr][nc]){
                        q.offer(Point(nr, nc, cur.level+1))
                        v[nr][nc] = true
                    }
                }
            }

            return listOf(price, count)
        }

        // 격자의 크기, 금의 가격
    
        var answer = 0
        for(r in 0 until n){
            for(c in 0 until n){
                // 일단 n/2 + 1까지만 해보자.
                for(k in 0 .. n/2+1){
                    val (price, count) = diamond(Point(r, c, 0), k)
                    
                    if(price - (2*k*k + 2*k + 1) > 0){
                        // println("($r, $c), size : $k, price : $price, count: $count")
                        answer = maxOf(answer, count)
                    }
                }
            }
        }

        println(answer)
    }
}

data class Point(val r:Int, val c:Int, val level:Int)

fun main(){
    val foo = Main()
    foo.solution()
}