import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System. in);

        int day2 = sc.nextInt();
        int hour2 = sc.nextInt();
        int mins2 = sc.nextInt();
        
        int diff = (day2 * 24 * 60 + hour2 * 60 + mins2) - (11 * 24 * 60 + 11 * 60 + 11);

        if(diff < 0){
            System.out.printf("%d", -1);
        }
        else{
            System.out.printf("%d", diff);
        }
    }
}