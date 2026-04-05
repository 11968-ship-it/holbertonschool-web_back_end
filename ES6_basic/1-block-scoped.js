export default function taskBlock(trueOrFalse) {
  let task = false;   // outer scope
  let task2 = true;   // outer scope

  if (trueOrFalse) {
    let task = true;   // block scoped, does NOT overwrite outer task
    let task2 = false; // block scoped, does NOT overwrite outer task2
  }

  return [task, task2];
}
