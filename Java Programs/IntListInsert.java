// Ian Coffey
// IntListInsert.java
// To Use ArrayList To Store An Order Of User Supplied Integers

// Import Libraries
import java.util.*;

// Create Main Class
class IntListInsert 
{
	public static void main(String [] args) 
	{
		// Variable, Scanner, & ArrayList Declarations
		Scanner reader = new Scanner(System.in);
		int userNums, count = 0;
		ArrayList <Integer> nums = new ArrayList <Integer>();	
		
		// Output Small Decorative Header
		System.out.print("============================== IntListInsert ==============================\n\n");
		
		// Prompt User For # If Integers To Be Entered
		System.out.print("How Many Integers Would You Like To Enter? : ");
		userNums = reader.nextInt();
		
		// Input Values
		for (int i = 0; i < userNums; i++) 
		{		
			// Prompt User For Integer
			System.out.print("Enter Integer : ");
			
			// Read In Integer & Convert It To Wrapper Class
			Integer temp = new Integer(reader.nextInt());
			
			// Add Temp Into Nums
			nums.add(temp);
		}
		
		// Sort Values
		while (count != userNums - 1) 
		{		
			// Check If Current Element Is Larger Than Adjacent Element
			if (nums.get(count) > nums.get(count + 1)) 
			{
				// Swap Positions
				Integer temp = new Integer(nums.get(count));
				nums.set(count, nums.get(count + 1));
				nums.set(count + 1, temp);
				
				// Set Count To 0
				count  = 0;
			}
			
			// Check For Repeat Values
			else if (nums.get(count) == nums.get(count + 1)) 
			{
				// Remove Element
				nums.remove(count);
				
				// Set Count To 0
				count = 0;
			}
			
			else {
				// Increment Count
				count++;
			}
		}				
		// Output Sorted ArrayList
		System.out.print("\nYour Sorted ArrayList Is: " + nums);
	}
}