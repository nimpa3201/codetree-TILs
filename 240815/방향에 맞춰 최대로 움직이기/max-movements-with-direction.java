import java.util.*;
import java.io.*;

public class Main {
    static int[][] dir = {{-1, 0}, {-1 ,1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}};
    static int N;
    static Node[][] map;
    static int ans = 0;
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new Node[N][N];
        // 값 입력
        for(int r = 0; r < N; r++){
            String[] inputs = br.readLine().split(" ");
            for(int c = 0; c < N; c++){
                map[r][c] = new Node(Integer.parseInt(inputs[c]));
            }
        }

        // 방향 입력
        for(int r = 0; r < N; r++){
            String[] inputs = br.readLine().split(" ");
            for(int c = 0; c < N; c++){
                map[r][c].d = Integer.parseInt(inputs[c]) - 1;
            }
        }

        String[] inputs = br.readLine().split(" ");
        int sr = Integer.parseInt(inputs[0]) - 1;
        int sc = Integer.parseInt(inputs[1]) - 1;

        backtracking(sr, sc, 0);

        System.out.println(ans);
    }

    public static void backtracking(int cr, int cc, int cnt){
        // 반복
        List<int[]> candidates = new ArrayList<>();
        int val = map[cr][cc].val;
        int d = map[cr][cc].d;

        int nr = cr;
        int nc = cc;

        while(true) {
            nr += dir[d][0];
            nc += dir[d][1];

            if(nr >= 0 && nr < N && nc >= 0 && nc < N) {
                if(val < map[nr][nc].val) {
                    candidates.add(new int[]{nr, nc});
                }
            } else {
                break;
            }
        }

        for(int[] arr : candidates){
            backtracking(arr[0], arr[1], cnt + 1);
        }

        // 종료 조건
        if(candidates.size() == 0){
            ans = Math.max(ans, cnt);
        }
    }

    public static class Node{
        public int val, d;

        public Node(int val){
            this.val = val;
            d = 0;
        }
    }
}