import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[100];
        int[] arr2 = new int[100];
        int c = 0;
        int c2 = 0;


        for(int i = 0; i < n; i++){
            char q = sc.next().charAt(0);
            int w = sc.nextInt();

            for(int j = 1; j <= w; j++){
                if(q == 'R'){
                    
                    arr[c] = c2;
                    c2++;

                }
                else{
                    arr[c] = c2;
                    c2--;

                }
                c++;


            }
        }
        c = 0;
        c2 = 0;


        
        for(int i = 0; i < m; i++){
            char q = sc.next().charAt(0);
            int w = sc.nextInt();

            for(int j = 1; j <= w; j++){
                if(q == 'R'){
                    
                    arr2[c] = c2;
                    c2++;

                }
                else{
                    arr2[c] = c2;
                    c2--;

                }
                c++;


            }
        }
        int z = 1;

        while(true){
            if(arr[z] == arr2[z]){
                break;

            } 
            z++;

        }

        if(arr[z] == 0 && arr2[z] == 0){
            System.out.printf("%d ", -1);    
        }
        else{
            System.out.printf("%d ", z);
        }



        


        // 여기에 코드를 작성해주세요.
    }
}