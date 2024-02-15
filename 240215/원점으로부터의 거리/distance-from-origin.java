import java.util.Scanner;
import java.util.Arrays;

class data implements Comparable<data> {
    
    int x;
    int y;
    int number;


    data(){}

    data(int x, int y, int number){
        this.x = x;
        this.y = y;
        this.number = number;
    }

    public int compareTo(data datas){
        return (this.x + this.y) - (datas.x + datas.y) ;
    } 
    
}
public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        data[] datas = new data[n];

        for(int i = 0; i < n; i++){

            int x = sc.nextInt();
        
            int y = sc.nextInt();
            int number = i+1;

            if(x < 0){
                x *= -1;

            }
            if(y < 0){
                y *= -1;
                
            }

            datas[i] = new data(x, y, number);
        }

        Arrays.sort(datas);

        for(int i = 0; i < n; i++){
            System.out.printf("%d\n", datas[i].number);

        }

        

        
        // 여기에 코드를 작성해주세요.
    }
}