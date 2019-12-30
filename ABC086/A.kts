fun main(args: Array<String>) {
    val (a, b) = readLine()!!.split(" ").map(String::toInt)
    if (a * b % 2 == 0) {
        println("Even")
    } else {
        println("Odd")
    }
}