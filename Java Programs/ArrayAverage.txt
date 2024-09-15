// Ian Coffey
// ArrayAverage.java
// To Calculate The Average Values Of An Array.

// Import Libraries
import java.util.*;

// Initialize Main Class
public class ArrayAverage 
{
	public static void main(String [] args) 
	{
		// Variable, Scanner, & Array Declaration
		double average;
		double [] nums = new double[10];
		Scanner reader = new Scanner(System.in);
		
		// Output Small Decorative Header
		System.out.println("============================== Array Average ==============================");
		System.out.println("");
		
		// Prompt User For 10 Real Numbers
		for (int i  = 0; i < 10; i++)
		{
			// Prompt User For Digit
			System.out.print((i + 1) + ") Enter Digit: ");
			
			// Record Value Into Array
			nums[i] = reader.nextDouble();
		}
		
		// Calculate Average
		average = getAverage(nums);
		
		// Output Average 
		System.out.println("");
		System.out.println("The Average Value Of This Array Is: " + average);
		
		// Output Elements Greater Than Average
		System.out.print("The Elements Greater Than " + average + " In This Array Include:");
		
		for (double currentNum : nums) 
		{
			if (currentNum > average) 
			{
				System.out.print(" " + currentNum + " ");
			}
		}
	}
	
	// Method To Calculate Avergae Of Array
	public static double getAverage(double [] inc_array) 
	{
		// Local Variable Declaration
		double sum = 0;
		
		// Use A For-Each To Calculate Average
		for (double currentNum : inc_array) 
		{
			sum += currentNum;
		}
		
		// Divide Sum By 10 To Calculate Average
		sum /= 10;
		
		// Return Average
		return sum;
	}
}