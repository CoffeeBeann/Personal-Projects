// Ian Coffey
// Mouse.java
// To Simulate Mouse Movement To Automate Tasks

// Import Libraries 
import java.awt.event.InputEvent;
import java.awt.MouseInfo;
import java.awt.event.MouseListener;
import java.awt.event.*;
import java.awt.PointerInfo;
import java.awt.Point;
import java.awt.Robot;
import java.util.*;

class Mouse
{
   
    public static void main(String[] args) throws Exception 
    {
		// Varaible & Object Declarations
		Scanner reader = new Scanner(System.in);
		Robot Mouse = new Robot();
		Random random = new Random();
		int mask = InputEvent.BUTTON1_DOWN_MASK;
		int user = 0;
		
		// Pause Program Until User Input 
		System.out.println(": Press Enter For Clicks");
		user = reader.nextInt();
		
		// Time Setup
		Thread.sleep(2000);
		
		// Infinite Loop To Move Mouse 
        while (true) 
        {
			// Simulate Click         
			Mouse.mousePress(mask);
			Thread.sleep(5);
			Mouse.mouseRelease(mask);
			Thread.sleep(5);
				
			/* Get Coordinates
			PointerInfo info = MouseInfo.getPointerInfo();
			Point a = info.getLocation();
			xPos = (int) a.getX();
			yPos = (int) a.getY();
				
			// Determine If Coordinates Need To Be Displayed 
			if (xTemp != xPos || yTemp != yPos) 
			{
				// Display Coordinates
				System.out.println("X: " + xPos + " Y: " + yPos);					
			} 
			
			// Set New xTemp & yTemp Coordinates 
			xTemp = xPos;
			yTemp = yPos;
			}*/
			
		}
    }
}