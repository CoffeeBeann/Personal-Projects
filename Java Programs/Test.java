// Ian Coffey
// Test.java
// To Test Code

// Import Libraries
import java.awt.event.InputEvent;
import java.awt.MouseInfo;
import java.awt.event.MouseListener;
import java.awt.PointerInfo;
import java.awt.Point;
import java.awt.Robot;
import java.util.*;

// Initialize Main Class
public class Test 
{
	public static void main(String [] args) throws Exception
	{
		// Variable & Scanner Declaration
		Robot Mouse = new Robot();
		Scanner reader = new Scanner(System.in);
		int xPos = 0;
		int yPos = 0;
		
		while (true) 
		{
			// Prompt User For Specified Coordiates
			System.out.print("\nEnter X: ");
			xPos = reader.nextInt();
			
			System.out.print("\nEnter Y: ");
			yPos = reader.nextInt();
			
			// Move Mouse To Specified Coordinates
			Mouse.mouseMove(xPos,yPos);
			
			// Clear Screen
			clear();
		}
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

