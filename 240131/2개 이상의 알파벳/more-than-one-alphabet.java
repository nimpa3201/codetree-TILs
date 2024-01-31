import java.util.Scanner;

public class Main {

    public static boolean arr(String a){
        for(int i = 0; i < a.length()-1; i++){
            if(a.charAt(i) == a.charAt(i + 1)){

            }
            else{
                return true;

            }
        }
        return false;

    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        String n = sc.next();


        if(arr(n)){
            System.out.printf("Yes");

        }
        else{
            System.out.printf("No");
        }
     
    }
   
}