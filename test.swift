import Foundation

var sum: Float = 723.67
var multiple: Bool = true

// Ensure proper conversion from String to Float
guard let c = Float("Original sum: $\(sum)") else {
    fatalError("Failed to convert string to float")
}

// Function to calculate bills and print them
func calculateBills(amount: inout Float, denomination: Float, denominationName: String) {
    let numBills = Int(amount / denomination)
    if numBills > 1 {
        multiple = true
    }
    let billString = multiple ? "\(numBills) x \(denominationName) bills" : "\(numBills) x \(denominationName) bill"
    print(billString)
    amount = amount.truncatingRemainder(dividingBy: denomination)
}

calculateBills(amount: &sum, denomination: 100, denominationName: "$100")
calculateBills(amount: &sum, denomination: 50, denominationName: "$50")
calculateBills(amount: &sum, denomination: 20, denominationName: "$20")
calculateBills(amount: &sum, denomination: 10, denominationName: "$10")
calculateBills(amount: &sum, denomination: 5, denominationName: "$5")
calculateBills(amount: &sum, denomination: 2, denominationName: "$2")
calculateBills(amount: &sum, denomination: 1, denominationName: "$1")
calculateBills(amount: &sum, denomination: 0.50, denominationName: "half-dollar coins")
calculateBills(amount: &sum, denomination: 0.25, denominationName: "quarters")
calculateBills(amount: &sum, denomination: 0.10, denominationName: "dimes")
calculateBills(amount: &sum, denomination: 0.05, denominationName: "nickels")
calculateBills(amount: &sum, denomination: 0.01, denominationName: "pennies")

