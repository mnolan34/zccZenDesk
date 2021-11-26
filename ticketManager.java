import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.Base64;
//import java.util.Scanner;
//import org.json.simple.JSONArray;
//import org.json.simple.JSONObject;
//import org.json.simple.parser.JSONParser;


public class ticketManager {
	
	//tracks page to display of the 
	int currentPage;
	
	ticketManager(){
		currentPage = 0;
	}

	/**
	 * connect()
	 * connects to the API at Zendesk
	 * No input, will output String message if connected/fails to connect
	 */
	public HttpURLConnection connect() {
		try {
			URL url = new URL("https://zccterra.zendesk.com/api/v2/tickets.json");
			HttpURLConnection conn = (HttpURLConnection) url.openConnection();
			
			//set login token
			String username = "nolan.matt@northeastern.edu/token";
			String apiToken = "us7JSCXEcuEZjlnMuqoo8cnCCIbe0hNT8jVlMcS4";
			
			//Set Login, and encode it
			String apiLogin = username + ":" + apiToken;
			String encoded = Base64.getEncoder().encodeToString(apiLogin.getBytes());
			
			//Set Properties for Auth and Content TYpe
			conn.setRequestProperty("Authorization", "Basic " + encoded);
			conn.setRequestProperty("Content-Type", "application/json");
			conn.setRequestMethod("GET");
			
			
			conn.connect();
			int responseCode = conn.getResponseCode();
			System.out.println(conn.getResponseMessage());
			if(responseCode == 200) {
				System.out.println("Connect successful");
			}else {
				throw new IOException();
			}
			
			return conn;
		} catch (MalformedURLException e) {
			System.out.println("Bad URL, please try again");
			return null;
		} catch(IOException i) {
			System.out.println("Connection failed, pleast try again");
			return null;
		}
		
		
	}
	
	/**
	 * retrieve()
	 * retrieves tickets for the system
	 */
	//public void retrieve(HttpURLConnection url) {
	//	String inline = "";
	//	Scanner scanner = new Scanner(url.openStream());
	//	
	//	while(scanner.hasNext()) {
	//		inline += scanner.nextLine();
	//	}
		
	//	scanner.close();
		
	//	JSONParser parse = new JSONParser();
	//	JSONObject dataObj = (JSONObject) parse.parse(inline);
		
	//}
	
	/**
	 * will print
	 */
	public static void print() {
		
	}
	
	public static void main(String args[]) {
		ticketManager task = new ticketManager();
		HttpURLConnection site = task.connect();
		//task.retrieve(site);
		
	}
}
