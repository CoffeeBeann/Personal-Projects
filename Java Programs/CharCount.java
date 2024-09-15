// Ian Coffey
// CharCount.java
// To Use Two Parallel Arrays To Store The # of Occurrences For Each Character In A User-Supplied String.

// Import Libraries
import java.util.*;

// Create Main Class
class CharCount 
{
	public static void main(String [] args) 
	{
		// Variable, Scanner, & ArrayList Declaration
		Scanner reader = new Scanner(System.in);
		String userInput = "";
		ArrayList <Character> characters = new ArrayList <Character>();
		ArrayList <Integer> frequency = new ArrayList <Integer>();
		
		// Output Small Decorative Header
		System.out.print("============================== CharCount ==============================\n\n");
		
		// Prompt User For Sentence 
		System.out.print("Enter String: ");
		userInput = reader.nextLine();
		
		// Transfer Characters To ArrayList Using toCharArray
		for (char i : userInput.toCharArray()) 
		{
			characters.add(i);
		}
		
		// Determine The Frequency Of The Letters In Characters
		for (int i = 0; i < characters.size(); i++)
		{
			// Create & Set FrequencyChar At 1 To Have A Minimum Frequency
			Integer frequencyChar = new Integer(1);
			
			for (int j = i + 1; j < characters.size(); j++) 
			{
				// Check If Elements Of I & J Are The Same
				if (characters.get(i) == characters.get(j)) 
				{
					// Increment Frequecny
					frequencyChar++;
					
					// Avoid Repeat Characters By Removing Current Char
					characters.remove(j);
				}
			}
			// Add Frequency Of Letter Into ArrayList
			frequency.add(frequencyChar);
		}
		
		// Output ArrayLists
		System.out.println("Character     Frequency");
		
		for(int i = 0; i < frequency.size(); i++) 
		{  
		   // Check For Spaces
		   if (characters.get(i) == ' ') 
		   {
		       System.out.print("\tSpace" + "\t\t" + frequency.get(i));
		   }
		   else {
		   
               System.out.println("\t" + characters.get(i) + "\t\t\t" + frequency.get(i));
		   }
        }  		
	}
}