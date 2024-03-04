import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int a = sc.nextInt();

        char o = sc.next().charAt(0);

        int c = sc.nextInt();

        if(arr(a,c,o)== -1){
            System.out.printf("False");

        }
        else{ 
            System.out.printf("%d %c %d = %d", a, o, c, arr(a,c,o));
        }
        
        // 여기에 코드를 작성해주세요.
    }

    public static int arr(int a, int c, char o){

        if(o == '+'){
            return a + c;

        }
        else if(o == '-'){
            return a - c;

        }
        else if(o == '/'){
            return a / c;

        }
        else if(o == '*'){
            return a * c;

        }
        return -1;

    
    }

}