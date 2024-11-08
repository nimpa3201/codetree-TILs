import java.util.Scanner;

public class Main {

    public static void aa(int n, int m){
        int box;
        if(n > m){
            box = n;
            n = m;
            m = box;
        }
        box = n;

        int cnt = 1;
        while(true){
            if((box % n == 0) && (box% m == 0)){
                System.out.printf("%d",box);
                break;
            }
            box++;
        }
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        


        aa(n,m);

        // 여기에 코드를 작성해주세요.
    }
}