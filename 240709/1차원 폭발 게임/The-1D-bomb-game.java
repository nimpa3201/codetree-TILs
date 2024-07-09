import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int N = input[0];
        int M = input[1];

        List<Integer> list = new ArrayList();
        for(int i = 0; i < N; i++){
            list.add(Integer.parseInt(br.readLine()));
        }
        while(true){
            // 전체 스캔
            ArrayList<int[]> deleteList = new ArrayList();
            // 각 숫자의 개수를 셀 값
            int cnt = 0;
            // 값이 달라졌음을 비교할 이전 값
            int prev = -1;
            for(int i = 0; i < list.size(); i++){
                // 이전 값과 다른 새로운 값이 들어오면 비교
                if(prev != list.get(i)){
                    // 이전 숫자의 개수가 M보다 크면 deleteList 넣음
                    if(cnt >= M){
                        deleteList.add(new int[]{prev, cnt, i - cnt});
                    }

                    cnt = 1;
                    prev = list.get(i);
                }else{
                    cnt++;
                }
            }
            if(cnt >= M){
                deleteList.add(new int[]{prev, cnt, list.size() - cnt});
            }

            if(deleteList.size() == 0){
                break;
            }

            // 삭제
            for(int[] delete : deleteList){
                for(int i = delete[2]; i < delete[2] + delete[1]; i++){
                    list.set(i, 0);
                }
            }

            list = list.stream().filter(e -> e != 0).collect(Collectors.toList());
        }
        System.out.println(list.size());
        list.stream().forEach(System.out::println);
    }
}