import java.util.Scanner;

class IntWrapper {
    int value;

    public IntWrapper(int value) {
        this.value = value;
    }
}

public class Main {    
    // 문제에서 설명한 대로 a와 b를 변경합니다.
    // call by reference를 구현합니다.
    public static void changeNumber(IntWrapper a, IntWrapper b) {
        if(a.value > b.value) {
            b.value += 10;
            a.value *= 2;
        }
        else {
            a.value += 10;
            b.value *= 2;
        }
    
        return;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 변수 선언 및 입력:
        int a = sc.nextInt();
        int b = sc.nextInt();

        IntWrapper aWrapper = new IntWrapper(a);
        IntWrapper bWrapper = new IntWrapper(b);

        changeNumber(aWrapper, bWrapper);

        a = aWrapper.value;
        b = bWrapper.value;

        System.out.print(a + " " + b);
    }
}