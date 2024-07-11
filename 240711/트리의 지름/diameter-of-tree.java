import java.util.*;
import java.io.*;

public class Main {
    static int idx, max;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        
        ArrayList<int[]>[] tree = new ArrayList[N+1];

        for(int i = 1; i <= N; i++){
            tree[i] = new ArrayList();
        }

        for(int i = 0; i < N-1; i++){
            String[] inputs = br.readLine().split(" ");

            int src = Integer.parseInt(inputs[0]);
            int dst = Integer.parseInt(inputs[1]);
            int val = Integer.parseInt(inputs[2]);

            tree[src].add(new int[]{dst, val});
            tree[dst].add(new int[]{src, val});
        }

        boolean[] v = new boolean[N+1];
        v[2] = true;
        dfs(2, 0, v, tree);
        // System.out.println("new dfs!!!");
        max = 0;
        v = new boolean[N+1];
        v[idx] = true;
        dfs(idx, 0, v, tree);

        System.out.println(max);
    }

    private static void dfs(int cur, int sum, boolean[] v, ArrayList<int[]>[] tree){
        // System.out.printf("current : %d, sum : %d\n", cur, sum);
        for(int[] node : tree[cur]){
            if(!v[node[0]]){
                v[node[0]] = true;
                dfs(node[0], sum+node[1], v, tree);
                v[node[0]] = false;
            }
        }

        // 만약 다 방문했다면, 길이 비교
        if(max < sum){
            max = sum;
            idx = cur;
            // System.out.printf("new max! idx : %d, sum : %d\n", cur, max);
        }
    }
}