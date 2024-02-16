import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        String n = sc.next();

        int c = 0;

        for(int i = 0; i < n.length(); i++){
            c = c * a + (n.charAt(i) - '0');
        }

        
        
        int[] arr = new int[20];
        int q = 0;

        while(true){
            if(c < 2){
                arr[q++] = c%b;

                break;
            }
            
            arr[q++] = c%b;
            c /= b;

        }


        for(int i = q-1; i >= 0; i--){
            System.out.printf("%d", arr[i]);
        }           
    
        


    
        
        // 여기에 코드를 작성해주세요.
    }
}