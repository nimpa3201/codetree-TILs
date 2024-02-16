import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System. in);
        int number = sc.nextInt();
        String temp = Integer.toString(number);
        int[] digits = new int[temp.length()];
        for (int i = 0; i < temp.length(); i++){
            digits[i] = temp.charAt(i) - '0';

        }


        int num = 0;

        for(int i = 0; i <digits.length; i++){
            num = num * 2 + digits[i];

        }
        System.out.printf("%d", num);

        
    }
}