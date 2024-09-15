// Ian Coffey
// Audio.java
// To Output Audio Files

// Import Libraries
import java.util.*;
import java.io.File;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;

// Establish Main Class
public class Audio 
{
	public static void main(String [] args) throws Exception
	{
		
		File sound = new File("C:\\Users\\iankc\\Desktop\\Wheel_Of_Meals\\Sound\\Sentry.wav");
		
		playAudio(sound, 20700);
		
		Thread.sleep(1000);
		
		
	}
	
	// Function To Output Audio Files
	public static void playAudio(File sound, int sleepTime) throws Exception
	{
		// Establish Try Catch Block
		try 
		{
			Clip clip = AudioSystem.getClip();
			clip.open(AudioSystem.getAudioInputStream(sound));
			clip.start();
			
			Thread.sleep((clip.getMicrosecondLength()/sleepTime) + 1);
			
			
		} catch (Exception e) 
		{
			e.printStackTrace();
		}
		
	}
}