import java.util.Scanner;

public class Main {
    public static void main(String[] args){

        Scanner sc = new Scanner(System. in);

        int y = sc.nextInt();

        if(arr(y)){
            System.out.printf("true");

        }
        else{
            System.out.printf("false");

        }


    }

    public static boolean arr(int i){
        if(i % 4 == 0){

            if(i % 100 == 0 && i % 400 != 0){
                return false;

            }
            return true;

        }
        return false;


    }
}