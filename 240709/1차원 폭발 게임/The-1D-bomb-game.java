import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int N = input[0];
        int M = input[1];

        LinkedList<Integer> list = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            list.add(Integer.parseInt(br.readLine()));
        }

        boolean changesMade = true;
        while (changesMade) {
            changesMade = false;
            int cnt = 1;
            Iterator<Integer> it = list.iterator();
            int prev = it.next();
            ListIterator<Integer> delStart = list.listIterator();

            while (it.hasNext()) {
                int current = it.next();
                if (current == prev) {
                    cnt++;
                } else {
                    if (cnt >= M) {
                        changesMade = true;
                        for (int i = 0; i < cnt; i++) {
                            delStart.next();
                            delStart.remove();
                        }
                    } else {
                        for (int i = 0; i < cnt; i++) {
                            delStart.next();
                        }
                    }
                    cnt = 1;
                    prev = current;
                }
            }

            if (cnt >= M) {
                changesMade = true;
                for (int i = 0; i < cnt; i++) {
                    delStart.next();
                    delStart.remove();
                }
            }
        }

        System.out.println(list.size());
        list.forEach(System.out::println);
    }
}