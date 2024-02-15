import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System. in);


        int[] arr = new int[]{0,31,28,31,30,31,30,31,31,30,31,30,31};

        int m1 = sc.nextInt();
        int d1 = sc.nextInt();

        int m2 = sc.nextInt();
        int d2 = sc.nextInt();
        int c = 1;

        while(true){
            if(m1 == m2 && d1 == d2){
                break;

            }
            c++;
            d1++;

            if(d1 > arr[m1]){
                m1++;
                d1 = 1;

            }
        }
        
        
        System.out.printf("%d",c);




        // 여기에 코드를 작성해주세요.
    }
}