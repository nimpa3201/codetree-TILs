import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static int[][] map;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] inputs = br.readLine().split(" ");

        n = Integer.parseInt(inputs[0]);
        m = Integer.parseInt(inputs[1]);

        map = new int[n][n];
        for(int r = 0; r < n; r++){
            inputs = br.readLine().split(" ");
            for(int c = 0; c < n; c++){
                map[r][c] = Integer.parseInt(inputs[c]);
            }
        }
        
        // 한 점에서 금들의 상대적 위치를 기록
        int maxValue = 0;
        int maxGold = 0;
        for(int r = 0; r < n; r++){
            for(int c =0; c < n; c++){
                List<Integer> distances = getDistances(r, c);
                distances.sort(Comparator.naturalOrder());
                //System.out.println(distances);

                for(int i = 0; i < distances.size(); i++){
                    int k = distances.get(i);
                    int temp = ((i+1) * m) - (k*k + (k+1)*(k+1));

                    if(temp >= 0){
                        maxGold = Math.max(maxGold, i+1);
                    }
                }

                //System.out.printf("%d, %d : %d\n", r, c, maxGold);
            }
        }

        System.out.println(maxGold);

    }

    public static List<Integer> getDistances(int sr, int sc){
        List<Integer> arr = new ArrayList();
        for(int r = 0; r < n; r++){
            for(int c = 0; c < n; c++){
                if(map[r][c] == 1){
                    arr.add(Math.abs(r - sr) + Math.abs(c - sc));
                }
            }
        }

        return arr;
    }
}