
public class ScannerDemo {

	private static String File1 = "src/prog1.jay";
	private static int counter = 1;

	public static void main(String args[]) {

		TokenStream ts = new TokenStream(File1);

		System.out.println("File"+File1);
		Token t;

		while (!ts.isEndofFile()) {
			
			t= ts.nextToken();
			t.toString();
			System.out.println("Token " + counter + " - Type:" + t.getType() + " - Value: " + t.getValue());
			counter = counter +1;
			
		}
	}
}
