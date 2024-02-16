import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System. in);
        int day1 = 11;
        int hour1 = 11;
        int mins1 = 11;

        int day2 = sc.nextInt();
        int hour2 = sc.nextInt();
        int mins2 = sc.nextInt();
        int c = 0;

        
        //                                1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
        int[] num_of_days = new int[]{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        while(true) {
            if(day1 == day2 && hour1 == hour2 && mins1 == mins2)
                break;
            mins1++;
            c++;

        
            if(mins1 == 60) {
                hour1++;
                mins1 = 0;

            }
            if(hour1 == 24){
                day1++;
                hour1 = 0;

            }

        }
        
        System.out.println(c);
    }
}