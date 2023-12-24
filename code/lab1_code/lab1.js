const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function getValidNumber(prompt) {
  return new Promise((resolve) => {
    rl.question(prompt, (input) => {
      let number = parseFloat(input);
      if (!isNaN(number)) {
        resolve(number);
      } else {
        console.log('Введите корректное число.');
        resolve(getValidNumber(prompt));
      }
    });
  });
}

function calculateDiscriminant(a, b, c) {
  return b * b - 4 * a * c;
}

function getRoots(a, b, c) {
  const discriminant = calculateDiscriminant(a, b, c);

  if (discriminant > 0) {
    const root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
    const root2 = (-b - Math.sqrt(discriminant)) / (2 * a);
    return [root1, root2];
  } else if (discriminant === 0) {
    const root = -b / (2 * a);
    return [root];
  } else {
    return [];
  }
}
function getRoots1(a,b,c){
  let result = []
  let D = b*b - 4*a*c
  if (D == 0.0){
     let root = -b / (2.0*a)
     let roota = Math.sqrt(root)
     let rootb = Math.sqrt(root) * (-1)
      result.push(roota)
      result.push(rootb)
      return [roota,rootb]
  }
  else if (D > 0.0){
    let sqD = Math.sqrt(D)
    let  root1 = (-b + sqD) / (2.0*a)
    let  root2 = (-b - sqD) / (2.0*a)
    let  root1a = Math.sqrt(root1)
    let  root1b = Math.sqrt(root1) * (-1)
    let  root2a = Math.sqrt(root2)
    let  root2b = Math.sqrt(root2) * (-1)
      result.push(root1a)
      result.push(root1b)
      result.push(root2a)
      result.push(root2b)
      return [root1a,root1b,root2a,root2b]
  }
  else{
    return []
  }

}

async function main() {
  let a, b, c;

  if (process.argv.length === 5) {
    // Если коэффициенты заданы через командную строку
    a = parseFloat(process.argv[2]);
    b = parseFloat(process.argv[3]);
    c = parseFloat(process.argv[4]);
  } else {
    // Ввод коэффициентов с клавиатуры
    a = await getValidNumber('Введите коэффициент A: ');
    b = await getValidNumber('Введите коэффициент B: ');
    c = await getValidNumber('Введите коэффициент C: ');
  }

  const roots = getRoots1(a, b, c);

  if (roots.length === 0) {
    console.log('Уравнение не имеет действительных корней.');
  } else {
    console.log('Действительные корни уравнения: ', roots);
  }

  rl.close();
}

main();
