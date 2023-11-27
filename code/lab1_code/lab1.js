const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function getValidNumber(prompt) {
  return new Promise((resolve) => {
    rl.question(prompt, (input) => {
      const number = parseFloat(input);
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

  const roots = getRoots(a, b, c);

  if (roots.length === 0) {
    console.log('Уравнение не имеет действительных корней.');
  } else {
    console.log('Действительные корни уравнения: ', roots);
  }

  rl.close();
}

main();
