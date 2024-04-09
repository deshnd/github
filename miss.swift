import Foundation
func readLines() -> [String] {
    var lines = [String]()
    while let line = readLine() {
        lines += [line]
    }
    return lines
}
func printLines(lines: [String]) {
    for line in lines {
        print(line)
    }
}
