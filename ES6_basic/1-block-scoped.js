export default function taskBlock(trueOrFalse) {
  let task = false;   // outer variable
  let task2 = true;   // outer variable

  if (trueOrFalse) {
    let task = true;    // block-scoped: DOES NOT overwrite outer
    let task2 = false;  // block-scoped: DOES NOT overwrite outer
  }

  return [task, task2];  // outer variables unchanged
}
