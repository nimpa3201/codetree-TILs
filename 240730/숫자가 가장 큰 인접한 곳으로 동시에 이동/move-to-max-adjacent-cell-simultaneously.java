import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");

        int N = Integer.parseInt(inputs[0]);
        int M = Integer.parseInt(inputs[1]);
        int T = Integer.parseInt(inputs[2]);

        int[][] grid = new int[N][N];

        for(int r = 0; r < N; r++){
            inputs = br.readLine().split(" ");
            for(int c = 0; c < N; c++){
                grid[r][c] = Integer.parseInt(inputs[c]);
            }
        }

        List<int[]> marbles = new ArrayList<>();

        for(int i = 0; i < M; i++){
            inputs = br.readLine().split(" ");
            int sr = Integer.parseInt(inputs[0]);
            int sc = Integer.parseInt(inputs[1]);

            marbles.add(new int[]{sr-1, sc-1});
        }
        int[][] dir = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        // t동안 구슬 이동
        for (int time = 0; time < T; time++){
            // 이동
            for(int[] arr : marbles){
                int maxValue = -1;
                int nnr = 0, nnc = 0;
                // 상하좌우 체크
                for(int[] d : dir){
                    int nr = arr[0] + d[0];
                    int nc = arr[1] + d[1];

                    if(nr >= 0 && nr < N && nc >= 0 && nc < N){
                        int value = grid[nr][nc];
                        if(value > maxValue){
                            maxValue = value;
                            // 새로운 위치
                            nnr = nr;
                            nnc = nc;
                        }
                    }
                }
                arr[0] = nnr;
                arr[1] = nnc;
            }

            // 중복 제거
            List<int[]> distinct = new ArrayList();
            OUTER : for(int i = 0; i < marbles.size(); i++){
                for(int j = 0; j < marbles.size(); j++){
                    // 자기 자신 패스
                    if(i == j) continue;

                    // 중복일 경우 패스
                    if(marbles.get(i)[0] == marbles.get(j)[0] && marbles.get(i)[1] == marbles.get(j)[1]){
                        continue OUTER;
                    }
                }
                distinct.add(marbles.get(i));
            }
            
            
            marbles = distinct;

        }
        System.out.println(marbles.size());
    }
    
}