// Ian Coffey
// JavaKeyBindings.java
// To Test Key Bindings In java Soure CodeSetCache

// Import Libraries
import java.util.*;
import java.io.*;
import javax.swing.*;
import java.awt.FlowLayout;
import java.awt.event.KeyEvent;

// Establish Main Class
public class JavaKeyBindings 
{
	public static void main(String [] args) 
	{
		// Frame Declarations
		JFrame frame = new JFrame();
		JPanel panel = new JPanel(new FlowLayout());
		JTextField field = new JTextField(10);
		
		// Add Key Listener
		field.addKeyListener(new Listener());
		
		// Add Text Box To Canvas
		panel.add(field);
		frame.getContentPane().add(panel);
		
		// Set Frame Size 
		frame.setSize(500,500);
		
		// Make Canvas Visible
		frame.setVisible(true);
		
	}
}

class Listener implements KeyListener 
{
	public void keyTyped(KeyEvent letter)
	{
		System.out.println("Key Typed: " + letter.getKeyChar());
	}
	
	public void keyPressed(KeyEvent letter)
	{
		System.out.println("Key Pressed: " + letter.getKeyChar());
	}
	
	public void keyReleased(KeyEvent letter)
	{
		System.out.println("Key Released: " + letter.getKeyChar());
	}
}