// Ian Coffey
// LibraryTest.java
// To Model The Functions Of A Library

// Import Libraries
import java.*;

// Initialize Book Class
class Book
{
	// Variable Declaration
	private String author, title;
	
	// Default Constructor
	public Book()
	{
		// Instanciate Instance Variables
		author = "";
		title = "";
	}
	
	// Constrcutor That Accepts Author & Title
	public Book(String inc_title, String inc_author) 
	{
		// Initialize Variables To Incoming Strings
		author = inc_author;
		title = inc_title;
	}
	
	// Instanciate Public Methods
	public String getAuthor() 
	{ 
		// Return Author Name
		return author; 
	}
	
	public String getTitle() 
	{
		// Return Title Name 
		return title; 
	}
	
	public String toString() 
	{ 
		// Return Author & Title Name
		return "This Book Is: " + title + " By " + author;
	}
	
} // End Book Class

// Initialize Patron Class
class Patron
{
	// Variable Declaration
	private Book myBook1, myBook2, myBook3;
	private String patron;
	
	// Default Constructor
	public Patron()
	{
		// Initialize Instance Variables
		myBook1 = myBook2 = myBook3 = null; 
		patron = "";
	}
	
	// Constructor That Accepts Patron Name
	public Patron(String inc_name) 
	{
		// Initialize Instance Variables
		myBook1 = myBook2 = myBook3 = new Book(); 
		patron = inc_name;
	}
	
	// Initialize Public Methods
	public String getName() 
	{
		return patron; // Return Patron Name
	}
	
	// Check Out Book
	public boolean bookBorrow(Book inc_book) 
	{
		// Check If Book 1 Isn't Null
		if (myBook1 != null) 
		{
			// Set Book To Inc_book & Return True
			myBook1 = inc_book;
			return true;
		}
		
		// Check If Book 2 Isn't Null
		if (myBook2 != null) 
		{
			// Set Book To Inc_book & Return True
			myBook2 = inc_book;
			return true;
		}
		
		// Check If Book 3 Isn't Null
		if (myBook3 != null) 
		{
			// Set Book To Inc_book & Return True
			myBook3 = inc_book;
			return true;
			
		} else {
			
			// If All Books Have Been Checked Out
			return false; 
			
		}
	}
	
	// Return Book With Given Title
	public boolean returnBook(String inc_title) 
	{
		// Check If Book1 Isn't Null
		if (myBook1 != null && (myBook1.getTitle()).equals(inc_title))
		{
			// Set Book To Null
			myBook1 = null;
			return true;
		}
		
		// Check If Book2 Isn't Null
		if (myBook2 != null && (myBook2.getTitle()).equals(inc_title))
		{
			// Set Book To Null
			myBook2 = null;
			return true;
		}
		// Check If Book3 Isn't Null
		if (myBook3 != null && (myBook3.getTitle()).equals(inc_title))
		{
			// Set Book To Null
			myBook3 = null;
			return true;
			
		} else { // If No Book Matches Title
			return false;
		}
	}
	
	// Check If Book Is Null & Return Book Title
	public boolean hasBook(String inc_title) 
	{
		// Check If Book1 Isn't Null
		if (myBook1 != null && (myBook1.getTitle()).equals(inc_title))
		{
			// Return True
			return true;
		}
		
		// Check If Book2 Isn't Null
		if (myBook2 != null && (myBook2.getTitle()).equals(inc_title))
		{
			// Return True
			return true;
		}
		
		// Check If Book3 Isn't Null
		if (myBook3 != null && (myBook3.getTitle()).equals(inc_title))
		{
			// Return True
			return true;
			
		} else { // If No Book Matches Title
			return false;
		}
	}
	
	// Return Patron Instance Variables
	public String toString() 
	{
		return "The Patron " + patron + " Has Checked Out: " + myBook1.getTitle() + ", " + myBook2.getTitle() + ", &" + myBook3.getTitle();
	}
}

// Initialize Test Class
public class LibraryTest
{
	public static void main(String [] args) 
	{
		// Patron Declaration
		Patron Ian = new Patron("Ian");
		Patron John = new Patron("John");
		Patron Smith = new Patron("Smith");
		
		// Book Declaration
		Book newBook1 = new Book("The Odyssey", "Homer");
		Book newBook2 = new Book("The Once & Future King", "T.H. White");
		Book newBook3 = new Book("The Other Wes Moore", "Wes Moore");
		
		// Have Ian Check Out The Odyssey
		Ian.bookBorrow(newBook1);
		
		// Have John Check Out The Once & Future King
		John.bookBorrow(newBook2);
		
		// Have Smith Check Out The Other Wes Moore
		Smith.bookBorrow(newBook3);
		
		// Check To See If The Odyssey Is Checked Out
		if (Ian.hasBook(newBook1.getTitle()))
		{
			// Output That Book Is Currently Checked Out
			System.out.println(Ian.getName() + " Has Checked Out " + newBook1.getTitle());
		}
		
		// Check If The Once & Future King Is Checked Out
		if (John.hasBook(newBook2.getTitle())) 
		{
			// Output That Book Is Currently Checked Out
			System.out.println(John.getName() + " Has Checked Out " + newBook2.getTitle());
		}
		
		// Check To See If The Other Wes Moore Is Checked Out
		if (Smith.hasBook(newBook3.getTitle()))
		{
			// Output That Book Is Currently Checked Out
			System.out.println(Smith.getName() + " Has Checked Out " + newBook3.getTitle());
		}
		
		// Output White Space
		System.out.println("");
		
		// Output Ian's Attributes (Including Book)
		System.out.println(Ian.toString());
		System.out.println(newBook1.toString());
		
		// Output White Space
		System.out.println("");
		
		// Output John's Attributes (Including Book)
		System.out.println(John.toString());
		System.out.println(newBook2.toString());
		
		// Output White Space
		System.out.println("");
		
		// Output Smith's Attributes (Including Book)
		System.out.println(Smith.toString());
		System.out.println(newBook3.toString());
		
		// Output White Space
		System.out.println("");
		
		// Return The Odyssey, The Once & Future King, & The Other Wes Moore
		if (Ian.returnBook("The Odyssey")) 
		{
			// Output That Book Has Been Returned
			System.out.println(Ian.getName() + " Has Returned " + newBook1.getTitle());
		}
		
		if (John.returnBook("The Once & Future King")) 
		{
			// Output That Book Has Been Returned
			System.out.println(John.getName() + " Has Returned " + newBook2.getTitle());
		}
		
		if (Smith.returnBook("The Other Wes Moore")) 
		{
			// Output That Book Has Been Returned
			System.out.println(Smith.getName() + " Has Returned " + newBook3.getTitle());
		}
	}
}