import java.util.Scanner;

public class Main{
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);


        String a = sc.next();
        
        if(arr(a)){
            System.out.printf("Yes");

        }
        else{
            System.out.printf("No");

        }

    }

    public static boolean arr(String a){
        int c = a.length();

        for(int i = 0; i < c; i++){

            if(a.charAt(i) != a.charAt((c-1)-i)) {
                return false;

            } 
            
             
        }
        return true;




    }


}