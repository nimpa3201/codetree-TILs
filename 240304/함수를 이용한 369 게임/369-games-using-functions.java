import java.util.Scanner;

public class Main{
    public static void main(String[] args){

        Scanner sc = new Scanner(System. in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = 0;

        for(int i = a; i <= b; i++){
            if(arr(i)){
                c++;

            }
        }
        System.out.printf("%d", c);


    }
    public static boolean arr(int i){
        return i % 3 == 0 || i % 10 == 3  || i % 10 == 6 || i % 10 == 9 || i / 10 == 3  || i / 10 == 6 || i / 10 == 9;

    }
}