public class Switchcase {
    public static void main(String[] args) {
        int days = 5;
        switch (days) {
            case 1:
                System.out.println("Sunday");
                break;
            
            case 2:
                System.out.println("Monday");
                break;
            
            case 3:
                System.out.println("Tuesday");
                break;
            
            case 4:
                System.out.println("Wednesdat");
                break;
           
            case 5:
                System.out.println("Thursday");
                break;
            
            case 6:
                System.out.println("Friday");
                break;
            
            case 7:
                System.out.println("saturday");
                break;
        
            default:
                System.out.println("Enter days of week");
                break;
        }
    }
}
