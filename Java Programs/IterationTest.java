// Ian Coffey
// IterationText.java
// To Text Java Source Logic

// Import Libraries
import java.util.*;
import java.io.*;

// Establish Main Class
class IterationTest 
{
	public static void main(String [] args) throws Exception
	{
		// Variable Declarations
		Scanner reader = new Scanner(System.in);
		int iterations;
		float seconds;
		
		// Output Small Decorative Header
		System.out.println("\n\n\n\t\t    ============================== Logic Test ==============================\n\n");
		
		// Prompt User For Input
		System.out.print("\n\t\t\t\t\t\tEnter Iterations: ");
		iterations = reader.nextInt();
		
		clear();
		
		// Output Small Decorative Header
		System.out.println("\n\n\n\t\t    ============================== Logic Test ==============================\n\n");
		
		// Prompt User For Input
		System.out.print("\n\t\t\t\t\t\tEnter Seconds: ");
		seconds = reader.nextFloat();
		
		
	}
	
	// Function To Clear Screen
	public static void clear() throws Exception
	{
		// Estbalish Try-Catch Block
		try 
		{
			// Clear Screen
			new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
			
		} catch (Exception ie) { 
			ie.printStackTrace(); 
		}
	}
}