function getCoef(index, prompt1) {
    try {
        coefStr = process.argv[index]
    }
    finally {
        print(prompt1)
        coefStr = prompt()
    }
    coef = parseFloat(coefStr)
    return coef
}

function getRoots(a,b,c){
    let result = []
    let D = b*b - 4*a*c
    if (D==0){
        let root = -b/(2.0)*a
        let roota = Math.sqrt(root)
        let rootb = Math.sqrt(root) * (-1)
        result.push(roota)
        result.push(rootb)
    }
    else if (D > 0){
        let sqD = Math.sqrt(D)
        let root1 = (-b + sqD) / (2.0*a)
        let root2 = (-b - sqD) / (2.0*a)
        let root1a = Math.sqrt(root1)
        let root1b = Math.sqrt(root1) * (-1)
        let root2a = Math.sqrt(root2)
        let root2b = Math.sqrt(root2) * (-1)
        result.push(root1a)
        result.push(root1b)
        result.push(root2a)
        result.push(root2b)
    }
    return result
}



function main() {
    console.log("Биквадратное уравнение")
    let a = getCoef(2, "Введите коэффициент А:")
    let b = getCoef(3,"Введите коэффициент B:")
    let c = getCoef(4,"Введите коэффициент C:")


    roots= getRoots(a,b,c)
    
}