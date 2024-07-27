import java.util.Scanner;

public class Largestno {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int x, y, z;
        x=sc.nextInt();
        y=sc.nextInt();
        z=sc.nextInt();
        if (x>y) {
            System.out.println(x);
        }
        else if(y>z){
            System.out.println(y);
        }
        else{
            System.out.println(z);
        }
    }
}
