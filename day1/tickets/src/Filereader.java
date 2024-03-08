import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files


public class Filereader {
    public String[] contents = new String[5047];
  // public static void main(String[] args) {
  //   new Filereader();
  // }

  public Filereader() {
    int x = 0;
    try {
      File myObj = new File("why/ok.txt");
      Scanner myReader = new Scanner(myObj);
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        contents[x] = data;

        // System.out.println(data);
        x++;
      }
      myReader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }


    
  }

  public String[] getContents() {
    return this.contents;
  }
}

