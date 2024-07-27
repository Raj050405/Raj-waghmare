public class Switchcasecase {
    public static void main(String[] args) {
        int year = 2;
        String branch = "Arts";

        switch (year) {
            case 1:
                switch (branch)
                {
                    case "Arts":
                        System.out.println("English");
                        break;
                    case "Commerce":
                        System.out.println("Economics");
                        break;
                    case "Science":
                        System.out.println("Physics");
                        break;
                    default:
                        System.out.println("You entered wrong branch");
                        break;
                }
                break;
            case 2:
                switch (branch)
                {
                    case "Arts":
                        System.out.println("Hindi, Marathi");
                        break;
                    case "Commerce":
                        System.out.println("Book keeping, accounting");
                        break;
                    case "Science":
                        System.out.println("Chemistry, biology");
                        break;
                    default:
                        System.out.println("You entered wrong branch");
                        break;
                }
                break;
            case 3:
                switch (branch)
                {
                    case "Arts":
                        System.out.println("History, geopgraphy, drawing");
                        break;
                    case "Commerce":
                        System.out.println("Maths, organization, Ca");
                        break;
                    case "science":
                        System.out.println("Mathematics, Evs, IT");
                        break;
                    default:
                        System.out.println("You entered wrong branch");
                        break;
                }
                break;
        
            default:
                System.out.println("You entered worng year");
                break;
        }
    }
}