/**
	Multi-line comments for documentation.
**/
class Main {
	static public function main():Void {
		// Single line comment
		trace("Hello, trace!");
		Sys.println("Hello, println!");
		Sys.print("Hello, print!"); // no added newline
		Sys.stderr().writeString("Yow!\n");
	}
}
