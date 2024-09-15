// Ian Coffey
// Spanish Project.java
// To Test A User On Preterite Verb Knowlegde

// Import Libraries
import java.util.*;

// Establish Main Class
class Spanish_Project 
{
	public static void main(String [] args) throws Exception
	{
		// Variable & Scanner Declarations
		Scanner reader = new Scanner(System.in);
		String answer;
		String userAnswer;
		int score = 0;
		
		// Output Small Decorative Header
		System.out.print("\n\n\t============================== Preterite Test ==============================\t Score: " + score + "/7");
		
		// Question 1
		answer = "You Came";
		System.out.print("\n\n\tQuestion 1)\n\tQue es Signigica?: Viniste\n");
		System.out.print("\n\tEnter Translation: ");
		userAnswer = reader.nextLine();
		
		// Check If Answer Is Correct
		if (userAnswer.equalsIgnoreCase(answer)) 
		{
			System.out.print("\n\tCORRECT!");
			score++;
			sleep(2000);
			
		} else {
			System.out.print("\n\tIncorrect :(");
			sleep(2000);
		}
		
		// Output Small Decorative Header
		System.out.print("\n\n\tScore: " + score + "/7");
		
		// Question 2
		answer = "I Wanted";
		System.out.print("\n\n\tQuestion 2)\n\tQue es Signigica?: Yo Quise\n");
		System.out.print("\n\tEnter Translation: ");
		userAnswer = reader.nextLine();
		
		// Check If Answer Is Correct
		if (userAnswer.equalsIgnoreCase(answer)) 
		{
			System.out.print("\n\tCORRECT!");
			score++;
			sleep(2000);
		} else {
			System.out.print("\n\tIncorrect :(");
			sleep(2000);
		}
		
		// Output Small Decorative Header
		System.out.print("\n\n\tScore: " + score + "/7");
		
		// Question 3
		answer = "We Said";
		System.out.print("\n\n\tQuestion 3)\n\tQue es Signigica?: Nosotros Dijimos\n");
		System.out.print("\n\tEnter Translation: ");
		userAnswer = reader.nextLine();
		
		// Check If Answer Is Correct
		if (userAnswer.equalsIgnoreCase(answer) || userAnswer.equalsIgnoreCase("We Told")) 
		{
			System.out.print("\n\tCORRECT!");
			score++;
			sleep(2000);
		} else {
			System.out.print("\n\tIncorrect :(");
			sleep(2000);
		}
		
		// Output Small Decorative Header
		System.out.print("\n\n\tScore: " + score + "/7");
		
		// Question 4
		answer = "They Brought";
		System.out.print("\n\n\tQuestion 4)\n\tQue es Signigica?: Trajeron\n");
		System.out.print("\n\tEnter Translation: ");
		userAnswer = reader.nextLine();
		
		// Check If Answer Is Correct
		if (userAnswer.equalsIgnoreCase(answer)) 
		{
			System.out.print("\n\tCORRECT!");
			score++;
			sleep(2000);
		} else {
			System.out.print("\n\tIncorrect :(");
			sleep(2000);
		}
		
		// Output Small Decorative Header
		System.out.print("\n\n\tScore: " + score + "/7");
		
		// Question 5
		answer = "He Could Not";
		System.out.print("\n\n\tQuestion 5)\n\tQue es Signigica?: El no Pudo\n");
		System.out.print("\n\tEnter Translation: ");
		userAnswer = reader.nextLine();
		
		// Check If Answer Is Correct
		if (userAnswer.equalsIgnoreCase(answer) || userAnswer.equalsIgnoreCase("He Couldn't")) 
		{
			System.out.print("\n\tCORRECT!");
			score++;
			sleep(2000);
		} else {
			System.out.print("\n\tIncorrect :(");
			sleep(2000);
		}
		
		// Output Small Decorative Header
		System.out.print("\n\n\tScore: " + score + "/7");
		
		// Question 6
		answer = "They Had";
		System.out.print("\n\n\tQuestion 6)\n\tQue es Signigica?: Ellas Tuvieron\n");
		System.out.print("\n\tEnter Translation: ");
		userAnswer = reader.nextLine();
		
		// Check If Answer Is Correct
		if (userAnswer.equalsIgnoreCase(answer)) 
		{
			System.out.print("\n\tCORRECT!");
			score++;
			sleep(2000);
		} else {
			System.out.print("\n\tIncorrect :(");
			sleep(2000);
		}
		
		// Output Small Decorative Header
		System.out.print("\n\n\tScore: " + score + "/7");
		
		// Question 7
		answer = "I Was";
		System.out.print("\n\n\tQuestion 7)\n\tQue es Signigica?: Yo Estuve\n");
		System.out.print("\n\tEnter Translation: ");
		userAnswer = reader.nextLine();
		
		// Check If Answer Is Correct
		if (userAnswer.equalsIgnoreCase(answer)) 
		{
			System.out.print("\n\tCORRECT!");
			score++;
			sleep(2000);
		} else {
			System.out.print("\n\tIncorrect :(");
			sleep(2000);
		}

		// Output Score
		for(int i = 0; i < 100; i++)
		{
			System.out.print("\n");
		}
		
		System.out.print("\t\t\t\t\t|------------------|\n");
		System.out.print("\t\t\t\t\t|YOUR SCORE WAS " + score + "/7|\n");
		System.out.print("\t\t\t\t\t|------------------|");
		
		for(int i = 0; i < 16; i++)
		{
			System.out.print("\n");
		}
		
	}
	// Function To Pause A Program
	public static void sleep(int time) 
	{
		// Establish Try Catch Block
		try 
		{
			// Pause Program
			Thread.sleep(time);
		} catch (Exception e) { e.printStackTrace();}
		
	}
}
		
		
		
		
		
		
		