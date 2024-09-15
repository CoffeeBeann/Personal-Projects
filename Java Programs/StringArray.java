// Ian Coffey
// StringArray.java
// To Read In An Array Of Strings, Determine Longest, Shortest, & Alphabetically First String.

// Import Libraries
import java.util.*;

// Initialize Main Class
public class StringArray
{
	public static void main(String [] args)   
	{
		// Variable, Scanner, & Array Declaration
		int userInput_Nums;
		String [] stringArray;
		String maxLength = "", alphaFirst = "z", minLength = "          ";
		Scanner reader = new Scanner(System.in);
		  
		// Output Small Decorative Header
		System.out.println("============================== String Array ==============================");
		System.out.println("");
		  
		// Prompt User For Number Of Strings They Would Like To Enter
		System.out.print("How Many Strings Would You Like To Enter: ");
		userInput_Nums = reader.nextInt();
		  
		// Create An Array With User's Size
		stringArray = new String[userInput_Nums];
		  
		// Flush Input Stream
		reader.nextLine();
		  
		// Prompt User For Strings Using For Loop
		for (int i = 0; i < stringArray.length; i++)
		{
			// Prompt User For String
			System.out.print((i + 1)+ ") Enter String: ");
			
			// Read In User's Input Into A String
			String newString = new String(reader.nextLine());
			   
			// Save Input Into String Variable
			stringArray[i] = newString;
		}
		
		// Determine Longest & Shortests String
		for (int i = 0; i < stringArray.length; i++)
		{	
			// Determine Longest String
			if (maxLength.length() < stringArray[i].length()) 
			{
				maxLength = stringArray[i];
			}
			
			// Determine Shortest String
			if (minLength.length() > stringArray[i].length()) 
			{
				minLength = stringArray[i];
			}
		
			// Determine Alphabetically First String
			if (alphaFirst.compareTo(stringArray[i]) > 0) 
			{
				alphaFirst = stringArray[i];
			}
		}
		
		// Output Longest, Shortest, & Alphabetically First String
		System.out.println("");
		System.out.println("The Shortest String Entered Was: " + minLength);
		System.out.println("The Longest String Entered Was: " + maxLength);
		System.out.println("The String That Was Alphabetically First Was: " + alphaFirst);
	}
}