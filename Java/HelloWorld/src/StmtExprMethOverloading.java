
public class StmtExprMethOverloading {
    public static void main(String[] args) {

        int myVar = 100;
        System.out.println("The value of myVar is : " + myVar);
        myVar++;
        System.out.println("The value of myVar is : " + myVar);
        myVar--;
        System.out.println("The value of myVar is : " + myVar);
        System.out.println("This is " +
                "another line" +
                "Still prints on a single line");

        int anotherVar = 50;
        anotherVar++;
        boolean gameOver = true;
        int score = 800;
        int levelCompleted = 5;
        int bonus = 100;
        System.out.println("Another var value is: " + anotherVar); //Java reads like this way, but we need readability to be maintained and white spaces//
        int highScore = calculateScore(gameOver, score, levelCompleted, bonus);
        System.out.println("The High Score is : " + highScore);
        score = 10000;
        levelCompleted = 8;
        bonus = 200;
        System.out.println("The new High score is :" +calculateScore(gameOver, score, levelCompleted, bonus)); //Directly print method statement

//        gameOver = true;
//        score = 800;
//        levelCompleted = 5;
//        bonus = 100;
//        if (score < 10000 && score > 1000) {
//            System.out.println("Your score was less that or equal to 10000 but greater than 1000");
//        } else if(score < 1000) {
//            System.out.println("Your score was less than 1000");
//        }
//        else {
//            System.out.println("You Got here");
//        }
//        finalScore = score;
//        if (gameOver) {
//            finalScore += (levelCompleted * bonus);
//            System.out.println("Your final score with level completed  " + levelCompleted +  finalScore);
//        }

    }
    public static int calculateScore(boolean gameOver, int score, int levelCompleted, int bonus) { // Java will create variable names in the memory for each method call
// Java does not support passing default values to method parameters
//        if (score < 10000 && score > 1000) {
//            System.out.println("Your score was less that or equal to 10000 but greater than 1000");
//        } else if(score < 1000) {
//            System.out.println("Your score was less than 1000");
//        }
//        else {
//            System.out.println("You Got here");
//        }
        int finalScore = score;
        if (gameOver) {
            finalScore += (levelCompleted * bonus);
            finalScore += 1000;
            System.out.println("Your final score with level completed  " +  finalScore);

        }
        return finalScore;

    }


}
