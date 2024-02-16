public class Main {
    public static void main(String[] args) {
        int month = 2, day = 5;
        int elapsedDays = 0;

        //                                1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
        int[] num_of_days = new int[]{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        while(true) {
            if(month == 4 && day == 1)
                break;
        
            elapsedDays++;
            day++;
        
            if(day > num_of_days[month]) {
                month++;
                day = 1;
            }
        }
        
        System.out.print(elapsedDays);
    }
}