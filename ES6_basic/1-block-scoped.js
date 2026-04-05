export default function taskBlock(trueOrFalse) {
  let task = false;  // outer variable
  let task2 = true;  // outer variable

  if (trueOrFalse) {
    task = true;      // reassign outer variable
    task2 = false;    // reassign outer variable
  }

  return [task, task2];
}
