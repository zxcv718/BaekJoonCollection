import Foundation

func laserTower() {
    let n = Int(readLine()!)!
    let towers = readLine()!.split(separator: " ").map { Int($0)! }
    
    var stack = [(index: Int, height: Int)]()
    var result = Array(repeating: 0, count: n)
    
    for i in 0..<n {
        while !stack.isEmpty && stack.last!.height < towers[i] {
            stack.removeLast()
        }
        
        if !stack.isEmpty {
            result[i] = stack.last!.index + 1
        }
        
        stack.append((i, towers[i]))
    }
    
    print(result.map { String($0) }.joined(separator: " "))
}

laserTower()