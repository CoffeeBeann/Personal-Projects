// Ian Coffey
// TimeTest.java
// To Convert Standard Civilian Time Into Military Time & Vice Versa

// Import Libraries
import java.util.*;

// Intitalize Sever Class
class TimeConvert
{
	// Instance Variable Declaration
	private int hour, minute;
	private String meridiem;
	 
	// Default Constructor
	public TimeConvert()
    {
		// Initialize All Variables To 0
		hour = 0;
		minute = 0;
		meridiem = "";
	}
	 
	// Constructor That Accept Hour & Meridiem Parameters
	public TimeConvert(int inc_hour, String inc_meridiem)
	{
	    // Initialize Variables To Incoming Parameters
		hour = inc_hour;
		meridiem = inc_meridiem;
		minute = 0;
	}
	 
	// Constructor That Accepts Minute, Hour, & Meridiem Parameters
	public TimeConvert(int inc_minute, int inc_hour, String inc_meridiem)
	{
		// Initialize Variables To Incoming Parameters
	    minute = inc_minute;
		hour = inc_hour;
		meridiem = inc_meridiem;
	}
	 
	// Copy Concstructor
	public TimeConvert(TimeConvert inc_object)
	{
	    // Copy Incoming Time Object Into timeCopy
		TimeConvert timeCopy = new TimeConvert(inc_object);
	}
	 
	// Public Method That Validates Incoming Values
	void setTime(int inc_minute, int inc_hour, String inc_string)
	{
		// Validate Minute Time
		setMinute(inc_minute);
		  
		// Validate Hour Time
		setHour(inc_hour);
		  
		// Validate Meridiem
		setMeridiem(inc_string);
	}
	 
	// Public Method That Validates Minute Value
	void setMinute(int inc_minute)
	{
		// Validate Minute Time
		if (inc_minute < 0 || inc_minute > 60)
		{
			minute = 0; // Set Minute To 0
	   
		} else {
	   		minute = inc_minute; // Set Minute To Inc_Minute
	   
		}
	}
	 
	 // Public Method That Validates Hour Value
	 void setHour(int inc_hour)
	 {
		 // Validate Hour Time
		 if (inc_hour < 0 || inc_hour > 24)
	 	 {
	 		hour = 0; // Set Hour To 0
	   
		 } else {
	   
	         hour = inc_hour; // Set Hour To Inc_Hour
	     }
	 }
	 
	 // Public Method That Validates Meridiem Values
	 void setMeridiem(String inc_meridiem)
	 {
		 // Check If Hour Is Universal
		 if (hour > 12)
		 {
			 // Set Meridiem To Universal Time
			 inc_meridiem = "U"; 
		 } 
		 	
		 // Check If Meridiem Is Invalid
		 if (hour < 0 || hour > 24) 
		 {
		 	// Set Meridiem To Error
		 	inc_meridiem = "E";
		 }		
	 }
	 
	 // Method That Returns Minute Value
	 int getMinute()
	 {
	 	return minute; // Return Minute
	 }
	 
	 // Method That Returns Hour Value
	 int getHour()
	 {
	 	return hour; // Return Hour
	 }
	 
	 // Method That Returns Meridiem Value
	 String getMeridiem()
	 {
	 	return meridiem; // Return Meridiem
	 }
	 
	 // Public Method That Outputs Universal Time
	 public String toUniversalString()
	 {	 		
		// Check If It Is Midnight
		if (hour == 12 && meridiem.equalsIgnoreCase("AM")) 
		{					
			// Return Hour As 00 
			return "00:" + minute + " U\n";
		} 
		
		// Check If Meridiem Is AM (Morning)
		if (meridiem.equalsIgnoreCase("AM")) 
		{
			// For Loop To Check Time 1:00am - 9:00am
			for (int i = 1; i <= 9; i++) 
			{
				// Check If Hour Value Equals Index
				if (hour == i) 
				{
					// Check If Minute Needs A Leading 0
					if (minute < 10) 
					{
						// Return Universal Time With Leading 0
						return "0" + i + ":0" + minute + " U\n";
						
					} else {
						
						// Return Universal Time
						return "0" + i + ":" + minute + " U\n";
					}
				}
			}
		}
		
		// Check If Meridiem Is PM (Morning)
		if (meridiem.equalsIgnoreCase("PM")) 
		{
			// For Loop To Check Time 1:00pm - 9:00pm
			for (int i = 1; i <= 9; i++) 
			{
				// Check If Hour Value Equals Index
				if (hour == i) 
				{
					// Check If Minute Needs A Leading 0
					if (minute < 10) 
					{
						// Return Universal Time With Leading 0
						return (i + 12) + ":0" + minute + " U\n";
						
					} else {
						
						// Return Universal Time
						return (i + 12) + ":" + minute + " U\n";
						
					}
				}
			}
		}
		
		// Check If Minute Needs A Leading 0
		if (minute < 10) 
		{
			// Check If Hour Needs A Leading 0
			if (hour < 10) 
			{
				// Return Time As Is With 'U' For Universal & A Leading 0
				return "0" + hour + ":0" + minute + " U\n";
			}
			
		} else {
			
			// Check If Hour Needs A Leading 0
			if (hour < 10) 
			{
				// Return Time As Is With 'U' For Universal & A Leading 0
				return "0" + hour + ":" + minute + " U\n";
			}
		}
		
		// Return Time As Is With 'U' For Universal 
		return hour + ":" + minute + " U\n";
			
	 }
		
	 // Public Method That Outputs Standard Time
	 public String toStandardString() 
	 {	 	
	 	// Declare Local Variable To Avoid Changing Hour Value
	 	int tempHour;
	 	
	 	// Check If Hour Is Either 0 or 24
	 	if (hour == 0 || hour == 24) 
	 	{
	 		// Check If Minute Needs A Leading 0
			if (minute < 10) 
			{
	 			// Return Standard Hour As 12 With A Leading 0
	 			return 12 + ":0" + minute + "\n";
	 			
			} else {
				
				// Return Standard Hour As 12
	 			return 12 + ":" + minute + "\n";
			}
	 	}
	 	
	 	// Check If It Is The Afternoon & Evening (13:00 - 23:00)
	 	if (hour >= 13 || hour <= 23) 
	 	{
	 		// Set Temp Hour To Hour Value
	 		tempHour = hour;
	 		
	 		// Subtract 12 From Temp Hour
	 		tempHour -= 12;
	 		
	 		// Return Standard Time
	 		return tempHour + ":" + minute + "\n";
	 	}
	 	
	 	// Return Time As Is With No 'U'
	 	return hour + ":" + minute;
	 }
}

public class TimeTest
{
	public static void main(String [] args)
	{
		// Variable, Scanner, & Object Declaration
		Scanner reader = new Scanner(System.in);
		int userNum = 0, minute = 0, hour = 0;
		String meridiem = "";
		TimeConvert time1 = null;
		
		// Output Small Decorative Header
		Sop("");
		Sop("============================== Time Convert ==============================\n");
		
		// Output Menu Of Options
		Sop("1) Constuct Default Time Object\n");
		Sop("2) Construct Object With Hour & Meridiem Parameters\n");
		Sop("3) Construct Object With Minute, Hour, & Meridiem Parameters\n");
		Sop("4) Copy Time Object\n");
		Sop("\n");
		
		// Prompt User For Option
		Sop("Enter Option: ");
		userNum = reader.nextInt();
		
		// Determine Choice Entered
		if (userNum == 1)
		{
			// Construct Default Time Object
			time1 = new TimeConvert();
		}
			
		if (userNum == 2) 
		{
			// Prompt User For Hour Parameter
			Sop("\n");
			Sop("Enter In Hour: ");
					
			// Read In User Input
			hour = reader.nextInt();
					
			// Flush Input Stream
			reader.nextLine();
					
			// Prompt User For Meridiem Parameters
			Sop("Enter In Meridiem: ");
					
			// Read In User Input
			meridiem = reader.nextLine();
					
			// Construct Time Object With Hour & Meridiem Parameters
			time1 = new TimeConvert(hour, meridiem);
		}		
		
		if (userNum == 3) 
		{
			// Prompt User For Minute Parameter
			Sop("\n");
			Sop("Enter In Minute: ");
					
			// Read In User Input
			minute = reader.nextInt();
					
			// Prompt User For Hour Parameter
			Sop("Enter In Hour: ");
					
			// Read In User Input
			hour = reader.nextInt();
					
			// Flush Input Stream
			reader.nextLine();
					
			// Prompt User For Meridiem Parameters
			Sop("Enter In Meridiem: ");
					
			// Read In User Input
			meridiem = reader.nextLine();
					
			 // Construct Time Object With Minute, Hour, & Meridiem Parameters
			time1 = new TimeConvert(minute, hour, meridiem);
		}	
				
		if (userNum == 4) 
		{
			// Construct A Copy Of Time Object
		 	TimeConvert copyTime = new TimeConvert(time1);
		}
		
		// Validate New Time Object Creates
		time1.setTime(minute, hour, meridiem);
		
		// Output Small Decorative Header
		Sop("============================== Time Convert ==============================\n");
			
		// Output Menu Of New Options
		Sop("1) Get Minute\n");
		Sop("2) Get Hour\n");
		Sop("3) Get Meridiem\n");
		Sop("4) Convert Standard To Universal\n");
		Sop("5) Convert Universal To Standard\n");
		Sop("6) Quit\n");
		Sop("\n");
		
		while (userNum != 6)
		{
			// Prompt User For Option
			Sop("Enter Option: ");
			userNum = reader.nextInt();
			
			if (userNum == 1 )
			{
				// Output Minute Value
				Sop("The Minute Value At This Moment Is: " + time1.getMinute() + "\n");
			}	
				
			if (userNum == 2) 
			{
				// Output Hour Value
				Sop("The Hour Value At This Moment Is: " + time1.getHour() + "\n");		
			}
			
			if (userNum == 3) 
			{
				// Output Meridiem Value
				Sop("The Meridiem At This Moment Is: " + time1.getMeridiem() + "\n");	
			}		
			 
			if (userNum == 4) 
			{
				// Output Universal Time
				Sop("The Current Universal Time Is " + time1.toUniversalString());
			}		
			 
			if (userNum == 5) 
			{
				// Output Standard Time
				Sop("The Current Standard Time Is " + time1.toStandardString());
			}	
		}	 		
	}
	
	// Method That Prints Input Onto Console
	public static void Sop(String inc_string) 
	{
		// Output Inc_String To Console
		System.out.print(inc_string);	
	}
}