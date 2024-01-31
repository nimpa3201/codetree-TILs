import java.util.Scanner;

class arr{

    int value;
    public arr (int q) {
        this.value = q;
        
    }
}

class arr2{

    int value;
    public arr2 (int q){
        this.value = q*-1;
        
    }
}

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        for(int i = 0; i < n; i++){
            int x = sc.nextInt();

            if(x > 0){
                arr w = new arr(x);
                System.out.printf("%d ", w.value);
            }
            else {
                arr2 e = new arr2(x);
                System.out.printf("%d ", e.value);

            }
            
            
        }
        // 여기에 코드를 작성해주세요.
    }
}