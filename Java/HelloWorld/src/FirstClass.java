public class FirstClass {
    public static void main(String[] args) {
        System.out.println("Hello, Sadashiv!");
        boolean isKc = true;
        if (isKc == true) {
            System.out.println("Yes Kc");
        } else {
            System.out.println("No Kc");
        }
        String firstName = "Sadashiv";
        int pinCode = 586125;
        if (firstName == "Sadashiv" && pinCode == 586125){
            System.out.println("Your native is Babalad");
        }
        if (pinCode == 1235 || firstName == "Sadashiv");
            System.out.println("Either of one condition is true");
            System.out.println("End of the program"); //Since no code block it's get executed

        if (pinCode == 1235 || firstName == "Sadashiv"){
            System.out.println("Either of one condition is true");
            System.out.println("End of the program");
        }
        int newValue = 50;
        if (newValue == 50) {
            System.out.println("New value is greater than 25");
        }
        boolean isCar = false;
        if (!isCar) { //(isCar == true)
            System.out.println("This is not supposed to be printed");
        }
        //Ternary Operator
        //operand1 ? operand2 : operand3
        String MakeOfCar = "Tata";
        boolean isDomestic = MakeOfCar == "Tata" ? true: false;
        if (isDomestic) {
            System.out.println("The car is domestic");
        } else {
            System.out.println("The car is imported");
        }
        double val1 = 20.00d;
        double val2 = 80.00d;
        double sumTotal = ((val1 + val2) * 100.00d);
        System.out.println("MyValuesTotal = " + sumTotal);
        double theReminder = sumTotal % 40.00d;
        boolean isReminder = (theReminder == 0) ? true : false;
        if (!isReminder){
            System.out.println("Got some Reminder");

        }
        else {
            System.out.println("Got no Reminder");
        }



    }
}
