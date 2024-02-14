import java.util.Scanner;
import java.util.Arrays;

class data_1 implements Comparable<data_1> {
    String name;
    int tole;
    int gg;

    data_1(){};

    data_1(String name1, int tole1, int gg1){
        this.name = name1;
        this.tole = tole1;
        this.gg = gg1;

    }

    public int compareTo(data_1 qq){
        return this.tole - qq.tole;

    }


}


public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        data_1[] data_1s = new data_1[n];


        for(int i = 0; i < n; i++){
           String na = sc.next();
           int to = sc.nextInt();
           int ho = sc.nextInt();
           data_1s[i] = new data_1(na, to, ho);

        }
        Arrays.sort(data_1s);

        for(int i = 0; i < n; i++)
            System.out.println(data_1s[i].name + " " + data_1s[i].tole + " " + data_1s[i].gg);
        // 여기에 코드를 작성해주세요.
    }
}