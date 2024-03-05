import java.util.Scanner;

class arr{
    int value;

    public arr(int value){
        this.value = value;

    }
}

public class Main{

    public static void arr2(arr a, arr b) {
        int temp;
        temp = a.value;
        a.value = b.value;
        b.value = temp;

    }
    public static void main(String[] args){

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();
        int m = sc.nextInt();


        arr a = new arr(n);
        arr b = new arr(m);

        arr2(a, b);

        System.out.printf("%d %d", a.value, b.value);




    } 
}