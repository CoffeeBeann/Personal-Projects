// Ian Coffey
// HouseDrawTest.java
// To Draw A House Using User Inputed Values

// Import Libraries
import java.util.*;
import TurtleGraphics.*;

// Initialize Server Class
class HouseDraw 
{
	// Intialize Instance Variables
	private int xPosition, yPosition, myPen;
	private String houseSize;
	
	// Default Constructor (No Args Given)
	public HouseDraw() 
	{
		// Intialize X & Y Coordinates To Bottom Left Of Window
		xPosition = yPosition = -150;
		
		// Initialize House Size To "Small"
		houseSize = "Small";
		
		// Instanciate Pen Object
		Pen myPen = new StandardPen();	
	}
	
	// Copy Constructor To Accept House Size
	public HouseDraw(String inc_string) 
	{
		// Intialize X & Y Coordinates To Bottom Left Of Window
		xPosition = yPosition = -150;
		
		// Set House Size To Incoming String
		houseSize = inc_string;	
			
		// Instanciate Pen Object
		Pen myPen = new StandardPen();
	}
	
	// Copy Constructor To Accept X & Y Coordinates
	public HouseDraw(int inc_x, int inc_y) 
	{
		// Intialize X & Y Coordinates To Incoming Values
		xPosition = inc_x;
		yPosition = inc_y;
		
		// Set House Size To Small
		houseSize = "Small";
		
		// Instanciate Pen Object
		Pen myPen = new StandardPen();	
	}
	
	// Copy Constructor To Accept House Object
	public HouseDraw(HouseDraw inc_object) 
	{
		// Set New House Object Equal To Incoming Object
		HouseDraw newHouse = inc_object; 
			
		// Instanciate Pen Object
		Pen myPen = new StandardPen();
	}
	
	// Initialize Private Methods
	private void drawPerimeter(int inc_side) 
	{
	
	}
	
	private void drawRoof(int inc_side) 
	{
		
	}
	
	// Initialize Public Methods
	void setxPosition(int inc_x) // Set X Position To Incoming Value
	{
		xPosition = inc_x;
	}
	void setyPosition(int inc_y) // Set Y Position To Incoming Value
	{
		yPosition = inc_y;
	}
	void setHouseSize(String inc_string) // Validate House Size & Set House Size To Incoming String
	{
		// Check If Incoming String Has A Valid Size
		if (inc_string.equals("Small") || inc_string.equals("small") || inc_string.equals("Medium") || inc_string.equals("medium") || inc_string.equals("Large") || inc_string.equals("Large")) 
		{
			houseSize = inc_string; // Set House Size Equal To Incoming String
		} else {
			houseSize = "Small"; // Set House Size Equal To "Small" As Default
		}
	}
	int getxPosition() // Return X Position
	{
		return xPosition;
	}
	int getyPosition() // Return X Position
	{
		return yPosition;
	}
	String getSize() // Return House Size
	{
		return houseSize;
	}
	void draw() // Draw House Using Inputed Values 
	{
	}
}

// Initialize Client Class 
public class HouseDrawTest 
{
	public static void main(String [] args) 
	{
		// Variable & Scanner Declaration
		Scanner reader = new Scanner(System.in);
		int i = 1;
		String userInput = "";
		
		// Output Small Decorative Header
		System.out.println("============================== House Draw ==============================");
		
		// Output White Space
		System.out.println(""); 
			
		// Instanciate For Loop To Output Graphics Windows
		for (i = 1; i <= 4; i++) 
		{
			// Prompt User For House Size
			System.out.print("Enter In Size Of House(Small, Medium, Large): ");
			userInput = reader.nextLine();
			
			// Instanciate New House Object
			HouseDraw newHouse = new HouseDraw(userInput);
			
			// Validate House Size
			newHouse.setHouseSize(userInput);		
					
			// If User Input Is "Small"
			if (userInput.equals("Small") || userInput.equals("small")) 
			{
				
			}
			// If User Input Is "Medium"
			if (userInput.equals("Medium") || userInput.equals("medium")) 
			{
				
			}
			// If User Input Is "Large"
			if (userInput.equals("Large") || userInput.equals("large")) 
			{
				
			}
		}
	}
}