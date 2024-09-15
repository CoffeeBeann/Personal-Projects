// Ian Coffey
// TestEnviornment.java
// To Isolate Java Source Code For Development

// Import Libraries
import java.util.*;
import java.io.*;

// Establish Main Class
class TestEnviornment 
{
	public static void main(String [] args) throws Exception
	{
		
		String FILE_PATH = "C:\\Users\\iankc\\Desktop\\Work\\TotalCalls.txt";
		//PrintWriter writer = new PrintWriter(FILE_PATH);
		//writer.print("Overide");
		
		// other operations
		//writer.close();
		
		System.out.print(textReturn(FILE_PATH, 0));
		
	}
	
	public static int totalRegistry(String filePath) throws IOException 
	{
		// Establish Try-Catch Block
		try 
		{
			// FileReader, LineNumberReader, & Variable Declarations
			FileReader fileRead = new FileReader(filePath);
			LineNumberReader lineReader = new LineNumberReader(fileRead);
			int lineNums = 0;
				
			// Use While Loop To Count Line Numbers
			while (lineReader.readLine() != null) 
			{
				lineNums++;
			}
				
			// Close LineNumberReader
			lineReader.close();
				
			// Return lineNums
			return lineNums;
				
		} catch (IOException e) {
			e.printStackTrace();
		}
		// Return 0 As Default
		return 0;
	} 
	
	// Function To Return Text At A Specified Line In A File (To Be Used In Later Development)
	public static String textReturn(String filePath, int lineNum) throws Exception
	{
		// Local Variable Declarations
		String text = "";
		int maxLines = totalRegistry(filePath);
			
		// Establish Try-Catch Block
		try {
			// FileReader & BufferedReader Declarations
			FileReader readfile = new FileReader(filePath);
			BufferedReader readbuffer = new BufferedReader(readfile);
			
			// Traverse File For Specified Line
			for (int i = 0; i < maxLines; i++)
			{
				if (i == lineNum) 
				{
					text = readbuffer.readLine();
						
				} else {
					readbuffer.readLine();
				}
			}
				
		} catch (IOException e) {
			// Output Error Message
			e.printStackTrace();
		}
			
		// Return Text
		return text;
	}	
}















